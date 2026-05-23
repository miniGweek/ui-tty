# O-001: Production Delivery Harness

## Prompt Trace

- Prompt: PRM-005-artifact-elicitation.md and PRM-020-stage-1-problem-contract.md
- Inputs: User direction to create a generic repo delivery process first, AGENTS.md, docs/delivery-workflow.md, docs/prompts/README.md, docs/templates/outcome-brief.md
- Output: docs/outcomes/O-001-production-delivery-harness.md
- Date: 2026-05-23
- Operator: Codex

## Summary

Create a generic production delivery harness for this repository. The harness will define the baseline process, checks, and evidence required to take future software variants from idea to production-grade delivery.

The harness should be product-neutral first. Future variants, such as a hosted web app, local app, desktop app, server tool, or agent-assisted workflow, inherit the baseline unless a variant profile explicitly documents an override.

## Goals

- Define the baseline production delivery process for future variants.
- Make production readiness visible before implementation starts.
- Require test, security, release, rollback, observability, and support expectations to be addressed in the delivery plan.
- Keep variant-specific choices separate from the generic baseline.
- Make deviations from the baseline explicit and reviewable.

## Non-Goals

- Do not choose the final product architecture for the UI remote terminal yet.
- Do not choose a frontend, backend, hosting, or packaging stack yet.
- Do not create implementation tickets for product code yet.
- Do not define enterprise-scale process that is not needed for an early repository.
- Do not replace outcome briefs, delivery plans, architecture docs, design docs, specs, task contracts, or verification records.

## Users

- Primary user: an engineer or agent using this repository to plan and deliver software variants.
- Secondary user: a reviewer deciding whether a variant is ready to implement, release, or operate.

## Success Criteria

- The repository has a documented generic production readiness standard.
- The repository has a documented test strategy that can be specialized by variant.
- The repository has a documented security review path.
- The repository has a documented release and rollback process.
- The repository has documented observability and runbook expectations.
- Future variant profiles can state inherited baseline controls and explicit overrides.
- A delivery plan can reference the harness and produce clear readiness evidence before release.

## Constraints

- Technical: the harness must be stack-neutral until the first variant chooses a stack.
- Product: the harness must support multiple future variants without forcing premature product architecture.
- Time: the first version should be lightweight enough to use immediately.
- Operational: the harness must produce evidence that a future engineer or agent can inspect without relying on chat history.

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The harness becomes too generic to guide real delivery. | Variants may still guess production requirements. | Add concrete checklists and require variant profiles to map inherited controls and overrides. |
| The harness becomes too heavy for early development. | Delivery slows before the product shape is known. | Keep the baseline lean and require only controls that affect production readiness. |
| Product-specific assumptions enter the generic baseline. | Future variants inherit the wrong constraints. | Keep stack and deployment choices in variant profiles, not the baseline harness. |
| Readiness evidence is not captured. | Reviewers cannot tell whether a variant is ready. | Require verification records and prompt trace for governed artifacts. |

## Open Questions

- What variant profile should be created first?
- What production bar should each variant default to: internal tool, private beta, or public users?
- Which CI provider and deployment target should the first variant use?
- What security review depth is required for the first variant?
- What support and incident response expectations should apply before public release?

## Scope Check

This outcome defines the generic delivery harness only. Product architecture and implementation remain out of scope.

## Language/Readability Check

No new repository terms are introduced beyond production delivery harness and variant profile. Both are used as direct names for the baseline process and per-product specialization.

## Recommended Next Step

Create a delivery plan for this outcome. The plan should sequence the production readiness standard, test strategy, security review path, release and rollback process, observability/runbook expectations, and variant profile template.
