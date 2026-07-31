# System Architecture

**Project:** AI Knowledge Platform
**Document:** System Architecture
**Version:** 1.0
**Status:** Living Document

---

# Purpose

This document describes the high-level architecture of the AI Knowledge Platform.

It explains:

- System boundaries
- Architectural layers
- Dependency direction
- Major components
- Data flow
- Design principles

This document intentionally avoids implementation details.

Implementation belongs in code.

Architecture belongs here.

---

# Architectural Philosophy

The system follows a layered architecture.

Each layer has a single responsibility.

Layers communicate only through well-defined interfaces.

Business logic remains independent from infrastructure.

Infrastructure can change without changing business logic.

---

# High-Level Architecture

                        Client
                           │
                           ▼
                    FastAPI Routes
                           │
                           ▼
                    Application Services
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   Document Service   Chat Service   Retrieval Service
         │                 │                 │
         └──────────────┬──┴─────────────────┘
                        ▼
                  Domain Components
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   Repository      AI Provider      File Storage
        │               │                │
        ▼               ▼                ▼
 PostgreSQL        OpenAI/Groq/...    Local/S3

---

# Architectural Layers

## 1. API Layer

Purpose

Expose HTTP endpoints.

Responsibilities

- Request validation
- Response formatting
- Dependency injection
- HTTP status codes

Must NOT

- Write SQL
- Build prompts
- Generate embeddings
- Call provider SDKs directly
- Contain business logic

Think of this layer as a translator between HTTP and the application.

---

## 2. Application Layer

Purpose

Coordinate business workflows.

Responsibilities

- Use cases
- Orchestration
- Transactions
- Service coordination

Examples

Upload document.

Create conversation.

Answer question.

Delete document.

This is where business behavior lives.

---

## 3. Domain Layer

Purpose

Represent the core concepts of the application.

Examples

Document

Conversation

Message

Chunk

Embedding

RetrievalResult

The domain should not know

FastAPI

SQLAlchemy

OpenAI

pgvector

HTTP

---

## 4. Repository Layer

Purpose

Persist and retrieve data.

Responsibilities

Database interaction only.

Repositories own

- queries
- inserts
- updates
- deletes

Repositories do NOT

- construct prompts
- call LLMs
- make business decisions

---

## 5. AI Layer

Purpose

Encapsulate all AI-related functionality.

Responsibilities

Prompt construction

Embedding generation

Provider abstraction

Generation

Retrieval orchestration

Tool calling

Agent logic (future)

The AI layer should expose business capabilities rather than provider-specific APIs.

---

## 6. Infrastructure Layer

Purpose

Interact with external systems.

Examples

PostgreSQL

LLM Providers

Storage

Logging

Configuration

Infrastructure is replaceable.

Business logic should remain unaware of implementation details.

---

# Dependency Rule

Dependencies always point inward.

Correct

API

↓

Application

↓

Domain

↓

Repository / AI Interfaces

↓

Infrastructure

Incorrect

API

↓

Database

or

Application

↓

OpenAI SDK

or

Route

↓

SQLAlchemy

or

Route

↓

Prompt Builder

These shortcuts create tight coupling.

---

# Core Components

## Document Pipeline

Responsibilities

Upload

Store

Parse

Chunk

Embed

Persist

Future

OCR

DOCX

Images

Web Pages

---

## Retrieval Pipeline

Responsibilities

Receive user query.

Generate query embedding.

Perform vector search.

Rank results.

Return relevant context.

Retrieval should remain independently testable.

---

## Generation Pipeline

Responsibilities

Build prompt.

Inject retrieved context.

Call provider.

Return structured response.

Generation should never perform retrieval directly.

---

## Conversation Pipeline

Responsibilities

Store messages.

Manage history.

Control context size.

Prepare conversation state.

Future

Summaries

Memory

Compression

---

# AI Provider Architecture

The application should never depend directly on a provider.

Instead

Application

↓

LLM Interface

↓

Provider Adapter

↓

Provider SDK

Supported providers may include

OpenAI

Anthropic

Groq

Gemini

Local models

Changing providers should not affect business logic.

---

# Storage Strategy

Initially

Local filesystem

Later

Object storage

The application should depend on a storage abstraction rather than a specific storage implementation.

---

# Retrieval Architecture

Retrieval consists of independent stages.

Query

↓

Embedding

↓

Vector Search

↓

Ranking

↓

Context Selection

↓

Generation

Each stage should be independently testable and replaceable.

---

# Error Boundaries

Errors should be handled as close as possible to their source.

API

HTTP errors

Application

Business errors

Repository

Persistence errors

Infrastructure

External service errors

Avoid generic exception handling at the top of the stack.

---

# Cross-Cutting Concerns

The following concerns apply across all layers.

Logging

Configuration

Validation

Observability

Testing

These should remain consistent throughout the project.

---

# Future Evolution

The architecture is intentionally designed to support future capabilities.

Potential additions

- Property brochures
- OCR
- Multi-document retrieval
- AI Agents
- Tool Calling
- MCP
- Background workers
- Event-driven processing

These features should integrate naturally without requiring major architectural changes.

---

# Architectural Goals

The architecture should remain

Simple

Modular

Replaceable

Testable

Observable

Provider Agnostic

Easy to understand

Easy to extend

---

# Architecture Is a Living Document

This document should evolve as the system evolves.

When significant architectural decisions are made, update this document accordingly.

The architecture should describe the system as it exists today—not as it existed months ago.