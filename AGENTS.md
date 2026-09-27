# AGENTS.md — atap

Read by every agent that works in this repo: Claude Code (via `CLAUDE.md`), Cursor (local
and Cursor Projects), and Claude Chat. This file holds only pointers and facts specific
to this repo. **Everything shared lives in one place:**
https://raw.githubusercontent.com/garywelz/copernicus-web/main/governance/AGENT_ROLES.md

## Before you do anything

Fetch these live, with plain fetches (no cache-busters). GitHub wins over any uploaded,
remembered, or pasted copy.

- Agent roles, lanes, session rules, repo↔Space map: https://raw.githubusercontent.com/garywelz/copernicus-web/main/governance/AGENT_ROLES.md
- Constitution: https://raw.githubusercontent.com/garywelz/copernicus-web/main/governance/CONSTITUTION.md
- Bulletin (read the newest entries): https://raw.githubusercontent.com/garywelz/copernicus-web/main/governance/BULLETIN.md

Then follow the **Session rules** and your lane in `AGENT_ROLES.md`, and report in its
four-section format. If this repo has `docs/GOVERNANCE_LOCAL.md`, read it too: it may add
to or tighten the shared rules, never loosen their invariants
(`governance/ENGINE_ONBOARDING.md` §3).

## The floor — holds even if the fetch fails

1. Propose before executing; Gary approves significant changes first.
2. Never force-push or rewrite history; no autonomous or triggered run pushes to `main`.
3. Never print credential-shaped files in full; if one reaches output, say so at once.

*(Deliberately duplicated in every repo's `AGENTS.md`; canonical text is in
`AGENT_ROLES.md` → Session rules. Change it there first.)*

## This repo

- **The ATAP engine** — axiomatic theories, algorithms, and proofs as dependency graphs.
  Live frontier: whether the algorithm-capsule regularity is real or a selection
  artifact (n=3). Focus file: `docs/research_focus.json`.
- Holds papers, the focus file, and docs (Reorg Plan, Option B). Deploy-coupled math
  content stays in `copernicus-web`; `math_processes` in Firestore is ATAP data operated
  by Core.
- arXiv acquisition has failed with 429s/timeouts before; treat an empty arXiv result
  as an instrument question first.
