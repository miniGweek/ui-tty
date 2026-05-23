# P-001: Production Delivery Harness

## Prompt Trace

- Prompt: PRM-005-artifact-elicitation.md and PRM-050-stage-4-phase-roadmap.md
- Inputs: docs/outcomes/O-001-production-delivery-harness.md, AGENTS.md, docs/delivery-workflow.md, docs/prompts/README.md, docs/templates/delivery-plan.md, user decision to start with essential docs plus minimum viable enforcement
- Output: docs/plans/P-001-production-delivery-harness.md
- Date: 2026-05-23
- Operator: Codex

## Source Outcome

- Outcome brief: docs/outcomes/O-001-production-delivery-harness.md

## Summary

Deliver the generic production delivery harness in two tracks: essential production engineering docs and minimum viable enforcement. The first version must be usable before the product stack is chosen.

The baseline rule is: product variants inherit the generic harness unless a variant profile explicitly documents an override. Product-specific build, test, deployment, and runtime checks are deferred until a variant chooses its stack.

## Milestones

| Milestone | Purpose | Acceptance Check | Status |
| --- | --- | --- | --- |
| M1: Baseline standard | Define the production engineering expectations every variant inherits. | Production readiness, test strategy, security review, release/rollback, observability/runbook, definition of done, and variant profile docs exist. | In progress |
| M2: Minimum viable enforcement | Add a local policy check command for governed docs. | A single command verifies the repo documentation governance rules and exits non-zero on failure. | Not started |
| M3: Harness review | Verify the harness is usable for the first product variant. | A review packet shows what is ready, what is deferred, and what a variant must still decide. | Not started |

## Slices

| Slice | Goal | Scope | Explicit Exclusions | What Ships | Acceptance Tests | Risks | Start Condition | Rollback or Stopping Point | Human Review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 Production readiness standard | Define the baseline release bar. | Readiness standard, definition of done, required evidence. | Product stack checks, hosting-specific requirements. | `docs/engineering/production-readiness.md` and readiness checklist template. | A future variant can identify required evidence before release. | Too generic to guide decisions. | O-001 exists. | Stop after doc review if readiness requirements are unclear. | Yes |
| 1.2 Test strategy | Define stack-neutral testing expectations. | Test layers, red-green TDD expectation, evidence rules, variant-specific test hooks. | Concrete test framework selection. | `docs/engineering/test-strategy.md`. | A variant can map its unit, integration, end-to-end, and manual checks. | Over-prescribing before stack choice. | Slice 1.1 draft exists. | Stop if test categories cannot stay stack-neutral. | Yes |
| 1.3 Security review path | Define when and how security review happens. | Threat model trigger, review depth, sensitive change categories, evidence. | Full security policy or compliance program. | `docs/engineering/security-review.md`. | A variant can tell when security review is required. | Missing high-risk categories. | Slice 1.1 draft exists. | Stop if review triggers are unclear. | Yes |
| 1.4 Release, rollback, and operations baseline | Define release evidence, rollback, observability, and runbook expectations. | Release readiness, rollback/stopping points, logs/metrics/traces expectations, runbook notes. | Specific cloud, CI, or deployment platform. | `docs/engineering/release-and-rollback.md` and `docs/engineering/observability-and-runbooks.md`. | A variant can describe how it releases, observes, and rolls back. | Baseline may become too platform-specific. | Slices 1.1 and 1.2 drafts exist. | Stop if deployment target assumptions enter the baseline. | Yes |
| 1.5 Variant profile template | Define how variants inherit or override the baseline. | Variant profile template with inherited controls, overrides, risk level, required checks. | First product variant profile. | `docs/templates/variant-profile.md`. | A future variant can document inherited controls and deviations. | Variants may bypass baseline without explaining why. | Slices 1.1 through 1.4 drafted. | Stop if override rules are ambiguous. | Yes |
| 2.1 Policy check command | Add a local command for docs governance. | Markdown link/ASCII checks, prompt inventory check, prompt trace checks, required index/map checks, banned wording checks. | Product build, app tests, deployment checks. | A script such as `scripts/check-docs.sh`. | The command passes on the current repo and fails on missing governed prompt inventory. | False positives that slow work. | Prompt and template rules are stable enough to check. | Disable only the failing check with a documented reason. | Yes |
| 2.2 CI-ready check contract | Document how CI should call the local check command later. | Command contract, expected exit codes, what CI must report. | Creating CI workflow before provider is chosen. | `docs/engineering/ci-check-contract.md`. | A future CI job can call the same local command without redesign. | CI assumptions leak in too early. | Slice 2.1 exists. | Stop at documented contract if CI provider is undecided. | Yes |
| 3.1 Harness review packet | Prepare the first review of the harness. | Summary, readiness evidence, deferred decisions, risks, recommendation. | Implementing first product variant. | Review packet in `docs/verification/`. | Reviewer can decide whether the harness is ready to govern the first variant. | Review packet hides unresolved gaps. | Milestones M1 and M2 complete. | Stop if core docs or policy checks are missing. | Yes |

## Task Contracts

| Task | Purpose | Depends On | Status |
| --- | --- | --- | --- |
| T-001 | Create production readiness standard and checklist template. | O-001, P-001 | Drafted |
| T-002 | Create stack-neutral test strategy. | T-001 | Drafted |
| T-003 | Create security review path. | T-001 | Drafted |
| T-004 | Create release, rollback, observability, and runbook baseline. | T-001, T-002 | Drafted |
| T-005 | Create variant profile template. | T-001, T-002, T-003, T-004 | Drafted |
| T-006 | Add docs governance check command. | T-005 | Not started |
| T-007 | Document CI-ready check contract. | T-006 | Not started |
| T-008 | Create harness review packet. | T-001 through T-007 | Not started |

## Dependencies

- O-001 production delivery harness outcome brief.
- Current governed prompt and template structure.
- User decision that the first harness version is docs plus minimum viable enforcement.

## Verification Plan

- Markdown links resolve.
- Markdown is ASCII unless explicitly justified.
- Prompt README lists every governed prompt file.
- Templates include `Prompt Trace`.
- New important docs are listed in `docs/FILE-INDEX.md`.
- New work types are mapped in `docs/FILE-MAP.md`.
- The docs governance check command passes locally once Slice 2.1 exists.

## Status Log

| Date | Change |
| --- | --- |
| 2026-05-23 | Created initial delivery plan. |
| 2026-05-23 | Drafted Slice 1.1 production readiness standard and checklist template. |
| 2026-05-23 | Drafted Slice 1.2 stack-neutral test strategy. |
| 2026-05-23 | Drafted Slice 1.3 security review path. |
| 2026-05-23 | Drafted Slice 1.4 release/rollback and observability/runbook baselines. |
| 2026-05-23 | Drafted Slice 1.5 variant profile template. |

## Scope Check

This plan covers the generic production delivery harness only. Product stack selection, product architecture, hosting, deployment provider, and product implementation remain out of scope.

## Language/Readability Check

The plan uses standard engineering terms. The terms production delivery harness and variant profile are carried from O-001 and remain specific to this repository workflow.

## Leveling Check

The plan has three milestones and eight slices. Each slice has one primary decision and produces a reviewable artifact or local enforcement command.

## Recommended First Slice

Start with Slice 1.1: Production readiness standard.

## Why That Slice Should Come First

The readiness standard defines the baseline that the test strategy, security review, release process, observability expectations, variant profile, and policy checks must enforce.
