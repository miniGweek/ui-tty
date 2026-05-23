Proceed to Stage 6 only.

Review the detailed design on three lenses: scope placement, readability/terminology,
and consistency with upstream artifacts.

Scope and readability - review the design for:
- bloat
- misplaced content
- unclear terminology
- non-mainstream language
- invented terms
- duplicated rationale
- future-phase leakage
- implementation-ticket leakage
- appendix/example leakage

Classify every major section (each top-level section) as one of:
- necessary for this phase
- belongs in architecture overview
- belongs in future phase
- belongs in implementation ticket
- belongs in appendix/example
- duplicate rationale
- should be removed
- needs clearer language
- uses non-mainstream or invented terminology

Terminology - for each important (load-bearing) term, classify it as:
- mainstream and clear
- mainstream but needs definition
- overloaded or inconsistently used
- invented but justified
- invented and should be replaced
- too vague or metaphorical

Consistency with upstream - answer yes/no with a one-line reason, and flag any "no":
- Does the design stay inside the slice scope defined in the phase roadmap?
- Does it honour the architecture invariants and the authority/approval model?
- Does it avoid silently expanding scope (every expansion declared, not assumed)?
This lens checks fit, not full correctness. A "no" is a blocking issue.

Closers check - confirm the design's required closers are present and substantive
(not hand-waved), especially:
- "what would make this design wrong?"
- "smallest reversible implementation step"
A missing or empty required closer is a blocking issue.

Tests - assess coverage against this rubric and list anything missing:
- happy path
- negative / error / human-review path
- boundary or invariant test (the design's own invariants and "must not" rules)

Return:
- blocking issues
- non-blocking issues
- suggested cuts
- suggested splits
- terminology issues
- unclear component names
- suggested plain-language replacements
- missing tests
- review readiness: ready / revise / split

Verdict definitions:
- ready - no blocking issues; any non-blocking items are optional. Proceed.
- revise - no structural problem, but blocking issues or required fixes exist; fold
  them in, then proceed. No re-review needed unless asked.
- split - the design carries more than one primary decision, or two unrelated
  concerns; split it into separate slice designs before proceeding.

Blocking vs non-blocking:
- blocking - a consistency "no"; a missing or empty required closer; a missing
  happy-path or invariant test; an invented-and-should-be-replaced term; or any
  issue that would mislead an implementer. Must be resolved before proceeding.
- non-blocking - bloat, duplication, trims, plain-language polish, or a missing
  secondary test. Improves the design but does not gate it.

Do not rewrite the whole design unless I ask.
