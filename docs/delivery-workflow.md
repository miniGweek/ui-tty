# Delivery Workflow

## Reader and Action

Reader: an internal software engineer or AI-agentic engineer joining the repository cold.

After reading this document, the reader should be able to start a feature, choose the right artifact, create task contracts, execute a slice, and record verification evidence.

## Principles

- Outcomes before implementation. Code starts from an explicit intended result.
- One active outcome by default. Split outcomes only when they can ship independently.
- Thin vertical slices. Prefer small tasks that deliver observable behavior.
- Durable decisions. Architecture choices live in docs, not only in chat or commits.
- Evidence before completion. A task is complete only when its acceptance checks have current evidence.

## Lean Gates

| Gate | Required artifact | Exit criteria |
| --- | --- | --- |
| Intent | Outcome brief | Goals, non-goals, users, constraints, success criteria, and risks are explicit. |
| Sequencing | Delivery plan | Milestones, task order, dependencies, and acceptance checks are clear. |
| System design | Architecture overview or ADR | Components, boundaries, data flow, and material decisions are recorded when needed. |
| Implementation design | Design doc | Implementation approach, interfaces, state, alternatives, and trade-offs are recorded when needed. |
| Behavior design | Spec | User-visible behavior, interfaces, states, errors, and edge cases are defined. |
| Execution | Task contract | Inputs, outputs, dependencies, files likely touched, acceptance checks, and verification method are defined. |
| Completion | Verification record | Fresh evidence shows the task or slice meets its acceptance checks. |

## Artifact Naming

- Outcome brief: `docs/outcomes/O-001-short-name.md`
- Delivery plan: `docs/plans/P-001-short-name.md`
- Architecture overview: `docs/architecture/A-001-short-name.md`
- Architecture decision record: `docs/architecture/ADR-001-short-name.md`
- Design doc: `docs/design/D-001-short-name.md`
- Spec: `docs/specs/S-001-short-name.md`
- Task contract: `docs/tasks/T-001-short-name.md`
- Verification record: `docs/verification/V-001-short-name.md`

Keep identifiers stable. If a title changes, keep the identifier and update the slug only when it improves clarity.

## Operating Process

1. Create or update the outcome brief.
2. Check that success criteria are observable.
3. Create the delivery plan and split it into thin task contracts.
4. Add architecture, design, or spec artifacts only where they reduce ambiguity.
5. Execute one task contract at a time.
6. Record verification evidence in the task contract or a linked verification record.
7. Update the delivery plan with actual status.

## Completion Rules

- Do not mark an outcome complete because all tasks are closed. Mark it complete when success criteria have evidence.
- Do not expand scope inside a task contract. Create a follow-up task when new work is discovered.
- Do not leave failed verification as prose only. Record the command, result, and next action.
- If verification cannot run, record the reason and the residual risk.
