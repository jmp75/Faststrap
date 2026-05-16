# Carousel

Responsive slideshow component for cycling through images or content.

## Basic Usage

```python
from faststrap import Carousel, CarouselItem

Carousel(
    CarouselItem(Img(src="/img/slide1.jpg"), caption="First slide"),
    CarouselItem(Img(src="/img/slide2.jpg"), caption="Second slide"),
    CarouselItem(Img(src="/img/slide3.jpg"), caption="Third slide"),
    carousel_id="myCarousel",
)
```

## API Reference

### Carousel

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*items` | `CarouselItem` | - | Carousel items |
| `carousel_id` | `str \| None` | `None` | Unique carousel ID. Auto-generated when omitted. |
| `controls` | `bool \| None` | `UNSET` | Show previous/next controls. |
| `indicators` | `bool \| None` | `UNSET` | Show slide indicators. |
| `interval` | `int \| None` | `UNSET` | Auto-play interval in milliseconds. |
| `keyboard` | `bool \| None` | `UNSET` | Enable keyboard navigation. |
| `pause` | `bool \| str \| None` | `UNSET` | Pause behavior, such as `"hover"` or `False`. |
| `ride` | `bool \| str \| None` | `UNSET` | Auto-start behavior, such as `"carousel"` or `False`. |
| `wrap` | `bool \| None` | `UNSET` | Loop from last slide to first. |
| `fade` | `bool \| None` | `UNSET` | Use fade transition. |
| `dark` | `bool \| None` | `UNSET` | Use dark carousel controls/indicators. |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### CarouselItem

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*content` | `Any` | - | Slide content |
| `caption` | `str \| None` | `None` | Slide caption. |
| `caption_title` | `str \| None` | `None` | Caption title. |
| `active` | `bool` | `False` | Set as active slide. |
| `interval` | `int \| None` | `None` | Per-slide interval override. |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Examples

### Auto-playing Carousel

```python
Carousel(
    CarouselItem(Img(src="/img/1.jpg"), active=True),
    CarouselItem(Img(src="/img/2.jpg")),
    CarouselItem(Img(src="/img/3.jpg")),
    carousel_id="autoCarousel",
    interval=3000  # 3 seconds
)
```

### Fade Transition

```python
Carousel(
    CarouselItem(Img(src="/img/1.jpg"), active=True),
    CarouselItem(Img(src="/img/2.jpg")),
    carousel_id="fadeCarousel",
    fade=True
)
```

### With Captions

```python
Carousel(
    CarouselItem(
        Img(src="/products/laptop.jpg"),
        caption="Premium Laptop - $999",
        active=True
    ),
    CarouselItem(
        Img(src="/products/phone.jpg"),
        caption="Smartphone - $699"
    ),
    carousel_id="productCarousel",
)
```

## Notes

- The first item should usually pass `active=True`.
- This component requires Bootstrap JavaScript.
- If you render multiple carousels with the same content and no explicit `carousel_id`, Faststrap adds a suffix to avoid duplicate IDs in the same Python process.

## Accessibility

- Uses proper ARIA attributes
- Keyboard navigation supported
- Screen reader announcements for slide changes

## See Also

- [Image](image.md) - For single images
- [Card](card.md) - For content cards

## API Reference

::: faststrap.components.display.carousel.Carousel

::: faststrap.components.display.carousel.CarouselItem
