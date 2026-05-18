# Agentic Commerce Swarm

[![Tests](https://github.com/clawmerio/agentic-commerce-swarm/actions/workflows/tests.yml/badge.svg)](https://github.com/clawmerio/agentic-commerce-swarm/actions/workflows/tests.yml)

> Multi-agent commercial orchestration workbench built with LangGraph, LLM agents, persistent memory, quality review and human-in-the-loop approval.

## Overview

**Agentic Commerce Swarm** is an experimental multi-agent workbench for commercial automation, marketing operations and conversion-focused website improvement.

The project explores how a coordinated group of AI agents can transform a high-level business request into a structured campaign proposal while preserving safety, reviewability and role separation.

Instead of using a single chatbot to generate generic content, Agentic Commerce Swarm uses a staged pipeline of specialized agents:

```text
User request
↓
Squad Lead
↓
Diagnostician
↓
Strategist
↓
Copywriter
↓
Sanitizer
↓
Analyst
↓
Designer
↓
WebDev
↓
QA Auditor
↓
Human-in-the-loop approval
```

## Why this project matters

Most LLM automations fail because they mix strategy, copywriting, design, implementation and approval in a single unstructured conversation.

This project separates those responsibilities into explicit agent roles and adds:

- persistent memory;
- quality review;
- compliance/safety checks;
- deterministic site-change workflow;
- human approval before real changes;
- versioned outputs for auditability.

The result is a practical prototype for **agentic business operations**, not just prompt-based content generation.

---

## Current status

This repository should be treated as a **functional prototype / experimental workbench**, not a production SaaS.

| Area | Status |
|---|---|
| Multi-agent pipeline | Implemented |
| CLI workflow | Implemented |
| Persistent memory | Implemented / evolving |
| Quality review loop | Implemented / needs stronger tests |
| Sanitizer / compliance layer | Implemented as a pipeline role |
| Human-in-the-loop approval | Implemented conceptually and operationally |
| Rubric-based evaluation | Partial / roadmap |
| Public demo dataset | Roadmap |
| Visual Kanban handoff UI | Roadmap |
| Production deployment | Roadmap |

---

## Architecture

### Agent roles

| Agent | Responsibility |
|---|---|
| Squad Lead | Converts the user request into a conservative internal brief |
| Diagnostician | Reviews current context and previous outputs before strategy |
| Strategist | Defines the narrowest conversion path supported by evidence |
| Copywriter | Produces approved campaign and website copy |
| Sanitizer | Checks unsafe, non-compliant or risky content |
| Analyst | Scores quality and can force revision loops |
| Designer | Defines layout and visual direction without inventing copy |
| WebDev | Maps approved copy into website-change proposals |
| QA Auditor | Challenges the full pipeline before human review |
| HITL | Final human decision point before real-world changes |

### Runtime flow

```text
main.py
├── loads environment
├── initializes LLMs
├── initializes persistent memory
├── builds the agent pipeline
├── executes agent nodes
├── saves versioned outputs
└── returns final report for human review
```

### Memory layer

The memory layer is designed to preserve learning across runs.

Current memory categories include:

- approved campaigns;
- rejected outputs and reasons;
- strategies;
- web development proposals.

This allows the swarm to avoid repeating weak patterns and reuse stronger historical decisions.

---

## Tech stack

- Python
- LangGraph
- LangChain
- OpenAI-compatible chat models
- ChromaDB
- python-dotenv
- Rich CLI utilities
- pytest for minimal validation

See [`requirements.txt`](requirements.txt) and [`requirements-dev.txt`](requirements-dev.txt) for dependencies.

---

## Repository structure

```text
.
├── main.py                     # Main orchestrator
├── squad.py                    # Interactive CLI entrypoint
├── memory.py                   # ChromaDB memory layer
├── requirements.txt            # Python dependencies
├── requirements-dev.txt        # Test dependencies
├── .env.example                # Safe environment template
├── docs/
│   ├── ARCHITECTURE.md         # Architecture notes
│   ├── WORKFLOW.md             # Development workflow
│   ├── ROADMAP.md              # Current and future scope
│   ├── SECURITY.md             # Secrets and data policy
│   └── HANDOFF_MODEL.md        # Logical agent handoff
├── examples/
│   ├── demo-site/              # Fictional demo website
│   └── sanitized-runs/         # Public-safe examples
└── tests/                      # Minimal smoke/unit tests
```

---

## Setup

Create a local environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\\Scripts\\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For development and tests:

```bash
pip install -r requirements-dev.txt
pytest
```

Create your local environment file:

```bash
cp .env.example .env
```

Then add your own API key locally:

```env
OPENAI_API_KEY="your_api_key_here"
```

Run the interactive CLI:

```bash
python squad.py
```

---

## Demo artifact

A sanitized example run is available at:

```text
examples/sanitized-runs/demo_run.md
```

It uses fictional data and demonstrates the expected structure of a full pipeline output without exposing private business information.

---

## Safety model

This project is designed around the idea that AI-generated business changes should be reviewed before being applied.

Core safety principles:

- no credentials in Git;
- no direct production edits without human review;
- copy, design and web implementation should remain separate roles;
- outputs should be saved as artifacts before being promoted;
- raw business data must be sanitized before publication;
- historical transcripts should not override verified code.

---

## What this repository is good for

This repo is useful as a portfolio case for:

- AI automation engineering;
- multi-agent orchestration;
- LangGraph pipelines;
- LLM memory systems;
- human-in-the-loop workflows;
- commercial automation;
- AI-assisted website optimization;
- quality and compliance layers for agentic systems.

---

## Curriculum positioning

**Project title:** Agentic Commerce Swarm  
**Short description:** Multi-agent commercial orchestration workbench built with LangGraph, ChromaDB memory, specialized LLM agents, QA review and human-in-the-loop approval.

Example resume bullet:

> Built a LangGraph-based multi-agent workbench for commercial automation, combining specialized LLM agents, persistent ChromaDB memory, quality review, compliance checks and human-in-the-loop approval before website-change proposals.

---

## Important note

This repository is a curated and sanitized portfolio version. It intentionally avoids exposing private paths, credentials, raw customer data or business-sensitive artifacts.

If real-world examples are added, use sanitized demo data only.
