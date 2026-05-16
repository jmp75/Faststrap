# Sheet

`Sheet` is a mobile-first bottom panel component built on top of `Drawer`.
It defaults to bottom placement and rounded top corners.

## Quick Start

```python
from faststrap import Button, Sheet

Button(
    "Open actions",
    data_bs_toggle="offcanvas",
    data_bs_target="#mobileActions",
)

Sheet(
    "Quick actions go here",
    sheet_id="mobileActions",
    title="Actions",
)
```

## Notes

- `Sheet` wraps `Drawer` with `placement="bottom"`.
- Pass `height` to control panel height (for example `"50%"`, `"70vh"`).
- Other `Drawer` kwargs such as `backdrop` and `scroll` are supported.
- Requires Bootstrap JavaScript because it uses the offcanvas behavior from `Drawer`.
- Trigger it with `data_bs_toggle="offcanvas"` and `data_bs_target="#yourSheetId"`.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `*children` | `Any` | Required | Sheet content |
| `sheet_id` | `str \| None` | `None` | ID used by trigger target |
| `title` | `str \| None` | `None` | Optional header title |
| `height` | `str` | `"auto"` | CSS height for the sheet |
| `**kwargs` | `Any` | - | Forwarded to `Drawer` |

## Example With Form Controls

```python
Sheet(
    Input("email", label="Invite by email"),
    Button("Send invite", variant="primary"),
    sheet_id="inviteSheet",
    title="Invite teammate",
    height="60vh",
)
```

::: faststrap.components.display.sheet.Sheet
    options:
        show_source: true
        heading_level: 4
