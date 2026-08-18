# JARVIS Control-Plane Design Hypothesis — L0

**Status:** DESIGN HYPOTHESIS — NOT IMPLEMENTED  
**Repository:** `vitrixLab/JARVIS`  
**Branch:** `working/jarvis-l0`  
**Base:** `main`

## Purpose

Define a future control-plane boundary for JARVIS without restructuring the current application during L0.

## Proposed responsibility split

### Python Control Plane

- agent/reasoning loop;
- task planning;
- tool calling;
- LLM/RAG integration;
- workflow orchestration;
- repository adapters;
- governance and preflight controls;
- AIOpsLab orchestration;
- evidence collection;
- session/provenance records;
- evaluation coordination.

### Native Performance Plane

- FermatEngine;
- heavy mathematical/physics computation;
- GPU operations;
- low-latency paths;
- performance-critical rendering/computation.

### Web Presentation Plane

- browser visualization;
- interactive controls;
- canvas/UI presentation;
- browser-side interaction.

## Boundary rule

```text
Reason/orchestrate  → Python
Compute/render fast → Native/C++/GPU
Present/interact    → Web/JavaScript
```

## Proposed future module shape

```text
src/
├── core/
│   ├── agent/
│   ├── orchestration/
│   ├── governance/
│   ├── tools/
│   └── evidence/
│
├── adapters/
│   ├── aiops/
│   ├── github/
│   └── native/
│
├── ui/
│
└── main.py
```

This is a design hypothesis only. It does not imply that these directories should be created now.

## Integration boundaries

```text
                  JARVIS Python Control Plane
                              │
          ┌───────────────────┼────────────────────┐
          │                   │                    │
      GitHub adapter      AIOpsLab adapter     Native adapter
          │                   │                    │
      repository          autonomous ops       FermatEngine
       controls           environments         C++/GPU
          │                   │
          └──────────── evidence / provenance ───┘
                              │
                         evaluation
```

The adapters should isolate external systems from the core orchestration model. This keeps JARVIS as the control plane rather than making any single integration the application itself.

## Governance boundary

A future autonomous action should pass through a policy boundary before mutation:

```text
Intent
  ↓
Scope resolution
  ↓
Branch/path authorization
  ↓
Action execution
  ↓
Automated validation
  ↓
Provenance/audit
  ↓
Human authorization where required
```

Privileged, irreversible, history-rewriting, credential-sensitive, or protected-branch operations should remain explicitly gated.

## Current implementation distinction

The L0 inspection verified that JARVIS already has a hybrid Python/native/Web shape. It did **not** verify that the future AI/control-plane, AIOpsLab, GitHub governance, evidence/RAG, or provenance layers are already implemented.

Those capabilities remain proposed.

## Non-goals for L0

- no rewrite into Python;
- no C++ migration;
- no Rust migration;
- no TypeScript replacement of Python;
- no dependency changes;
- no workflow changes;
- no restructuring of `src/`;
- no implementation of AIOpsLab adapters;
- no GitHub automation implementation;
- no autonomous repository mutation.

## Acceptance criterion for future implementation

Any later implementation PR should demonstrate that the proposed boundary improves separation of concerns without degrading the existing FermatEngine/native and Web/visualization paths. Performance, build reproducibility, integration correctness, and governance controls must be measured rather than assumed.
