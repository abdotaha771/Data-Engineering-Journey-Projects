# ETL Weather Project

This project builds a simple weather ETL pipeline that:

- fetches city coordinates from the Open-Meteo geocoding API,
- extracts current weather data from the Open-Meteo forecast API,
- transforms the data into a pandas DataFrame,
- loads the results into a SQL Server table named `weather_logs`.

## Project Files

- `etl_weather.py` – main ETL script
- `requirements.txt` – Python dependencies
- `.env.example` – environment variables for database connection

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in this folder with your SQL Server settings:
   ```env
   DB_HOST=your_server_name_or_ip
   DB_NAME=your_database_name
   DB_DRIVER=your_db_driver
   ```

## Run the ETL

```powershell
python etl_weather.py
```

## Notes

- The script uses `requests`, `pandas`, `sqlalchemy`, `python-dotenv`, and `pyodbc`.
- Make sure your SQL Server ODBC driver is installed and available on your machine.
- If PowerShell blocks activation, run:
  ```powershell
  Set-ExecutionPolicy -Scope Process RemoteSigned
  ```
