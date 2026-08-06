# 🚀 Data Engineering Journey & Projects

Welcome to my central repository documenting my step-by-step journey in **Data Engineering**. 


---

## 📌 Roadmap & Progress

- ✅ **[Module 1: Relational Databases & Advanced SQL](./01-sql-and-relational-databases)** *(Source: Eng. Baraa 30-Hour Course)*
- ✅ **[Module 2: Python Refresher & Initial Projects](./02-python-refresher)** *(Data Structures, Web Scraping, APIs & ETL)*
- 🔄 **[Module 3: Containerization & Infrastructure as Code](./03-containerization-and-Infrastructure-as-Code)** *(Docker & Terraform)*

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

## 🐳 Module 3: Containerization & Infrastructure as Code

Setting up local and cloud engineering environments using Docker, PostgreSQL, and provisioning cloud assets using Terraform.

### 📚 Learning Resources & Fundamentals:
* **Video Foundations:** Started Containerization fundamentals with [Docker Tutorial for Beginners (Full Course)](https://www.youtube.com/watch?v=3c-iBn73dDE) by TechWorld with Nana.
* **Hands-on Labs & Curriculum:** Progressing through the hands-on modules in the Data Engineering Zoomcamp repository:
  * 📄 **[Introduction to Docker](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/01-introduction.md)
  * 📄 **[Virtual Environments and Data Pipelines](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/02-virtual-environment.md)
  * 📄 **[Dockerizing the Pipeline](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/docker-sql/03-dockerizing-pipeline.md)

> 💡 **Learning Strategy:** Practicing hands-on container setup alongside AI-assisted learning (ChatGPT/Gemini) to deep-dive into complex CLI flags, container architecture, and debugging edge cases in real time.
