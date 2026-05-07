# FormWizard

`FormWizard` and `WizardStep` build a server-driven multi-step form flow. They are designed for HTMX partial replacement: your server decides the current step, then returns the wizard again.

Use `Stepper` when you only need progress display. Use `FormWizard` when the user is actively moving through form panels.

## Import

```python
from faststrap import FormWizard, WizardStep, Input
```

## Basic Usage

```python
FormWizard(
    WizardStep(
        "Account",
        Input("email", input_type="email", label="Email"),
    ),
    WizardStep(
        "Profile",
        Input("company", label="Company"),
    ),
    current_step=0,
    endpoint="/setup",
    hx_target="#setup-wizard",
    id="setup-wizard",
)
```

## Complete HTMX Flow

```python
from fasthtml.common import fast_app
from faststrap import FormWizard, WizardStep, Input

app, rt = fast_app()


def setup_wizard(step: int = 0):
    return FormWizard(
        WizardStep("Account", Input("email", input_type="email", label="Email")),
        WizardStep("Profile", Input("company", label="Company")),
        WizardStep("Finish", Input("plan", label="Plan")),
        current_step=step,
        endpoint="/setup",
        hx_target="#setup-wizard",
        id="setup-wizard",
    )


@rt("/")
def home():
    return setup_wizard()


@rt("/setup", methods=["POST"])
async def setup(request):
    form = await request.form()
    step = int(form.get("step", 0))
    return setup_wizard(step)
```

The wizard posts a `step` value when the user clicks Back, Next, or Finish. Your route can validate the current step before returning the next one.

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `*steps` | `Any` | `WizardStep` panels. |
| `current_step` | `int` | Zero-based active step index. |
| `endpoint` | `str | None` | Form/HTMX endpoint. |
| `method` | `get | post` | Submission method. |
| `step_name` | `str` | Submitted field name for the next step index. |
| `next_label` | `str` | Next button label. |
| `previous_label` | `str` | Previous button label. |
| `finish_label` | `str` | Final step button label. |
| `show_stepper` | `bool` | Show a progress stepper above the current panel. |
| `hx_target` | `str | None` | HTMX target for partial replacement. |

::: faststrap.components.forms.form_wizard.FormWizard
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.forms.form_wizard.WizardStep
    options:
        show_source: true
        heading_level: 3
