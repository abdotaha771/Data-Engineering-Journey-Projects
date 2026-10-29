import os
import sys
import time
import argparse
import pandas as pd
from sqlalchemy import create_engine, text
from tqdm.auto import tqdm

def connect_with_retry(db_url, max_retries=10, delay=3):
    for attempt in range(1, max_retries + 1):
        try:
            engine = create_engine(db_url)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Successfully connected to PostgreSQL database!")
            return engine
        except Exception:
            print(f"Database connection attempt {attempt}/{max_retries} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    
    print("Could not connect to PostgreSQL database after multiple attempts.")
    sys.exit(1)

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    file_path = params.file_path

    if not os.path.exists(file_path):
        print(f"Error: CSV file not found at path: {file_path}")
        print("Please verify the file exists inside your local ./data directory.")
        sys.exit(1)

    db_url = f"postgresql+psycopg://{user}:{password}@{host}:{port}/{db}"
    engine = connect_with_retry(db_url)

    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

    df_iter = pd.read_csv(
        file_path,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000,
        low_memory=False
    )

    print("Creating table schema in PostgreSQL...")
    first_chunk = next(df_iter)

    first_chunk.head(n=0).to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    first_chunk.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False
    )
    print(f"First chunk inserted: {len(first_chunk):,} rows")

    for df_chunk in tqdm(df_iter, desc="Ingesting Chunks"):
        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False
        )

    print("\nData ingestion process completed successfully!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL')
    parser.add_argument('--user', default='root', help='User name for postgres')
    parser.add_argument('--password', default='root', help='Password for postgres')
    parser.add_argument('--host', default='db', help='Host for postgres')
    parser.add_argument('--port', default='5432', help='Port for postgres')
    parser.add_argument('--db', default='ny_taxi', help='Database name for postgres')
    parser.add_argument('--table_name', default='yellow_taxi_data', help='Table name')
    parser.add_argument('--file_path', default='/app/data/yellow_tripdata_2021-01.csv', help='CSV file path')

    args = parser.parse_args()
    main(args)