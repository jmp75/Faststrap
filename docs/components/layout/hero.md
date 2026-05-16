# Hero Section

The `Hero` component (often called a Jumbotron) is a large, prominent section typically found at the top of landing pages to showcase the primary value proposition of a site.

!!! tip "Bootstrap Reference"
    Hero sections are usually custom implementations of Containers and Spacing. FastStrap provides a dedicated component to standardize this common pattern.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="px-4 py-5 my-5 text-center bg-light rounded w-100">
      <h1 class="display-5 fw-bold">Build Faster with FastStrap</h1>
      <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">The definitive Bootstrap component library for FastHTML.</p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <button type="button" class="btn btn-primary btn-lg px-4 gap-3">Get Started</button>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Hero(
    title="Build Faster with FastStrap",
    subtitle="The definitive Bootstrap component library for FastHTML.",
    cta=Button("Get Started", size="lg", variant="primary"),
    bg_variant="light",
    align="center",
)
```
  </div>
</div>

<div class="result" markdown>
![Screenshot: Large centered hero section with title and button](../../assets/images/hero-basic.png)
</div>

---

## Visual Examples & Use Cases

### 1. Dark Mode Hero
Use `bg_variant="dark"` for a premium, high-contrast look. FastStrap will add `text-white` automatically for dark hero backgrounds unless you pass `text_color`.

!!! note "Code & Output"
    ```python
<div class="component-preview">
  <div class="preview-header">Live Preview (Dark)</div>
  <div class="preview-render p-0 overflow-hidden">
    <div class="px-4 py-5 text-start bg-dark text-white w-100">
      <h1 class="display-5 fw-bold">Modern Python Development</h1>
      <p class="lead mb-0">Zero JS, Infinite Possibilities.</p>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Hero(
    title="Modern Python Development",
    subtitle="Zero JS, Infinite Possibilities.",
    bg_variant="dark",
    align="start",
)
```
  </div>
</div>
    ```

### 2. Branded Backgrounds
Use `bg_color` for custom brand colors, or pass normal HTML attributes such as `style` through `**kwargs` when you need a richer background treatment.

```python
Hero(
    title="Adventure Awaits",
    subtitle="Design a landing-page hero without leaving Python.",
    bg_color="#0f172a",
    text_color="text-white",
    cta=Button("Start Exploring", variant="light"),
)
```

---

## Practical Functionality

### 1. Customizing Children
The `cta` argument can accept any FastHTML element or component.

```python
Hero(
    ...,
    cta=Div(
        Button("Download", variant="primary"),
        Button("View Source", variant="link"),
        cls="d-flex gap-2 justify-content-center"
    )
)
```

---

## Parameter Reference

| FastStrap Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | Main large heading (H1). |
| `subtitle` | `str \| None` | Secondary text or description. |
| `cta` | `Any` | Call to action area, usually a button or button group. |
| `align` | `str` | Alignment: `start`, `center`, `end`. |
| `bg_variant` | `str \| None` | Bootstrap background utility suffix, such as `primary`, `light`, or `dark`. |
| `bg_color` | `str \| None` | Custom background color. Hex values are applied as inline background color. |
| `text_color` | `str \| None` | Text color class, such as `text-white` or `text-dark`. |
| `py` | `str` | Vertical padding scale used for `py-{value}`. Default `5`. |
| `container` | `bool` | If `True`, wraps content in a `.container`. Default `True`. |
| `**kwargs` | `Any` | Additional HTML attributes, including `id`, `cls`, `style`, and HTMX attributes. |

::: faststrap.components.layout.hero.Hero
    options:
        show_source: true
        heading_level: 4
