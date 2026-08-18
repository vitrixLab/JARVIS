# JARVIS Graph Evidence Engine (GE-001)

## Design-Only Architecture and Implementation Specification

**Status:** DESIGN-ONLY
**Security Incident:** `SEC-20260819-0046` — OPEN / ACTIVE
**Repository mutation:** PROHIBITED
**External API/token dependency:** PROHIBITED
**Secrets:** PROHIBITED
**Branch/PR creation:** PROHIBITED

---

## 1. Purpose

The **JARVIS Graph Evidence Engine (GE-001)** extends JARVIS's existing governance and evidence concepts into a structured mechanism for analyzing public or locally supplied data without allowing the LLM to become the source of truth.

The governing principle is:

```text
Public data
    ↓
Graph engineering
    ↓
Validated graph
    ↓
Evidence / provenance
    ↓
LLM analysis
```

The prohibited architecture is:

```text
LLM
  ↓
invented graph
  ↓
answer
```

GE-001 therefore treats the graph and its evidence/provenance records as the authoritative analytical substrate. The LLM is an **evidence consumer and reasoning layer**, not a graph-authoring authority.

The design also follows a broader engineering pattern visible in the supplied system documentation: source data is separated from generated structures, dependencies are explicit, validation occurs before downstream processing, and automation is organized into distinct engines rather than allowing one component to implicitly perform every responsibility.
No implementation is authorized by this specification.

---

## 2. Architecture Overview

GE-001 consists of six conceptual layers:

```text
┌───────────────────────────────────────────────┐
│                 Public / Local Data           │
│     documents, datasets, records, metadata    │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│               Graph Engineering               │
│ entity extraction / relationship construction │
│ claim construction / normalization            │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                Validation Layer               │
│ schema / relationship / provenance validation │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│              Evidence + Provenance             │
│ source → evidence → claim → graph assertions  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                Retrieval Layer                │
│ structured graph queries + evidence retrieval │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│             LLM Evidence Consumer             │
│ synthesis / explanation / uncertainty handling │
└───────────────────────────────────────────────┘
```

### Architectural boundary

The LLM may:

* query validated graph evidence;
* compare claims;
* summarize supported evidence;
* identify conflicts;
* explain uncertainty;
* produce an analytical response whose assertions reference supplied evidence.

The LLM may not:

* silently create authoritative entities;
* silently create authoritative relationships;
* fabricate sources;
* fabricate provenance;
* upgrade `UNKNOWN` or `UNVERIFIED` evidence to `VERIFIED`;
* present unsupported inference as established fact.

### Separation of responsibilities

| Component         | Authority                        |
| ----------------- | -------------------------------- |
| Source data       | Original information             |
| Graph engineering | Structured representation        |
| Validation        | Structural/evidentiary integrity |
| Provenance        | Traceability                     |
| Retrieval         | Evidence selection               |
| LLM               | Analysis and explanation         |

This separation is consistent with the supplied architecture documentation's emphasis on distinct lookup, validation, synchronization, calculation, and posting responsibilities rather than collapsing them into one automation component.

---

## 3. Core Data Model

### 3.1 Entity

An **Entity** represents an identifiable object in the graph.

Conceptual structure:

```text
Entity
├── id
├── type
├── canonical_name
├── aliases[]
├── attributes
├── status
└── provenance_refs[]
```

Required semantic properties:

* stable internal identifier;
* entity type;
* canonical representation;
* optional aliases;
* structured attributes;
* evidence/provenance references.

Examples of entity types may include:

```text
PERSON
ORGANIZATION
PRODUCT
LOCATION
DOCUMENT
EVENT
CONCEPT
DATASET
```

The exact controlled vocabulary is **UNKNOWN** and must be finalized during implementation.

An entity must not be considered authoritative merely because an LLM generated its name.

---

### 3.2 Relationship

A **Relationship** connects two entities.

Conceptual structure:

```text
Relationship
├── id
├── subject_entity_id
├── predicate
├── object_entity_id
├── attributes
├── confidence
├── evidence_refs[]
└── provenance_refs[]
```

Example:

```text
Entity A
   │
   └──[RELATIONSHIP]──► Entity B
```

