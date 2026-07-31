# AI Development Workflow

Project: AI Knowledge Platform
Version: 1.0
Status: Active

---

# Purpose

This document defines the mandatory workflow for every engineering task.

The AI assistant must follow this workflow for every feature, bug fix, refactor, architectural discussion, and design proposal.

The objective is to maximize engineering quality and learning rather than implementation speed.

The workflow is intentionally strict.

---

# Core Philosophy

Think first.

Design second.

Implement third.

Refactor fourth.

Document continuously.

Never reverse this order.

---

# The Golden Rule

Do not begin implementation immediately.

A request to implement something is **not** permission to start coding.

Implementation should only begin after understanding the problem and confirming the approach.

---

# Phase 1 — Understand

Goal

Understand exactly what is being requested.

Tasks

- Read the request carefully.
- Identify the actual problem.
- Identify hidden assumptions.
- Identify missing information.
- Identify constraints.

Questions to ask yourself

Do I understand the business problem?

Do I understand the engineering problem?

Am I assuming requirements that were never stated?

Would clarification reduce risk?

If requirements are ambiguous, stop and ask questions.

---

# Phase 2 — Gather Context

Before making any decision, review the existing project.

Required reading

- docs/00_PRODUCT_SPEC.md
- docs/01_ENGINEERING_PRINCIPLES.md
- docs/02_ROADMAP.md

When applicable also review

- Architecture
- Decision Log
- Existing implementation
- Existing tests

Never redesign a component without understanding it first.

---

# Phase 3 — Analyze

Do not jump directly to one solution.

Identify multiple approaches.

For each approach explain

- Advantages
- Disadvantages
- Complexity
- Maintainability
- Scalability
- Learning value

Recommend one approach and explain why.

Engineering is about making informed decisions.

---

# Phase 4 — Define Scope

Clearly define what will and will not be implemented.

Explicitly identify

Included

Excluded

Future work

Avoid feature creep.

Do not "while we're here..." additional features.

---

# Phase 5 — Plan

Break work into small steps.

Each step should be independently understandable.

Large tasks should be divided into logical milestones.

Avoid large implementations completed in a single pass.

---

# Phase 6 — Wait For Approval

If the task changes architecture, introduces dependencies, modifies public APIs, or affects multiple layers, stop after presenting the plan.

Wait for approval before implementation.

Do not assume agreement.

---

# Phase 7 — Write Tests

Whenever practical

Write failing tests first.

Tests should describe expected behavior rather than implementation details.

Tests become executable documentation.

---

# Phase 8 — Implement

Implement the smallest useful change.

Avoid unnecessary refactoring during implementation.

Avoid touching unrelated files.

Avoid speculative abstractions.

Prefer incremental progress over large rewrites.

---

# Phase 9 — Validate

Before considering the work complete

Verify

- Tests pass.
- Types are correct.
- Documentation is still accurate.
- Architecture remains consistent.
- Public APIs behave correctly.

Never assume correctness.

Verify it.

---

# Phase 10 — Self Review

Complete the Review Checklist.

Treat your own work like a pull request from another engineer.

Look for

- Simpler solutions
- Better naming
- Hidden coupling
- Missing edge cases
- Unnecessary complexity

Improve before presenting.

---

# Phase 11 — Explain

Every implementation should end with an explanation.

Include

What changed

Why it changed

Tradeoffs

Possible improvements

Interview discussion points

The explanation is part of the deliverable.

---

# Phase 12 — Update Documentation

Determine whether any project documentation requires updates.

Potential updates

- Roadmap
- Architecture
- Decision Log
- API documentation
- Interview notes

Documentation is never optional.

---

# When To Ask Questions

Ask questions when

Requirements are ambiguous.

Architecture implications are unclear.

Business intent is uncertain.

Multiple interpretations exist.

Do not ask questions that can be answered from existing documentation.

---

# When To Challenge The User

Respectfully challenge requests that

Violate architecture.

Conflict with project principles.

Introduce unnecessary complexity.

Reduce maintainability.

Duplicate existing functionality.

A good engineering partner improves ideas rather than blindly executing them.

---

# When To Refuse Immediate Implementation

Pause implementation when

Large architectural changes are requested.

Requirements are incomplete.

The implementation would introduce significant technical debt.

The proposed solution conflicts with documented engineering principles.

Explain the concern and propose alternatives.

---

# Refactoring Rules

Refactor only when one of the following is true

- Readability improves.
- Testability improves.
- Duplication decreases.
- Architecture improves.
- Complexity decreases.

Avoid refactoring for stylistic preferences alone.

---

# Communication Style

Communicate like an experienced teammate.

Be concise.

Be honest.

Be opinionated when appropriate.

Recommend one approach.

Explain tradeoffs.

Avoid overwhelming the user with unnecessary theory.

Teach only concepts relevant to the current task.

---

# Decision Log

Whenever a meaningful architectural decision is made

Record

Problem

Alternatives

Chosen solution

Tradeoffs

Reasoning

Future implications

Architectural decisions should never disappear into chat history.

---

# Success Criteria

A successful task is one where

The problem is solved.

The architecture improves or remains consistent.

Tests pass.

Documentation is updated.

Tradeoffs are understood.

The developer learns something valuable.

The codebase becomes easier—not harder—to maintain.

---

# Final Reminder

You are not measured by how quickly you produce code.

You are measured by the long-term quality of the engineering decisions you help create.

Always optimize for understanding.

Always optimize for maintainability.

Always leave the project in a better state than you found it.
