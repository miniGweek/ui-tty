# File Index

This file is the repository inventory. Update it when important files or directories are added, moved, renamed, or deleted.

## Root

| Path | Purpose |
| --- | --- |
| `.gitignore` | Local generated files that Git should ignore. |
| `AGENTS.md` | Working rules for agents and engineers in this repository. |
| `README.md` | Repository entry point and delivery flow summary. |
| `docs/` | Source of truth for planning, design, execution, and verification docs. |

## Docs

| Path | Purpose |
| --- | --- |
| `docs/README.md` | Docs entry point. |
| `docs/delivery-workflow.md` | Lean delivery workflow and gates. |
| `docs/FILE-INDEX.md` | Inventory of important files and directories. |
| `docs/FILE-MAP.md` | Guide for where different kinds of work belong. |
| `docs/outcomes/` | Outcome briefs. |
| `docs/outcomes/O-001-production-delivery-harness.md` | Outcome brief for the generic production delivery harness. |
| `docs/plans/` | Delivery plans. |
| `docs/plans/P-001-production-delivery-harness.md` | Delivery plan for the generic production delivery harness. |
| `docs/architecture/` | Architecture overviews and ADRs. |
| `docs/design/` | Implementation design docs. |
| `docs/specs/` | Behavior specs. |
| `docs/tasks/` | Task contracts. |
| `docs/verification/` | Verification records. |
| `docs/templates/` | Templates for delivery artifacts. |
| `docs/templates/production-readiness-checklist.md` | Template for release readiness evidence and review decisions. |
| `docs/templates/variant-profile.md` | Template for declaring variant assumptions, inherited controls, overrides, and required checks. |
| `docs/prompts/` | Governed prompts for planning and design work. |
| `docs/engineering/` | Production delivery harness standards and operating docs. |
| `docs/engineering/production-readiness.md` | Generic production readiness standard for future variants. |
| `docs/engineering/test-strategy.md` | Stack-neutral test strategy for future variants. |
| `docs/engineering/security-review.md` | Security review path and threat model triggers for future variants. |
| `docs/engineering/release-and-rollback.md` | Stack-neutral release evidence and rollback expectations for future variants. |
| `docs/engineering/observability-and-runbooks.md` | Stack-neutral observability and runbook expectations for future variants. |
| `docs/engineering/docs-governance-checks.md` | Local docs governance checks and enforcement timing. |
| `docs/prompts/README.md` | Prompt order, usage rules, artifact mapping, and prompt trace requirements. |
| `docs/prompts/PRM-005-artifact-elicitation.md` | Interactive prompt for choosing and drafting the right governed artifact. |

## Scripts and Tests

| Path | Purpose |
| --- | --- |
| `scripts/` | Local automation scripts. |
| `scripts/docs-lint.sh` | Shell entrypoint for docs governance checks. |
| `scripts/docs_lint.py` | Python implementation of docs governance checks. |
| `tests/` | Local test suite. |
| `tests/test_docs_lint.py` | Baseline tests for the docs linter. |
| `tests/test_docs_lint_policy.py` | Policy behavior tests for the docs linter. |

## Maintenance

- Add entries for files that future agents or engineers need to find quickly.
- Do not list every generated file, cache, or dependency directory.
- Keep descriptions short and stable.
