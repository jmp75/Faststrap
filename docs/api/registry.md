# Component Registry

Faststrap registers public components with lightweight metadata so humans, CLIs, and AI agents can discover what already exists before inventing new wrappers.

## Why It Exists

- Discover components by category or search text.
- Check whether a component requires Bootstrap JavaScript.
- Build documentation, tooling, or agent workflows from the same public component inventory.
- Keep custom components discoverable when you use the `@register` decorator.

## Quick Start

```python
from faststrap import find_components, list_components, list_component_metadata

display_components = list_components(category="display")
card_like = find_components("card")

for meta in list_component_metadata(category="feedback"):
    print(meta["name"], meta["requires_js"])
```

## Categories

The built-in registry categories are:

| Category | Typical components |
| --- | --- |
| `forms` | `Button`, `Input`, `FormGroup`, `InlineEditor` |
| `display` | `Card`, `DataTable`, `Avatar`, `MetricCard` |
| `feedback` | `Alert`, `Modal`, `Toast`, `ModernToast` |
| `navigation` | `Navbar`, `Tabs`, `CommandPalette`, `Pagination` |
| `layout` | `Container`, `Row`, `Col`, `Hero` |
| `patterns` | `FeatureGrid`, `PricingGroup`, `NavbarModern` |

## Functions

### `list_components(category=None)`

Return registered component names. Pass a category to filter the list.

```python
from faststrap import list_components

all_names = list_components()
forms = list_components(category="forms")
```

### `find_components(query, category=None)`

Search component names, categories, modules, and docstrings using a case-insensitive substring match.

```python
from faststrap import find_components

find_components("toast")
find_components("card", category="display")
```

### `get_component(name)`

Return a component callable by name, or `None` if no component is registered under that name.

```python
from faststrap import get_component

Modal = get_component("Modal")
if Modal is not None:
    modal = Modal("Body", title="Loaded dynamically")
```

### `get_components_by_pattern(pattern, category=None)`

Return component callables whose registry text matches a query. This is useful for agent/tool workflows that need to inspect and reuse existing components.

```python
from faststrap import get_components_by_pattern

for component in get_components_by_pattern("metric"):
    print(component.__name__)
```

### `list_component_metadata(category=None)`

Return metadata dictionaries for every registered component.

```python
from faststrap import list_component_metadata

metadata = list_component_metadata(category="navigation")
```

Common metadata keys:

| Key | Type | Description |
| --- | --- | --- |
| `name` | `str` | Registered component name. |
| `category` | `str \| None` | Registry category. |
| `requires_js` | `bool` | Whether Bootstrap JavaScript is needed. |
| `bootstrap_version` | `str` | Minimum Bootstrap version recorded by the component. |
| `module` | `str` | Python module where the component is defined. |
| `doc` | `str \| None` | Component docstring. |
| `func` | `Callable` | Original component function. |

## Registering Custom Components

Use `@register` when a custom component should be discoverable by tooling.

```python
from typing import Any

from fasthtml.common import Div
from faststrap import register


@register(category="display", requires_js=False)
def ProductCard(*children: Any, **kwargs: Any) -> Div:
    return Div(*children, cls="product-card", **kwargs)
```

## API Reference

::: faststrap.core.registry.register

::: faststrap.core.registry.list_components

::: faststrap.core.registry.find_components

::: faststrap.core.registry.get_component

::: faststrap.core.registry.get_components_by_pattern

::: faststrap.core.registry.list_component_metadata
