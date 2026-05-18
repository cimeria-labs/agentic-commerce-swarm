# Roadmap

This roadmap separates what is already implemented, what is partially implemented and what should be treated as future work.

## Implemented in this curated repo

| Area | Notes |
|---|---|
| Multi-agent orchestration | Public-safe staged pipeline in `main.py` |
| CLI entrypoint | Interactive workflow in `squad.py` |
| Persistent memory | ChromaDB-backed memory layer with graceful fallback |
| Output artifact generation | Runs saved as Markdown artifacts |
| Human-in-the-loop concept | Workflow centered on review before changes |
| Safety/compliance role | Sanitizer included as pipeline role |
| QA role | QA Auditor included as final challenge layer |
| Security policy | `docs/SECURITY.md` |
| Handoff model | `docs/HANDOFF_MODEL.md` |

## Partially implemented

| Area | Gap |
|---|---|
| Rubric-based evaluation | Needs structured rubric files and integration |
| Deterministic apply flow | Currently proposal-only in public version |
| Memory quality loop | Memory stores runs, but promotion rules need refinement |
| Tests | Smoke tests should be added |
| Demo site analysis | Demo site exists but can be expanded |

## Not included in this curated version

- private business data;
- raw campaign outputs;
- local machine paths;
- real customer/contact data;
- visual Kanban UI;
- daemon mode;
- production deployment scripts.

## P0 — Portfolio readiness

- Add safe demo run artifacts.
- Add smoke tests.
- Add one architecture diagram.
- Add screenshots only if sanitized.

## P1 — Engineering maturity

- Add typed configuration.
- Add test fixtures.
- Add role-separation regression tests.
- Add cost/token logging.
- Add structured run metadata.

## P2 — Product evolution

- Add visual Kanban handoff UI.
- Add daemon/background mode.
- Add web dashboard.
- Add provider fallback.
- Add deployment guide.

## Long-term vision

```text
Business request
↓
Agentic diagnosis
↓
Strategy and content generation
↓
Safety and QA
↓
Human approval
↓
Versioned execution
↓
Measurement and memory feedback
```
