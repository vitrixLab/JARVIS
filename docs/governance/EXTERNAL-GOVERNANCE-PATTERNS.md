# JARVIS External Governance Design Patterns

- Control Number: GOV-PAT-001
- Revision: 0.1
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-patterns
- Base SHA: 5b0a3c272b4a76fb9469ed8e185ce838912a6eb1
- Authorization: AUTH-023
- Merge Authorization: NOT AUTHORIZED

## 1. Purpose

Capture external governance/design patterns observed from upstream repository PR reconnaissance and map them to JARVIS governance primitives.

This document is informational. It does not change JARVIS implementation.

## 2. Source

Primary upstream source:

- `microsoft/agent-framework`

Access pattern:

fork → upstream → open PR reconnaissance

## 3. Observed External Patterns

### PAT-001 — Fail-Closed Execution

External evidence:

- `microsoft/agent-framework#7562`
- Introduces first-class `MiddlewareFailure`
- Prevents enforcement failures from becoming ordinary tool failures
- Cancels sibling tool calls
- Settles persisted conversations after aborted batch

JARVIS relevance:

- Authorization → execution → enforcement → fail-closed → evidence
- Prevents accidental fail-open behavior

Status: `INFORMATIONAL`

---

### PAT-002 — Parallel Authorization Correctness

External evidence:

- `microsoft/agent-framework#7692`
- Fixes parallel HITL approval where only first approved tool executed
- Later approvals could be silently skipped

JARVIS relevance:

- L2/L3 authorization semantics
- Batch operations must not silently drop approvals

Status: `INFORMATIONAL`

---

### PAT-003 — State Ownership / Isolation

External evidence:

- `microsoft/agent-framework#7712`
- Caller-owned checkpoints
- Prevents shared mutable checkpoint state
- Prevents cross-workflow state contamination

JARVIS relevance:

- Ledger/evidence state isolation
- Branch/PR/SHA records must not share mutable state

Status: `INFORMATIONAL`

---

### PAT-004 — Turn-Scoped Memory Lifecycle

External evidence:

- `microsoft/agent-framework#7289`
- Compaction moved to turn boundary
- Prevents persisted history being rewritten mid-task

JARVIS relevance:

- Evidence consistency
- Memory/context must not be mutated during active governance task

Status: `INFORMATIONAL`

---

### PAT-005 — Protocol Capability vs Transport Failure

External evidence:

- `microsoft/agent-framework#7656`
- Valid JSON-RPC error response to MCP ping means server is reachable
- Avoids reconnecting based only on non-standard error code

JARVIS relevance:

- Distinguish capability failure from transport failure
- Avoid false infrastructure warnings

Status: `INFORMATIONAL`

---

### PAT-006 — Grounded Resource Access

External evidence:

- `microsoft/agent-framework#7664`
- Eliminates invented skill resources
- Only resources explicitly grounded in loaded skill are accessible

JARVIS relevance:

- Evidence-grounded RAG
- Prevent model-inferred fictional paths

Status: `INFORMATIONAL`

## 4. JARVIS Mapping Table

| Pattern | JARVIS Governance Primitive |
|---|---|
| Fail-closed execution | Enforcement + authorization |
| Parallel authorization | L2/L3 approval semantics |
| State ownership | Ledger/evidence isolation |
| Turn-scoped lifecycle | Evidence consistency |
| Capability vs transport | Error classification |
| Grounded resources | RAG evidence grounding |

## 5. Boundary

This is pattern intelligence only.

It does not authorize:

- code changes
- workflow changes
- dependency changes
- merge
- upstream writes
