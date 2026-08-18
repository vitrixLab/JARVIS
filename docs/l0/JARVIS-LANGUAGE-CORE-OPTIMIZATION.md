# JARVIS Language Core Optimization — Combined Record

**Status:** READ-ONLY ASSESSMENT + DESIGN HYPOTHESIS — now preserved as an L0 documentation artifact  
**Repository:** `vitrixLab/JARVIS`  
**Branch:** `working/jarvis-l0`  
**Base:** `main`

## Direct Answer

Python is the right core for JARVIS only if it remains the **orchestration/control plane**, not the compute engine.

JARVIS should not become Python-only.

```text
Python        → orchestration, AI/agent, future governance/control plane
C++ / native  → FermatEngine, GPU/physics/performance-critical work
Web / JS      → visualization, browser UI, interactive presentation
Rust          → defer until concrete safety/concurrency requirement exists
```

Core principle:

```text
Do not optimize JARVIS by choosing one language.
Optimize it by making language boundaries explicit.
```

## Language Map

| Area | Finding | Status |
|---|---|---|
| Python | `src/main.py` is application coordinator / GUI / AI-VIE startup | VERIFIED / CURRENT |
| C++ | FermatEngine.cpp/.h provides native high-performance engine | VERIFIED / CURRENT |
| C++ → Web | `bindings.cpp` exposes FermatEngine via Emscripten | VERIFIED / CURRENT |
| Web | `index.html` + `sketch.js` | VERIFIED / CURRENT |
| Rust | Not identified | UNKNOWN / future option |
| TypeScript | Not identified in inspected tree | UNKNOWN / future option |
| Python ↔ C++ binding | Not found in inspected material | UNKNOWN |
| Build metadata | CMakeLists.txt, pyproject.toml, requirements.txt, package.json not established | UNKNOWN |
| Future AI/control-plane functionality | Proposed; not established as current implementation | SUPPORTED as direction, not current fact |

## Python Suitability

**Verdict: Python is appropriate as the orchestration/control-plane language.**

The inspected `src/main.py` acts as a coordinator: it creates the Qt application, initializes visual controllers, wraps the audio engine, initializes the VIE/interaction manager, starts the interaction thread, wires visualization and interaction components, and owns application lifecycle.

The README describes JARVIS as an AI OS with automation, analytics, cross-platform integration, voice interaction, and adaptive UI, but those product-level capabilities must not be represented as fully implemented merely from the README. The inspected implementation currently concentrates heavily on GUI/VFX/audio/VIE coordination.

## Recommended Boundary

```text
JARVIS
  ├── Python Control Plane
  │     - agent/reasoning loop
  │     - task planning
  │     - tool calling
  │     - LLM/RAG
  │     - workflow orchestration
  │     - repository adapters
  │     - governance/preflight
  │     - AIOpsLab orchestration
  │     - session/provenance
  │     - evaluation
  │
  ├── Native Performance Plane
  │     - FermatEngine
  │     - particle computation
  │     - physics/math
  │     - GPU operations
  │     - low-latency rendering
  │
  └── Web / Presentation Plane
        - browser visualization
        - interactive controls
        - canvas
```

Rule:

```text
Reason/orchestrate  → Python
Compute/render fast → Native/C++/GPU
Present/interact    → Web/JavaScript
```

## TypeScript Adoption Addendum

**Status: HYPOTHESIS / UNVERIFIED for JARVIS**

Adopt TypeScript patterns where they provide compact typed schemas, repository/control-plane adapters, structured tool definitions, UI/dashboard consolidation, or low-boilerplate integration middleware.

Do **not** use TypeScript to replace Python agent/LLM reasoning and orchestration, C++/FermatEngine performance-critical computation, or the existing Emscripten/Web boundary unless performance evidence supports such a change.

Language alone does not guarantee lower token usage. Potential gains come from compact typed schemas, normalized JSON contracts, deterministic serialization, adapters that avoid repeated context, and structured tool definitions.

Therefore:

```text
TypeScript patterns may reduce JARVIS orchestration token overhead
if reused as structured adapter/schema patterns.
```

The token-efficiency benefit remains **UNKNOWN** until measured.

## Key Risks

1. `src/main.py` risks becoming a monolith.
2. A native boundary exists, but direct Python ↔ FermatEngine binding remains unverified.
3. Build reproducibility remains insufficiently established by the L0 inspection.
4. README vision is broader than the currently verified implementation.

## Explicit Unknowns

- exact Python dependency manifest;
- exact C++ build process;
- whether FermatEngine.cpp contains the full GPU implementation;
- whether Python communicates with the native engine elsewhere;
- complete `src` dependency graph;
- exact VIE/AI implementation;
- deployment architecture;
- existing CI/CD automation;
- existing AIOps integration;
- unindexed build/configuration files.

These remain unresolved; no guessing is permitted.

## Future Structure — Design Only

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

No restructuring is included in this L0 artifact.

## Governance State

| Item | State |
|---|---|
| Language-core assessment | Complete / L0 documentation |
| Python verdict | Keep as orchestration/control plane |
| C++/FermatEngine | Keep native |
| Web/JS | Keep presentation layer |
| Rust | Defer |
| TypeScript | Adopt schema/adapter/tool patterns only |
| Repository main | Unchanged |
| Implementation changes | None |
| Dependency/workflow changes | None |
| Merge / upstream | Not authorized |
