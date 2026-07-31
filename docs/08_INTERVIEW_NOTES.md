# Interview Notes

**Project:** AI Knowledge Platform
**Document:** Interview Preparation Notes
**Status:** Living Document

---

# Purpose

This document captures the engineering knowledge gained while building this project.

It is not intended to be a collection of generic interview questions.

Instead, it documents the reasoning, tradeoffs, and lessons learned from **this implementation**.

After every significant feature, this document should be updated.

If a design decision cannot be explained here, it probably wasn't understood well enough.

---

# Interview Strategy

When discussing this project during interviews, focus on:

- Why the problem exists.
- Why the chosen solution was selected.
- What alternatives were considered.
- What tradeoffs were accepted.
- What would change in production.

Avoid simply describing the implementation.

Interviewers are evaluating engineering judgment.

---

# Project Overview

Be able to explain the project in under two minutes.

Example structure

1. What problem does the project solve?
2. What technologies are used?
3. How does the system work at a high level?
4. What engineering challenges were solved?
5. What would you improve with more time?

---

# High-Level Architecture

Be prepared to explain:

- Why layered architecture was chosen.
- Why responsibilities are separated.
- How requests move through the system.
- Why provider abstraction exists.
- Why AI logic is isolated.

Expected discussion

Explain responsibilities instead of listing technologies.

---

# Backend Engineering

Be prepared to discuss:

- FastAPI
- Dependency injection
- Service layer
- Repository layer
- Configuration management
- Error handling
- Logging
- Testing
- Migrations

Example questions

Why did you separate services and repositories?

Why not put everything in the route handlers?

How would your architecture change for a much larger team?

---

# Database

Topics

- PostgreSQL
- pgvector
- Migrations
- Indexing
- Transactions

Example questions

Why PostgreSQL instead of MongoDB?

Why pgvector instead of Qdrant?

When would you migrate to a dedicated vector database?

What are the limitations of pgvector?

---

# Document Processing

Topics

- Upload pipeline
- Parsing
- Chunking
- Metadata

Example questions

How do you process uploaded documents?

Why split documents into chunks?

How do you choose chunk size?

What problems does chunk overlap solve?

---

# Embeddings

Topics

- Embedding generation
- Similarity search
- Retrieval

Example questions

What are embeddings?

Why not use keyword search?

Why generate embeddings once instead of on every request?

How do embedding models differ?

---

# Retrieval-Augmented Generation (RAG)

Topics

- Retrieval
- Context building
- Generation
- Hallucination reduction

Example questions

Explain the RAG pipeline.

Why use RAG instead of fine-tuning?

How do you reduce hallucinations?

How do you determine the number of retrieved chunks?

---

# Prompt Engineering

Topics

- Prompt templates
- Context injection
- Prompt organization

Example questions

How are prompts managed?

Why aren't prompts hardcoded throughout the application?

How do you improve prompts over time?

---

# Provider Abstraction

Topics

- Interfaces
- Adapters
- Vendor lock-in

Example questions

Why did you abstract the LLM provider?

What challenges arise when supporting multiple providers?

What provider-specific features are difficult to abstract?

---

# Streaming

Topics

- Streaming responses
- User experience
- Async programming

Example questions

Why stream responses?

How does streaming improve perceived performance?

What implementation challenges exist?

---

# Conversation Memory

Topics

- Chat history
- Context windows
- Summarization

Example questions

Why can't you send the entire conversation every time?

How do you manage long conversations?

What are the tradeoffs of summarization?

---

# Tool Calling

Topics

- Function schemas
- Tool execution
- Validation

Example questions

What is tool calling?

How is it different from RAG?

How do you validate tool results?

---

# AI Agents

Topics

- Planning
- Tool orchestration
- Agent loops

Example questions

What distinguishes an AI agent from a chatbot?

When is an agent unnecessary?

How do you prevent infinite tool loops?

---

# Model Context Protocol (MCP)

Topics

- MCP clients
- MCP servers
- Tool interoperability

Example questions

What problem does MCP solve?

How is MCP different from a REST API?

Why might organizations adopt MCP?

---

# Software Engineering

Topics

- TDD
- Refactoring
- Architecture
- Documentation

Example questions

Why did you use TDD?

How did documentation influence development?

How did you avoid overengineering?

---

# Scaling Discussions

Be prepared to answer:

How would this architecture change if:

- One million documents were stored?
- Multiple organizations used the platform?
- Multiple AI providers were active simultaneously?
- Documents exceeded current context limits?
- OCR became a requirement?
- Real-time collaboration was introduced?

Focus on architectural evolution rather than immediate implementation.

---

# Common Tradeoff Discussions

Every major decision should have a tradeoff.

Examples

Provider abstraction

Pros

- Flexibility
- Testing
- Vendor independence

Cons

- Additional complexity
- More code to maintain

Repeat this thought process for every architectural decision.

---

# Common Mistakes to Avoid

Do not claim the system is production-ready unless it genuinely is.

Do not overstate scalability.

Do not exaggerate AI capabilities.

Do not hide limitations.

Strong engineers acknowledge tradeoffs.

---

# After Every Milestone

Update this document with:

- New interview questions
- Better explanations
- New tradeoffs
- Lessons learned
- Production considerations

Interview preparation should happen continuously throughout development.

---

# Final Objective

At the end of the project, I should be able to explain every major engineering decision without referring to the code.

The implementation demonstrates technical ability.

The explanation demonstrates engineering maturity.

Both are required for a strong interview.
