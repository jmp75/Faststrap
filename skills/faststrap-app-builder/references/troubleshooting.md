# Troubleshooting

Use this guide when a Faststrap page works technically but still feels wrong, generic, or inconsistent.

---

## Problem: The UI Looks Like Generic Bootstrap

Diagnosis:

- there is no strong palette
- cards still look like untouched Bootstrap defaults
- typography hierarchy is weak
- the page has structure but no visual system

Fix:

1. define a palette before styling components
2. define hero, section, body, and label text roles
3. add a surface system for cards, panels, and shells
4. run the Bootstrap-smell audit from the skill

---

## Problem: The Layout Feels Cramped on Mobile

Diagnosis:

- desktop composition was built first
- rows were not defined mobile-first
- secondary panels stayed visible on small screens even when too dense

Fix:

1. start from `cols=1`
2. expand at `cols_md` or `cols_lg`
3. hide dense supporting content with `d-none d-lg-block` where appropriate
4. simplify card internals before adding more CSS

---

## Problem: HTMX Validation Feedback Does Not Appear

Diagnosis:

- the field has no stable target
- the endpoint returns markup that does not match the swap target
- validation exists only on blur and not on submit

Fix:

1. give the field feedback region a stable id
2. return valid or invalid feedback markup with the same target id
3. keep final server-side validation in the submit endpoint
4. follow the pattern in `form-workflow.md`

---

## Problem: Search / Filtering Works but Feels Incomplete

Diagnosis:

- the results update, but there is no loading, empty, or error state
- the filter controls are structurally present but visually disconnected

Fix:

1. group filters in `FilterBar(...)` where it fits
2. add an empty result state
3. add a placeholder or spinner while the target refreshes
4. style the filter region like a coherent control panel

---

## Problem: A Table Is Becoming Hard to Manage

Diagnosis:

- raw table markup is being used for behavior that `DataTable()` already supports
- sorting, search, and pagination are being rebuilt by hand

Fix:

1. switch to `DataTable()` if the page needs sort, search, or pagination
2. use raw `Table()` only for simple fixed tables
3. use `DataTable.export_params(...)` and `ExportButton(...)` for exports

---

## Problem: Light and Dark Modes Require Too Much Repetition

Diagnosis:

- custom CSS is styling every component ad hoc
- there is no shared token layer for surfaces, text, and borders

Fix:

1. move repeated colors into CSS custom properties
2. define separate light/dark semantic tokens
3. style cards and panels from shared tokens instead of literal values
4. follow `css-architecture.md`

---

## Problem: The App Has Too Much Inline Styling

Diagnosis:

- one-off `style=...` strings have accumulated
- the same visual decision is repeated in many places

Fix:

1. move repeated values into CSS classes
2. keep inline style use limited to true one-off showcase cases
3. create mounted CSS assets once the app has multiple routes or reusable sections

---

## Problem: The Wrong Reference Was Chosen

Diagnosis:

- a legacy/simple example was treated as the quality target
- multiple unrelated references were blended together

Fix:

1. reopen `reference-index.md`
2. choose one primary reference
3. add only one secondary reference if needed
4. prefer flagship references when the user wants premium output

---

## Problem: HTMX Attributes Are Not Working in a New Framework Component

Diagnosis:

- the component likely did not apply `convert_attrs(kwargs)`

Fix:

1. inspect the component implementation
2. ensure `convert_attrs(kwargs)` is applied before returning markup
3. if the component is part of Faststrap itself, treat it as a framework authoring issue, not an app bug

This issue matters most when building or reviewing Faststrap components, not ordinary app pages that use existing components.

---

## Problem: The Page Still Feels Flat After the First Pass

Diagnosis:

- layout is correct, but surface contrast and hierarchy are weak

Fix:

1. strengthen section contrast
2. improve title/body/label hierarchy
3. add depth with borders, shadows, or subtle glass treatment
4. refine buttons and control states
5. remove any untouched Bootstrap-default surfaces still visible

---

## Escalation Rule

If the page is functionally correct but still visually weak after one pass:

- do not add random effects
- go back to:
  - reference choice
  - palette
  - typography
  - surface strategy
  - spacing rhythm

Most "generic" Faststrap output problems come from those five areas.
