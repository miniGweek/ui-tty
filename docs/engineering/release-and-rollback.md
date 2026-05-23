# Release and Rollback

## Prompt Trace

- Prompt: PRM-005-artifact-elicitation.md
- Inputs: docs/outcomes/O-001-production-delivery-harness.md, docs/plans/P-001-production-delivery-harness.md, docs/engineering/production-readiness.md, docs/engineering/test-strategy.md, docs/engineering/security-review.md, user decision to split release/rollback from observability/runbooks
- Output: docs/engineering/release-and-rollback.md
- Date: 2026-05-23
- Operator: Codex

## Source

- Outcome brief: docs/outcomes/O-001-production-delivery-harness.md
- Delivery plan: docs/plans/P-001-production-delivery-harness.md
- Production readiness standard: docs/engineering/production-readiness.md
- Slice: 1.4 Release, rollback, and operations baseline

## Reader and Action

Reader: an engineer, agent, or reviewer preparing a variant for release.

After reading this document, the reader should be able to state what release evidence, rollback path, and stopping point a variant needs before release.

## Principles

- A release must be repeatable.
- A release must have a rollback or stopping point.
- Release evidence must be current.
- Product-specific deployment details belong in the variant profile.
- Unknown release impact blocks public-user release.
- Rollback cannot rely only on memory or chat history.

## Required Release Evidence

Every variant release must record:

- release bar
- variant profile
- source revision or artifact version
- required checks and results
- security review status
- release steps
- rollback or stopping point
- expected user or operator impact
- known risks and accepted deferrals
- release owner or operator

## Release Bars

| Release Bar | Release Expectation |
| --- | --- |
| Public users | Repeatable release steps, reviewed rollback, current checks, security review, production readiness checklist. |
| Private beta | Repeatable release steps, rollback or stopping point, limited user scope, current checks, accepted deferrals. |
| Internal tool | Repeatable release or install steps, recovery notes, current checks, known limitations. |

## Pre-Release Gate

Before release, a variant must show:

- outcome and variant profile are current
- required tests and policy checks passed
- required security review is complete
- release steps are documented
- rollback or stopping point is documented
- observability and runbook expectations are documented
- production readiness checklist is reviewed

If any gate is skipped, the release record must include an accepted deferral.

## Rollback and Stopping Point

Every variant must define at least one of:

- rollback to previous version
- disable feature flag
- stop deployment before user impact
- restore from backup
- manual recovery procedure
- revert commit and redeploy
- disable integration or external dependency

Public-user variants must document who can perform rollback and what signal triggers it.

## Release Record

Each release should produce a release record with:

- variant name
- release bar
- release date
- version or commit
- checks run
- security review reference
- production readiness checklist reference
- release steps
- rollback steps
- owner
- decision: release / hold / rollback

The release record may live in `docs/verification/` until a dedicated release system exists.

## Deferrals

Release deferrals must state:

- deferred item
- reason
- allowed release bar
- owner
- follow-up trigger
- risk

Deferrals are not allowed for unknown rollback, unknown security scope, or missing release owner in public-user releases.

## Review Questions

- Can another engineer or agent repeat the release?
- Is the release tied to a known source revision or artifact?
- Are required checks current?
- Is rollback documented and reviewed?
- Is user or operator impact understood?
- Are deferrals explicit and appropriate for the release bar?
- Is the release decision clear?

## Open Decisions

- CI provider is not chosen.
- Deployment target is not chosen.
- Artifact packaging format is not chosen.
- Release record naming is not yet standardized beyond the generic docs structure.

## Scope Check

This document defines stack-neutral release and rollback expectations. It does not choose CI, hosting, deployment tooling, package format, or environment strategy.

## Language/Readability Check

The document uses standard release engineering terms. Stopping point means a documented point where release can safely halt before or after user impact.

## Recommended Next Step

Use this document with observability and runbook expectations before creating a variant profile.
