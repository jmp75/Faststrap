# Customization & Theming

FastStrap is designed to be highly customizable. You can tweak everything from individual component colors to the entire application's theme.

!!! tip "Junior Dev Tip"
    You don't need to be a CSS expert to customize FastStrap. Most changes can be done directly in Python using built-in functions.

---

## 1. Global Component Defaults

Consistency is key. Instead of passing `variant="primary"` to every single button, you can set a global default for your entire app.

```python
from faststrap import set_component_defaults

# Set all buttons to be 'secondary' and 'outline' by default
set_component_defaults("Button", variant="secondary", outline=True)

# Now this button will be secondary outline without any arguments!
btn = Button("Click Me")
```

### Supported Components
Most complex components support `set_component_defaults`. This is great for keeping your UI consistent across many pages.

### When to apply defaults
Set component defaults once during app startup, before the first component is
rendered, close to `add_bootstrap(...)` or your shared theme setup.
`set_component_defaults()` updates process-global state, so it is best treated
as application configuration rather than something to call inside request
handlers.

```python
from faststrap import add_bootstrap, create_theme, set_component_defaults

theme = create_theme(primary="#5B6CFF", success="#10B981")

add_bootstrap(app, theme=theme)
set_component_defaults("Button", variant="primary")
set_component_defaults("Input", cls="rounded-3")
```

### Clearing a global default

If a global default is set, pass `None` on a specific component call to clear it
for that instance.

```python
set_component_defaults("Button", size="lg")

Button("Large by default")
Button("Normal size here", size=None)
```

---

## 2. Using `create_theme`

Bootstrap 5 uses a set of "Brand Colors" (Primary, Secondary, Success, etc.). You can override these globally using `create_theme`.

```python
from faststrap import add_bootstrap, create_theme

# Define your brand colors
my_brand = create_theme(
    primary="#6f42c1",   # Purple
    secondary="#e83e8c", # Pink
    success="#20c997"    # Teal
)

# Apply it to your app
add_bootstrap(app, theme=my_brand)
```

### How it works
This function generates a small CSS block that overwrites Bootstrap's internal variables. It ensures that everything using `variant="primary"` (Buttons, Alerts, Badges, etc.) will now use your custom purple color.

### Built-in themes

Faststrap includes these built-in theme names:

```python
from faststrap import list_builtin_themes

list_builtin_themes()
# ["green-nature", "blue-ocean", "purple-magic", "red-alert", ...]
```

Use one directly with `add_bootstrap()`:

```python
add_bootstrap(app, theme="green-nature", mode="auto")
```

Use `get_builtin_theme(name)` when you need the `Theme` instance itself, for example to inspect or reuse its variables.

---
    
## 3. Custom Fonts (Google Fonts)

Faststrap makes it easy to use Google Fonts in your application without writing any HTML or CSS.

```python
from faststrap import add_bootstrap, create_theme

# Built-in theme with custom font
add_bootstrap(
    app, 
    theme="green-nature",
    font_family="Inter",              # Font name from options below
    font_weights=[400, 500, 600, 700] # Font weights to load
)

# Custom theme with custom font
my_theme = create_theme(primary="#7BA05B")
add_bootstrap(
    app, 
    theme=my_theme, 
    font_family="Roboto Slab"
)
```

The font will be automatically loaded from Google Fonts (with optimizations) and applied as the default body font for your application.

---

## 4. Dark Mode Support

FastStrap supports Bootstrap's native color modes.

```python
# 1. Automatic (Matches user's system settings) - Default
add_bootstrap(app, mode="auto")

# 2. Forced Dark Mode
add_bootstrap(app, mode="dark")

# 3. Forced Light Mode
add_bootstrap(app, mode="light")
```

### Dark Mode Toggle
If you want to allow users to switch themes manually, you can use standard HTMX to update the `data-bs-theme` attribute on the `<html>` tag.

---

## 5. Per-Component CSS Variables

For one-off customizations that are too specific for a global theme, use the `css_vars` argument. This is the "Pro" way to customize without writing external CSS files.

```python
# Making a one-off "Gold" button
gold_style = {
    "--bs-btn-bg": "#ffd700",
    "--bs-btn-border-color": "#ffd700",
    "--bs-btn-color": "#000"
}

Button("Upgrade to Pro", css_vars=gold_style)
```

---

## 6. Custom CSS & Classes

If you need full control, you can always link your own CSS file and use the `cls` argument to apply your styles.

```python title="app.py"
@app.route("/")
def home():
    return Button("Special Action", cls="my-custom-glow-effect")
```

```css title="static/styles.css"
.my-custom-glow-effect {
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    transition: transform 0.2s;
}

.my-custom-glow-effect:hover {
    transform: scale(1.05);
}
```

---

## 7. Custom Components and `convert_attrs`

If you create your own wrapper component, route `**kwargs` through
`convert_attrs(kwargs)` so HTMX, `data_*`, `aria_*`, and style helpers keep
working.

```python
from fasthtml.common import Div
from faststrap import convert_attrs, merge_classes


def PromoPanel(*children, **kwargs):
    attrs = {"cls": merge_classes("promo-panel", kwargs.pop("cls", ""))}
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
```

Without `convert_attrs()`, attributes such as `hx_get="/api/promo"` would not
be converted to `hx-get`, which can make HTMX interactions fail silently.

---

## Best Practices

1.  **Start with Global Defaults**: It saves time and makes your code cleaner.
2.  **Use `create_theme` for Branding**: Change the primary color once, and it propagates everywhere.
3.  **Use CSS Variables for Tweaks**: Avoid inline `style={"color": ...}` when possible; CSS variables are more compatible with Bootstrap's state logic (hover/active/disabled).
4.  **Configure Defaults at Startup**: Treat `set_component_defaults()` as app configuration, not per-request logic.
5.  **Leverage Utilities**: Before writing custom CSS, check if a [Bootstrap Utility](https://getbootstrap.com/docs/5.3/utilities/api/) (like `p-3`, `m-2`, `shadow-sm`) can do the job.
6.  **Preserve Attribute Conversion**: When authoring custom wrappers, always pass `**kwargs` through `convert_attrs()`.
