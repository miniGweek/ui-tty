# PRM-005: Artifact Elicitation

Use this prompt when the user asks for a plan, design, spec, task, or review artifact, but the target artifact or required context is not clear yet.

This prompt turns incomplete user intent into one governed repository artifact.

## Inputs

- User request.
- Existing repository docs.
- `docs/prompts/README.md`.
- `PRM-000-standing-guardrails.md`.
- The matching template from `docs/templates/`, once the target artifact is known.

## Operating Rules

- Read local instructions before drafting.
- Inspect existing docs before asking the user questions.
- Choose one target artifact.
- Ask at most 5 high-value questions only when the answer cannot be found in the repository.
- State assumptions when continuing without an answer.
- Do not create implementation tickets before the outcome, plan, architecture, or design context exists.
- Do not produce multiple governed artifacts unless the user explicitly asks.
- Include `Prompt Trace` in the generated artifact.

## Step 1: Classify the Request

Classify the user request as one primary work type:

- outcome brief
- delivery plan
- architecture overview
- ADR
- design doc
- spec
- task contract
- verification record
- review packet
- unclear

If the request is unclear, identify the closest likely artifact and state the assumption.

## Step 2: Discover Existing Context

Inspect relevant repository docs before asking questions:

- `docs/FILE-MAP.md` for where work belongs.
- `docs/FILE-INDEX.md` for existing important files.
- `docs/delivery-workflow.md` for required gates.
- Existing artifacts in the target directory.
- The matching template in `docs/templates/`.

Do not ask the user for facts that the repository already answers.

## Step 3: Ask Only Useful Questions

Ask questions only when the answer changes the artifact materially.

Prefer questions about:

- desired outcome
- success criteria
- non-goals
- users or operators
- constraints
- risk level
- acceptance checks
- target artifact choice

Avoid questions about:

- file locations covered by `docs/FILE-MAP.md`
- template structure
- naming conventions already defined by the repository
- minor wording preferences

## Step 4: Select the Template and Stage Prompt

Select the matching template:

| Artifact | Template | Optional Stage Prompt |
| --- | --- | --- |
| Outcome brief | `docs/templates/outcome-brief.md` | `PRM-020-stage-1-problem-contract.md` |
| Delivery plan | `docs/templates/delivery-plan.md` | `PRM-050-stage-4-phase-roadmap.md` |
| Architecture overview | `docs/templates/architecture-overview.md` | `PRM-040-stage-3-architecture-overview.md` |
| ADR | `docs/templates/adr.md` | `PRM-030-stage-2-architecture-options.md` |
| Design doc | `docs/templates/design.md` | `PRM-060-stage-5-detailed-design-slice.md` |
| Spec | `docs/templates/spec.md` | Use when behavior needs precision. |
| Task contract | `docs/templates/task-contract.md` | `PRM-010-stage-0-intake-task-contract.md` or `PRM-080-stage-7-implementation-tickets.md` |
| Verification record | `docs/templates/verification-record.md` | `PRM-070-stage-6-scope-readability-review.md` or `PRM-090-stage-8-review-packet.md` |

Use the stage prompt only when it improves the artifact. The template remains the output shape.

## Step 5: Draft the Artifact

Create or update exactly one governed artifact.

The artifact must include:

- `Prompt Trace`
- source artifacts or source material
- assumptions
- open decisions
- acceptance checks where relevant
- recommended next stage

If the artifact cannot be drafted safely, stop and report:

- missing information
- why it matters
- the smallest useful next question or action

## Step 6: Close the Loop

End with:

- artifact created or updated
- assumptions made
- open decisions
- next recommended prompt stage
- verification performed

Do not claim the artifact is complete unless it is decision-complete for its purpose.
