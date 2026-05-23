# File Map

This file explains where work belongs. Use it before creating new files.

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
| Template | `docs/templates/` | Use when adding or changing delivery artifact formats. |

## Repository Navigation

| Work Type | Location | Notes |
| --- | --- | --- |
| Agent instructions | `AGENTS.md` | Keep lightweight. Put detailed process in docs. |
| Repository overview | `README.md` | Keep focused on how to start. |
| File inventory | `docs/FILE-INDEX.md` | Update when important files or directories change. |
| File placement guide | `docs/FILE-MAP.md` | Update when new work types or directories are introduced. |

## Maintenance Rule

When a change creates, moves, renames, or deletes important files or directories, update both `docs/FILE-INDEX.md` and `docs/FILE-MAP.md` in the same change. If no update is needed, state why in the final summary.
