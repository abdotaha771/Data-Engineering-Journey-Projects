# Module 9: AI for Data Engineering

This module introduces practical AI capabilities for data professionals, including large language models (LLMs), AI agents, retrieval-augmented generation (RAG), vector databases, and AI-assisted development.

## Learning Resources

- **[AI TUTORIAL For Data Domain (AI Agents, LLMs, RAG, Vector DB)](https://youtu.be/kHq77-I1ZjE)** by Ansh Lamba
- **[CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition)](https://youtu.be/lkc-F5I8gFE)** by Ansh Lamba

## Why AI Belongs in the Roadmap

AI is increasingly used around data platforms rather than as a replacement for their foundations. Reliable data engineering remains essential for preparing data, controlling access, evaluating quality, and supplying trustworthy context to AI applications. This module builds on the SQL, Python, cloud, dbt, and Airflow work already covered.

## Topics

### AI and LLM foundations

- LLM capabilities, limitations, and common data-domain use cases
- Prompt design and structured outputs
- Embeddings and semantic similarity
- Token, latency, and cost considerations
- Privacy, access control, and responsible use of sensitive data

### Data-domain AI patterns

- AI agents and tool calling
- Retrieval-augmented generation (RAG)
- Document ingestion, chunking, metadata, and retrieval
- Vector databases and similarity search
- Connecting AI applications to governed warehouse and lake data
- Evaluation, monitoring, and protection against inaccurate or unsupported answers

### AI-assisted engineering

- Using Claude Code to understand and modify data projects
- Generating tests, documentation, SQL, and pipeline scaffolding
- Reviewing AI-generated code for correctness, security, and maintainability
- Keeping human review and Git-based change control in the development loop

## Suggested Practice Workflow

1. Build a small document-ingestion flow that extracts text and metadata.
2. Generate embeddings and store them in a vector database.
3. Implement a RAG question-answering flow with source references.
4. Add an evaluation set for retrieval quality and answer faithfulness.
5. Use an AI coding assistant to improve a small Python, dbt, or Airflow task.
6. Review the generated changes, add tests, and commit them through the GitHub workflow.

## Outcome

By the end of this module, the roadmap should include a small, evaluated data-domain AI application and a clear understanding of how AI can safely interact with the existing data platform. AI-assisted development should improve productivity without replacing testing, version control, data governance, or engineering judgment.