Every material relationship must be traceable to evidence.

A relationship without supporting evidence is not eligible for presentation as a verified graph fact.

---

### 3.3 Claim

A **Claim** represents an assertion that can be evaluated against evidence.

Conceptual structure:

```text
Claim
├── id
├── subject
├── predicate
├── object/value
├── evidence_refs[]
├── provenance_refs[]
├── state
└── temporal metadata
```

Claims are the primary boundary between raw evidence and graph assertions.

Examples:

```text
Organization A
  └──[OPERATES_IN]──► Location B

Person A
  └──[AUTHORED]──► Document B
```

The claim state must reflect the state of its supporting evidence.

---

### 3.4 Source

A **Source** identifies the origin from which evidence was obtained.

Conceptual structure:

```text
Source
├── id
├── identity
├── source_type
├── locator
├── version
├── retrieval_metadata
└── content_hash
```

A source may be:

* a local document;
* a local dataset;
* a public webpage;
* a public data file;
* another explicitly authorized public source.

External source access is **not authorized by GE-001 itself**.

---

### 3.5 Evidence

An **Evidence** record identifies the specific material supporting or contradicting a claim.

Conceptual structure:

```text
Evidence
├── id
├── source_id
├── locator
├── extracted_content
├── claim_refs[]
├── state
├── captured_at
└── provenance_id
```

Evidence should be as precise as practical.

For example, a source-level citation alone may be insufficient if the source contains thousands of unrelated records. The evidence record should identify the relevant location, section, row, record, paragraph, or equivalent locator whenever available.

---

### 3.6 Provenance

**Provenance** records how an evidence item came into the system.

Conceptual structure:

```text
Provenance
├── source_identity
├── retrieval_metadata
├── version
├── content_hash
└── processing_metadata
```

Provenance is not optional metadata attached for convenience. It is part of the evidence integrity model.

---

## 4. Provenance Contract

Every source/evidence object intended to support an authoritative graph assertion must satisfy the provenance contract.

### 4.1 Source identity

Source identity must establish what the source is.

Minimum conceptual fields:

```text
source_id
source_type
locator
publisher/owner
identity metadata
```

If a source identity cannot be established, the relevant information must remain `UNKNOWN` or `UNVERIFIED`.

---

### 4.2 Retrieval metadata

Retrieval metadata should establish when and under what conditions the source was acquired.

Conceptual fields:

```text
retrieved_at
retrieval_method
retrieval_context
```

For local files, retrieval metadata may identify the local acquisition event rather than an Internet request.

Network retrieval is not authorized in the current design-only/security state.

---

### 4.3 Version

Where the source exposes a version, revision, publication date, dataset release, or equivalent identifier, it should be recorded.

```text
version:
  known version → record it
  no identifiable version → UNKNOWN
```

The system must never manufacture a version identifier.

---

### 4.4 Content hash

A deterministic content hash should be associated with the source representation where technically applicable.

Conceptually:

```text
content_hash = SHA-256(canonical_source_content)
```

The exact canonicalization procedure remains to be specified during implementation.

The purpose is to detect source changes and support reproducibility.

---

### Provenance invariant

A graph claim cannot reach `VERIFIED` solely because an LLM believes it is correct.

The minimum chain is:

```text
Claim
  ↓
Evidence
  ↓
Source
  ↓
Provenance
```

If any required link is absent, the system must preserve the appropriate uncertainty state.

---

## 5. Validation Rules

Validation is a separate layer and must execute before evidence is made available as authoritative graph material.

The supplied system architecture similarly defines explicit validation, lookup, synchronization, and posting responsibilities and specifies required-field, duplicate, missing-reference, and amount validation rules.

### 5.1 Schema validation

Validate:

* required identifiers;
* permitted entity types;
* relationship structure;
* claim structure;
* evidence structure;
* provenance structure;
* data types;
* required references;
* identifier uniqueness.

Invalid records must not enter the validated graph.

---

### 5.2 Relationship validation

Validate:

1. subject entity exists;
2. object entity exists;
3. predicate is permitted;
4. relationship direction is valid;
5. relationship cardinality is valid where defined;
6. relationship has appropriate evidence;
7. relationship does not create an invalid graph structure.

