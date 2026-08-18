# Documentation Control & Lifecycle SOP v1.0

- Control Number: GOV-DOC-001
- Revision: 1.0
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-docs
- Base SHA: c553fd92d9033f8d51f8c520203c5145c12f5f55
- Head SHA: PENDING — assigned by commit
- Date: 2026-08-18
- Authorization: L1 WRITE — explicitly authorized for this file/path
- Merge Authorization: NOT AUTHORIZED

---

## 1. Purpose

Provide a controlled lifecycle for material governance, research, assessment, and related documentation artifacts so that the repository, rather than chat history, serves as the system of record.

The lifecycle is:

```text
Chat/planning idea
        ↓
Formal draft
        ↓
Document control assignment
        ↓
Scoped branch/PR
        ↓
Read-only review
        ↓
Explicit authorization
        ↓
Commit
        ↓
PR remains draft/unmerged unless separately approved
```

---

## 2. Core Principles

1. Chat is working memory, not the system of record.
2. Every authoritative governance, research, or assessment artifact must be committed to a designated repository.
3. Each controlled document receives a control number, revision, status, date, branch/SHA references, and authorization state.
4. No merge occurs unless governance separately authorizes the merge.
5. Historical versions remain immutable; updates create new commits and do not rewrite history.
6. Documentation-only authorization does not authorize code, dependency, workflow, configuration, or other unrelated repository changes.

---

## 3. Document Control

Each authoritative document must carry controlled front matter:

```markdown
# <Title>

- Control Number:
- Revision:
- Status:
- Repository:
- Branch:
- Base SHA:
- Head SHA:
- Date:
- Authorization:
- Merge Authorization: NOT AUTHORIZED
```

For a document that has not yet been committed, SHA fields must be recorded as `PENDING` rather than guessed or fabricated. Once committed, the actual commit SHA becomes part of the evidence record.

---

## 4. Lifecycle Statuses

Controlled documentation uses the following lifecycle statuses:

```text
DRAFT
IN REVIEW
ACCEPTED
SUPERSEDED
```

A status change must be traceable to a documented review or authorization event where applicable.

---

## 5. Repository and Branch Control

Material documentation must be placed in a designated repository and controlled documentation directory.

The standard governance documentation structure is:

```text
docs/governance/
├── DOCUMENTATION-CONTROL-SOP.md
├── PREFLIGHT-PROTOCOL.md
├── OPTION-SIMULATION-SOP.md
├── CLEARANCE-LEVELS.md
├── INCIDENT-LOG.md
└── AUTHORIZATION-RECORDS.md
```

For each change:

- Branch from a known base SHA.
- Use a scoped working branch.
- Perform a pre-write branch and target-path check.
- Keep one documentation scope per PR where practical.
- Do not modify unrelated files.
- Force-push and history rewriting are prohibited.

---

## 6. PR and Commit Control

Governance documentation should use a draft PR when a review artifact is required.

Required controls:

- The PR must remain draft/unmerged unless separate merge authorization is issued.
- The commit must identify the documentation scope clearly.
- No code, dependency, workflow, or unrelated configuration changes may be included unless separately authorized.
- The commit SHA and branch become part of the audit trail after commit.

A PR's existence does not constitute implementation or merge authorization.

---

## 7. Authorization Boundary

Documentation creation and merge are separate authorization events.

The minimum controlled sequence is:

```text
Explicit authorization
        ↓
Repository/branch/path allowlist
        ↓
Pre-write branch/path check
        ↓
Expected scope/diff check
        ↓
Commit
        ↓
Draft PR / read-only review
        ↓
Separate merge authorization, if required
```

An L1 authorization applies only to its explicitly allowlisted repository, branch, path, and operation.

---

## 8. Immutability and Historical Record

Historical controlled documents and their commits must not be rewritten to conceal, alter, or remove prior evidence.

Corrections and revisions are made through new commits and documented revision changes.

Force-push, history rewriting, and destructive branch operations are outside this SOP's documentation authorization unless separately and explicitly authorized at the appropriate governance level.

---

## 9. Audit Trail

Where applicable, retain the following metadata:

```text
repository
branch
base SHA
head SHA
PR number
commit range
evidence files
incident IDs
authorization records
review records
```

Machine-readable records should be preferred where practical.

---

## 10. Separation of Governance Artifacts

The documentation lifecycle must preserve separation between:

```text
research evidence
      ↓
governance decisions
      ↓
implementation authorization
      ↓
implementation PRs
```

A research or governance document must not be treated as implementation authorization merely because it has been accepted or committed.

---

## 11. Current Controlled Artifact Record

This document was authorized specifically for creation at:

```text
Repository: vitrixLab/JARVIS
Branch: working/governance-docs
Path: docs/governance/DOCUMENTATION-CONTROL-SOP.md
Commit message: docs: add documentation control and lifecycle SOP v1.0
Merge: PROHIBITED
```

No other repository path is authorized by this record.

---

## 12. Compliance Rule

If a material governance artifact exists only in chat, it is considered planning/work memory and is not the authoritative system-of-record artifact.

The authoritative version is the controlled repository version identified by its repository, branch/ref, commit SHA, revision, status, and authorization record.

---

## 13. Revision History

| Revision | Date | Status | Change |
|---|---|---|---|
| 1.0 | 2026-08-18 | DRAFT | Initial controlled documentation lifecycle SOP |
