
# Coding Standards

**Project:** AI Knowledge Platform
**Document:** Engineering Standards
**Status:** Living Document

---

# Purpose

This document defines how code should be written, organized, reviewed, and maintained throughout the project.

The goal is consistency—not perfection.

Every engineer (human or AI) should produce code that feels like it belongs to the same codebase.

Formatting tools enforce syntax.

This document defines engineering judgment.

---

# Core Philosophy

Code is read far more often than it is written.

Optimize for the next engineer reading the code.

Assume they know Python.

Do not assume they know your thought process.

The code should explain itself.

---

# Engineering Priorities

When making implementation decisions, optimize in this order.

1. Correctness
2. Readability
3. Simplicity
4. Maintainability
5. Testability
6. Extensibility
7. Performance

Never sacrifice readability for micro-optimizations.

---

# Project Structure

Every file should have a clear responsibility.

Avoid dumping unrelated functionality into existing modules.

If a file begins serving multiple unrelated purposes, split it.

Folders should communicate intent.

Avoid generic folders such as

```
utils/
helpers/
misc/
common/
```

unless they contain functionality that is genuinely shared across multiple domains.

---

# Layer Responsibilities

## API Layer

Responsible for

- HTTP
- validation
- serialization
- dependency injection

Must never contain

- business logic
- SQL
- prompt construction
- provider SDK calls

---

## Service Layer

Responsible for

- business workflows
- orchestration
- coordination

Must not know

- HTTP
- SQL syntax
- provider SDK details

---

## Repository Layer

Responsible only for persistence.

Never implement business rules here.

Repositories answer questions such as

- Save
- Update
- Delete
- Find

They do not decide *why*.

---

## AI Layer

Responsible for

- prompts
- embeddings
- retrieval
- generation
- tool execution

The AI layer should expose business capabilities.

It should never expose provider-specific SDK behavior.

---

# Naming

Names should communicate intent.

Prefer

```
DocumentRepository
ConversationService
EmbeddingGenerator
PromptBuilder
```

Avoid

```
Manager
Helper
Processor
Handler
Utility
Thing
DataManager
```

If a name is vague, the abstraction is probably vague.

---

# Functions

Functions should do one thing.

Good functions

- are easy to test
- have descriptive names
- minimize side effects
- have clear inputs
- have clear outputs

Avoid functions that require scrolling to understand.

---

# Classes

Create classes when they model behavior.

Do not create classes simply because a language supports them.

Prefer composition.

Avoid deep inheritance.

---

# Dependency Injection

Dependencies should be injected.

Avoid creating dependencies inside business logic.

Good

```
DocumentService(repository, parser)
```

Avoid

```
DocumentService()

service creates repository

repository creates database

database creates provider
```

Hidden dependencies make testing difficult.

---

# Configuration

Configuration belongs outside application code.

Never hardcode

- model names
- API keys
- URLs
- ports
- file paths

Configuration should be centralized.

---

# Error Handling

Raise meaningful exceptions.

Avoid generic exceptions.

Prefer domain-specific exceptions.

Handle errors close to their source.

Never silently ignore failures.

---

# Logging

Logs should explain

- what happened
- why it happened
- where it happened

Avoid

- debug spam
- duplicated logs
- sensitive information

Logs should help operators, not just developers.

---

# Comments

Comments explain *why*.

Code explains *how*.

Avoid comments that simply repeat the code.

Bad

```
# Increment counter
counter += 1
```

Good

```
# Retry because the provider occasionally returns transient failures.
```

---

# Documentation

Public modules should be understandable without reading implementation details.

Complex workflows deserve documentation.

Do not document the obvious.

Document decisions.

---

# AI-Specific Standards

Prompt templates belong in dedicated modules.

Never construct prompts throughout the codebase.

Retrieval should remain independent of generation.

Providers should remain independent of business logic.

Embedding generation should remain independently testable.

---

# Database Standards

Repositories own persistence.

Business logic should not write SQL.

Schema changes require migrations.

Avoid leaking ORM models into unrelated layers.

---

# Testing Standards

Tests are first-class citizens.

Business logic must be tested.

Edge cases matter.

Failure cases matter.

Avoid testing framework internals.

Prefer behavior over implementation details.

Tests should remain readable.

---

# Refactoring

Refactor when

- duplication appears
- complexity increases
- responsibilities blur
- testing becomes difficult

Do not refactor purely because a different style is preferred.

---

# External Dependencies

Every dependency introduces maintenance cost.

Before adding a dependency ask

- Does the standard library solve this?
- Can existing project code solve this?
- Is the dependency actively maintained?
- Is it widely adopted?
- Is it worth the operational cost?

Favor fewer dependencies.

---

# Performance

Measure before optimizing.

Document significant optimizations.

Never make code harder to understand for hypothetical performance gains.

---

# Code Reviews

Before considering work complete ask

- Is the code easy to understand?
- Is the architecture respected?
- Is it testable?
- Is it documented?
- Is it maintainable?
- Can this be simpler?

---

# Engineering Principle

Every commit should improve one or more of the following

- clarity
- correctness
- maintainability
- testability
- scalability
- developer understanding

Avoid commits that merely increase complexity.

---

# Final Rule

If another engineer cannot understand your implementation within a few minutes, the implementation should be simplified.

Readable code scales better than clever code.