Where a relationship is inferred rather than directly stated by a source, it must be explicitly marked as an inference and must not be represented as direct source fact.

---

### 5.3 Provenance validation

Validate:

* source identity exists;
* source reference resolves;
* retrieval metadata exists where required;
* version is either known or explicitly `UNKNOWN`;
* content hash exists where required;
* evidence points to its source;
* claim points to evidence;
* no provenance chain is broken.

---

### Validation result

Validation should produce an explicit result rather than silently dropping problems.

Conceptually:

```text
ValidationResult
├── valid: boolean
├── errors[]
├── warnings[]
└── rejected_records[]
```

Validation failures must be inspectable.

---

## 6. Graph Storage / Representation

### 6.1 Local-first architecture

GE-001 should begin as a **local-first** engine.

The initial implementation should not require:

* PostgreSQL;
* pgvector;
* Redis;
* Cloudflare;
* external graph databases;
* external queues;
* cloud storage;
* external APIs.

## The supplied BookFlow architecture documents PostgreSQL/Prisma and external connector infrastructure, but those are not required dependencies for GE-001's initial graph-evidence core. BookFlow's connector architecture also explicitly separates external systems from the core application and emphasizes isolated, controlled integration.

### 6.2 In-memory representation

The first execution model may use in-memory structures:

```text
Map<EntityId, Entity>
Map<RelationshipId, Relationship>
Map<ClaimId, Claim>
Map<SourceId, Source>
Map<EvidenceId, Evidence>
Map<ProvenanceId, Provenance>
```

This supports deterministic local testing without infrastructure dependencies.

---

### 6.3 File-based representation

For reproducibility, the engine should also support deterministic local files.

Possible representation:

```text
graph/
  schema/
  examples/
```

with structured records such as JSON or another explicitly approved serialization format.

The exact serialization format is **UNKNOWN** and is intentionally not fixed by this specification.

---

### 6.4 Determinism

Given identical:

```text
input data
+
normalization rules
+
schema version
+
processing configuration
```

the graph construction process should produce the same graph.

Determinism is a core acceptance requirement.

---

## 7. Retrieval Layer

The retrieval layer provides structured access to validated graph material.

### 7.1 Structured query

Queries should operate against graph structures rather than asking the LLM to reconstruct the graph.

Conceptual examples:

```text
find entity by ID
find entities by type
find relationships from entity
find relationships to entity
find claims about entity
find evidence supporting claim
find conflicting claims
find sources supporting entity
```

A query should return structured records rather than only natural-language prose.

---

### 7.2 Evidence retrieval

Evidence retrieval should expose:

```text
claim
→ supporting evidence
→ source
→ provenance
→ evidence state
```

A retrieval result should preserve the distinction between:

* directly supported information;
* inferred information;
* conflicting information;
* missing information.

---

### 7.3 No hidden retrieval authority

The retrieval layer must not silently call external services in the initial design.

External retrieval becomes a separate integration boundary and requires an explicit security/authorization gate.

---

## 8. LLM Evidence-Consumption Interface

The LLM receives **validated evidence**, not an unrestricted opportunity to create authoritative graph facts.

### 8.1 Permitted LLM operations

The LLM may:

* summarize evidence;
* compare claims;
* explain relationships;
* identify conflicts;
* generate hypotheses;
* identify unanswered questions;
* distinguish evidence from inference;
* produce human-readable analysis.

### 8.2 Required evidence context

An LLM request should conceptually contain:

```text
query
validated graph context
claims
evidence
sources
provenance
evidence states
```

The LLM should not receive an unqualified statement such as:

```text
"Tell me what the graph says."
```

without supplying the graph/evidence context through the controlled interface.

---

### 8.3 Required output contract

The LLM response should conceptually separate:

```text
ANSWER
SUPPORTED_CLAIMS
INFERENCES
CONFLICTS
UNKNOWN_INFORMATION
EVIDENCE_REFERENCES
```

For example:

```text
ANSWER:
  ...

SUPPORTED_CLAIMS:
  - claim_id: C-001
    evidence: E-001

INFERENCES:
  - ...

CONFLICTS:
  - ...

UNKNOWN_INFORMATION:
  - ...

EVIDENCE_REFERENCES:
  - source_id: S-001
    provenance_id: P-001
```

