# Stepper

`Stepper` and `StepperStep` show progress through a multi-step flow such as onboarding, checkout, setup, or account verification.

`Stepper` is display-only by default. It does not manage state for you; your route or application state decides which step is current.

## Import

```python
from faststrap import Stepper, StepperStep
```

## Basic Usage

```python
Stepper(
    StepperStep("Account", status="complete"),
    StepperStep("Profile", status="current"),
    StepperStep("Billing", status="pending"),
)
```

## Numbered Steps

```python
Stepper(
    StepperStep("Account", step=1, status="complete"),
    StepperStep("Profile", step=2, status="current"),
    StepperStep("Billing", step=3),
)
```

## Vertical Stepper

```python
Stepper(
    StepperStep("Account", description="Create your workspace", status="complete"),
    StepperStep("Profile", description="Add your team details", status="current"),
    StepperStep("Billing", description="Choose a plan"),
    orientation="vertical",
)
```

## Clickable Steps

```python
Stepper(
    StepperStep("Account", status="complete", href="/setup/account"),
    StepperStep("Profile", status="current", href="/setup/profile"),
    StepperStep("Billing", href="/setup/billing"),
)
```

## Parameters

| Component | Param | Type | Description |
| :--- | :--- | :--- | :--- |
| `Stepper` | `*steps` | `Any` | `StepperStep` children or strings. |
| `Stepper` | `orientation` | `horizontal | vertical` | Layout direction. |
| `Stepper` | `numbered` | `bool` | Adds numbers when string steps are passed. |
| `StepperStep` | `title` | `str` | Step label. |
| `StepperStep` | `description` | `str | None` | Optional helper text. |
| `StepperStep` | `status` | `complete | current | pending | error` | Step state. |
| `StepperStep` | `step` | `int | str | None` | Marker content. |
| `StepperStep` | `icon` | `str | None` | Bootstrap icon override. |
| `StepperStep` | `href` | `str | None` | Optional link target. |

::: faststrap.components.display.stepper.Stepper
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.display.stepper.StepperStep
    options:
        show_source: true
        heading_level: 3
