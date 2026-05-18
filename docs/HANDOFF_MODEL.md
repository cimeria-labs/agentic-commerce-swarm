# Handoff Model

This document describes the logical handoff model used by Agentic Commerce Swarm.

A visual Kanban handoff UI is a roadmap item. The current public version focuses on the logical agent handoff.

## Current logical handoff

```text
User
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
Human Review
```

## Agent contracts

| From | To | Artifact passed | Main constraint |
|---|---|---|---|
| User | Squad Lead | Raw request | Preserve intent |
| Squad Lead | Diagnostician | Internal brief | Do not invent context |
| Diagnostician | Strategist | Evidence-based diagnosis | Strategy must follow evidence |
| Strategist | Copywriter | Strategic direction | Copy must match approved strategy |
| Copywriter | Sanitizer | Draft copy | Reject unsafe or non-compliant content |
| Sanitizer | Analyst | Sanitized copy | Score quality and force revisions when needed |
| Analyst | Designer | Approved copy + quality notes | Designer must not invent copy |
| Designer | WebDev | Visual/layout brief | WebDev must use approved copy only |
| WebDev | QA Auditor | Website-change proposal | Must be reviewable |
| QA Auditor | Human | Final report | Challenge claims before approval |

## Revision loop

```text
Copywriter
↓
Sanitizer
↓
Analyst
├── approve → Designer
└── revise  → Copywriter or Strategist
```

The system should prefer a conservative revision loop over silently promoting weak output.

## Future visual handoff

A future UI can represent each agent as a stage in a board:

```text
Backlog → Brief → Diagnosis → Strategy → Copy → Safety → QA → Web Proposal → Human Review → Approved
```

Useful UI features:

- card per request;
- visible current owner;
- status by agent;
- revision count;
- confidence score;
- QA blockers;
- artifact links;
- human approval button;
- rollback link.
