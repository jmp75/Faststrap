# Grid System

Bootstrap's grid system uses a series of containers, rows, and columns to layout and align content. It's built with flexbox and is fully responsive. FastStrap mirrors this with `Container`, `Row`, and `Col`.

!!! tip "Bootstrap Reference"
    [Bootstrap 5 Grid System Documentation](https://getbootstrap.com/docs/5.3/layout/grid/)

---

## Quick Start

The grid follows a 12-column system.

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="container text-center border p-3">
      <div class="row g-2">
        <div class="col-4 border bg-light py-3">Left (4/12)</div>
        <div class="col-4 border bg-light py-3">Center (4/12)</div>
        <div class="col-4 border bg-light py-3">Right (4/12)</div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
Container(
    Row(
        Col("Left Column", width=4),
        Col("Center Column", width=4),
        Col("Right Column", width=4)
    )
)
```
  </div>
</div>

<div class="result" markdown>
![Screenshot: A three-column layout with equal widths](../../assets/images/grid-basic.png)
</div>

---

## Recommended Pattern

Prefer `Row(..., cols=...)` when you want evenly sized cards or repeated items,
and define the mobile layout first.

```python
Row(
    Card("Revenue"),
    Card("Retention"),
    Card("Pipeline"),
    cols=1,
    cols_md=2,
    cols_lg=3,
    gutter=3,
)
```

This makes the intended stack explicit:

- mobile: 1 item per row
- tablet: 2 items per row
- desktop: 3 items per row

Use custom `cls="row ..."` only when you specifically need raw Bootstrap row
behavior that is not already covered by `Row()` arguments.

---

## Visual Examples & Use Cases

### 1. Responsive Breakpoints
You can specify different widths for different screen sizes (`sm`, `md`, `lg`, `xl`, `xxl`).

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Responsive)</div>
  <div class="preview-render">
    <div class="row w-100 g-2 text-center">
      <div class="col-12 col-md-6 col-lg-4 border bg-light py-3">Item 1</div>
      <div class="col-12 col-md-6 col-lg-4 border bg-light py-3">Item 2</div>
      <div class="col-12 col-md-12 col-lg-4 border bg-light py-3">Item 3</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# 1 column on mobile, 2 on tablet, 3 on desktop
Row(
    Col("Item 1", width=12, md=6, lg=4),
    Col("Item 2", width=12, md=6, lg=4),
    Col("Item 3", width=12, md=12, lg=4)
)
```
  </div>
</div>

You can also control equal-width card grids at the row level:

```python
Row(
    Card("Item 1"),
    Card("Item 2"),
    Card("Item 3"),
    cols=1,
    cols_md=2,
    cols_lg=3,
)
```

### 2. Alignment & Spacing (Gutter)
Bootstrap's Flexbox utilities are available through the `Row` and `Col` arguments.

!!! note "Code & Output"
<div class="component-preview">
  <div class="preview-header">Live Preview (Centered)</div>
  <div class="preview-render">
    <div class="row justify-content-center w-100 g-4 text-center">
      <div class="col-6 border bg-info-subtle py-3">I am centered</div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
# Centered Row with gap (gutter) level 4
Row(
    Col("I am centered", width=6),
    justify="center",
    gutter=4
)
```
  </div>
</div>

### 3. Container Fluid
By default, `Container` has a fixed width that changes at each breakpoint. Use `fluid=True` for a container that is always 100% wide.

```python
Container("Full width content", fluid=True)
```

---

## Practical Functionality

### 1. Auto-width Columns
If you don't specify a width, `Col` will automatically share the space with other sibling columns.

```python
Row(
    Col("Variable width"),
    Col("Variable width"),
    Col("Variable width")
)
```

### 2. Offsetting Columns
Move columns to the right using `offset`.

```python
Row(
    Col("Centered offset", width=6, offset=3)
)
```

---

## Parameter Reference

### Container
| Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `fluid` | `bool` | `.container-fluid` | Spans the full width of the viewport. |

### Row
| Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `cols` | `int` | `.row-cols-{val}` | Equal columns for the default/mobile layout. |
| `cols_sm` | `int` | `.row-cols-sm-{val}` | Equal columns from the `sm` breakpoint upward. |
| `cols_md` | `int` | `.row-cols-md-{val}` | Equal columns from the `md` breakpoint upward. |
| `cols_lg` | `int` | `.row-cols-lg-{val}` | Equal columns from the `lg` breakpoint upward. |
| `cols_xl` | `int` | `.row-cols-xl-{val}` | Equal columns from the `xl` breakpoint upward. |
| `cols_xxl` | `int` | `.row-cols-xxl-{val}` | Equal columns from the `xxl` breakpoint upward. |
| `gutter` | `int` | `.g-{val}` | Spacing between columns (0-5). |
| `gx` | `int` | `.gx-{val}` | Horizontal gutter only. |
| `gy` | `int` | `.gy-{val}` | Vertical gutter only. |
| `justify` | `str` | `.justify-content-{val}` | Alignment: `start`, `center`, `end`, `around`, `between`. |
| `align` | `str` | `.align-items-{val}` | Vertical alignment: `start`, `center`, `end`. |

### Col
| Param | Type | Bootstrap Class | Description |
| :--- | :--- | :--- | :--- |
| `span` | `int \| bool` | `.col` / `.col-{val}` | Auto width when `True`, or a specific mobile/default span (1-12). |
| `sm` | `int` | `.col-sm-{val}` | Width from the `sm` breakpoint upward. |
| `md` | `int` | `.col-md-{val}` | Width from the `md` breakpoint upward. |
| `lg` | `int` | `.col-lg-{val}` | Width from the `lg` breakpoint upward. |
| `xl` | `int` | `.col-xl-{val}` | Width from the `xl` breakpoint upward. |
| `xxl` | `int` | `.col-xxl-{val}` | Width from the `xxl` breakpoint upward. |
| `offset` | `int` | `.offset-{val}` | Prepend empty columns. |
| `offset_sm` | `int` | `.offset-sm-{val}` | Offset from the `sm` breakpoint upward. |
| `offset_md` | `int` | `.offset-md-{val}` | Offset from the `md` breakpoint upward. |
| `offset_lg` | `int` | `.offset-lg-{val}` | Offset from the `lg` breakpoint upward. |
| `offset_xl` | `int` | `.offset-xl-{val}` | Offset from the `xl` breakpoint upward. |
| `offset_xxl` | `int` | `.offset-xxl-{val}` | Offset from the `xxl` breakpoint upward. |

::: faststrap.components.layout.grid.Container
    options:
        heading_level: 4

::: faststrap.components.layout.grid.Row
    options:
        heading_level: 4

::: faststrap.components.layout.grid.Col
    options:
        heading_level: 4