The exact machine-readable schema is **UNKNOWN** and must be finalized during implementation.

---

### 8.4 Prohibition on ungrounded assertions

The LLM must not represent an unsupported assertion as a verified graph fact.

If no supporting evidence exists, the response must explicitly indicate:

```text
UNKNOWN
```

or another applicable evidence state.

If evidence conflicts, the LLM must report the conflict rather than arbitrarily selecting one source.

---

## 9. Public/Local Test Dataset Design

The initial dataset must be:

* small;
* reproducible;
* public or synthetic;
* locally available;
* secret-free;
* deterministic;
* easy to inspect manually.

### Recommended conceptual dataset

A small synthetic organization/network dataset may contain:

```text
Entities:
  Organization A
  Organization B
  Person A
  Document A
  Location A

Relationships:
  Person A → AUTHORED → Document A
  Organization A → LOCATED_IN → Location A
  Organization A → PARTNERED_WITH → Organization B
```

The dataset should deliberately include:

1. valid entities;
2. valid relationships;
3. supported claims;
4. an `UNKNOWN` field;
5. an intentionally conflicting claim;
6. an obsolete source/version;
7. an unsupported relationship that validation rejects.

This permits the engine to test both positive and negative governance behavior.

No credentials, API keys, production records, private lead information, or incident credentials may appear in the dataset.

The supplied Facebook/JARVIS research explicitly emphasizes that repositories should not contain access tokens, app secrets, or actual client data.

---

## 10. Security / Governance Constraints

### 10.1 Credentials

GE-001 must not require or access:

* Cloudflare credentials;
* Google credentials;
* NVIDIA credentials;
* `DATABASE_URL`;
* `SESSION_PASSWORD`;
* API keys;
* access tokens;
* OAuth secrets;
* webhook secrets;
* any other credential.

No credential rotation is claimed or implied by this specification.

---

### 10.2 Network access

The initial engine must operate without network access.

```text
Default:
  NETWORK = DENY
```

External retrieval can only be introduced after:

1. architecture review;
2. security review;
3. explicit authorization;
4. credential-management design;
5. provenance requirements;
6. authorization for the specific integration.

---

### 10.3 Evidence states

GE-001 shall recognize the following evidence states:

| State        | Meaning                                                                            |
| ------------ | ---------------------------------------------------------------------------------- |
| `VERIFIED`   | Evidence and provenance satisfy the validation contract and support the claim      |
| `SUPPORTED`  | Evidence supports the claim but does not meet the strongest verification threshold |
| `UNVERIFIED` | Information exists but has not passed sufficient verification                      |
| `UNKNOWN`    | Required information/evidence is unavailable                                       |
| `CONFLICT`   | Valid evidence materially disagrees                                                |
| `OBSOLETE`   | Evidence is superseded or no longer current                                        |
| `CURRENT`    | Evidence has been established as current under the applicable source/version rules |

`CURRENT` and `VERIFIED` are not necessarily interchangeable.

A current source may contain an unverified claim.

A verified historical claim may no longer be current.

---

### 10.4 Governance state transitions

Evidence state changes should be explicit.

Conceptually:

```text
UNKNOWN
   ↓
UNVERIFIED
   ↓
SUPPORTED
   ↓
VERIFIED
```

Alternative states may branch:

```text
VERIFIED → OBSOLETE
VERIFIED → CONFLICT
```

The precise transition matrix is **UNKNOWN** and must be defined during implementation.

The LLM must never independently perform an evidence-state upgrade.

---

### 10.5 Existing governance compatibility

GE-001 should align with JARVIS's existing concepts of:

* authorization levels;
* preflight validation;
* provenance;
* evidence states;
* read-only boundaries;
* review-only boundaries.

No claim is made here about the exact current repository implementation of those mechanisms beyond the supplied project context.

---

## 11. Development Phases

### Phase 1 — Schema + Data Model

Define:

* Entity;
* Relationship;
* Claim;
* Source;
* Evidence;
* Provenance;
* identifiers;
* state vocabulary;
* schema versioning.

**Dependency:** none.

---

### Phase 2 — Provenance

