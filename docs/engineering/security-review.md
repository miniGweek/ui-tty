# Security Review Path

## Prompt Trace

- Prompt: PRM-005-artifact-elicitation.md
- Inputs: docs/outcomes/O-001-production-delivery-harness.md, docs/plans/P-001-production-delivery-harness.md, docs/engineering/production-readiness.md, docs/engineering/test-strategy.md, user decision that Level 1 security review is release-blocking for public-user variants
- Output: docs/engineering/security-review.md
- Date: 2026-05-23
- Operator: Codex

## Source

- Outcome brief: docs/outcomes/O-001-production-delivery-harness.md
- Delivery plan: docs/plans/P-001-production-delivery-harness.md
- Production readiness standard: docs/engineering/production-readiness.md
- Test strategy: docs/engineering/test-strategy.md
- Slice: 1.3 Security review path

## Reader and Action

Reader: an engineer, agent, or reviewer deciding what security evidence a variant needs before release.

After reading this document, the reader should be able to classify the required review level, identify threat model triggers, and record security evidence for a variant.

## Security Review Levels

| Level | Name | Required When | Release Impact |
| --- | --- | --- | --- |
| Level 1 | Security review | Every public-user variant. | Release-blocking until complete. |
| Level 2 | Threat model | Any trigger in this document is present. | Release-blocking until complete or explicitly accepted by the reviewer. |

Private beta and internal-tool variants must still record whether Level 1 or Level 2 is required. They may defer parts of the review only when the variant profile documents the limit, reason, owner, and revisit trigger.

## Level 1: Security Review

Level 1 is a short release-blocking review for every public-user variant.

It must answer:

- What users or operators can access the variant?
- What data does the variant read, write, store, transmit, or display?
- What external inputs exist?
- What outputs can affect users, files, systems, or decisions?
- Does the variant use authentication, authorization, sessions, secrets, files, network access, model calls, tool use, or production writes?
- What could a malicious or mistaken user do?
- What is the rollback or stopping point if security behavior is wrong?
- Does any Level 2 trigger apply?

Level 1 evidence may be short, but it must be explicit. A public-user variant cannot release with unknown security scope.

## Level 2: Threat Model Triggers

Level 2 is required when a variant touches any of these areas:

| Trigger | Examples |
| --- | --- |
| Authentication or sessions | Login, tokens, cookies, identity providers, session storage. |
| Authorization or permissions | Roles, access control, admin functions, shared resources. |
| Sensitive data | Personal data, customer data, secrets, credentials, private files. |
| External input | User text, uploaded files, URLs, webhooks, imported documents, untrusted data. |
| Network-facing API | Public API, internal API exposed beyond a single local process, webhook receiver. |
| File system access | Reading, writing, deleting, moving, or generating files. |
| Tool execution | Shell commands, browser actions, API calls, plugins, MCP tools, deployment tools. |
| Model-assisted output used in decisions | Model output affects user-visible behavior, data changes, review decisions, or execution. |
| Production writes | Database writes, remote service changes, infrastructure changes, user-impacting writes. |
| Irreversible or hard-to-reverse actions | Deletes, migrations, sends, purchases, approvals, access changes. |
| Payments or billing | Pricing, checkout, invoices, metering, account limits. |
| Secrets or credentials | API keys, tokens, certificates, passwords, signing material. |
| Multi-user state | Shared projects, collaboration, tenancy, user-generated content. |
| Admin or operator functions | Moderation, support tools, elevated commands, impersonation, audit changes. |

If unsure whether a trigger applies, treat it as applying until reviewed.

## Threat Model Shape

A Level 2 threat model must include:

- scope and non-scope
- assets to protect
- users, operators, and trust boundaries
- data flow or workflow summary
- permissions and authority model
- key threats
- mitigations
- residual risks
- required tests or checks
- logging and audit expectations
- rollback or containment plan
- reviewer decision

Use STRIDE or another mainstream security review structure when it helps. Do not force a formal framework when a direct threat list is clearer.

## Required Evidence

| Review Level | Evidence Required |
| --- | --- |
| Level 1 | Security scope, data handled, external input, authority involved, Level 2 trigger decision, reviewer decision. |
| Level 2 | Threat model, mitigations, required tests, residual risks, reviewer decision, accepted deferrals. |

Security evidence must be linked from the variant profile or production readiness checklist.

## Release Blocking Rules

- Public-user variants cannot release without completed Level 1 review.
- Variants with Level 2 triggers cannot release without a completed threat model or explicit reviewer acceptance.
- Security review cannot be replaced by passing tests.
- Security deferrals must state owner, risk, allowed release bar, and revisit trigger.
- Unknown security scope blocks release.

## Deferrals

Security deferrals are allowed only when the release bar and risk allow them.

Deferrals are not allowed for:

- unknown authentication or authorization behavior
- unknown sensitive data handling
- missing rollback for irreversible actions
- unreviewed secrets handling
- unreviewed production writes for public-user variants
- unreviewed tool execution for public-user variants

## Variant Profile Requirements

Each variant profile must record:

- release bar
- whether Level 1 review is required
- whether Level 2 threat model is required
- triggers present or explicitly absent
- security evidence location
- accepted deferrals
- reviewer or owner

## Review Questions

- Is the release bar public users, private beta, or internal tool?
- Is Level 1 complete when required?
- Are all Level 2 triggers checked?
- Is data handling clear?
- Are permissions and authority boundaries clear?
- Are external inputs treated as untrusted?
- Are model calls or tool use prevented from becoming unchecked authority?
- Are secrets and credentials protected?
- Are rollback and containment paths documented?
- Are residual risks visible to a reviewer?

## Open Decisions

- The first product variant has not been chosen.
- Security reviewer ownership is not assigned.
- Security evidence file naming is not yet standardized beyond the generic docs structure.
- Product-specific threat model depth is not chosen.

## Scope Check

This document defines the generic security review path only. It does not create a full compliance program, choose security tooling, or define product-specific controls.

## Language/Readability Check

The document uses standard software engineering and security review terms. Level 1 and Level 2 are local labels for review depth and are defined in this document.

## Recommended Next Step

Create the release, rollback, and operations baseline for Slice 1.4.
