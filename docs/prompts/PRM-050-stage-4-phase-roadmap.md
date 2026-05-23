Proceed to Stage 4 only.

Create a phased delivery roadmap with two explicit levels. Do not collapse them.

Levels:
- Phase - a coarse delivery milestone. A phase groups related slices that ship
  together and reach one reviewable milestone.
- Slice - a unit of work inside a phase with exactly ONE primary decision. Each
  slice maps to exactly one Stage 5 detailed design ("one detailed design per
  slice"). A slice is feature-sized.

Number slices as phase.slice (e.g. 2.3). Avoid numbering that collides with any
stage or component names used by the system being designed.

For each PHASE include:
- phase name
- phase goal (the milestone it reaches)
- the observable value the phase delivers
- the slices it contains

For each SLICE include:
- slice name
- goal
- scope
- explicit exclusions
- what ships
- acceptance tests
- risks
- what must be true before starting
- rollback or stopping point
- whether it needs human review

Rules:
- Each slice must be independently reviewable and produce observable value.
- Each slice must have exactly one primary decision. If it has more than one,
  split it.
- Do not combine unrelated concerns into one slice.
- Each slice must have a small, testable outcome.
- Order slices so deterministic controls exist before any model-assisted or
  autonomous behaviour depends on them.
- A single-slice phase is a smell: you have probably mislabeled a slice as a
  phase. Re-level.

Also propose artifact names (one detailed-design name per slice).

Do not write any detailed designs yet.

Before finishing, run a leveling check and state the result:
- Phases are milestones; slices are single-decision units.
- Rough scale: ~2-5 phases, each with ~2-6 slices. More than ~8 phases means you
  are labeling slices as phases.

At the end include:
- Scope check
- Language/readability check
- Leveling check (confirm phase vs slice; flag any single-slice phase or any
  slice with more than one primary decision)
- Recommended first slice
- Why that slice should come first
