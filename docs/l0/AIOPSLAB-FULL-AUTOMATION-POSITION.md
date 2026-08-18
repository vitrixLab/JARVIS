# AIOpsLab Full-Automation Position — JARVIS L0

**Status:** Research-backed position / L0 design record  
**Repository:** `vitrixLab/JARVIS`  
**Branch:** `working/jarvis-l0`  
**Scope:** Reference architecture and governance position; no implementation migration

## Executive position

Microsoft AIOpsLab demonstrates that useful AI-powered automation is an end-to-end operational loop rather than an LLM connected directly to a shell. The framework coordinates environment provisioning, workloads, fault injection, telemetry, agent interaction, sessions, and evaluation.

The JARVIS adoption position is:

> **Automate the operational lifecycle end-to-end where actions are bounded, observable, reversible, and evaluated; keep repository history, security-sensitive configuration, and irreversible governance decisions behind explicit authorization gates.**

Human administrator absence must not be interpreted as unrestricted authorization.

## Automation layers to adopt as design principles

### Environment automation

Use reproducible infrastructure and environment provisioning for experiments and validation.

### Scenario automation

Represent workloads, faults, problem initialization, recovery, and cleanup as reproducible scenarios.

### Observability automation

Treat logs, metrics, and traces as the evidence plane for agent reasoning and evaluation.

### Agent automation

Keep agents behind explicit interfaces and bounded actions. The orchestrator remains the control boundary between reasoning and environment mutation.

### Evaluation automation

Preserve session-level evidence and evaluate detection, localization, analysis, and mitigation rather than using only a binary success label.

### CI automation

Continuously exercise the real orchestration path and preserve diagnostics on failure.

### Governance automation

Before any write, verify:

1. repository and branch;
2. intended target path(s);
3. expected base commit;
4. operation type;
5. authorization;
6. reversibility;
7. audit/provenance record.

## JARVIS control-plane position

```text
AI reasoning
    ↓
Orchestrator / policy boundary
    ↓
Validated action
    ↓
Sandbox / branch / isolated environment
    ↓
Automated tests + evaluation
    ↓
Audit record
    ↓
Explicit authorization for protected or irreversible mutation
```

This model preserves autonomy without treating an administrative vacuum as a permission escalation.

## What should be adopted

- orchestrator-first automation;
- scenario-as-code;
- environment-as-code;
- telemetry-as-evidence;
- session-level provenance;
- automated evaluation;
- CI integration testing;
- automatic failure diagnostics;
- interchangeable agent interfaces;
- bounded tool/action interfaces;
- repository pre-write controls.

## What should not be adopted blindly

AIOpsLab research does not establish that an AI agent should have unrestricted authority over repository administration, protected branches, credentials, or irreversible Git history.

Therefore JARVIS should not interpret autonomy as:

- force-pushing by default;
- rewriting history to conceal mistakes;
- deleting branches or records without policy;
- modifying protected configuration without a gate;
- treating lack of human response as authorization;
- bypassing the orchestrator and policy layer.

## Maturity target

| Level | Capability | JARVIS position |
|---|---|---|
| 0 | Manual operation | Fallback |
| 1 | Scripted automation | Foundation |
| 2 | Orchestrated automation | Reference baseline |
| 3 | AI-assisted closed-loop operations | Primary development target |
| 4 | Governed autonomous operations | **Recommended target** |
| 5 | Fully autonomous unrestricted administration | **Not adopted** |

## Conclusion

The highest-value JARVIS adoption is to combine AIOpsLab-style orchestrated autonomous operations with reproducible environments, telemetry-driven reasoning, measurable evaluation, continuous integration, provenance, and explicit repository governance.

The result should be a system that can continue operating when human availability is low without making human absence equivalent to unrestricted authorization.

## Sources

- Microsoft AIOpsLab repository: https://github.com/microsoft/AIOpsLab
- Microsoft AIOpsLab documentation: https://microsoft.github.io/AIOpsLab/
- Chen et al., *AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds* (MLSys 2025): https://arxiv.org/abs/2501.06706
- Shetty et al., *Building AI Agents for Autonomous Clouds: Challenges and Design Principles* (SoCC 2024): https://doi.org/10.1145/3698038.3698525

**Classification:** The AIOpsLab architecture description is source-derived; the JARVIS governance and adoption position is a VitrixLab design decision.
