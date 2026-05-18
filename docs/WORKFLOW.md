# Workflow

## Development workflow

1. Create a branch for each change.
2. Keep changes small and reviewable.
3. Do not commit secrets or raw business data.
4. Prefer sanitized examples over real outputs.
5. Review diffs before merging.

## Run workflow

1. Define a commercial task.
2. Run the CLI:

```bash
python squad.py
```

3. Review the generated artifact in `data/outputs/`.
4. Treat the output as a proposal, not a production change.
5. Promote only safe, reviewed examples to `examples/sanitized-runs/`.

## Human-in-the-loop workflow

```text
Agent output
↓
QA report
↓
Human review
↓
Approved artifact
↓
Manual implementation or controlled apply
```

## Documentation workflow

Update docs when behavior changes.

Recommended docs:

- `docs/ARCHITECTURE.md`
- `docs/HANDOFF_MODEL.md`
- `docs/SECURITY.md`
- `docs/ROADMAP.md`
