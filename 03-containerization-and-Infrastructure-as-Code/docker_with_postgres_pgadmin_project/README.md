# Docker + PostgreSQL + pgAdmin — NYC Taxi Ingestion Project

Production-ready local pipeline for ingesting and exploring tabular data using Docker, PostgreSQL, and pgAdmin.

## Overview

This project demonstrates a multi-container setup using Docker Compose to run a PostgreSQL database and pgAdmin for database administration, plus a lightweight ingestion service that loads CSV data into the database. It is designed for local development, testing, and learning containerized data ingestion patterns.

Key components:

- PostgreSQL server (persistent data via Docker volumes)
- pgAdmin web UI for database management
- Ingestion script and Dockerfile for building a custom image to import CSV data

## Repository layout

- `docker-compose.yaml` — orchestrates Postgres, pgAdmin, and ingestion container(s)
- `Dockerfile` — image used for the ingestion/worker service
- `ingest_data.py` — example script to load CSV data into Postgres
- `requirements.txt` — Python runtime dependencies for the ingestion script
- `data/` — sample CSV dataset(s)
- `postgresql_data/` — Postgres data directory persisted by Docker (not for manual edits)

## Prerequisites

- Docker & Docker Compose (or Docker Desktop) installed and running
- Python 3.9+ (optional, for running the ingestion script locally)
- Sufficient disk space for database volumes

On Windows, run Docker Desktop as administrator if you encounter permission issues with volumes.

## Quickstart — Run with Docker Compose

1. From this project directory, build and start the containers:

```bash
docker compose up --build
```

2. Confirm containers are running:

```bash
docker compose ps
```

3. Access pgAdmin in your browser (default):

- URL: http://localhost:8080
- Add a server in pgAdmin with the Postgres container host (service name `db` in this compose project), port `5432`, and the credentials configured in `docker-compose.yaml` or `.env`.

4. Postgres database is available on port `5432` on the host (if exposed). Use `psql` or any DB client to connect.

## Running the ingestion script

Option A — Inside the ingestion container (recommended via compose):

- If the compose file includes a service to run `ingest_data.py`, it will run automatically or be available to exec into.

Option B — Locally using Python:

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/Scripts/activate  # PowerShell/Cmd on Windows: .venv\Scripts\Activate.ps1 or Activate.bat
pip install -r requirements.txt
```

2. Run the ingestion script (example):

```bash
python ingest_data.py --file_path data/yellow_tripdata_2021-01.csv \
  --host localhost --port 5432 --user <db_user> --password <db_password> --db <db_name>
```

Adjust flags according to the script's CLI options.

## Configuration

- Environment variables are typically defined in `docker-compose.yaml` or a `.env` file. Common variables:
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `POSTGRES_DB`
  - `PGADMIN_DEFAULT_EMAIL`
  - `PGADMIN_DEFAULT_PASSWORD`

If you add a `.env` file, ensure it is kept out of source control when containing secrets.

## Volumes & Data Persistence

Postgres data is stored in a Docker volume or host-mapped directory (`postgresql_data/`) so database state persists across container restarts. Do not edit the raw files inside this directory manually — use SQL clients or pgAdmin.

## Building the ingestion image manually

```bash
docker build -t taxi-ingest:latest .
```

Then run it with environment variables linking to the Postgres service.

## Troubleshooting

- If `docker compose up` fails due to port conflicts, ensure `8080` or `5432` are free or change the host mapping in `docker-compose.yaml`.
- Permission errors on Windows with named volumes: run Docker Desktop with elevated privileges or switch to WSL2 backend.
- If database connection fails from the host, verify `ports` mapping in `docker-compose.yaml` and that the container's Postgres service is `healthy`.

## Security notes

- This setup is intended for local development. Do not expose pgAdmin or Postgres to public networks without appropriate firewalling and secure credentials.
- Rotate secrets and avoid committing real passwords to the repository.

## Next steps and enhancements

- Add a small orchestration script to run ingestion on a schedule (cron or Airflow integration).
- Add tests for the ingestion script and CI steps to build the Docker image.
- Add documentation for the SQL schema and sample queries used for analysis.

## License & Credits

This project follows the repository license (see root `LICENSE`). Credit: Data Engineering Zoomcamp exercises and personal implementations.

---
