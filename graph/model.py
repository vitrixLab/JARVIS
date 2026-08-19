"""Typed, serialisable GE-001 graph records.

The implementation is intentionally stdlib-only and local-first.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any


class EvidenceState(str, Enum):
    VERIFIED = "VERIFIED"
    SUPPORTED = "SUPPORTED"
    UNVERIFIED = "UNVERIFIED"
    UNKNOWN = "UNKNOWN"
    CONFLICT = "CONFLICT"
    OBSOLETE = "OBSOLETE"
    CURRENT = "CURRENT"


@dataclass(frozen=True)
class Entity:
    id: str
    type: str
    canonical_name: str
    aliases: tuple[str, ...] = ()
    attributes: dict[str, Any] = field(default_factory=dict)
    status: EvidenceState = EvidenceState.UNVERIFIED
    provenance_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class Relationship:
    id: str
    subject_entity_id: str
    predicate: str
    object_entity_id: str
    attributes: dict[str, Any] = field(default_factory=dict)
    confidence: float | None = None
    evidence_refs: tuple[str, ...] = ()
    provenance_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class Claim:
    id: str
    subject: str
    predicate: str
    object_or_value: Any
    evidence_refs: tuple[str, ...] = ()
    provenance_refs: tuple[str, ...] = ()
    state: EvidenceState = EvidenceState.UNVERIFIED
    temporal_metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Source:
    id: str
    identity: str
    source_type: str
    locator: str
    publisher_owner: str | None = None
    version: str | None = None
    retrieval_metadata: dict[str, Any] = field(default_factory=dict)
    content_hash: str | None = None


@dataclass(frozen=True)
class Evidence:
    id: str
    source_id: str
    locator: str
    extracted_content: str
    claim_refs: tuple[str, ...] = ()
    state: EvidenceState = EvidenceState.UNVERIFIED
    captured_at: str | None = None
    provenance_id: str | None = None


@dataclass(frozen=True)
class Provenance:
    id: str
    source_identity: str
    retrieval_metadata: dict[str, Any] = field(default_factory=dict)
    version: str | None = None
    content_hash: str | None = None
    processing_metadata: dict[str, Any] = field(default_factory=dict)


def to_record(value: Any) -> dict[str, Any]:
    """Return a JSON-compatible record with enum values represented as strings."""
    record = asdict(value)
    return _normalise(record)


def _normalise(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        return {str(k): _normalise(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_normalise(v) for v in value]
    return value
