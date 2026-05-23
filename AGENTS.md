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

## Commits

- Use Conventional Commits for commit messages.
- Format: `<type>(optional-scope): <summary>`.
- Use common types such as `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, and `build`.
- Keep summaries imperative and concise.
