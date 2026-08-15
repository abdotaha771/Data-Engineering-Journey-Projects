# 🚀 Data Engineering Journey & Projects

Welcome to my central repository documenting my step-by-step journey in **Data Engineering**. 


---
## 📌 Roadmap & Milestones

### 🚩 Milestone 1: Modern Data Warehouse & Batch Pipelines (Job-Ready Target)
> **Goal:** Build automated, production-grade batch ELT pipelines on the cloud and start applying for Junior Data Engineer & Analytics Engineer roles.

- ✅ **[Module 1: Relational Databases & Advanced SQL](./01-sql-and-relational-databases)** *(Source: Eng. Baraa 30-Hour Course)*
- ✅ **[Module 2: Python Refresher & Initial Projects](./02-python-refresher)** *(Data Structures, Web Scraping, APIs & ETL)*
- ✅ **[Module 3: Containerization with Docker](./03-containerization-with-docker)** *(Docker & Docker Compose)*
- 🔄 **[Module 4: Cloud Data Warehousing](./04-cloud-data-warehousing-gcp)** *(GCP, GCS, BigQuery, IAM & BigLake)*
- ⏳ **[Module 5: Analytics Engineering with dbt](./05-analytics-engineering-dbt)** *(dbt Core, Data Modeling, Testing & Documentation)*
- ⏳ **[Module 6: Workflow Orchestration](./06-workflow-orchestration)** *(Apache Airflow & Pipeline Automation)*
- 🎯 **Capstone Project 1:** *End-to-End Batch Pipeline (API/DB ➔ GCS ➔ BigQuery ➔ dbt ➔ Airflow / Docker)*

---

### 🚩 Milestone 2: Distributed Computing & Lakehouse Architecture
> **Goal:** Scale data transformations to large-scale datasets and master open-format Lakehouse architectures.

- ⏳ **[Module 7: Unified Data Processing & Lakehouse](./07-batch-processing-spark)** *(Apache Spark, PySpark, Databricks & Delta Lake)*
- 🎯 **Capstone Project 2:** *Large-Scale Lakehouse Pipeline (PySpark / Databricks + Delta Lake Medallion Architecture)*

---

### 🚩 Milestone 3: Real-Time Streaming, IaC & Production DataOps
> **Goal:** Build low-latency event-driven architectures with full infrastructure automation and CI/CD pipelines.

- ⏳ **[Module 8: Stream Processing & Real-Time Ingestion](./08-stream-processing-kafka)** *(Apache Kafka & Event Streaming)*
- ⏳ **[Module 9: Production-Grade DataOps, IaC & Observability](./09-production-and-dataops)** *(Terraform, CI/CD, Data Quality, Monitoring & Secrets)*
- 🏆 **[Module 10: End-to-End Master Capstone Project](./10-end-to-end-capstone-project)** *(Hybrid Batch + Streaming Production Architecture with Full DataOps)*
---

## 🗄️ Module 1: Relational Databases & Advanced SQL

