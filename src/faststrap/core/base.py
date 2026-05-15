"""Base classes and protocols for FastStrap components."""

from abc import ABC, abstractmethod
from typing import Any, Protocol

from ..utils.attrs import convert_attrs


class Component(Protocol):
    """Protocol for FastStrap components."""

    def render(self) -> Any:
        """Render component to FastHTML object."""
        ...


class BaseComponent(Component, ABC):
    """Base class for stateful components with shared functionality.

    Note: Most Faststrap components are implemented as functions for simplicity.
    This base class is provided for:

    1. **Advanced users** who want to create stateful component classes
    2. **Future framework extensions** that may need class-based components
    3. **Third-party component libraries** built on Faststrap

    For most use cases, prefer function-based components as shown in the
    Faststrap component library (see Button, Card, Navbar, etc.).

    Examples:
        Creating a custom stateful component:

        >>> from faststrap.core.base import BaseComponent
        >>> from faststrap import Card, Button
        >>>
        >>> class StatefulCounter(BaseComponent):
        ...     def __init__(self, initial=0, **kwargs):
        ...         super().__init__(**kwargs)
        ...         self.count = initial
        ...
        ...     def render(self):
        ...         return Card(
        ...             Button(f"Count: {self.count}"),
        ...             **self.merge_attrs(cls="counter-card")
        ...         )
    """

    def __init__(self, *children: Any, **kwargs: Any):
        self.children = list(children)
        self.attrs = kwargs.copy()
        self._classes: list[str] = []

    @abstractmethod
    def render(self) -> Any:
        """Render component. Must be implemented by subclasses."""
        pass

    def add_class(self, *classes: str) -> "BaseComponent":
        """Add CSS classes fluently."""
        self._classes.extend(classes)
        return self

    def merge_attrs(self, **defaults: Any) -> dict[str, Any]:
        """Merge component attributes with defaults.

        The merged attribute set is passed through ``convert_attrs()`` so
        class-based components preserve the same HTMX, ``data_*``, ``aria_*``,
        ``style={...}``, and ``css_vars={...}`` behavior as function-based
        FastStrap components.
        """
        merged = {**defaults, **self.attrs}

        default_cls = defaults.get("cls")
        user_cls = self.attrs.get("cls")
        merged.pop("cls", None)

        attrs = convert_attrs(merged)

        all_classes = merge_classes(default_cls, user_cls, self._classes)
        if all_classes:
            attrs["cls"] = all_classes

        return attrs


def merge_classes(*class_lists: Any) -> str:
    """Merge multiple class strings or lists, removing duplicates."""
    classes: list[str] = []
    seen = set()

    def _process(item: Any) -> None:
        if not item:
            return
        if isinstance(item, (list, tuple)):
            for sub in item:
                _process(sub)
        elif isinstance(item, str):
            for cls in item.split():
                cls = cls.strip()
                if cls and cls not in seen:
                    classes.append(cls)
                    seen.add(cls)

    for item in class_lists:
        _process(item)

    return " ".join(classes)
