# Structured Display

`KeyValueList`, `RecordDetail`, `CodeBlock`, and `JsonViewer` are small data/dev-app primitives for admin panels, AI tools, and internal dashboards.

## Quick Start

```python
from faststrap import CodeBlock, JsonViewer, KeyValueList, RecordDetail

KeyValueList({
    "Status": "Ready",
    "Owner": "Ops",
})

RecordDetail(
    {"ID": 42, "State": "queued"},
    title="Training Job",
    subtitle="Submitted 2 minutes ago",
)

CodeBlock("print('hello')", language="python", filename="demo.py")
JsonViewer({"accuracy": 0.94, "loss": 0.12}, title="Metrics")
```

## Parameters

| Component | Key Parameters | Notes |
| --- | --- | --- |
| `KeyValueList` | `items`, `striped`, `compact` | Accepts a dict, tuple list, or label/value mappings. |
| `RecordDetail` | `items`, `title`, `subtitle`, `actions` | Card-style detail view around `KeyValueList`. |
| `CodeBlock` | `code`, `language`, `filename`, `copy`, `wrap` | Escapes code content by default. `copy=True` shows a visual badge only. |
| `JsonViewer` | `data`, `title`, `expanded` | Pretty-prints JSON-like data using `json.dumps(..., default=str)`. |

## Notes

- `CodeBlock` does not ship a syntax highlighter in core. It emits `language-*` classes so an optional highlighter can enhance it later.
- `JsonViewer(title=...)` uses a native `<details>` element; omit `title` for an always-visible block.
- These components are core-safe: no JavaScript and no extra dependencies.

## API Reference

::: faststrap.components.display.structured.KeyValueList
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.display.structured.RecordDetail
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.display.structured.CodeBlock
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.display.structured.JsonViewer
    options:
        show_source: true
        heading_level: 4
