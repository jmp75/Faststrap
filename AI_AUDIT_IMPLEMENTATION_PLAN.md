# AI Audit Implementation Plan

This plan consolidates the actionable findings from the recent external Faststrap evaluations produced with Kilo Code and Gemini.

The goal is to fix the highest-value framework, showcase, and skill issues **before** adding new component surface area.

---

## Purpose

Faststrap is already capable, but the audits surfaced three real categories of follow-up work:

1. framework ergonomics that still leak too much Bootstrap/FastHTML structure
2. showcase quality and consistency issues that affect perception
3. skill gaps that can still let AI builders fall back to generic Bootstrap output

This plan intentionally addresses those first so future component additions land on a stronger base.

---

## Scope

This plan covers:

- framework ergonomics and API consistency
- theme/design-system refinements
- showcase cleanup and positioning
- skill hardening for AI-assisted builds
- docs and validation changes needed to support the above

This plan does **not** include:

- support for alternative CSS frameworks
- replacing Bootstrap as the core design contract
- large new component additions beyond what is needed to resolve the audits

Those remain out of scope for this phase.

---

## Audit Findings We Agree Are Actionable

### Framework

- `Navbar(items=...)` ergonomics are still brittle and can force builders back into raw structure.
- Component APIs are not yet consistent enough around:
  - root `cls`
  - slot classes
  - child attribute escape hatches
- Faststrap still relies too heavily on repeated showcase-level CSS for:
  - radius
  - shadow
  - surface treatment
- Some premium design patterns are not encoded strongly enough in reusable framework primitives.

### Showcase

- Older showcases should not remain the flagship visual reference.
- Premium-quality output is now possible, but the reference layer is still uneven.
- Bootstrap visual leakage still shows most clearly in:
  - tables
  - alerts
  - plain buttons
  - basic cards

### Skill

- The skill is strong, but it should better enforce:
  - typography scale
  - spacing rhythm
  - form density
  - accessibility expectations
  - empty/loading/error state quality
  - stronger anti-default-Bootstrap checks
- AI builders need stronger rules for when inline `Style(...)` is acceptable and when CSS should move into assets.

---

## Findings We Are Explicitly Not Treating As Core Problems

- “Faststrap should support other CSS frameworks.”
- “Using Bootstrap utilities for layout is an abstraction leak by itself.”
- “Delete all older showcases.”
- “Deprecate `BaseComponent`” as an immediate priority.

These are either off-target, overstated, or lower-priority than the items above.

---

## Implementation Phases

## Phase 0 - Triage and Guardrails

**Goal:** Lock the scope and avoid drifting into unrelated redesign work.

### Tasks

1. Mark the accepted audit findings as the current stabilization focus.
2. Explicitly reject non-goals in roadmap/docs where needed.
3. Freeze major new component work until this plan is substantially complete.

### Exit Criteria

- This plan is accepted as the working sequence.
- New component additions remain deferred until framework/showcase/skill fixes are complete enough.

---

## Phase 1 - Navbar and Core Ergonomics

**Goal:** Fix the highest-friction framework issues first.

### Workstream 1A - `Navbar` repair

1. Audit current `Navbar(items=...)` output.
2. Normalize the generated Bootstrap structure so common nav usage works without manual fallback composition.
3. Add regression tests for:
   - basic link items
   - active items
   - right-aligned or CTA items
   - dropdown-containing navbars if supported
4. Update docs and skill references once the bug is fixed.

### Workstream 1B - Component API consistency

1. Audit composite components for consistency around:
   - root `cls`
   - `*_cls` slots
   - child attrs
   - slot injection
2. Define a preferred consistency contract.
3. Prioritize the most commonly used components first:
   - `Navbar`
   - `Card`
   - `Feature`
   - `PricingGroup`
   - `TestimonialSection`
   - dashboard-oriented composed surfaces
4. Add child-attribute escape hatches only where they materially reduce reimplementation pressure.

### Exit Criteria

- `Navbar(items=...)` is no longer a known skill-documented workaround.
- A documented consistency pattern exists for component customization.
- The highest-traffic composed components support cleaner extension.

---

## Phase 2 - Theme and Design-System Hardening

**Goal:** Reduce repeated bespoke CSS in showcases by improving the shared design contract.

### Workstream 2A - Theme tokens

1. Add theme-level support for:
   - border radius tiers
   - shadow tiers
   - surface/background roles
   - muted text roles where useful
2. Ensure tokens work cleanly in both light and dark modes.
3. Document how theme tokens should replace one-off repeated visual overrides where appropriate.

### Workstream 2B - Premium default guidance

1. Identify where core surfaces still look too default-Bootstrap when unstyled:
   - tables
   - alerts
   - cards
   - buttons
