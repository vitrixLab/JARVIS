import unittest

from graph.model import Claim, Entity, Evidence, EvidenceState, Provenance, Relationship, Source
from graph.store import GraphStore
from graph.validate import validate_store


class GraphEngineTests(unittest.TestCase):
    def make_store(self):
        store = GraphStore()
        store.add(Provenance("P-1", "local:test", {"retrieval_method": "fixture"}, "1", "hash-1"))
        store.add(Source("S-1", "local:test", "SYNTHETIC", "fixtures/network.json", "JARVIS", "1", {"retrieved_at": "fixture"}, "hash-1"))
        store.add(Entity("E-1", "PERSON", "Person A", provenance_refs=("P-1",)))
        store.add(Entity("E-2", "DOCUMENT", "Document A", provenance_refs=("P-1",)))
        store.add(Evidence("EV-1", "S-1", "entities/E-1", "Person A", ("C-1",), EvidenceState.VERIFIED, "fixture", "P-1"))
        store.add(Claim("C-1", "E-1", "AUTHORED", "E-2", ("EV-1",), ("P-1",), EvidenceState.VERIFIED))
        store.add(Relationship("R-1", "E-1", "AUTHORED", "E-2", evidence_refs=("EV-1",), provenance_refs=("P-1",)))
        return store

    def test_valid_graph(self):
        result = validate_store(self.make_store())
        self.assertTrue(result.valid, result.errors)

    def test_missing_evidence_rejected(self):
        store = self.make_store()
        store.claims["C-1"] = Claim("C-1", "E-1", "AUTHORED", "E-2", ("MISSING",), ("P-1",), EvidenceState.VERIFIED)
        result = validate_store(store)
        self.assertFalse(result.valid)
        self.assertIn("C-1", result.rejected_records)

    def test_graph_hash_is_deterministic(self):
        first = self.make_store().graph_hash()
        second = self.make_store().graph_hash()
        self.assertEqual(first, second)

    def test_duplicate_id_rejected(self):
        store = self.make_store()
        with self.assertRaises(ValueError):
            store.add(Entity("E-1", "PERSON", "Duplicate"))

    def test_relationship_traversal(self):
        store = self.make_store()
        self.assertEqual([r.id for r in store.relationships_from("E-1")], ["R-1"])
        self.assertEqual([r.id for r in store.relationships_to("E-2")], ["R-1"])

    def test_reachability_terminates_on_cycle(self):
        store = self.make_store()
        store.add(Entity("E-3", "ORGANIZATION", "Organization B", provenance_refs=("P-1",)))
        store.add(Relationship("R-2", "E-2", "REFERENCES", "E-3", evidence_refs=("EV-1",), provenance_refs=("P-1",)))
        store.add(Relationship("R-3", "E-3", "RELATED_TO", "E-1", evidence_refs=("EV-1",), provenance_refs=("P-1",)))
        self.assertEqual(store.reachable_entities("E-1"), ["E-1", "E-2", "E-3"])
        self.assertEqual(store.reachable_entities("E-1"), ["E-1", "E-2", "E-3"])


if __name__ == "__main__":
    unittest.main()
