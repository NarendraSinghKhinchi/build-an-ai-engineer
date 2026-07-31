# Learning Goals

**Project:** AI Knowledge Platform
**Document:** Learning Goals
**Status:** Living Document

---

# Purpose

This project exists to develop practical AI engineering skills through the design and implementation of a production-quality backend.

The objective is not simply to build a working application.

The objective is to understand the reasoning behind every engineering decision and become capable of applying those principles to future projects.

Every milestone should contribute to this goal.

---

# Success Definition

This project is successful if, after completing it, I can confidently:

- Design an AI backend from scratch.
- Explain architectural decisions.
- Discuss engineering tradeoffs.
- Build Retrieval-Augmented Generation (RAG) systems.
- Work with multiple LLM providers.
- Design scalable APIs.
- Build maintainable backend services.
- Debug AI applications.
- Evaluate AI frameworks critically.
- Confidently discuss the project during technical interviews.

A working application alone is **not** considered success.

---

# Engineering Goals

By the end of the project I should understand:

## Backend Architecture

- Layered architecture
- Separation of concerns
- Dependency injection
- Repository pattern
- Service layer
- Configuration management
- Background processing
- Modular application design

Success Criteria

I can explain why each architectural layer exists and what responsibilities belong in it.

---

## API Design

Topics

- REST principles
- Request validation
- Error handling
- API versioning
- Asynchronous endpoints
- File uploads
- Streaming responses

Success Criteria

I can design consistent APIs without relying on examples.

---

## Database Design

Topics

- Relational modeling
- PostgreSQL
- Migrations
- Indexing
- Transactions
- Query optimization
- Vector storage using pgvector

Success Criteria

I understand when relational data and vector data should coexist.

---

# AI Engineering Goals

## Embeddings

Learn

- What embeddings are.
- Why they work.
- Similarity search.
- Embedding models.
- Embedding tradeoffs.

Success Criteria

I can explain embeddings without using buzzwords.

---

## Chunking

Learn

- Fixed-size chunking.
- Recursive chunking.
- Semantic chunking.
- Chunk overlap.
- Token limits.

Success Criteria

I can justify a chunking strategy for a specific use case.

---

## Retrieval-Augmented Generation (RAG)

Learn

- Retrieval pipeline.
- Context construction.
- Ranking.
- Grounding.
- Hallucination reduction.

Success Criteria

I can design and implement a complete RAG pipeline without following a tutorial.

---

## Prompt Engineering

Learn

- Prompt structure.
- System prompts.
- Prompt templates.
- Context injection.
- Output formatting.
- Prompt versioning.

Success Criteria

I understand prompts as part of the application architecture rather than simple strings.

---

## Large Language Models

Learn

- Context windows.
- Tokenization.
- Temperature.
- Model selection.
- Provider differences.
- Cost considerations.

Success Criteria

I can choose an appropriate model for a given problem and explain why.

---

## Provider Abstraction

Learn

- Adapter pattern.
- Vendor lock-in.
- Capability differences.
- Interface design.

Success Criteria

I can switch providers without changing business logic.

---

## Streaming

Learn

- Streaming responses.
- Server-Sent Events.
- Incremental generation.
- User experience considerations.

Success Criteria

I understand both the implementation and the user-facing benefits of streaming.

---

## Conversation Management

Learn

- Chat history.
- Memory strategies.
- Context selection.
- Token budgeting.
- Conversation summarization.

Success Criteria

I can explain why long conversations require memory management.

---

## Tool Calling

Learn

- Function calling.
- Tool schemas.
- Tool execution.
- Validation.
- Error handling.

Success Criteria

I can build reliable tool integrations for an LLM.

---

## AI Agents

Learn

- Planning.
- Reasoning loops.
- Tool orchestration.
- Reflection.
- Agent architecture.

Success Criteria

I understand when an agent is appropriate and when simple RAG is sufficient.

---

## Model Context Protocol (MCP)

Learn

- MCP concepts.
- MCP clients.
- MCP servers.
- Resource discovery.
- Tool interoperability.

Success Criteria

I can explain how MCP differs from traditional API integrations.

---

# Software Engineering Goals

Throughout the project I will practice:

- Test-Driven Development
- Refactoring
- Code reviews
- Documentation-first development
- Architecture discussions
- Incremental delivery

Success Criteria

The project should reflect professional engineering practices rather than tutorial code.

---

# Interview Goals

By the end of the project I should confidently answer questions such as:

- Why RAG instead of fine-tuning?
- Why embeddings instead of keyword search?
- Why pgvector?
- Why provider abstraction?
- Why layered architecture?
- How would this scale?
- What are the limitations of your implementation?
- How would you reduce hallucinations?
- Why did you choose FastAPI?
- How would you support multiple document types?
- How would you introduce authentication later?
- How would you migrate to a dedicated vector database?

If I cannot explain a major design decision, I have not learned it well enough.

---

# Learning Principles

When introducing a new concept:

1. Understand the problem first.
2. Learn the underlying theory.
3. Implement a minimal solution.
4. Evaluate tradeoffs.
5. Refactor if necessary.
6. Reflect on what was learned.

Avoid memorizing APIs without understanding the motivation behind them.

---

# Project Milestones

Each completed milestone should improve at least one of the following:

- Engineering knowledge
- AI knowledge
- System design skills
- Communication skills
- Interview readiness

A milestone that only adds features without increasing understanding should be reconsidered.

---

# Reflection

At the end of each milestone, ask:

- What problem did this solve?
- Why was this approach chosen?
- What alternatives exist?
- What tradeoffs were accepted?
- How would this change at 10x scale?
- What interview questions could be asked about this feature?

Document the answers while they are fresh.

---

# Final Goal

By the end of this project, I should be able to sit in a backend or AI engineering interview and discuss this project with confidence.

I should be able to explain not only **what** I built, but **why** I built it that way, what alternatives I considered, and how I would evolve it for production use.

The project should represent engineering maturity, not just technical implementation.
