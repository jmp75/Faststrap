# GSAP Motion

GSAP Motion is an optional integration for richer, opinionated animation. Core Faststrap still uses `Fx` for zero-JS effects; use this integration only when a project explicitly wants GSAP.

## Install

```bash
pip install faststrap
```

The `gsap` extra is intentionally dependency-free in the Python package. GSAP itself is loaded from CDN by `add_gsap(app)` unless you pass a custom URL.

Faststrap exposes `GSAP_VERSION` and `GSAP_CDN_URL` when you need to inspect or reuse the default pinned asset. `GsapPreset` and `MotionPreset` are type aliases for the supported preset names.

## App Setup

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, add_gsap

app = FastHTML()
add_bootstrap(app)
add_gsap(app)
```

`add_gsap(app)` is idempotent, so repeated startup wiring will not add duplicate script tags.

## Component Motion

```python
from faststrap import Card, Gsap

Card(
    "Revenue is up 12%",
    header="Today",
    **Gsap.fade_up_attrs(duration=0.5, delay=0.1),
)
```

You can also use the generic helper when the preset is dynamic:

```python
Card("Pipeline refreshed", **Gsap.attrs(Gsap.pop, duration=0.35))
```

## Reveal Wrapper

```python
from faststrap import Button, Motion

Motion(
    Button("Save", variant="primary"),
    preset="pop",
)
```

`Motion` is an alias for `GsapReveal`. Use whichever name reads better in your app.

## Staggered Children

```python
from faststrap import Card, Row, Gsap

Row(
    Card("One"),
    Card("Two"),
    Card("Three"),
    **Gsap.stagger_attrs("fade-up", stagger=0.08),
)
```

## Presets

- `fade`
- `fade-up`
- `fade-down`
- `slide-left`
- `slide-right`
- `scale`
- `pop`

## Python Helpers

- `Gsap.attrs(...)`
- `Gsap.fade_attrs(...)`
- `Gsap.fade_up_attrs(...)`
- `Gsap.fade_down_attrs(...)`
- `Gsap.slide_left_attrs(...)`
- `Gsap.slide_right_attrs(...)`
- `Gsap.scale_attrs(...)`
- `Gsap.pop_attrs(...)`
- `Gsap.stagger_attrs(...)`

## Philosophy

- GSAP is never required for core Faststrap components.
- Server-rendered markup remains usable without GSAP.
- The runtime respects `prefers-reduced-motion`.
- Use GSAP for premium motion, guided flows, and showcase-level polish, not basic layout behavior.

## API Reference

::: faststrap.integrations.gsap.gsap_assets
    options:
        show_source: true
        heading_level: 3

::: faststrap.integrations.gsap.add_gsap
    options:
        show_source: true
        heading_level: 3

::: faststrap.integrations.gsap.Gsap
    options:
        show_source: true
        heading_level: 3

::: faststrap.integrations.gsap.GsapReveal
    options:
        show_source: true
        heading_level: 3
