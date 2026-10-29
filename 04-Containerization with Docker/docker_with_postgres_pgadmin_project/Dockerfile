FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script
COPY ingest_data.py .

# Command to execution
ENTRYPOINT ["python", "ingest_data.py"]