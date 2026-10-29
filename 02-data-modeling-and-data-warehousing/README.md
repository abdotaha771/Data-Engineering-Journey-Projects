# Module 2: Data Modeling & Data Warehousing

This module builds the conceptual foundation between relational SQL and practical data-engineering platforms. It explains how to model business data, design analytical schemas, and organize reliable warehouse layers before moving into Python, containers, and cloud services.

## Learning Resources

- **[Database Design & Data Modeling Full Course For Beginners (2026)](https://youtu.be/_jf7KZqne-8)** by Ansh Lamba
- **[Data Warehouse - The Ultimate Guide (2025) | Master Data Modeling](https://youtu.be/HKcEyHF1U00)** by Ansh Lamba

## Why This Module Comes After SQL

SQL provides the language for querying and transforming data. Data modeling determines what that data means, how entities relate to one another, and how the design supports both operational workloads and analytics. Warehousing then applies those principles to historical, integrated, and reporting-oriented data.

## Topics

### Database and data modeling

- Business entities, attributes, relationships, and cardinality
- Conceptual, logical, and physical data models
- Primary keys, foreign keys, constraints, and normalization
- Dimensional modeling, facts, dimensions, and grain
- Star schemas, snowflake schemas, and slowly changing dimensions

### Data warehouse foundations

- OLTP versus OLAP workloads
- Batch ingestion and historical data management
- Staging, Bronze, Silver, and Gold layers
- Data marts and serving analytics users
- Data quality, consistency, lineage, and governance
- Partitioning, clustering, and performance-aware design

## Suggested Practice Workflow

1. Choose a business process and define its grain.
2. Identify entities, relationships, facts, and dimensions.
3. Draw a conceptual and logical model.
4. Implement a small normalized operational schema.
5. Design a dimensional warehouse with Bronze, Silver, and Gold layers.
6. Document assumptions, keys, data quality rules, and access patterns.
7. Query the model with analytical SQL and compare the trade-offs.

## Outcome

By the end of this module, later Python, Docker, GCP, BigQuery, dbt, and Airflow projects should have an explicit data model and warehouse design rather than relying on ad hoc tables.
