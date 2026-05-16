# Component Defaults

Component defaults let you set project-wide behavior once, then override it per component call when needed.

## Startup-Only Configuration

Call `set_component_defaults()` during application startup before requests are being handled.

```python
from fasthtml.common import FastHTML
from faststrap import Button, add_bootstrap, set_component_defaults

app = FastHTML()
add_bootstrap(app)

set_component_defaults("Button", variant="secondary", size="lg")
```

Faststrap protects this state with a lock, but defaults are still process-global. Treat them like app configuration, not per-request state.

## Override Defaults Per Call

Explicit values win over global defaults.

```python
Button("Uses project defaults")
Button("Small danger action", variant="danger", size="sm")
```

## Clearing A Default With `None`

Faststrap uses the `UNSET` sentinel internally to mean "the caller did not pass this argument." That leaves `None` free to mean "clear the default for this one call."

```python
from faststrap import Button, set_component_defaults

set_component_defaults("Button", size="lg")

Button("Large by default")
Button("Normal size here", size=None)
```

## Using `UNSET` In Wrapper Components

If you write wrapper components, default your overridable parameters to `UNSET`. That preserves Faststrap's normal default-resolution behavior.

```python
from typing import Any

from faststrap import Button, UNSET


def SaveButton(*children: Any, variant: str | None = UNSET, **kwargs: Any):
    return Button(*children, variant=variant, icon="check", **kwargs)
```

Value behavior:

| Value | Meaning |
| --- | --- |
| Parameter omitted / `UNSET` | Use the global default, then the component fallback. |
| `None` | Explicitly clear the global default for this call. |
| Any concrete value | Use this value for this call. |

## Resetting Defaults

Use `reset_component_defaults()` in tests or setup scripts when you need to return to built-in defaults.

```python
from faststrap import reset_component_defaults

reset_component_defaults("Button")
reset_component_defaults()
```

## API Reference

::: faststrap.core.theme.UNSET

::: faststrap.core.theme.set_component_defaults

::: faststrap.core.theme.get_component_defaults

::: faststrap.core.theme.reset_component_defaults

::: faststrap.core.theme.resolve_defaults
