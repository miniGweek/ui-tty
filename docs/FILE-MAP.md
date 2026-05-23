# File Map

This file explains where work belongs. Use it before creating new files. It is not a file inventory; use `docs/FILE-INDEX.md` when you need to find a specific file.

## Planning and Delivery

| Work Type | Location | Notes |
| --- | --- | --- |
| Outcome brief | `docs/outcomes/` | Start here for a new product or feature outcome. |
| Delivery plan | `docs/plans/` | Sequence milestones, task contracts, dependencies, and checks. |
| Architecture overview | `docs/architecture/` | Use for system shape, boundaries, data flow, and operational concerns. |
| ADR | `docs/architecture/` | Use for one durable architecture decision. |
| Design doc | `docs/design/` | Use for implementation approach, trade-offs, state ownership, and interfaces. |
| Spec | `docs/specs/` | Use for user-visible behavior, APIs, states, errors, and edge cases. |
| Task contract | `docs/tasks/` | Use for one executable unit of work. |
| Verification record | `docs/verification/` | Use for evidence that a task, slice, or outcome meets its checks. |
| Production engineering doc | `docs/engineering/` | Use for production readiness, test strategy, security review, release, rollback, observability, and runbook standards. |
| Template | `docs/templates/` | Use when adding or changing delivery artifact formats. |
| Production readiness checklist | `docs/templates/production-readiness-checklist.md` | Use before releasing a variant. |
| Variant profile | `docs/templates/variant-profile.md` | Use before variant-specific architecture, design, or implementation starts. |
| Governed prompt | `docs/prompts/` | Use for stage-specific planning and design prompts. |
| Artifact elicitation prompt | `docs/prompts/PRM-005-artifact-elicitation.md` | Use when the user request does not clearly identify the target artifact or required context. |
| Local automation | `scripts/` | Put repeatable local checks and helper scripts here. |
| Test | `tests/` | Put local test suites here. |

## Repository Navigation

| Work Type | Location | Notes |
| --- | --- | --- |
| Agent instructions | `AGENTS.md` | Keep lightweight. Put detailed process in docs. |
| Repository overview | `README.md` | Keep focused on how to start. |
| File inventory | `docs/FILE-INDEX.md` | Update when important files or directories change. |
| File placement guide | `docs/FILE-MAP.md` | Update when new work types or directories are introduced. |
| Prompt governance | `docs/prompts/README.md` | Use before creating planning or design artifacts with prompts. |

## Maintenance Rule

When a change creates, moves, renames, or deletes important files or directories, update `docs/FILE-INDEX.md`. Update `docs/FILE-MAP.md` only when the change adds or changes where a type of work belongs. When a change creates or changes governed prompts, update `docs/prompts/README.md` too. If no update is needed, state why in the final summary.
