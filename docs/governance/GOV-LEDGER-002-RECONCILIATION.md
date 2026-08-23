# GOV-LEDGER-002 Reconciliation Mapping

- Control Number: GOV-LEDGER-002-RECON
- Revision: 0.1
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-ledger-002-reconciliation
- Base SHA: 3f84377ec24c8d9c3fd4bf77174002af7d207026
- Authorization: AUTH-GOVLEDGER-003
- Merge Authorization: NOT AUTHORIZED

## 1. Source-of-Truth Model

GitHub is authoritative for GitHub facts.

| Data | Authority |
|---|---|
| PR number/title | GitHub |
| State / draft / merged | GitHub |
| Base/head refs and SHAs | GitHub |
| Changed files/count | GitHub |
| CI/check status | GitHub |
| Security hold | JARVIS governance |
| Classification | JARVIS governance |
| Authorization | JARVIS governance |
| Causality | JARVIS governance |
| Merge policy | JARVIS governance |

## 2. Architecture

GitHub
  ↓ read-only facts
PR FACT COLLECTOR
  ↓
GENERATED PR FACTS
  ├── PR LEDGER VIEW
  └── GOV-LEDGER
        ├── governance decisions
        ├── security holds
        ├── authorizations
        ├── causality
        └── merge policy
              ↓
           GE-001

## 3. PR Ledger Role

The existing PR Ledger is retained as a derived PR evidence view.

It must not become a second authoritative source of GitHub facts.

## 4. Current Read-Only Reconciliation

### JARVIS active drafts

- PR #15 Graph Evidence Engine spec
- PR #14 Security incident record
- PR #13 README governance status
- PR #12 NS governance summarizer
- PR #11 L0 per-PR preflight
- PR #9 Facebook lead intake
- PR #8 JARVIS governance ledger
- PR #7 External governance patterns
- PR #6 SLA monetization roadmap
- PR #5 AI IDE integration matrix
- PR #4 Governance PoC/PoW
- PR #3 Governance checks automation
- PR #2 RAG documentation process
- PR #1 L0 control-plane resources

### JARVIS merged

- PR #10 Cross-repo governance check

### stabilisation-demo active drafts

- PR #92 Client dashboard image accessibility
- PR #89 Frontend pre-flight governance
- PR #87 Client dashboard design upgrade scope
- PR #86 Secured recovery process
- PR #85 TypeScript checks automation
- PR #84 UI/UX baseline

## 5. Implementation Boundary

This document is design-only.

No fact collector, YAML synchronizer, validator, renderer, workflow, or graph implementation is authorized.

## 6. Security

SEC-20260819-0046 remains OPEN / ACTIVE.

No secrets, credentials, Cloudflare settings, external APIs, or external model integration are authorized.
