# Timeline

`Timeline` and `TimelineItem` render chronological events such as activity feeds, audit logs, booking progress, release history, and customer support notes.

Use `TimelineItem` for each event, then wrap the items in `Timeline`.

## Import

```python
from faststrap import Timeline, TimelineItem
```

## Basic Usage

```python
Timeline(
    TimelineItem(
        "Account created",
        description="Ada created the workspace.",
        time="09:15",
        icon="person-plus",
        variant="success",
    ),
    TimelineItem(
        "Invite sent",
        description="Grace was invited as an admin.",
        time="09:32",
        icon="send",
        variant="primary",
    ),
)
```

## Compact Activity Feed

```python
Timeline(
    TimelineItem("Deployment started", time="10:00", icon="rocket"),
    TimelineItem("Health checks passed", time="10:03", icon="check-circle", variant="success"),
    TimelineItem("Release completed", time="10:05", icon="flag", variant="success"),
    density="compact",
)
```

## With Custom Metadata

```python
TimelineItem(
    "Payment failed",
    description="The customer's card was declined.",
    time="Today",
    icon="credit-card",
    variant="danger",
    meta=StatusBadge("Needs attention", status="error"),
)
```

## Parameters

| Component | Param | Type | Description |
| :--- | :--- | :--- | :--- |
| `Timeline` | `*items` | `Any` | `TimelineItem` children or custom timeline rows. |
| `Timeline` | `density` | `comfortable | compact` | Controls vertical spacing. |
| `TimelineItem` | `title` | `str` | Main event title. |
| `TimelineItem` | `description` | `Any | None` | Supporting event text or content. |
| `TimelineItem` | `time` | `str | None` | Timestamp or relative time. |
| `TimelineItem` | `icon` | `str | None` | Bootstrap icon name. |
| `TimelineItem` | `variant` | `str` | Bootstrap marker variant. |
| `TimelineItem` | `meta` | `Any | None` | Optional extra content such as badges or links. |

::: faststrap.components.display.timeline.Timeline
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.display.timeline.TimelineItem
    options:
        show_source: true
        heading_level: 3
