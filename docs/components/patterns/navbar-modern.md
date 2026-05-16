# NavbarModern

`NavbarModern` is a branded navigation pattern that wraps the core `Navbar` with sticky and glass styling defaults.

## Quick Start

```python
from faststrap import NavbarModern

NavbarModern(
    brand="Faststrap",
    items=[
        ("Docs", "/docs"),
        ("Showcase", "/showcase"),
        ("GitHub", "https://github.com/Faststrap-org/Faststrap"),
    ],
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `brand` | `Any` | required | Brand content passed to `Navbar`. |
| `items` | `list[Any] \| None` | `None` | Navigation items passed to `Navbar`. |
| `sticky` | `bool` | `True` | Adds `sticky-top`. |
| `glass` | `bool` | `True` | Adds the `navbar-glass` class. |
| `**kwargs` | `Any` | | Extra attributes passed to `Navbar`. |

## Notes

- This component requires Bootstrap JavaScript because it delegates to `Navbar`.
- Use the lower-level `Navbar` when you need complete control over Bootstrap behavior.
- Use `cls` to add brand-specific styling while keeping the default pattern classes.

## API Reference

::: faststrap.components.patterns.navbar.NavbarModern
