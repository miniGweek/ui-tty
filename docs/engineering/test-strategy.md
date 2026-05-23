# Test Strategy

## Prompt Trace

- Prompt: PRM-005-artifact-elicitation.md
- Inputs: docs/outcomes/O-001-production-delivery-harness.md, docs/plans/P-001-production-delivery-harness.md, docs/engineering/production-readiness.md, user decision to allow smaller end-to-end coverage when a variant surface is simple and justified
- Output: docs/engineering/test-strategy.md
- Date: 2026-05-23
- Operator: Codex

## Source

- Outcome brief: docs/outcomes/O-001-production-delivery-harness.md
- Delivery plan: docs/plans/P-001-production-delivery-harness.md
- Production readiness standard: docs/engineering/production-readiness.md
- Slice: 1.2 Test strategy

## Reader and Action

Reader: an engineer, agent, or reviewer defining test evidence for a future variant.

After reading this document, the reader should be able to choose the right test layers, record required evidence, and justify any reduced test set.

## Principles

- Test behavior, not implementation detail.
- Use red-green-refactor TDD when changing behavior.
- Prefer repeatable automated checks over manual checks.
- Keep tests close to the behavior they protect.
- Make release evidence current and easy to rerun.
- Let simple variants justify smaller test sets, but do not let them skip risk analysis.

## Test Layers

| Layer | Purpose | Expected Evidence |
| --- | --- | --- |
| Unit | Verify isolated behavior and edge cases. | Test command output or equivalent result. |
| Integration | Verify boundaries between components, storage, APIs, tools, or services. | Test command output, service logs, or controlled run evidence. |
| Contract or schema | Verify file formats, API shapes, event shapes, or command interfaces. | Schema validation, type checks, or contract tests. |
| End-to-end | Verify critical user or operator workflows through the real product surface. | Browser, CLI, API, desktop, or workflow run evidence depending on variant. |
| Manual review | Verify cases that cannot be automated yet. | Steps run, result, reviewer, and reason automation is deferred. |
| Policy checks | Verify governed repository rules. | Local policy command output. |

## Release Bar Defaults

| Release Bar | Default Test Expectation |
| --- | --- |
| Public users | Unit, integration, contract/schema, policy checks, and end-to-end coverage for critical workflows. |
| Private beta | Same as public users unless the variant profile limits scope and records accepted deferrals. |
| Internal tool | Unit, integration or equivalent boundary checks, policy checks, and manual verification for critical workflows when end-to-end automation is not useful yet. |

## End-to-End Coverage Rule

Public-user variants should have end-to-end coverage for critical workflows by default.

A variant may use a smaller test set when its surface is simple. The variant profile must record:

- why the surface is simple
- which critical workflows exist
- which workflows are covered by lower-level tests
- what manual verification remains
- what risk is accepted
- when end-to-end coverage must be added later
- who accepted the reduced set

Reduced end-to-end coverage is not allowed when the variant handles sensitive data, irreversible actions, payments, permissions, authentication, production writes, or safety-impacting behavior.

## TDD Rule

For behavior changes:

1. Write or update a failing test that describes the expected behavior.
2. Make the smallest code change that turns the test green.
3. Refactor only after the test is green.
4. Record the command or method used for verification.

If a behavior change cannot be tested first, record why in the task contract and add the smallest useful verification path before marking the task complete.

## Required Test Evidence

Every implementation task must record:

- test or check name
- command or method
- result
- date
- relevant artifact or task contract
- residual risk if a check cannot run

Every release review must record:

- required checks for the release bar
- checks that passed
- checks that failed
- checks deferred
- owner and trigger for each deferral

## Variant Test Plan

Each variant profile must define:

- release bar
- critical user or operator workflows
- required test layers
- commands or methods for each layer
- manual checks, if any
- deferrals and accepted risk
- what must pass before release

If the variant stack has no chosen framework yet, the profile records required layers and leaves framework selection open.

## Policy Checks

The generic harness will include a local docs governance check command. Product variants should add their own stack-specific check commands only after the stack is chosen.

Until then, the required generic checks are:

- Markdown links resolve.
- Markdown is ASCII unless explicitly justified.
- Governed prompts are listed in `docs/prompts/README.md`.
- Templates include `Prompt Trace`.
- Planning and design artifacts include `Prompt Trace`.
- Important files and directories are represented in `docs/FILE-INDEX.md` and `docs/FILE-MAP.md`.

## Review Questions

- Does the variant name its critical workflows?
- Does the test set match the release bar?
- Is reduced end-to-end coverage justified, reviewed, and time-bounded?
- Are sensitive or irreversible workflows covered at the right layer?
- Are failed or skipped checks visible?
- Can another engineer or agent rerun the evidence?

## Open Decisions

- The first product variant has not been chosen.
- Product-specific test frameworks are not chosen.
- The local docs governance command is not implemented yet.
- CI provider is not chosen.

## Scope Check

This strategy defines stack-neutral testing expectations. It does not choose product-specific frameworks, test runners, CI provider, or deployment checks.

## Language/Readability Check

The document uses standard software engineering terms. End-to-end coverage means workflow-level verification through the real product surface for the variant.

## Recommended Next Step

Create the security review path for Slice 1.3.
