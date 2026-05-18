# Public Release Checklist

Use this checklist before promoting this repository as a pinned GitHub project, portfolio case, LinkedIn post or resume artifact.

## Repository identity

- [ ] GitHub description is concise and honest.
- [ ] Topics/tags reflect the current implementation.
- [ ] README states prototype status clearly.
- [ ] README does not imply production SaaS, autonomous publishing or real customer deployment.
- [ ] License is present.

## Sensitive data

- [ ] No `.env` file committed.
- [ ] `.env.example` contains placeholders only.
- [ ] No API keys, tokens, cookies or service account JSON files.
- [ ] No local machine paths.
- [ ] No personal email, phone number or customer contact.
- [ ] No real client/company data.
- [ ] No raw transcripts or private chat exports.
- [ ] Generated outputs remain ignored unless intentionally sanitized.
- [ ] Vector DB/local memory folders remain ignored.

## Demo safety

- [ ] Demo company is fictional.
- [ ] Demo website contains no real business identity.
- [ ] Demo output is marked as sanitized/fictional.
- [ ] No invented performance metrics are presented as facts.
- [ ] No medical, legal, financial or compliance claims are overstated.

## Technical honesty

- [ ] Current implementation is separated from roadmap.
- [ ] LangGraph is described as planned/evolutionary unless a real graph implementation is committed.
- [ ] Human-in-the-loop is described as review workflow, not autonomous production control.
- [ ] Production deployment is marked as not included.
- [ ] Tests are described as minimal if only smoke tests exist.

## Suggested GitHub settings

- [ ] Add repository description:
  `Experimental multi-agent commercial orchestration workbench for marketing/CRO proposals, safety review, memory and human-in-the-loop approval.`
- [ ] Add topics:
  `ai-agents`, `multi-agent`, `commercial-automation`, `marketing-automation`, `cro`, `langchain`, `chromadb`, `human-in-the-loop`, `llmops`, `python`.
- [ ] Keep public only if all sensitive-data checks pass.

## Recommended pinning status

Pin only after:

1. README is accurate.
2. License exists.
3. Smoke tests exist.
4. Demo artifacts are fictional.
5. No private data is present.

This repository is suitable for public portfolio use as a **curated prototype**, not as a production product.
