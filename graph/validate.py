"""GE-001 structural and provenance validation."""
from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
import json

from .model import EvidenceState
from .store import GraphStore


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    rejected_records: list[str] = field(default_factory=list)


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(payload.encode("utf-8")).hexdigest()


def validate_store(store: GraphStore) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    rejected: list[str] = []

    for entity in store.entities.values():
        if not entity.id or not entity.type or not entity.canonical_name:
            errors.append(f"entity {entity.id or '<missing>'}: required field missing")
            rejected.append(entity.id or "<missing>")

    for relationship in store.relationships.values():
        if relationship.subject_entity_id not in store.entities:
            errors.append(f"relationship {relationship.id}: subject entity missing")
            rejected.append(relationship.id)
        if relationship.object_entity_id not in store.entities:
            errors.append(f"relationship {relationship.id}: object entity missing")
            rejected.append(relationship.id)
        if not relationship.predicate:
            errors.append(f"relationship {relationship.id}: predicate missing")
            rejected.append(relationship.id)
        if not relationship.evidence_refs:
            errors.append(f"relationship {relationship.id}: no supporting evidence")
            rejected.append(relationship.id)
        for evidence_id in relationship.evidence_refs:
            if evidence_id not in store.evidence:
                errors.append(f"relationship {relationship.id}: evidence {evidence_id} missing")
                rejected.append(relationship.id)

    for claim in store.claims.values():
        if not claim.id or not claim.subject or not claim.predicate:
            errors.append(f"claim {claim.id or '<missing>'}: required field missing")
            rejected.append(claim.id or "<missing>")
        if not claim.evidence_refs:
            errors.append(f"claim {claim.id}: no supporting evidence")
            rejected.append(claim.id)
        for evidence_id in claim.evidence_refs:
            evidence = store.evidence.get(evidence_id)
            if evidence is None:
                errors.append(f"claim {claim.id}: evidence {evidence_id} missing")
                rejected.append(claim.id)
                continue
            if claim.id not in evidence.claim_refs:
                errors.append(f"claim {claim.id}: evidence {evidence_id} does not reference claim")
                rejected.append(claim.id)
            if evidence.source_id not in store.sources:
                errors.append(f"evidence {evidence.id}: source {evidence.source_id} missing")
                rejected.append(evidence.id)
            if not evidence.provenance_id or evidence.provenance_id not in store.provenance:
                errors.append(f"evidence {evidence.id}: provenance missing")
                rejected.append(evidence.id)

    for source in store.sources.values():
        if not source.identity or not source.source_type or not source.locator:
            errors.append(f"source {source.id}: source identity/type/locator required")
            rejected.append(source.id)
        if source.content_hash is None:
            warnings.append(f"source {source.id}: content hash is UNKNOWN")

    for provenance in store.provenance.values():
        if not provenance.source_identity:
            errors.append(f"provenance {provenance.id}: source identity missing")
            rejected.append(provenance.id)
        if provenance.content_hash is None:
            warnings.append(f"provenance {provenance.id}: content hash is UNKNOWN")

    # A verified claim is only eligible when its evidence and provenance chain exists.
    for claim in store.claims.values():
        if claim.state is EvidenceState.VERIFIED and claim.id in rejected:
            errors.append(f"claim {claim.id}: VERIFIED state is invalid with broken evidence chain")

    return ValidationResult(valid=not errors, errors=errors, warnings=warnings, rejected_records=sorted(set(rejected)))
