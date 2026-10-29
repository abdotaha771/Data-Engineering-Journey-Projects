## Module 6: Cloud Data Platforms

This module builds cloud data-platform skills across **Google Cloud Platform (GCP), Amazon Web Services (AWS), and Microsoft Azure**. The learning path begins with transferable concepts and compares equivalent services across all three providers before selecting a future specialization.

## Platform Choice

No provider is treated as the permanent primary platform at this stage. The core comparison is:

| Data engineering capability | GCP | AWS | Azure |
|---|---|---|---|
| Object storage / data lake | Google Cloud Storage (GCS) | Amazon S3 | Azure Blob Storage / ADLS |
| Cloud data warehouse | BigQuery | Amazon Redshift | Microsoft Fabric / Synapse Analytics |
| Lakehouse querying | BigLake | Amazon Athena / Lake Formation | Microsoft Fabric / Synapse |
| Identity and access | Google Cloud IAM | AWS IAM | Microsoft Entra ID / Azure RBAC |
| Infrastructure as Code | Terraform | Terraform | Terraform |

The goal is to understand shared architecture and important service differences. A provider specialization can be chosen after the comparison work.

### Learning Resources & Fundamentals:

- **Interactive DataCamp Courses:**
  - **[Introduction to Data Engineering on Google Cloud](https://app.datacamp.com/learn/courses/introduction-to-data-engineering-on-google-cloud)**
  - **[Build Data Lakes and Data Warehouses on Google Cloud](https://app.datacamp.com/learn/courses/build-data-lakes-and-data-warehouses-on-google-cloud)**
- **AWS Comparison Resource:**
  - **[AWS Tutorial For Beginners (2026 Guide) | AWS Data Engineer](https://youtu.be/Ae3xyW2Ef0c)**

## Study Scope

1. **Cloud foundations:** projects/accounts, regions, billing awareness, and least-privilege IAM.
2. **Storage:** GCS buckets, object organization, lifecycle policies, and secure access.
3. **Warehousing:** BigQuery datasets, tables, loading patterns, partitioning, clustering, and cost-aware SQL.
4. **Lakehouse concepts:** external data and BigLake-style governed access.
5. **Infrastructure as Code:** provisioning repeatable resources with Terraform and separating configuration from secrets.
6. **Cross-cloud literacy:** compare equivalent storage, warehouse, lakehouse, identity, and orchestration services across GCP, AWS, and Azure.

## Intended Outcome

The practical outcome is a documented understanding of how to design and operate a cloud data platform across GCP, AWS, and Azure. Provider-specific implementation can be selected later and should connect the earlier Python, Docker, dbt, and Airflow modules.

### Certificate

- **[Module 6 Cloud Data Warehousing Certificate](./module-4-cloud-data-warehousing-certificate.pdf)**