2. Improve tasteful defaults only where they do not fight the Bootstrap-native contract.
3. Avoid over-stylizing core components globally.

### Exit Criteria

- Showcases need fewer repeated custom overrides for surface polish.
- Theme-aware design language becomes easier to express at the framework level.

---

## Phase 3 - Showcase Stabilization

**Goal:** Make the public reference layer visually trustworthy and structurally intentional.

### Workstream 3A - Reference classification

1. Formally separate:
   - flagship showcases
   - legacy showcases
   - learning examples
2. Stop presenting older weaker showcases as the premium standard.

### Workstream 3B - Visual cleanup

1. Audit tables, alerts, buttons, and cards across flagship showcases for Bootstrap leakage.
2. Fix inconsistent typography, spacing, and surface treatment.
3. Ensure mobile responsiveness is validated across all flagship files.

### Workstream 3C - Accessibility and interaction pass

1. Verify labels, headings, landmarks, and keyboard interactions in the flagship set.
2. Audit loading, empty, and error states across the flagship set.
3. Ensure theme toggles and nav interactions remain coherent in light and dark modes.

### Workstream 3D - Screenshot-ready docs integration

1. Keep the showcase docs aligned with the actual flagship set.
2. Add screenshots after visual QA is complete.

### Exit Criteria

- The showcase layer has a clear flagship set.
- Legacy references are demoted, not deleted.
- Flagship examples are visually and structurally consistent enough to serve as skill references.

---

## Phase 4 - Skill Hardening

**Goal:** Reduce AI failure modes and make premium output more enforceable.

### Workstream 4A - Design rules

Add explicit rules for:

1. typography scale
2. spacing rhythm
3. form density and section spacing
4. empty/loading/error states
5. accessibility expectations
6. responsive breakpoints and mobile-first structure

### Workstream 4B - Bootstrap smell prevention

Add a final-check checklist covering:

1. excessive border radius
2. pill-shaped nav/controls where not intended
3. default Bootstrap shadows
4. insufficient custom surface treatment
5. lack of motion/polish where appropriate
6. missing theme-awareness

### Workstream 4C - CSS organization rules

Clarify:

1. when inline `Style(...)` is acceptable
2. when CSS must move into asset files
3. showcase vs production-app expectations

### Workstream 4D - Temporary framework caveats

Until all framework fixes land, keep temporary skill guidance for:

1. components with known ergonomics gaps
2. legacy showcase files that should not be used as primary references

### Exit Criteria

- The skill becomes harder to misuse.
- AI builders have fewer routes back to generic Bootstrap-looking output.

---

## Phase 5 - Documentation and Positioning Cleanup

**Goal:** Make docs and repo messaging reflect the improved reality.

### Tasks

1. Update docs pages to reflect fixed framework ergonomics.
2. Keep showcase docs aligned with the current flagship set.
3. Add or update a concise “minimal good example” reference.
4. Ensure README and docs do not oversell incomplete areas.

### Exit Criteria

- README, roadmap, docs, and showcase references all tell the same story.

---

## Phase 6 - Validation and Re-Audit

**Goal:** Verify that the audit issues are materially resolved before starting new component expansion.

### Tasks

1. Run framework validation:
   - `black`
   - `ruff`
   - `mypy`
   - `pytest`
2. Run docs build validation.
3. Re-run a practical AI generation test using the skill.
4. Compare output against the original complaints:
   - Navbar ergonomics
   - Bootstrap leakage
   - skill enforceability
   - showcase quality

### Exit Criteria

- Core fixes are validated.
- A repeat external-style audit would score materially better.

---

## Priority Order

This is the safest execution order:

1. `Navbar` fix
2. component API consistency audit
3. theme/design token hardening
4. flagship showcase cleanup and legacy demotion
5. skill hardening
6. docs/README/positioning cleanup
7. re-audit and validation
8. only then start the next component expansion wave

---

## Deferred Until After This Plan

The following remain good ideas, but should wait until the audit findings above are addressed:

- `Stack`
- `Cluster`
- `Center`
- `Switcher`
- `Sidebar`
- `SearchBar`
- `ProfileDropdown`
- `Timeline`
- `Stepper`
- `FormWizard`
- `SplitPane`
- `MegaMenu`
- `CommandPalette`
- `ModernToast`
- `ChartJS`

---

## Success Definition

We should treat this plan as successful if, after completion:

1. Faststrap’s core ergonomics are less brittle.
2. The showcase layer more consistently proves premium output.
3. The skill more reliably pushes AI builders toward good Faststrap results.
4. We can begin new component additions from a more stable, credible foundation.
