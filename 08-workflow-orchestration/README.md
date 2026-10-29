# Module 8: Workflow Orchestration with Apache Airflow

This module focuses on orchestrating reliable data pipelines with Apache Airflow. It follows the cloud, warehouse, and dbt modules so that ingestion, transformation, testing, and delivery can be coordinated as one observable workflow.

## Learning Resource

- **[Airflow Tutorial For Beginners (2026) | Apache Airflow Full Course](https://youtu.be/IiczxlbQb8s)** by Ansh Lamba

## Why Airflow Comes After dbt

dbt defines and tests transformations inside the warehouse. Airflow coordinates the wider process: extracting or loading data, triggering dbt, waiting for upstream dependencies, handling retries, and notifying operators when a run needs attention. Keeping these responsibilities separate produces clearer and more maintainable pipelines.

## Topics

### Airflow foundations

- Airflow architecture and core components
- DAGs, tasks, operators, and task dependencies
- The Airflow UI and run history
- Scheduling, start dates, catchup, and cron expressions

### Pipeline design

- Building readable, idempotent DAGs
- Task grouping, parallel tasks, branching, and trigger rules
- Passing small pieces of metadata with XComs
- Using Jinja templates and connections without hard-coding secrets
- Retries, timeouts, failure handling, and backfills

### Data engineering integration

- Orchestrating Python ingestion jobs and containerized workloads
- Loading data into GCS and BigQuery
- Triggering dbt models and tests after warehouse loads
- Designing dependencies across ingestion, transformation, validation, and delivery
- Monitoring pipeline runs and diagnosing failures

## Suggested Practice Workflow

1. Create a local Airflow environment and run a minimal DAG.
2. Build a scheduled ingestion task with retries and logging.
3. Add a BigQuery or warehouse-loading step after ingestion.
4. Trigger dbt transformations and tests only after the load succeeds.
5. Add a failure path, retry policy, and clear task documentation.
6. Review the DAG in the Airflow UI and verify reruns are safe.

## Outcome

By the end of this module, the batch capstone should have a visible, scheduled workflow that coordinates the Python or Docker ingestion process, GCP warehouse loading, and dbt transformations while remaining reproducible and safe to rerun.
