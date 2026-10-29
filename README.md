# Data Engineering Journey & Projects

Welcome to my central repository documenting my step-by-step journey in **Data Engineering**.

---

## Roadmap & Milestones

### Milestone 1: Modern Data Warehouse & Batch Pipelines (Job-Ready Target)

> **Goal:** Build automated, production-grade batch ELT pipelines on the cloud and start applying for Junior Data Engineer & Analytics Engineer roles.

- ✓ **[Module 1: Relational Databases & Advanced SQL](./01-sql-and-relational-databases)** _(Source: Eng. Baraa 30-Hour Course)_
- ✓ **[Module 2: Data Modeling & Data Warehousing](./02-data-modeling-and-data-warehousing)** _(Database design, dimensional modeling & warehouse architecture)_
- ✓ **[Module 3: Python Refresher & Initial Projects](./03-python-refresher)** _(Data Structures, Web Scraping, APIs & ETL)_
- ✓ **[Module 4: Containerization with Docker](./04-Containerization%20with%20Docker)** _(Docker & Docker Compose)_
- ✓ **[Module 5: Git & GitHub](./05-git-and-github)** _(Version control, collaboration & portfolio workflows)_
- ✓ **[Module 6: Cloud Data Platforms](./06-cloud-data-platforms)** _(GCP, AWS & Azure cloud concepts)_
- ✓ **[Module 7: Analytics Engineering with dbt](./07-analytics-engineering-dbt)** _(dbt Core, Data Modeling, Testing & Documentation)_
- ✓ **[Module 8: Workflow Orchestration](./08-workflow-orchestration)** _(Apache Airflow & Pipeline Automation)_
- ✓ **[Module 9: AI for Data Engineering](./09-Ai-for-data-engineering)** _(LLMs, AI Agents, RAG, Vector Databases & AI-Assisted Development)_
- ○ **Capstone Project 1:** _End-to-End Batch Data Engineering Project_

---

### Milestone 2: Advanced Data Platforms & Production Engineering

> **Goal:** Extend the foundation into distributed processing, lakehouse architecture, real-time systems, infrastructure automation, and production DataOps.

- ○ **[Module 10: Unified Data Processing & Lakehouse](./10-batch-processing-spark)** _(Apache Spark, PySpark, Databricks & Delta Lake)_
- ○ **[Module 11: Stream Processing & Real-Time Ingestion](./11-stream-processing-kafka)** _(Apache Kafka & Event Streaming)_
- ○ **[Module 12: Production-Grade DataOps, IaC & Observability](./12-production-and-dataops)** _(Infrastructure automation, CI/CD, data quality, monitoring & secrets)_
- ○ **Final Project:** _End-to-End Production Data Platform_

---

## Module 1: Relational Databases & Advanced SQL

