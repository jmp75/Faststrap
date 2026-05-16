# Pricing

`PricingTier` and `PricingGroup` create common SaaS pricing sections with responsive cards.

## Quick Start

```python
from faststrap import PricingGroup, PricingTier

PricingGroup(
    PricingTier("Starter", 19, features=["3 projects", "Email support"]),
    PricingTier(
        "Pro",
        49,
        features=["Unlimited projects", "Priority support"],
        highlighted=True,
    ),
    title="Choose your plan",
    subtitle="Start small and scale when you need more.",
)
```

## Parameters

### `PricingTier`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `str` | required | Tier name. |
| `price` | `str \| int` | required | Price display value. |
| `period` | `str` | `"month"` | Billing period label. |
| `features` | `list[str] \| None` | `None` | Feature bullet list. |
| `button_text` | `str` | `"Get Started"` | CTA button text. |
| `button_href` | `str` | `"#"` | CTA link. |
| `highlighted` | `bool` | `False` | Adds stronger border/shadow and solid CTA. |
| `**kwargs` | `Any` | | Extra card attributes. |

### `PricingGroup`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*tiers` | `Any` | | Pricing tier elements. |
| `title` | `str` | `"Choose Your Plan"` | Section heading. |
| `subtitle` | `str \| None` | `None` | Optional section copy. |
| `header_cls` / `title_cls` / `subtitle_cls` | `str \| None` | `None` | Header styling hooks. |
| `row_cls` / `col_cls` | `str \| None` | `None` | Layout styling hooks. |
| `header_attrs` / `title_attrs` / `subtitle_attrs` | `dict \| None` | `None` | Extra header attributes. |
| `row_attrs` / `col_attrs` | `dict \| None` | `None` | Extra grid attributes. |
| `**kwargs` | `Any` | | Extra root attributes. |

## API Reference

::: faststrap.components.patterns.pricing.PricingTier

::: faststrap.components.patterns.pricing.PricingGroup
