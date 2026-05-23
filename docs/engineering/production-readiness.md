# Production Readiness Standard

## Prompt Trace

- Prompt: PRM-005-artifact-elicitation.md
- Inputs: docs/outcomes/O-001-production-delivery-harness.md, docs/plans/P-001-production-delivery-harness.md, user decision to use public users as the default production bar
- Output: docs/engineering/production-readiness.md
- Date: 2026-05-23
- Operator: Codex

## Source

- Outcome brief: docs/outcomes/O-001-production-delivery-harness.md
- Delivery plan: docs/plans/P-001-production-delivery-harness.md
- Slice: 1.1 Production readiness standard

## Reader and Action

Reader: an engineer, agent, or reviewer preparing a variant for release.

After reading this document, the reader should be able to decide what evidence a variant must provide before it is treated as production-ready.

## Default Bar

The default production bar is public users.

This does not mean every early variant must launch publicly. It means the baseline treats public release risk as the default unless a variant profile explicitly lowers the bar and explains why.

Variants may use one of three release bars:

| Bar | Use When | Required Decision |
| --- | --- | --- |
| Public users | The variant may be used by external users or handle real user data. | Default. No downgrade needed. |
| Private beta | Access is limited and reviewed, but real users or real data may be involved. | Variant profile must state beta limits, exit criteria, and controls deferred until public release. |
| Internal tool | Use is limited to trusted maintainers with no external users and no sensitive production data. | Variant profile must state why public-user controls are not required yet. |

## Production Ready Means

A variant is production-ready only when it has current evidence for:

- outcome and non-goals
- user and operator expectations
- architecture and major design decisions
- test coverage appropriate to the release bar
- security review appropriate to data, permissions, and exposure
- release, rollback, and stopping point
- observability and runbook expectations
- support and incident handling expectations
- known risks and accepted deferrals

Work is not production-ready only because implementation tasks are closed.

## Required Evidence

| Area | Evidence Required |
| --- | --- |
| Product intent | Outcome brief with success criteria, non-goals, constraints, and risks. |
| Variant scope | Variant profile showing inherited baseline controls and explicit overrides. |
| Architecture | Architecture overview or ADRs for system boundaries, data flow, security-sensitive decisions, and operational assumptions. |
| Design | Design docs for implementation slices with acceptance checks and rollback or stopping points. |
| Testing | Test strategy evidence for the variant release bar. |
| Security | Security review or documented reason why the variant does not trigger security review. |
| Release | Release procedure, rollback procedure, and required pre-release checks. |
| Observability | Logs, metrics, traces, health checks, or diagnostics appropriate to the variant. |
| Operations | Runbook notes for common failures and recovery actions. |
| Verification | Verification records showing current evidence for release checks. |

## Required Gates

| Gate | Required Before Release |
| --- | --- |
| Planning | Outcome brief, delivery plan, and variant profile exist. |
| Design | Architecture and design artifacts exist for material decisions. |
| Implementation | Task contracts have acceptance checks and verification evidence. |
| Test | Required tests pass or accepted deferrals are documented. |
| Security | Security review is complete when triggered by the variant risk profile. |
| Release | Release and rollback plan are documented and reviewed. |
| Operations | Observability and runbook expectations are documented. |
| Review | Production readiness checklist is complete and reviewed. |

## Definition of Done

A production slice is done when:

- acceptance checks are met
- verification evidence is current
- known risks are documented
- release impact is understood
- rollback or stopping point is documented
- docs and file maps are updated when needed
- no required gate is skipped without an explicit accepted deferral

## Deferrals

Deferrals are allowed only when they are explicit.

Each deferral must state:

- what is deferred
- why it is safe to defer
- release bar where the deferral is allowed
- owner
- follow-up trigger
- risk if the deferral remains open

Do not use deferrals to bypass security, data protection, rollback, or evidence requirements for public-user releases.

## Variant Profile Timing

A variant profile is required before variant-specific architecture, design, or implementation starts.

The profile may be lightweight at first. It must still state the release bar, users, runtime target, deployment assumptions, inherited baseline controls, overrides, and open decisions.

Do not use architecture or implementation work to discover the release bar. Record the release bar first, then design against it.

## Variant Overrides

The generic baseline applies to every variant. A variant profile may override the baseline only when it records:

- inherited control
- proposed override
- reason
- risk
- reviewer or owner
- expiry or revisit trigger

If no override is recorded, the baseline applies.

## Review Questions

- Does the variant identify its release bar?
- Are public-user controls applied or explicitly downgraded?
- Is the outcome still aligned with the implementation?
- Are user, operator, and support expectations clear?
- Are test, security, release, rollback, observability, and runbook expectations addressed?
- Are accepted risks visible to a reviewer?
- Is there fresh verification evidence?

## Open Decisions

- The first product variant has not been chosen.
- CI provider is not chosen.
- Deployment target is not chosen.
- Product-specific test tooling is not chosen.
- Support and incident response owner model is not chosen.

## Scope Check

This standard defines the generic release bar only. It does not choose stack, hosting, CI provider, deployment target, or product-specific checks.

## Language/Readability Check

The document uses standard software engineering terms. The terms variant and release bar are direct labels for product specialization and readiness level.

## Recommended Next Step

Create the stack-neutral test strategy for Slice 1.2.