**Learning Source:** [Eng. Baraa's 30-Hour Intensive Advanced SQL & Database Course](https://youtu.be/SSKVgrwhzus?si=_ZxvYuiNXkwpjuYh)

Before moving into distributed systems and orchestration, I established a robust foundation in relational database management, data modeling, and production-grade SQL development.

### Key Learnings & Concepts:

- **Advanced Querying:** Complex JOINs, Subqueries, CTEs (Common Table Expressions), Window Functions, and Analytical Aggregations.
- **Database Architecture & DDL/DML:** Schema design, normalization, indexing strategies, primary/foreign key constraints, and transactional safety.
- **Data Warehousing Foundations:** Multi-layered architecture modeling (Bronze/Landing, Silver/Staging, Gold/Analytics layers).
- **ETL Ingestion Scripts:** Writing automated `TRUNCATE` and `INSERT` batch pipeline scripts to transform and move data through data layers.

---

## Module 2: Data Modeling & Data Warehousing

Building the data-modeling and warehouse-design foundation needed to turn SQL knowledge into reliable analytical systems.

### Learning Resources

- **[Database Design & Data Modeling Full Course For Beginners (2026)](https://youtu.be/_jf7KZqne-8)**
- **[Data Warehouse - The Ultimate Guide (2025) | Master Data Modeling](https://youtu.be/HKcEyHF1U00)**

See the [Module 2 README](./02-data-modeling-and-data-warehousing/README.md) for the detailed topics and practice workflow.

---

## Module 3: Python Refresher & Initial Projects

Before diving into complex distributed systems, I reviewed Python fundamentals by building core CLI projects, web scrapers, and automated database pipelines focused on data structures, control flow, functions, file persistence, and validation.

### Recommended Revision Resource:

- **[Python for Data Engineering Course](https://github.com/behnamyazdan/PythonForDataEngineeringCourse):** A recommended external repository to quickly look up or revise Python fundamentals and concepts relevant to Data Engineering.

### Included Projects:

1. **[To-Do List Application](./03-python-refresher/To-Do%20List%20Application)**
   - **Focus:** Data Structures (Lists, Dicts), Exception Handling, File I/O (`json` persistence).
   - **Features:** Full CRUD operations for daily task tracking.

2. **[Books Catalog Web Scraper](./03-python-refresher/Web_Scraping_books_to_scrap)**
   - **Focus:** Web Scraping, Resilient Network Requests, Data Cleaning, Batch Export (`CSV`).
   - **Features:** Robust scraper handling dynamic pagination, automated retries, HTML parsing with BeautifulSoup, schema validation, and tabular data export using Pandas.

3. **[Automated Weather ETL Pipeline](./03-python-refresher/etl_weather)**
   - **Focus:** REST APIs Integration, Data Transformation, SQL Server Database Loading, Automation.
   - **Features:** End-to-end pipeline fetching weather data via Open-Meteo API, normalizing JSON payloads with Pandas, appending records to MS SQL Server via SQLAlchemy/PyODBC, and automating ingestion with Windows Task Scheduler.

---

## Module 4: Containerization with Docker

Setting up reproducible local data engineering environments using Docker, PostgreSQL, and Docker Compose

### Learning Resources & Fundamentals:

- **Video Foundations:** Started Containerization fundamentals with [Docker Tutorial for Beginners (Full Course)](https://www.youtube.com/watch?v=3c-iBn73dDE) by TechWorld with Nana.
- **Hands-on Labs & Curriculum:** Progressing through the hands-on modules in the Data Engineering Zoomcamp repository:
  - **[Introduction to Docker](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/01-introduction.md)**
  - **[Virtual Environments and Data Pipelines](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/02-virtual-environment.md)**
  - **[Dockerizing the Pipeline](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/03-dockerizing-pipeline.md)**
  - **[Running PostgreSQL with Docker](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/04-postgres-docker.md)**
  - **[NY Taxi Dataset and Data Ingestion](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/05-data-ingestion.md)**
  - **[Creating the Data Ingestion Script](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/06-ingestion-script.md)**
  - **[pgAdmin - Database Management Tool](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/07-pgadmin.md)**
  - **[Dockerizing the Ingestion Script](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/08-dockerizing-ingestion.md)**
  - **[Docker Compose](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/09-docker-compose.md)**

> **Learning Strategy:** Practicing hands-on container setup alongside AI-assisted learning (ChatGPT/Gemini).

### Highlighted Project: Multi-Container NYC Taxi Ingestion Pipeline

> **Next Step:** After going through the Zoomcamp reading materials above, head directly to my production-ready project folder below to explore, run, and understand how all these components work together seamlessly in a single command.

**[NYC Taxi Data Ingestion Pipeline Project](./04-Containerization%20with%20Docker/docker_with_postgres_pgadmin_project)**

---

## Module 5: Git & GitHub

Building the version-control and collaboration habits required to manage data engineering projects professionally.

### Learning Resource

- **Video Course:** [Complete Git and GitHub Tutorial For Data Engineers (2025)](https://youtu.be/Kr8l7rQGwNs)

### Key Learnings & Practice

- Git fundamentals: repositories, commits, branches, merges, remotes, and tags.
- GitHub workflows: pull requests, code review, issues, and project documentation.
- Data-engineering-safe practices: `.gitignore`, keeping secrets out of Git, reproducible commits, and useful README files.
- Portfolio workflow: organizing projects, writing meaningful commit messages, and collaborating without overwriting work.

See the [Git & GitHub module README](./05-git-and-github/README.md) for the detailed study scope and practice checklist.

---

## Module 6: Cloud Data Platforms

Building cloud-based data-platform knowledge across the three major providers without choosing a permanent primary provider.

**Platform approach:** GCP, AWS, and Azure are all part of the learning scope. The roadmap will first establish transferable cloud concepts, then explore the equivalent services and workflows across the three providers before deciding where to specialize.

### Learning Resources & Fundamentals:

- **Interactive DataCamp Courses:**
  - **[Introduction to Data Engineering on Google Cloud](https://app.datacamp.com/learn/courses/introduction-to-data-engineering-on-google-cloud)**
  - **[Build Data Lakes and Data Warehouses on Google Cloud](https://app.datacamp.com/learn/courses/build-data-lakes-and-data-warehouses-on-google-cloud)**
- **AWS Comparison Resource:** [AWS Tutorial For Beginners (2026 Guide) | AWS Data Engineer](https://youtu.be/Ae3xyW2Ef0c)
- **Azure Scope:** Core Azure storage, analytics, identity, and orchestration equivalents will be added as the provider comparison work progresses.

### Certificate

- **[Module 6 Cloud Data Warehousing Certificate](./06-cloud-data-platforms/module-4-cloud-data-warehousing-certificate.pdf)** — Cloud Data Warehousing

---

## Module 7: Analytics Engineering with dbt

Transforming raw warehouse data into analytics-ready models, implementing data testing and documentation, and establishing reliable data transformation workflows using dbt (data build tool).

### Learning Resources & Fundamentals:

- **Interactive DataCamp Skill Track:**
  - **[dbt Fundamentals](https://app.datacamp.com/learn/skill-tracks/dbt-fundamentals)**
- **Video Course:** [Data Build Tool (DBT) - The Ultimate Guide | With CI/CD](https://youtu.be/B8uwFmVt4sU)

### Certificate

- **[dbt Fundamentals Certificate](./07-analytics-engineering-dbt/dbt-fundamentals-certificate.pdf)** — Analytics Engineering with dbt

---

## Module 8: Workflow Orchestration with Apache Airflow

Coordinating ingestion, warehouse loading, dbt transformations, testing, retries, and monitoring as reliable scheduled workflows.

### Learning Resource

- **[Airflow Tutorial For Beginners (2026) | Apache Airflow Full Course](https://youtu.be/IiczxlbQb8s)** by Ansh Lamba

Airflow is introduced after dbt because dbt owns warehouse transformations while Airflow coordinates the complete pipeline across Python, Docker, GCP, BigQuery, and dbt. See the [Module 8 README](./08-workflow-orchestration/README.md) for the study scope and practice workflow.

---

## Module 9: AI for Data Engineering

Exploring practical AI applications for data engineering, including LLMs, AI agents, retrieval-augmented generation, vector databases, and AI-assisted development.

### Learning Resources

- **[AI TUTORIAL For Data Domain (AI Agents, LLMs, RAG, Vector DB)](https://youtu.be/kHq77-I1ZjE)** by Ansh Lamba
- **[CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition)](https://youtu.be/lkc-F5I8gFE)** by Ansh Lamba

AI is studied after the data platform foundation so it can be applied to reliable, governed data. See the [Module 9 README](./09-Ai-for-data-engineering/README.md) for the complete scope.
