# SEO API Reference

This section provides API-level reference for FastStrap SEO helpers. For guided examples and schema recipes, see the [SEO guide](../seo/index.md).

## URL vs Canonical

`SEO(url=...)` emits the Open Graph URL (`og:url`) for social cards. `SEO(canonical=...)` emits the search-engine canonical link (`<link rel="canonical">`). They are often the same absolute URL, but they are separate outputs and should both be set when you need both tags.

## SEO Meta Tags

::: faststrap.seo.meta.SEO
    options:
        show_root_heading: true
        show_source: true

## PageMeta Composer

::: faststrap.seo.page_meta.PageMeta
    options:
        show_root_heading: true
        show_source: true

## Structured Data

::: faststrap.seo.structured_data.StructuredData
    options:
        show_root_heading: true
        show_source: true
