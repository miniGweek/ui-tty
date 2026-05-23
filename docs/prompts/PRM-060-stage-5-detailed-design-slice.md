Proceed to Stage 5 only.

Write a detailed design for this slice only:

[SLICE ID AND NAME]

Hard rules:
- Design only this slice.
- Do not redesign the whole architecture.
- Do not include future slices or phases except in a short Deferred section.
- Do not include implementation ticket detail.
- Do not silently expand scope.
- Do not introduce new component names unless this slice needs them.
- Do not describe deterministic software using AI or agentic language.

Include:
- title
- phase and slice
- decision being made
- architecture context
- scope
- explicit non-scope
- design
- components touched
- interfaces/contracts only where needed
- validation/testing
- observability/operations
- risks/failure modes
- human approval points
- acceptance tests
- open decisions
- deferred items

For every major component, state:
- responsibility
- inputs
- outputs
- owner
- what it must not do

Keep it between 2,500 and 4,000 words unless the slice is very small.

At the end include:
- Scope creep check
- Language/readability check
- What would make this design wrong?
- Smallest reversible implementation step
- Recommended next artifact