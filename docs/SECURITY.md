# Security and Data Policy

Agentic Commerce Swarm is an experimental multi-agent workbench. It can generate business-facing artifacts and propose website changes, so security and reviewability are part of the project design.

## Core principles

- Do not commit secrets.
- Do not commit raw customer data.
- Do not publish private business artifacts without sanitization.
- Do not apply AI-generated changes to real assets without human review.
- Prefer deterministic changes over probabilistic full-file rewrites.
- Preserve audit trails for important runs.

## Secrets

Secrets must live only in local environment files such as `.env`.

Allowed in Git:

```env
OPENAI_API_KEY="your_api_key_here"
```

Not allowed in Git:

```env
OPENAI_API_KEY="real_key"
GEMINI_API_KEY="real_key"
DATABASE_URL="real_private_database_url"
```

If a secret is ever committed or pasted into a transcript:

1. Remove it from the repository/history or redact it from public materials.
2. Rotate the key with the provider.
3. Add or improve `.gitignore` rules.
4. Record the incident privately.

## Business data

Before making the repo public, sanitize:

- company names;
- customer names;
- phone numbers;
- emails;
- local file paths;
- campaign outputs based on real businesses;
- transcripts and chat exports;
- screenshots with private information.

Use fictional demo data in public examples.

## Human-in-the-loop approval

The project should not be treated as an autonomous production editor.

Any proposed change to a real website, campaign or customer-facing asset must pass through:

```text
agent output
↓
QA review
↓
human review
↓
versioned proposal
↓
intentional apply/deploy
```

## Public release checklist

- [ ] `.env` removed and ignored.
- [ ] `.env.example` contains placeholders only.
- [ ] local paths replaced with generic paths.
- [ ] business-specific data anonymized.
- [ ] outputs moved to sanitized examples.
- [ ] raw transcripts excluded.
- [ ] generated files, backups and vector DB stores excluded.
- [ ] README states prototype status honestly.
