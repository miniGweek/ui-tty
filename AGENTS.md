# AGENTS.md

## Communication

- Write status updates, summaries, errors, questions, and plans in plain English.
- Put the result before the mechanism.
- Prefer short sentences.
- Avoid jargon unless the user has already introduced it.

## Human-Facing Documents

- Write documents for the human reader first.
- Use clear mainstream software engineering vocabulary.
- Use agentic AI engineering vocabulary only when it makes the text more precise.
- Avoid esoteric words, domain-foreign metaphors, and overloaded terms.
- Reduce cognitive load. Prefer concrete nouns, active verbs, and direct structure.
- Match prose to existing identifiers. If a field is named `sourceTask`, call it "source task" in prose.

## Code Changes

- Practice red-green-refactor TDD when writing code.
- Start with a failing test that describes the expected behavior.
- Make the smallest code change that turns the test green.
- Refactor only after the test is green.
- Keep tests close to the behavior they protect.

## Operating Loop

- Discover before changing files.
- Plan only as much as needed for the size of the change.
- Write or update tests before implementation when behavior changes.
- Make the smallest useful change.
- Verify with commands, screenshots, or logs.
- Summarize what changed, what was verified, and what risk remains.

## Progressive Discovery

- Read local instructions first.
- Inspect existing files, tests, scripts, and docs before asking questions.
- Ask the user only when the answer cannot be found in the repo or the choice changes product intent.
- Prefer narrow searches before broad searches.
- State assumptions before acting on them.
- Update assumptions when new evidence changes them.

## Harness Engineering

- Prefer repeatable commands over manual steps.
- Add or use scripts for common checks when the repo grows.
- Keep test, lint, build, and run commands discoverable from the repo.
- Do not rely on hidden local state.
- Capture failing commands and outputs when debugging.
- Make verification easy for the next agent or engineer to rerun.

## Completion Standard

- Do not call work complete without fresh verification.
- Record the exact command or method used to verify the change.
- If verification cannot run, state why and describe the remaining risk.
- Do not hide failed checks. Report the failure and the next useful action.

## Change Discipline

- Keep changes scoped to the task.
- Do not refactor unrelated code while implementing a feature.
- Preserve user changes already present in the working tree.
- Prefer simple designs until the outcome requires more structure.
- Add abstractions only when they remove repeated complexity or protect a clear boundary.

## File Index and File Map

- Keep `docs/FILE-INDEX.md` as the inventory of important files and directories.
- Keep `docs/FILE-MAP.md` as the guide for where each kind of work belongs.
- When adding, moving, renaming, or deleting files, update both documents in the same change.
- If a change does not need an index or map update, say why in the final summary.
- Keep entries short. Prefer purpose and ownership over implementation detail.

## Prompt Governance

- For planning and design work, read `docs/prompts/README.md` before drafting artifacts.
- Use `PRM-000-standing-guardrails.md` with the active stage prompt.
- Use `PRM-005-artifact-elicitation.md` when the user asks for a plan, design, spec, task, or review artifact and the target artifact is unclear.
- Start at the lowest applicable stage and do not skip stages unless source artifacts already exist.
- Record prompt use in the generated artifact under `Prompt Trace`.
- If no governed prompt was used for a planning or design artifact, record `Prompt: none` and explain why.

## Commits

- Use Conventional Commits for commit messages.
- Format: `<type>(optional-scope): <summary>`.
- Use common types such as `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, and `build`.
- Keep summaries imperative and concise.
