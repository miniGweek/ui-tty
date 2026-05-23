# Docs Governance Checks

## Prompt Trace

- Prompt: PRM-050-stage-4-phase-roadmap.md and PRM-060-stage-5-detailed-design-slice.md
- Inputs: docs/plans/P-001-production-delivery-harness.md, AGENTS.md, docs/FILE-INDEX.md, docs/FILE-MAP.md, user request for docs-lint.sh
- Output: docs/engineering/docs-governance-checks.md, scripts/docs-lint.sh, scripts/docs_lint.py, tests/test_docs_lint.py, tests/test_docs_lint_policy.py
- Date: 2026-05-24
- Operator: Codex

## Purpose

`scripts/docs-lint.sh` is the local command for repository documentation governance. It checks the docs rules that should be true before a planning or design change is committed.

The command is intentionally local and stack-neutral. Future CI should call this command instead of reimplementing the checks.

## Command

Run from the repository root:

```sh
scripts/docs-lint.sh
```

The command exits `0` when the repo passes. It exits non-zero and prints every issue when a check fails.

## Checks

The command checks:

- Markdown files use ASCII text unless a future exception mechanism is added.
- Local Markdown links point to files that exist.
- Markdown file paths written in inline code resolve unless they are placeholders or plan references.
- `docs/prompts/README.md` lists every `PRM-*.md` prompt file.
- Prompt files listed in `docs/prompts/README.md` exist.
- Governed templates include `## Prompt Trace`.
- Governed docs outside directory `README.md` files include `## Prompt Trace`.
- Important paths are listed in both `docs/FILE-INDEX.md` and `docs/FILE-MAP.md`.
- Human-facing Markdown avoids banned wording patterns.

## Banned Wording Patterns

These patterns are blocked because they increase ambiguity, add jargon, or preserve common spelling errors:

- `out-of-distribution` <!-- docs-lint: allow banned wording -->
- `left-shifted` <!-- docs-lint: allow banned wording -->
- `context bleed` <!-- docs-lint: allow banned wording -->
- `folklore` <!-- docs-lint: allow banned wording -->
- `smuggled` <!-- docs-lint: allow banned wording -->
- `busywork` <!-- docs-lint: allow banned wording -->
- `we just` <!-- docs-lint: allow banned wording -->
- `backstop` <!-- docs-lint: allow banned wording -->
- `moat` <!-- docs-lint: allow banned wording -->
- `table stakes` <!-- docs-lint: allow banned wording -->
- `happy to` <!-- docs-lint: allow banned wording -->
- `AI-for-AI` <!-- docs-lint: allow banned wording -->
- `BigArchPrompt` <!-- docs-lint: allow banned wording -->
- `congnitive` <!-- docs-lint: allow banned wording -->
- `architecutre` <!-- docs-lint: allow banned wording -->
- `convenitonal` <!-- docs-lint: allow banned wording -->

## When To Run

Run `scripts/docs-lint.sh` after any change to:

- `AGENTS.md`
- `docs/`
- `scripts/`
- `tests/`
- repository governance files

Agents must run it before the final summary when those paths change. Agents must also run it before committing those changes.

This does not guarantee execution after every file write. The practical control is to enforce it at reviewable boundaries: before summary, before commit, and later in CI. A future pre-commit hook can call the same command if the team wants local Git enforcement.

## Extension Rule

Add tests in `tests/` before adding or changing checks in `scripts/docs_lint.py`. Keep the shell wrapper small and put policy logic in Python.
