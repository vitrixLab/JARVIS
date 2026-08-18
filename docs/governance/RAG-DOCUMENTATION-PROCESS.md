---
# RAG Documentation Process

- Control Number: GOV-RAG-001
- Revision: 0.1
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-docs
- Base SHA: NOT RECORDED
- Head SHA: NOT RECORDED
- Date: 2026-08-18
- Authorization: AUTHORIZATION 011
- Merge Authorization: NOT AUTHORIZED

---

## 1. Purpose

Define how governance, research, assessment, and technical documentation is prepared for RAG while keeping the repository as the system of record.

Core rule:

Git/repository artifact = authoritative source
RAG index = disposable, rebuildable projection

RAG must never replace the repository as the source of truth.

---

## 2. Process Flow

Source material
        ↓
Document identification + control number
        ↓
Normalization / extraction
        ↓
Structural preservation / chunking
        ↓
Metadata + provenance
        ↓
Evidence / confidence state
        ↓
Repository-authoritative document
        ↓
RAG projection / index
        ↓
Reconciliation + rebuildability

---

## 3. Document Identification

Before RAG ingestion, every document must have:

- Control Number
- Title
- Revision
- Repository
- Path
- Branch
- Base SHA
- Head SHA
- Status
- Authorization ID

Missing identifiers use:

NOT RECORDED

No inferred values.

---

## 4. Normalization Rules

Allowed transformations:

- Convert source to canonical Markdown
- Preserve headers and code blocks
- Preserve tables
- Preserve SHA/PR/path values exactly
- Preserve front matter

Prohibited transformations:

- Rewriting conclusions
- Filling missing evidence
- Converting UNKNOWN to VERIFIED
- Removing incident history
- Changing authorization states
- Merging distinct documents without provenance

---

## 5. Structural Preservation

- Keep sections and subsections stable.
- Chunk only at section boundaries where possible.
- Each chunk carries:

document_control_number
chunk_index
source_path

A chunk is a view, not an independent document.

---

## 6. Metadata Requirements

| Field | Required |
|---|---|
| control_number | YES |
| repository | YES |
| branch | YES |
| path | YES |
| revision | YES |
| status | YES |
| source_sha | IF AVAILABLE |
| authorization_id | IF PRESENT |
| evidence_state | YES |
| chunk_index | FOR RAG |
| parent_document | FOR CHUNKS |

---

## 7. Evidence States

Use only:

VERIFIED
SUPPORTED
UNVERIFIED
UNKNOWN
CONFLICT
OBSOLETE
CURRENT

No other value is permitted.

Rules:

UNVERIFIED ≠ VERIFIED
UNKNOWN    ≠ FAILURE
CONFLICT   ≠ SUCCESS

---

## 8. RAG Projection Rules

- RAG index may be regenerated from repository files at any time.
- RAG search results must link back to the repository path and revision.
- RAG embeddings are not canonical evidence.
- If RAG and repository disagree, repository wins.
- If repository evidence is missing, RAG must surface NOT RECORDED.

---

## 9. Rebuildability

A RAG index is valid only if:

1. Source documents are committed.
2. Source SHAs or branch/revision are recorded.
3. Document paths are stable or versioned.
4. Ingestion script/process is known.
5. Projection can be regenerated without chat memory.

If any requirement fails:

RAG index = UNVERIFIED

---

## 10. Reconciliation

After RAG ingestion:

- Compare indexed paths against repository tree.
- Compare control numbers against Document Ledger.
- Compare SHAs against Commit Ledger.
- Compare authorizations against Authorization Ledger.
- Mark missing history as NOT RECORDED.

No reconciliation may be skipped to save tokens.

---

## 11. Incident Handling

If RAG exposes an old unauthorized write, do not hide it.

Record:

Incident ID
Repository
Expected branch
Actual branch
SHA if known
Status
Disposition

Incorrect RAG retrieval does not erase repository history.

---

## 12. Authorization Boundary

Creating or updating this document requires L1 authorization.

Using it for RAG ingestion requires no new write if read-only.

Index creation is not repository authorization.

---

## 13. Current State

| Item | State |
|---|---|
| RAG Documentation Process | Ready for L1 commit |
| Repository write | NOT AUTHORIZED |
| Commit | NOT EXECUTED |
| PR | NOT CREATED |
| Merge | NOT AUTHORIZED |

---
