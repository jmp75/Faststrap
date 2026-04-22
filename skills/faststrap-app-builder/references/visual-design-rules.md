# Visual Design Rules

Use these rules when building a Faststrap page that should feel polished, modern, and intentionally designed rather than default Bootstrap.

These are not brand rules for one single project. They are the baseline quality bar for premium Faststrap work.

---

## Typography Hierarchy

Define a hierarchy before styling individual components.

Recommended roles:

- hero title
  - `clamp(1.9rem, 4vw, 2.6rem)`
  - weight `800`
  - tight line-height
  - slight negative tracking
- section title
  - around `1.1rem` to `1.2rem`
  - weight `700`
  - tighter tracking than body text
- body copy
  - around `0.9rem` to `1rem`
  - softer color than headings
  - readable line-height
- labels and eyebrow text
  - around `0.75rem` to `0.82rem`
  - uppercase only when it supports the design
  - high tracking used sparingly

Do not let all text sit at the same visual weight.

---

## Palette Rules

Choose a small palette and use it consistently.

Recommended structure:

- 1 primary brand color
- 1 secondary supporting color
- 1 accent for success/highlight states
- semantic danger/warning colors

Good examples:

- indigo + cyan + emerald
- sage + charcoal + warm neutral
- deep navy + gold + ivory

Avoid:

- default Bootstrap blue as the whole visual identity
- too many unrelated accent colors
- highly saturated colors everywhere at once

---

## Surface Strategy

Pick one clear surface strategy and apply it consistently.

Common patterns:

- dark shell + lighter translucent cards
- light shell + elevated white cards
- editorial split backgrounds with section contrast
- product shell with layered gradients and glass accents

Surface design should answer:

- what is the page background?
- what is the default card/panel treatment?
- what border/shadow language does the page use?
- how do sections separate from one another?

Avoid mixing three unrelated surface styles on one page.

---

## Radius and Shape

Use a deliberate radius system.

Recommended pattern:

- small controls: `0.5rem`
- cards/panels: `0.75rem`
- large shells/feature surfaces: `1rem`

Avoid leaving everything at untouched Bootstrap defaults when the page is meant to feel premium.

---

## Spacing Rhythm

Use a small number of spacing steps repeatedly.

Recommended base rhythm:

- `0.5rem`
- `0.75rem`
- `1.5rem`
- `2.25rem`
- `3rem`

Apply these across:

- section padding
- card padding
- control gaps
- stacks of text and actions

Good spacing feels intentional and repeatable.

---

## Buttons and Interactive States

Primary buttons should look deliberate.

Good primary button treatment often includes:

- stronger contrast than secondary buttons
- custom shadow or gradient
- subtle hover lift or polish
- clear pressed/focus states

Secondary buttons should still belong to the same visual system.

Avoid:

- flat untouched buttons on an otherwise premium surface
- too many button variants competing for attention

---

## Responsive Rules

Design mobile first.

Recommended approach:

- start with one-column layouts
- expand at `md` and `lg` only where the content has room
- use patterns like `Row(..., cols=1, cols_md=2, cols_lg=3)`
- hide dense supporting panels on mobile if they hurt clarity

Avoid:

- forcing desktop sidecars to remain visible at every breakpoint
- relying on desktop composition to collapse automatically

---

## States

Every polished page should account for:

- empty state
- loading state
- success state
- error state

These states should look integrated with the page, not bolted on at the end.

---

## Accessibility Baseline

Premium UI still has to be usable.

Check:

- text contrast in both light and dark themes
- clear focus visibility
- semantic heading order
- labels on controls and icon-only buttons
- error/success meaning not conveyed by color alone

---

## Fast Final Audit

Before finishing, ask:

- does the page have a clear visual hierarchy?
- does it feel branded rather than generic?
- do the cards and buttons look intentionally styled?
- does the mobile layout feel designed, not merely reduced?
- do loading and empty states fit the same visual system?

If the answer is no, the page needs another pass.
