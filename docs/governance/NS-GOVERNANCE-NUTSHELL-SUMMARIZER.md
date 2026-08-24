# NS Governance Nutshell Summarizer Proposal

- Control Number: GOV-NS-001
- Revision: 0.1
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-ns-proposal
- Authorization: AUTH-NS-001
- Merge Authorization: NOT AUTHORIZED

## 1. Purpose

Define a governance-aware summarization layer that reduces long chat/PR/log threads into a deterministic Nutshell state block.

## 2. Canonical NS Prompt

    You are a governance-aware DeepSeek-expert-level summarizer.

    When the user sends a pasted chat, always produce the shortest possible nutshell.

    Rules:
    1. Agree with correct technical findings.
    2. Do not re-litigate settled governance decisions.
    3. Correct only material factual errors, one line max.
    4. Preserve labels exactly:
       OPEN / DRAFT / UNMERGED
       MERGED
       PROHIBITED
       PASS / FAIL / UNKNOWN
    5. No repository writes, merges, PR edits, or branch changes are authorized.
    6. End with:

    Current state:
    - repo:
    - branch/PR:
    - merge:
    - next action:

## 3. Required Output Contract

Every NS response must end with:

    Current state:
    - repo: ...
    - branch/PR: ...
    - merge: ...
    - next action: ...

Must not invent writes, claim merges, expand scope, or omit labels.

## 4. Current Test Status

- NS prompt defined: VERIFIED
- DeepSeek-style baseline known: VERIFIED
- NVIDIA model catalog access: UNVERIFIED
- Minimal chat completion test: UNVERIFIED
- JARVIS integration: NOT IMPLEMENTED
- Repository writes: NONE

## 5. Development Phases

- Phase 0 — Formalize NS prompt/examples
- Phase 1 — Local runner in ns-test/
- Phase 2 — Cross-model benchmark
- Phase 3 — JARVIS read-only integration
- Phase 4 — Machine-readable JSON output

## 6. Security Boundaries

- API keys only in .env
- .env must be ignored by Git
- No verbose curl with Authorization
- No key in chat/logs
- If exposed: revoke immediately
- NS output must never contain secrets
- NS must never assert writes/merges without repository evidence

## 7. Next Action

- Revoke any exposed NVIDIA key.
- Run a private minimal NVIDIA chat completion test using stream: false and no verbose logging.
- If clean, formalize Phase 0/1.
