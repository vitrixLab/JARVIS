# JARVIS L0 Resource Index

**Status:** DRAFT — HUMAN REVIEW REQUIRED  
**Repository:** `vitrixLab/JARVIS`  
**Working branch:** `working/jarvis-l0`  
**Base:** `main`  
**Scope:** Planning and research documentation only

## Governance disposition

This branch contains the L0 documentation package for human review. It does not authorize merging, upstream contribution, protected-branch mutation, dependency changes, workflow changes, or implementation migration.

## L0 resources

1. **Language Core Optimization — Combined Record**
   - Establishes Python as the orchestration/control-plane language.
   - Retains C++/native for FermatEngine and performance-critical computation.
   - Retains Web/JavaScript for presentation and visualization.
   - Defers Rust pending a concrete requirement.
   - Treats TypeScript as a schema/adapter/tooling pattern rather than a Python replacement.
   - Explicitly separates verified implementation from future design hypotheses.

2. **AIOpsLab Full-Automation Position**
   - Uses Microsoft AIOpsLab as the reference model for orchestrated autonomous operations.
   - Adopts reproducible environments, scenario-as-code, telemetry-as-evidence, evaluation, provenance, CI validation, and bounded automation as design principles.
   - Rejects the assumption that absence of an administrator constitutes unrestricted authorization.

3. **JARVIS Control-Plane Design Hypothesis**
   - Future Python control plane for agent reasoning, task planning, tool calling, LLM/RAG, workflow orchestration, repository adapters, governance/preflight, AIOpsLab integration, evidence, provenance, and evaluation.
   - Native performance plane for FermatEngine, physics/math, GPU and low-latency workloads.
   - Web presentation plane for visualization and browser interaction.
   - No implementation restructuring is included in L0.

## Evidence discipline

Each resource distinguishes:

- **VERIFIED / CURRENT** — directly supported by inspected repository material.
- **SUPPORTED** — supported by source material or research but not necessarily implemented in the current tree.
- **HYPOTHESIS / PROPOSED** — architectural direction for future work.
- **UNKNOWN** — not established by the inspection and deliberately not inferred.

## Explicit L0 constraints

- No rewrite of JARVIS into Python-only.
- No C++/Python migration without separate authorization.
- No Rust adoption without a concrete requirement.
- No TypeScript replacement of Python orchestration.
- No dependency changes.
- No workflow changes.
- No merge or upstream action.
- No claim that future AI/control-plane capabilities are already implemented.
- Token-efficiency benefits from TypeScript remain **UNKNOWN** until measured.

## Canonical architecture hypothesis

```text
                    JARVIS
                       │
             ┌─────────▼─────────┐
             │ Python Control    │
             │      Plane        │
             ├───────────────────┤
             │ AI / Agent        │
             │ Orchestration     │
             │ Governance        │
             │ AIOpsLab          │
             │ GitHub            │
             │ Evidence / RAG    │
             └───────┬─────┬─────┘
                     │     │
              Native │     │ Web
                     │     │
              ┌──────▼─┐ ┌─▼────────┐
              │ C++/GPU│ │ JS/Web UI│
              │Fermat  │ │Visualize │
              │ Engine │ │Interact  │
              └────────┘ └──────────┘
```

## Review disposition

This resource package is intentionally documentation-first. Human review should determine whether the proposed control-plane direction is accepted before implementation work is authorized.

**Current state:** L0 documentation branch only; `main` remains untouched.
