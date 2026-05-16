# Markdown

Render markdown content into safe HTML with optional sanitization.

## Installation

```bash
pip install "faststrap[markdown]"
```

## Usage

```python
from faststrap import Markdown

Markdown(
    "# Hello\n\nThis is **safe** markdown.",
    cls="prose",
)
```

## Behavior

- Uses Python `markdown` for conversion.
- Sanitizes output with `bleach` by default.
- Raises a clear `ImportError` if optional dependencies are missing.

## Advanced Control

```python
Markdown(
    text,
    sanitize=True,
    extensions=["extra", "tables", "fenced_code"],
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | required | Markdown source text. |
| `sanitize` | `bool` | `True` | Sanitize rendered HTML with `bleach`. |
| `extensions` | `list[str] \| None` | `None` | Markdown extensions. Defaults to `extra`, `sane_lists`, `tables`, and `fenced_code`. |
| `allowed_tags` | `list[str] \| None` | `None` | Override allowed HTML tags for sanitization. |
| `allowed_attributes` | `dict[str, list[str]] \| None` | `None` | Override allowed attributes for sanitization. |
| `allowed_protocols` | `list[str] \| None` | `None` | Override allowed link protocols. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

## Security Notes

If you disable sanitization, only render trusted content.

## API Reference

::: faststrap.components.display.markdown.render_markdown

::: faststrap.components.display.markdown.Markdown
    options:
        show_source: true
        heading_level: 4
