# CommandPalette

`CommandPalette` and `CommandItem` provide a server-rendered command/search surface. It works as a normal search form first, then becomes more dynamic when you add HTMX endpoints.

This component intentionally avoids forcing a global keyboard shortcut or client-side command router. You can add those later as progressive enhancement.

## Import

```python
from faststrap import CommandPalette, CommandItem
```

## Basic Usage

```python
CommandPalette(
    CommandItem("Dashboard", href="/dashboard", icon="speedometer2"),
    CommandItem("Settings", href="/settings", icon="gear"),
    CommandItem("Invite team", href="/team/invite", icon="person-plus"),
)
```

## With Descriptions And Shortcuts

```python
CommandPalette(
    CommandItem(
        "Open settings",
        href="/settings",
        description="Manage workspace preferences",
        icon="gear",
        shortcut="Ctrl+,",
    ),
    CommandItem(
        "Create project",
        href="/projects/new",
        description="Start a new workspace project",
        icon="plus-circle",
        shortcut="N",
    ),
)
```

## HTMX Search

```python
CommandPalette(
    endpoint="/commands",
    hx_target="#global-command-results",
    id="global-command",
)
```

Your `/commands` route should return `CommandItem(...)` results or a small empty state.

## Parameters

| Component | Param | Type | Description |
| :--- | :--- | :--- | :--- |
| `CommandPalette` | `*commands` | `Any` | Initial command results. |
| `CommandPalette` | `name` | `str` | Search input name. |
| `CommandPalette` | `placeholder` | `str` | Search input placeholder. |
| `CommandPalette` | `endpoint` | `str | None` | Optional HTMX search endpoint. |
| `CommandPalette` | `method` | `get | post` | Search method. |
| `CommandPalette` | `empty` | `Any | None` | Fallback content when no commands are supplied. |
| `CommandItem` | `label` | `str` | Command label. |
| `CommandItem` | `href` | `str | None` | Optional navigation URL. |
| `CommandItem` | `description` | `str | None` | Supporting text. |
| `CommandItem` | `icon` | `str | None` | Bootstrap icon name. |
| `CommandItem` | `shortcut` | `str | None` | Shortcut hint. |

::: faststrap.components.navigation.command_palette.CommandPalette
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.navigation.command_palette.CommandItem
    options:
        show_source: true
        heading_level: 3
