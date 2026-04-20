# Navbar

`Navbar` is Faststrap's Bootstrap-native responsive navigation shell.

It handles:

- brand content
- automatic mobile collapse/toggler wiring
- simple navigation items through `items=[...]`
- mixed custom content when you need more than plain links

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Navbar](https://getbootstrap.com/docs/5.3/components/navbar/)

## Quick Start

```python
from faststrap import Button, Navbar, ThemeToggle

Navbar(
    brand="Faststrap",
    items=[
        ("Home", "/"),
        ("Docs", "/docs"),
        {"text": "Pricing", "href": "/pricing", "active": True},
        ThemeToggle(endpoint="/theme/toggle"),
        Button("Get Started", href="/signup", variant="primary", cls="ms-lg-3"),
    ],
    expand="lg",
    color_scheme="dark",
    bg="primary",
)
```

## Supported `items` Forms

`items=` is meant for common navbar composition and now supports:

1. Strings

```python
Navbar(brand="App", items=["Home", "Docs", "Pricing"])
```

These render as standard `nav-item` / `nav-link` pairs with `href="#"`.

2. Tuples

```python
Navbar(
    brand="App",
    items=[
        ("Home", "/"),
        ("Docs", "/docs"),
        ("Pricing", "/pricing", True),  # active item
    ],
)
```

Tuple format is:

- `(text, href)`
- `(text, href, active)`

3. Dictionaries

```python
Navbar(
    brand="App",
    items=[
        {"text": "Home", "href": "/"},
        {"text": "Docs", "href": "/docs", "active": True},
        {"text": "Pricing", "href": "/pricing", "cls": "fw-semibold"},
        {"text": "Disabled", "href": "#", "disabled": True},
    ],
)
```

Supported keys:

- `text`
- `href`
- `active`
- `disabled`
- `cls` for the link
- `item_cls` for the `nav-item` wrapper

4. Raw/custom children

If an item is already a custom element, Faststrap preserves it instead of forcing it into plain-link markup.

This lets you mix standard nav links with:

- `ThemeToggle`
- CTA buttons
- search forms
- custom dropdown wrappers

## How Grouping Works

Simple link-style items are automatically grouped into a Bootstrap `navbar-nav` wrapper.

Custom items are preserved outside that wrapper so mixed compositions still work cleanly.

That means this:

```python
Navbar(
    brand="Faststrap",
    items=[
        ("Home", "/"),
        ("Docs", "/docs"),
        Button("Start", href="/signup", variant="primary", cls="ms-lg-3"),
    ],
)
```

produces the correct Bootstrap navigation structure without making you manually build `navbar-nav`.

## When To Use Raw Composition

Use `Navbar(items=[...])` for normal navigation bars.

Drop to raw/custom composition only when you need a more unusual structure such as:

- multiple nav groups
- highly customized action rails
- custom collapse content layout
- premium marketing navbars with special wrappers

For those cases, `NavbarModern` or direct child composition is still a good option.

## Common Patterns

### Sticky Navbar

```python
Navbar(
    brand="Faststrap",
    items=[("Home", "/"), ("Docs", "/docs")],
    sticky="top",
    expand="lg",
)
```

### Light Navbar

```python
Navbar(
    brand="Faststrap",
    items=[("Home", "/"), ("Docs", "/docs")],
    color_scheme="light",
    bg="light",
)
```

### Dark Navbar

```python
Navbar(
    brand="Faststrap",
    items=[("Home", "/"), ("Docs", "/docs")],
    color_scheme="dark",
    bg="dark",
)
```

### Mixed Links + Actions

```python
Navbar(
    brand="Faststrap",
    items=[
        ("Components", "/components"),
        ("Showcase", "/showcase"),
        ThemeToggle(endpoint="/theme/toggle", cls="ms-lg-3"),
        Button("GitHub", href="https://github.com/Faststrap-org/Faststrap", cls="ms-lg-2"),
    ],
    expand="lg",
)
```

## Key Parameters

| Parameter | Purpose |
| --- | --- |
| `brand` | Brand text, logo, or custom element |
| `items` | Common navbar items and actions |
| `brand_href` | Brand link target |
| `color_scheme` | Bootstrap navbar text scheme |
| `bg` | Bootstrap background variant |
| `expand` | Collapse breakpoint |
| `sticky` | Sticky positioning |
| `fixed` | Fixed positioning |
| `container` | Container wrapper behavior |

## Notes

- `items=` is no longer a known workaround path; it is the preferred API for standard navbars.
- For highly branded/premium navbars, use `NavbarModern` or custom child composition on top of `Navbar`.

::: faststrap.components.navigation.navbar.Navbar
    options:
        show_source: false
        heading_level: 4
