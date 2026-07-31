# Future Ideas

**Project:** AI Knowledge Platform
**Document:** Future Ideas
**Status:** Living Document

---

# Purpose

This document captures ideas that are intentionally out of scope for the current project.

The goal is to preserve future opportunities without distracting from the current roadmap.

Adding an item here does **not** mean it should be implemented immediately.

The project should continue to prioritize learning goals over feature count.

---

# How to Use This Document

Before adding a new feature ask:

- Does it support the current roadmap?
- Does it improve the learning objectives?
- Does it significantly improve the product?
- Is now the right time?

If the answer is "not yet", record the idea here instead of expanding the current scope.

---

# Near-Term Improvements

These are features likely to be implemented after the MVP.

## Multiple Document Support

Support conversations across several uploaded documents.

Why

Users rarely ask questions about a single document in isolation.

---

## Document Collections

Allow users to organize documents into collections.

Example

- Property Brochures
- Legal Contracts
- Financial Reports

---

## Background Processing

Move expensive operations to asynchronous workers.

Examples

- Parsing
- Chunking
- Embedding generation

Benefits

- Faster API responses
- Better scalability
- Improved user experience

---

## Streaming Responses

Return generated responses incrementally.

Benefits

- Lower perceived latency
- Better chat experience

---

## OCR Support

Extract text from scanned PDFs and images.

Potential technologies

- Tesseract
- Cloud OCR services

---

# AI Enhancements

## Better Retrieval

Experiment with:

- Hybrid search
- Metadata filtering
- Re-ranking
- Semantic chunking

Goal

Improve answer quality rather than simply increasing context.

---

## Conversation Memory

Support long-running conversations.

Possible approaches

- Summarization
- Selective memory
- Semantic memory

---

## Prompt Versioning

Treat prompts as versioned assets.

Benefits

- Easier experimentation
- Better reproducibility
- Safer prompt improvements

---

## Tool Calling

Allow the model to invoke application tools.

Possible tools

- Search uploaded documents
- Retrieve document metadata
- List available documents

---

## AI Agent Mode

Introduce an agent capable of:

- Planning
- Multi-step reasoning
- Tool orchestration
- Reflection

This should be added only after the RAG pipeline is well understood.

---

## Model Context Protocol (MCP)

Expose project capabilities through an MCP server.

Potential capabilities

- Document search
- Conversation history
- Metadata lookup

Goal

Allow external AI clients to interact with the platform using a standard protocol.

---

# Production Enhancements

These are intentionally postponed to keep the MVP focused.

- Authentication
- Authorization
- User accounts
- Organizations and workspaces
- Role-based access control
- API keys
- Rate limiting
- Audit logs
- Monitoring
- Distributed tracing
- Object storage (S3 or compatible)
- Background job queues
- Caching
- CI/CD pipeline
- Containerized deployment

---

# Scalability Improvements

Future architectural work may include:

- Dedicated vector database
- Horizontal scaling
- Read replicas
- Event-driven processing
- Distributed workers
- Multi-region deployment

These should only be introduced when justified by actual scale.

---

# Domain Expansion

The architecture should naturally support additional content types.

Potential examples

- Property brochures
- DOCX files
- Markdown
- HTML pages
- Knowledge base articles
- Images with OCR
- CSV files
- Presentation slides

The goal is to support a generalized knowledge platform rather than a PDF-only application.

---

# Experiments

Ideas worth exploring without committing to them.

- Different embedding models
- Retrieval evaluation metrics
- Prompt optimization
- Local LLMs
- Fine-tuning experiments
- Response caching
- Structured outputs
- Citation generation

These experiments should be isolated so they do not destabilize the core system.

---

# Ideas Rejected for Now

This section records ideas that were intentionally postponed.

## Multi-Agent Architecture

Reason

Adds significant complexity before the value of a single-agent approach has been demonstrated.

---

## Microservices

Reason

Premature for the expected project size.

A modular monolith provides a better balance of simplicity and scalability.

---

## Dedicated Vector Database

Reason

PostgreSQL with pgvector is sufficient for the current scale and learning goals.

Migration remains possible in the future.

---

## Fine-Tuning

Reason

The project focuses on Retrieval-Augmented Generation.

Fine-tuning introduces different tradeoffs and learning objectives.

---

# Success Criteria

The project should evolve because real requirements demand it—not because new technologies become popular.

Every future feature should have a clear purpose, measurable value, and a documented reason for being added.

Avoid building features solely because they are trendy.

Engineering discipline includes knowing what **not** to build.
