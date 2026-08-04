import os
import urllib.parse
import requests
import pandas as pd
from datetime import datetime, timezone
from dotenv import load_dotenv
from sqlalchemy import create_engine
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- STEP 0: LOAD ENVIRONMENT VARIABLES ---
# قراءة الإعدادات من ملف .env حصرياً
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER")
COUNTRY = os.getenv("COUNTRY", "Egypt")

# التحقق من وجود المتغيرات الأساسية للاتصال
if not all([DB_HOST, DB_NAME, DB_DRIVER]):
    raise ValueError("Missing database configuration in .env file. Please check DB_HOST, DB_NAME, and DB_DRIVER.")

# بناء نص الاتصال باستخدام البيانات المقروءة من ملف .env
connection_string = (
    f"DRIVER={{{DB_DRIVER}}};"
    f"SERVER={DB_HOST};"
    f"DATABASE={DB_NAME};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"

def get_cities_for_country(COUNTRY):
    """
    جلب كافة مدن ومحافظات مصر الـ 27 كلياً بدون أي نقص وبأسمائها النظيفة.
    """
    # خريطة تربط الاسم المطلوب بالاسم المتوافق مع Open-Meteo API
    cities_map = {
        "Cairo": "Cairo",
        "Alexandria": "Alexandria",
        "Giza": "Giza",
        "Shubra El Kheima": "Shubra al Khaymah",
        "Port Said": "Port Said",
        "Suez": "Suez",
        "Mansoura": "Al Mansurah",
        "El Mahalla El Kubra": "El-Mahalla",
        "Tanta": "Tanta",
        "Asyut": "Asyut",
        "Ismailia": "Ismailia",
        "Faiyum": "Al Fayyum",
        "Zagazig": "Zagazig",
        "Aswan": "Aswan",
        "Damietta": "Damietta",
        "Damanhur": "Damanhur",
        "Minya": "Minya",
        "Beni Suef": "Bani Suwayf",
        "Qena": "Qina",
        "Sohag": "Sohag",
        "Hurghada": "Hurghada",
        "6th of October": "6th of October City",
        "Sharm El-Sheikh": "Sharm el Sheikh",
        "Luxor": "Luxor",
        "Marsa Matruh": "Marsa Matruh",
        "Arish": "EL Arish",
        "Kafr El Sheikh": "Kafr ash Shaykh"
    }

    cities_geo_data = []
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    print(f"Fetching location data for all 27 cities in {COUNTRY}...")
    
    for display_name, search_name in cities_map.items():
        url = (
            "https://geocoding-api.open-meteo.com/v1/search?"
            f"name={urllib.parse.quote_plus(search_name)}&count=10&language=en&format=json"
        )
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                results = response.json().get("results", [])
                for item in results:
                    if item.get("country") == "Egypt" :
                        cities_geo_data.append({
                            "city": display_name,  
                            "lat": item.get("latitude"),
                            "lon": item.get("longitude")
                        })
                        break
        except Exception as e:
            print(f"Error fetching coordinates for {display_name}: {e}")

    return cities_geo_data
# --- STEP 1: EXTRACT ---
def extract_weather_data(cities):
    """Fetches real-time weather from Open-Meteo API."""
    raw_data = []

    if not cities:
        print("No cities provided.")
        return raw_data

    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    for item in cities:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={item['lat']}&longitude={item['lon']}"
            f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        )
        try:
            response = session.get(url, timeout=20)
            if response.status_code == 200:
                payload = response.json()
                payload["city_name"] = item["city"]
                raw_data.append(payload)
            else:
                print(f"Failed to fetch weather for {item['city']}: Status {response.status_code}")
        except Exception as e:
            print(f"Network error for {item['city']}: {e}")

    return raw_data


# --- STEP 2: TRANSFORM ---
def transform_weather_data(raw_data):
    """Cleans JSON data and builds a pandas DataFrame matching SQL Server schema."""
    records = []

    for item in raw_data:
        current = item.get("current", {})

        records.append({
            "city": item.get("city_name"),
            "latitude": item.get("latitude"),
            "longitude": item.get("longitude"),
            "temperature_celsius": current.get("temperature_2m"),
            "relative_humidity": current.get("relative_humidity_2m"),
            "wind_speed_kmh": current.get("wind_speed_10m"),
            "weather_code": current.get("weather_code"),
            "recorded_at": pd.to_datetime(current.get("time")),
            "fetched_at": datetime.now(timezone.utc)
        })

    return pd.DataFrame(records)


# --- STEP 3: LOAD (HISTORICAL APPEND) ---
def load_data_to_sql_server(df, db_uri):
    """Inserts new records continuously into the weather_logs SQL Server table."""
    if df.empty:
        print("No data to load.")
        return False

    try:
        engine = create_engine(db_uri, fast_executemany=True)
        df.to_sql(
            name="weather_logs",
            con=engine,
            if_exists="append",
            index=False
        )
        print(f"Successfully appended {len(df)} new records into 'weather_logs'.")
        return True
    except Exception as e:
        print(f"Error loading data to database: {e}")
        return False


# --- PIPELINE EXECUTION ---
def run_etl():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting Weather ETL pipeline for {COUNTRY}...")

    # 1. Geocoding
    cities = get_cities_for_country(COUNTRY)
    print(f"Found {len(cities)} valid cities in {COUNTRY}.")

    # 2. Extract
    raw_weather = extract_weather_data(cities)
    print(f"Extracted weather data for {len(raw_weather)} cities.")

    if not raw_weather:
        print("Pipeline aborted: Failed to extract weather data.")
        return

    # 3. Transform
    transformed_df = transform_weather_data(raw_weather)

    # 4. Load
    success = load_data_to_sql_server(transformed_df, DATABASE_URI)
    if success:
        print("ETL pipeline execution finished successfully!\n")
    else:
        print("ETL pipeline failed during database loading.\n")


if __name__ == "__main__":
    run_etl()