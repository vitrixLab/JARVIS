"""Deterministic in-memory GE-001 graph store and local query interface."""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Iterable

from .model import Claim, Entity, Evidence, Provenance, Relationship, Source, to_record


@dataclass
class GraphStore:
    entities: dict[str, Entity] = field(default_factory=dict)
    relationships: dict[str, Relationship] = field(default_factory=dict)
    claims: dict[str, Claim] = field(default_factory=dict)
    sources: dict[str, Source] = field(default_factory=dict)
    evidence: dict[str, Evidence] = field(default_factory=dict)
    provenance: dict[str, Provenance] = field(default_factory=dict)

    def add(self, record: object) -> None:
        collection = {
            Entity: self.entities,
            Relationship: self.relationships,
            Claim: self.claims,
            Source: self.sources,
            Evidence: self.evidence,
            Provenance: self.provenance,
        }.get(type(record))
        if collection is None:
            raise TypeError(f"unsupported graph record: {type(record).__name__}")
        record_id = getattr(record, "id")
        if record_id in collection:
            raise ValueError(f"duplicate {type(record).__name__} id: {record_id}")
        collection[record_id] = record

    def add_all(self, records: Iterable[object]) -> None:
        for record in records:
            self.add(record)

    def entity(self, entity_id: str) -> Entity | None:
        return self.entities.get(entity_id)

    def relationships_from(self, entity_id: str) -> list[Relationship]:
        return [r for r in self.relationships.values() if r.subject_entity_id == entity_id]

    def relationships_to(self, entity_id: str) -> list[Relationship]:
        return [r for r in self.relationships.values() if r.object_entity_id == entity_id]

    def reachable_entities(self, start_entity_id: str) -> list[str]:
        """Return deterministic, cycle-safe entity reachability.

        Graph evidence may contain cycles. Traversal must terminate without repeatedly
        reprocessing an already visited entity, so automated graph analysis cannot loop
        indefinitely on a valid cyclic graph.
        """
        if start_entity_id not in self.entities:
            return []

        visited: set[str] = set()
        queue: list[str] = [start_entity_id]
        result: list[str] = []

        while queue:
            entity_id = queue.pop(0)
            if entity_id in visited:
                continue
            visited.add(entity_id)
            result.append(entity_id)
            neighbors = sorted(
                (r.object_entity_id for r in self.relationships_from(entity_id)),
            )
            queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

        return result

    def claims_for(self, subject: str) -> list[Claim]:
        return [c for c in self.claims.values() if c.subject == subject]

    def evidence_for_claim(self, claim_id: str) -> list[Evidence]:
        return [e for e in self.evidence.values() if claim_id in e.claim_refs]

    def source_for_evidence(self, evidence_id: str) -> Source | None:
        evidence = self.evidence.get(evidence_id)
        return self.sources.get(evidence.source_id) if evidence else None

    def provenance_for_evidence(self, evidence_id: str) -> Provenance | None:
        evidence = self.evidence.get(evidence_id)
        return self.provenance.get(evidence.provenance_id) if evidence and evidence.provenance_id else None

    def conflicting_claims(self, subject: str, predicate: str) -> list[Claim]:
        return [
            c for c in self.claims.values()
            if c.subject == subject and c.predicate == predicate
            and c.state.value == "CONFLICT"
        ]

    def canonical_payload(self) -> dict[str, list[dict]]:
        def records(values: Iterable[object]) -> list[dict]:
            return sorted((to_record(v) for v in values), key=lambda x: x["id"])
        return {
            "entities": records(self.entities.values()),
            "relationships": records(self.relationships.values()),
            "claims": records(self.claims.values()),
            "sources": records(self.sources.values()),
            "evidence": records(self.evidence.values()),
            "provenance": records(self.provenance.values()),
        }

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_payload(), sort_keys=True, separators=(",", ":"), ensure_ascii=False)

    def graph_hash(self) -> str:
        return hashlib.sha256(self.canonical_json().encode("utf-8")).hexdigest()
