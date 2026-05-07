# OnboardFlow Workspace

`showcase/onboardflow_workspace.py` is a v1 onboarding/workflow reference that demonstrates Faststrap's new guided-flow and validation surfaces.

## Highlights

- `FormWizard` and `WizardStep` for server-driven onboarding
- `Stepper` and `StepperStep` for setup progress
- `LiveValidationField` and `ValidationMessage` for HTMX-friendly validation
- `CalendarDatePicker` for single-date workflow inputs
- `InlineEditor` for in-place editing
- `ConfirmAction` for reset/destructive flows
- `AvatarGroup`, `StatusBadge`, `ResultCard`, and `Timeline` for workflow context
- Optional GSAP motion via `add_gsap()` and `Gsap` helpers

## Run Locally

```bash
python showcase/onboardflow_workspace.py
```

The app serves on port `5029`.