**Learning Source:** [Eng. Baraa's 30-Hour Intensive Advanced SQL & Database Course](https://youtu.be/SSKVgrwhzus?si=_ZxvYuiNXkwpjuYh)

Before moving into distributed systems and orchestration, I established a robust foundation in relational database management, data modeling, and production-grade SQL development.

### Key Learnings & Concepts:
* **Advanced Querying:** Complex JOINs, Subqueries, CTEs (Common Table Expressions), Window Functions, and Analytical Aggregations.
* **Database Architecture & DDL/DML:** Schema design, normalization, indexing strategies, primary/foreign key constraints, and transactional safety.
* **Data Warehousing Foundations:** Multi-layered architecture modeling (Bronze/Landing, Silver/Staging, Gold/Analytics layers).
* **ETL Ingestion Scripts:** Writing automated `TRUNCATE` and `INSERT` batch pipeline scripts to transform and move data through data layers.

---

## 🐍 Module 2: Python Refresher & Initial Projects

Before diving into complex distributed systems, I reviewed Python fundamentals by building core CLI projects, web scrapers, and automated database pipelines focused on data structures, control flow, functions, file persistence, and validation.

### 💡 Recommended Revision Resource:
* 📄 **[Python for Data Engineering Course](https://github.com/behnamyazdan/PythonForDataEngineeringCourse):** A recommended external repository to quickly look up or revise Python fundamentals and concepts relevant to Data Engineering.

### Included Projects:

1. **📝 [To-Do List Application](./02-python-refresher/To-Do%20List%20Application)**
   * **Focus:** Data Structures (Lists, Dicts), Exception Handling, File I/O (`json` persistence).
   * **Features:** Full CRUD operations for daily task tracking.

2. **📚 [Books Catalog Web Scraper](./02-python-refresher/Web_Scraping_books_to_scrap)**
   * **Focus:** Web Scraping, Resilient Network Requests, Data Cleaning, Batch Export (`CSV`).
   * **Features:** Robust scraper handling dynamic pagination, automated retries, HTML parsing with BeautifulSoup, schema validation, and tabular data export using Pandas.

3. **🌤️ [Automated Weather ETL Pipeline](./02-python-refresher/etl_weather)**
   * **Focus:** REST APIs Integration, Data Transformation, SQL Server Database Loading, Automation.
   * **Features:** End-to-end pipeline fetching weather data via Open-Meteo API, normalizing JSON payloads with Pandas, appending records to MS SQL Server via SQLAlchemy/PyODBC, and automating ingestion with Windows Task Scheduler.

---

## 🐳 Module 3: Containerization with Docker

Setting up reproducible local data engineering environments using Docker, PostgreSQL, and Docker Compose

### 📚 Learning Resources & Fundamentals:
* **Video Foundations:** Started Containerization fundamentals with [Docker Tutorial for Beginners (Full Course)](https://www.youtube.com/watch?v=3c-iBn73dDE) by TechWorld with Nana.
* **Hands-on Labs & Curriculum:** Progressing through the hands-on modules in the Data Engineering Zoomcamp repository:
  * 📄 **[Introduction to Docker](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/01-introduction.md)
  * 📄 **[Virtual Environments and Data Pipelines](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/02-virtual-environment.md)
  * 📄 **[Dockerizing the Pipeline](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/03-dockerizing-pipeline.md)
  * 📄 **[Running PostgreSQL with Docker](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/04-postgres-docker.md)
  * 📄 **[NY Taxi Dataset and Data Ingestion](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/05-data-ingestion.md)
  * 📄 **[Creating the Data Ingestion Script](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/06-ingestion-script.md)
  * 📄 **[pgAdmin - Database Management Tool](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/07-pgadmin.md)
  * 📄 **[Dockerizing the Ingestion Script](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/08-dockerizing-ingestion.md)
  * 📄 **[Docker Compose](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/09-docker-compose.md)
  

> 💡 **Learning Strategy:** Practicing hands-on container setup alongside AI-assisted learning (ChatGPT/Gemini).


### 🚀 Highlighted Project: Multi-Container NYC Taxi Ingestion Pipeline

> 💡 **Next Step:** After going through the Zoomcamp reading materials above, head directly to my production-ready project folder below to explore, run, and understand how all these components work together seamlessly in a single command.

👉 **[NYC Taxi Data Ingestion Pipeline Project](./03-containerization-and-Infrastructure-as-Code/docker_with_postgres_pgadmin_project)**

---

## ☁️ Module 4: Cloud Data Warehousing

Building cloud-based data warehouses, managing storage buckets, and understanding Infrastructure as Code using GCP, BigQuery, and Terraform.

### 📚 Learning Resources & Fundamentals:
* **Interactive DataCamp Courses:**
  * 📄 **[Introduction to Data Engineering on Google Cloud](https://app.datacamp.com/learn/courses/introduction-to-data-engineering-on-google-cloud)**
  * 📄 **[Build Data Lakes and Data Warehouses on Google Cloud](https://app.datacamp.com/learn/courses/build-data-lakes-and-data-warehouses-on-google-cloud)**

