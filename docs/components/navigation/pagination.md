# Pagination

The `Pagination` component creates Bootstrap page navigation for tables, search results, card feeds, and HTMX-powered partial updates.

## Quick Start

```python
from faststrap import Pagination

Pagination(current_page=2, total_pages=10)
```

## Common Patterns

### Compact Table Pagination

```python
Pagination(
    current_page=page,
    total_pages=total_pages,
    size="sm",
    align="end",
)
```

### First, Previous, Next, Last Controls

```python
Pagination(
    current_page=2,
    total_pages=100,
    show_first_last=True,  # adds << and >> controls
    show_prev_next=True,   # adds < and > controls
)
```

### Preserve Search And Filter Query Params

Use `query_params` when pagination links need to keep the current filter/search state.

```python
Pagination(
    current_page=page,
    total_pages=total_pages,
    base_url="/products",
    query_params={"q": query, "category": category},
    page_param="page",
)
```

### HTMX Pagination

Set `htmx=True` to render `hx-get` links while still keeping normal `href` values as a fallback.

```python
Pagination(
    current_page=page,
    total_pages=total_pages,
    base_url="/products",
    query_params={"q": query},
    htmx=True,
    hx_target="#product-list",
    hx_swap="outerHTML",
    hx_push_url=True,
)
```

A matching handler can return the updated list and pagination fragment:

```python
@app.get("/products")
def products(q: str = "", page: int = 1):
    items, total_pages = search_products(q=q, page=page)
    return Div(
        product_grid(items),
        Pagination(
            current_page=page,
            total_pages=total_pages,
            base_url="/products",
            query_params={"q": q},
            htmx=True,
            hx_target="#product-list",
            hx_swap="outerHTML",
            hx_push_url=True,
        ),
        id="product-list",
    )
```

## Responsive Pattern

```python
from faststrap import Div, Pagination


def ResponsivePagination(current: int, total: int):
    return Div(
        Pagination(
            current_page=current,
            total_pages=total,
            max_pages=7,
            show_first_last=True,
            cls="d-none d-md-flex",
        ),
        Pagination(
            current_page=current,
            total_pages=total,
            max_pages=3,
            show_first_last=False,
            size="sm",
            cls="d-md-none",
        ),
    )
```

## Defaults

```python
from faststrap import Pagination, set_component_defaults

set_component_defaults(
    "Pagination",
    align="center",
    show_first_last=True,
    max_pages=7,
)

Pagination(current_page=5, total_pages=20)
```

## Accessibility

Faststrap handles the important pagination semantics:

- `aria-label` on the outer `<nav>`
- `aria-current="page"` on the active page
- `aria-label` on first/previous/next/last controls
- disabled links for unavailable controls

Use a more specific label when the page has more than one paginator:

```python
Pagination(
    current_page=5,
    total_pages=20,
    aria_label="Product listing navigation",
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `current_page` | `int` | Required | Current active page, 1-indexed |
| `total_pages` | `int` | Required | Total number of pages |
| `size` | `"sm" | "lg" | None` | `None` | Bootstrap pagination size |
| `align` | `"start" | "center" | "end"` | `"start"` | Alignment of the pagination list |
| `max_pages` | `int | None` | `5` | Maximum numbered page links to show |
| `base_url` | `str | None` | `"#"` | Base URL used for page links |
| `page_param` | `str` | `"page"` | Query parameter name for page numbers |
| `query_params` | `dict[str, Any] | None` | `None` | Extra query params to preserve in generated links |
| `show_first_last` | `bool | None` | `False` | Show `<<` and `>>` controls |
| `show_prev_next` | `bool | None` | `True` | Show `<` and `>` controls |
| `htmx` | `bool` | `False` | Add HTMX attributes to page links |
| `hx_target` | `str | None` | `None` | Target for HTMX page updates |
| `hx_swap` | `str | None` | `"outerHTML"` | HTMX swap strategy |
| `hx_push_url` | `bool` | `False` | Push generated URLs into browser history |
| `**kwargs` | `Any` | - | Additional HTML attributes such as `cls`, `id`, or `aria_label` |

::: faststrap.components.navigation.pagination.Pagination
    options:
        show_source: true
        heading_level: 4
