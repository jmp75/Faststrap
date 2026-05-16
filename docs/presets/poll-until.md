# PollUntil

`PollUntil` is a zero-JavaScript HTMX helper for background jobs, ML training runs, imports, exports, and any task that should refresh until the server says it is done.

## Quick Start

```python
from faststrap.presets import PollUntil

PollUntil(
    endpoint="/jobs/42/status",
    interval=1500,
    content="Checking job status...",
)
```

## How It Stops

`PollUntil` does not parse response bodies on the client. The safe HTMX pattern is:

```python
@app.get("/jobs/42/status")
def job_status():
    if job.done:
        return ResultCard("Export complete", status="success")

    return PollUntil(
        endpoint="/jobs/42/status",
        interval=1500,
        content="Still working...",
    )
```

Because the default swap is `outerHTML` when `target="this"`, polling stops once the server returns final markup without polling attributes.

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | required | URL to poll with `hx-get`. |
| `target` | `str` | `"this"` | HTMX target. Use `"this"` for self-replacing polling blocks. |
| `interval` | `int` | `2000` | Polling interval in milliseconds. |
| `content` | `Any | None` | `None` | Initial placeholder content. |
| `**kwargs` | `Any` | `{}` | Additional HTML/HTMX/data/ARIA attributes. |

## Notes

- This is especially useful for long-running queues and ML jobs.
- Override `hx_swap` when polling should update another target instead of replacing itself.
