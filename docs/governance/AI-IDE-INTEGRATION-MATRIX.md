# AI IDE Integration Matrix

- Control Number: GOV-IDE-001
- Revision: 0.1
- Status: DRAFT
- Repository: vitrixLab/JARVIS
- Branch: working/governance-ai-ide
- Base SHA: 5b0a3c272b4a76fb9469ed8e185ce838912a6eb1
- Authorization: AUTH-021
- Merge Authorization: NOT AUTHORIZED

## Status

This document defines a future integration design. No agent is currently connected to JARVIS.

## Common Preflight Contract

AI Agent / IDE
        ↓
Proposed change
        ↓
JARVIS preflight
        ↓
L0 / L1 / L2 / L3 clearance
        ↓
repo / branch / path allowlist
        ↓
GO / NO-GO
        ↓
scoped execution
        ↓
post-write report
        ↓
ledger reconciliation

## Candidate Agents

| Agent | Type | Status |
|---|---|---|
| OpenAI Codex CLI | Local CLI | Design candidate |
| GitHub Copilot Agents | Cloud coding agent | Design candidate |
| AntiGravity | AI IDE / agent | Design candidate |
| Cursor | AI IDE | Design candidate |
| Claude Code | Local CLI | Design candidate |
| Windsurf / Cascade | AI IDE | Future candidate |
| Aider | CLI agent | Future candidate |

## Boundary

JARVIS is not yet a live enforcement gateway.

A future standard JARVIS API/MCP contract is required before any real integration.