Implement the provenance contract:

```text
source identity
retrieval metadata
version
content hash
```

Define deterministic canonicalization and hashing rules.

---

### Phase 3 — Validation

Implement:

```text
schema validation
relationship validation
provenance validation
```

Produce explicit validation errors and rejection results.

---

### Phase 4 — Local Test Dataset

Create a small deterministic dataset containing:

* valid records;
* unsupported records;
* conflicting claims;
* unknown fields;
* obsolete evidence.

No network or credentials.

---

### Phase 5 — Query Interface

Implement local structured retrieval:

```text
entity lookup
relationship traversal
claim lookup
evidence lookup
source lookup
provenance lookup
conflict lookup
```

---

### Phase 6 — LLM Interface

Introduce the LLM only as an evidence consumer.

The interface must enforce:

```text
graph evidence → LLM
```

and prohibit:

```text
LLM → authoritative graph
```

The exact model/provider is **UNKNOWN** and is intentionally not required for this phase's architecture.

---

### Phase 7 — External Integration

External integration is explicitly deferred.

It requires a separate security gate covering:

* network access;
* source authorization;
* credentials;
* secret storage;
* rate limits;
* provenance;
* privacy;
* auditability;
* failure behavior.

No external integration is authorized by GE-001.

---

## 12. Acceptance Criteria

GE-001 will be considered architecturally acceptable only when the following requirements are satisfied.

### 12.1 Deterministic graph construction

Given identical input and configuration:

```text
same input
→ same normalized graph
```

---

### 12.2 Every claim linked to a source

No authoritative claim may exist without:

```text
Claim
 ↓
Evidence
 ↓
Source
```

---

### 12.3 Every source has provenance

Every authoritative source must satisfy:

```text
Source
 ↓
Provenance
```

including the required provenance fields or explicitly declared `UNKNOWN` values where the specification permits them.

---

### 12.4 No LLM-only assertion

An LLM-generated assertion cannot become an authoritative graph claim solely because the LLM generated it.

Any unsupported assertion must remain:

```text
UNKNOWN
```

or another appropriate non-authoritative state.

---

### 12.5 No secret dependency

The local engine must execute without:

* API keys;
* access tokens;
* database credentials;
* Cloudflare credentials;
* Google credentials;
* NVIDIA credentials;
* session secrets;
* external service credentials.

---

### 12.6 Conflict preservation

Conflicting valid evidence must remain identifiable as:

```text
CONFLICT
```

rather than being silently collapsed into one answer.

---

### 12.7 Provenance preservation

Graph transformations and retrieval operations must preserve the ability to trace:

```text
LLM answer
   ↓
claim
   ↓
evidence
   ↓
source
   ↓
provenance
```

---

### 12.8 Local reproducibility

The initial GE-001 test suite must be runnable locally without external infrastructure.

---

## 13. Proposed Repository File Layout

**Future authorization only.**

No files are to be created under this design-only instruction.

```text
graph/
  schema/
  provenance/
  validation/
  retrieval/
  llm/
  examples/
```

### Intended responsibilities

```text
graph/schema/
    Entity / Relationship / Claim / Source / Evidence schemas

graph/provenance/
    provenance contract and hashing rules

graph/validation/
    schema, relationship, and provenance validation

graph/retrieval/
    structured graph and evidence queries

graph/llm/
    evidence-consumption interface and output contract

graph/examples/
    deterministic public/local test datasets
```

The layout intentionally mirrors the architectural separation between data structures, validation, retrieval, and downstream consumption rather than implementing a single monolithic graph module.

---

# Design Boundary

GE-001 is currently a **design specification only**.

No implementation, repository mutation, branch creation, pull request, merge, workflow modification, credential operation, external API connection, or secret handling is authorized.

The security incident `SEC-20260819-0046` remains **OPEN / ACTIVE** for purposes of this specification.

Any information not established by the supplied materials or this explicit design request remains **UNKNOWN**. In particular, this specification does not claim that credential rotation has occurred, that external model access works, or that any external JARVIS integration is operational.

Current state:

* repo: no repository action
* branch/PR: none
* merge: not applicable
* next action: await explicit authorization to commit the GE-001 specification
