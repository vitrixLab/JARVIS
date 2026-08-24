# Facebook Lead Intake & API Design

- Control Number: GOV-FB-001
- Revision: 0.1
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-fb-intake
- Base SHA: 5b0a3c272b4a76fb9469ed8e185ce838912a6eb1
- Authorization: AUTH-026
- Merge Authorization: NOT AUTHORIZED

## 1. Purpose

Document the future Facebook Page → JARVIS intake/qualification design as a planning artifact.

JARVIS is not a live API. This document records future implementation requirements only.

## 2. Intended Flow

Facebook Page / Messenger
        ↓
Meta webhook (HMAC verification)
        ↓
Secure intake API (auth, rate limit, idempotency)
        ↓
JARVIS lead scoring
        ↓
Rank: HIGH / MEDIUM / LOW / UNKNOWN
        ↓
Human review / portfolio / qualification questions
        ↓
Proposal/SLA only after human approval
        ↓
RAG learning record (anonymized, separated from client PII)

## 3. Meta Requirements

- Facebook App + Messenger product
- Page Access Token
- Webhook verification
- `pages_messaging`, `pages_manage_metadata` permissions
- App Review for production beyond admins/testers
- 24-hour messaging window compliance

## 4. Security and Privacy

- Verify `X-Hub-Signature`
- HTTPS only
- Rate limiting
- Idempotency keys
- Secrets via environment/secrets manager
- No tokens, PII, or private messages in repository
- Philippines Data Privacy Act applies; require legal review

## 5. Lead Scoring Model

Use current 0–40 qualification scorecard:

- Problem clarity
- Urgency
- Budget likelihood
- Repo/technical evidence
- Authority
- Service fit
- Close likelihood
- Reusability

Routing:

- HIGH: human review → full proposal/SLA
- MEDIUM: portfolio + qualification form
- LOW: portfolio/nurture
- UNKNOWN: 2–4 discovery questions first

## 6. Automation Boundary

Auto-send only:

- portfolio/capability overview
- qualification questions
- generic non-binding information

Do not auto-send:

- binding contracts
- signed SLAs
- pricing commitments without review
- implementation work without authorization

## 7. RAG Learning Rule

Separate:

- client-specific lead record
- generalized learning record

Strip private data before reusable learning.

## 8. Current State

- Design-only
- No API implementation
- No Facebook integration
- Merge prohibited
