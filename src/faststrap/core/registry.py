"""Component registry for FastStrap."""

from __future__ import annotations

import importlib
import pkgutil
import threading
import warnings
from collections.abc import Callable
from typing import Any, TypeVar

# Global registry for component metadata
_component_registry: dict[str, dict[str, Any]] = {}
_autodiscovered = False
_autodiscover_lock = threading.Lock()

F = TypeVar("F", bound=Callable[..., Any])


def register(
    name: str | None = None,
    category: str | None = None,
    bootstrap_version: str = "5.3.3",
    requires_js: bool = False,
) -> Callable[[F], F]:
    """Decorator to register component metadata.
    Args:
        name: Component name (defaults to function name)
        category: Component category (layout, display, etc.)
        bootstrap_version: Min Bootstrap version required
        requires_js: Whether component needs Bootstrap JS
    Example:
        >>> @register(category="feedback", requires_js=True)
        >>> def Modal(...): ...
    """

    def decorator(func: F) -> F:
        component_name = name or func.__name__

        _component_registry[component_name] = {
            "func": func,
            "category": category,
            "bootstrap_version": bootstrap_version,
            "requires_js": requires_js,
            "module": func.__module__,
            "doc": func.__doc__,
        }

        # Mark function as registered (Ruff B010 requires 'noqa', MyPy requires 'type: ignore')
        # fmt: off
        setattr(func, "__faststrap_registered__", True)  # noqa: B010 # type: ignore[attr-defined]
        setattr(func, "__faststrap_metadata__", _component_registry[component_name])  # noqa: B010 # type: ignore[attr-defined]
        # fmt: on

        return func

    return decorator


def get_registry() -> dict[str, dict[str, Any]]:
    """Get copy of component registry."""
    ensure_autodiscovered()
    return _component_registry.copy()


def get_component(name: str) -> Callable[..., Any] | None:
    """Get component function by name."""
    ensure_autodiscovered()
    return _component_registry.get(name, {}).get("func")


def list_components(category: str | None = None) -> list[str]:
    """List all registered components, optionally filtered by category.
    Args:
        category: Filter by category (layout, display, feedback, etc.)
    Returns:
        List of component names
    Example:
        >>> list_components(category="feedback")
        ['Alert', 'Toast', 'Modal', 'Spinner']
    """
    ensure_autodiscovered()

    if category is None:
        return list(_component_registry.keys())

    return [name for name, meta in _component_registry.items() if meta.get("category") == category]


def list_component_metadata(category: str | None = None) -> list[dict[str, Any]]:
    """List registered component metadata records.

    Args:
        category: Optional category filter.

    Returns:
        Metadata dictionaries with a stable ``name`` key added.
    """
    ensure_autodiscovered()
    records = []
    for name, meta in _component_registry.items():
        if category is not None and meta.get("category") != category:
            continue
        records.append({"name": name, **meta})
    return records


def find_components(
    query: str,
    *,
    category: str | None = None,
) -> list[str]:
    """Find components by name, category, module, or docstring text."""
    ensure_autodiscovered()
    normalized = query.casefold().strip()
    if not normalized:
        return list_components(category=category)

    matches = []
    for name, meta in _component_registry.items():
        if category is not None and meta.get("category") != category:
            continue
        haystack = " ".join(
            [
                name,
                str(meta.get("category") or ""),
                str(meta.get("module") or ""),
                str(meta.get("doc") or ""),
            ]
        ).casefold()
        if normalized in haystack:
            matches.append(name)
    return matches


def get_components_by_pattern(
    pattern: str, *, category: str | None = None
) -> list[Callable[..., Any]]:
    """Return component callables matching a pattern.

    This is a convenience API for agents and app builders that need to discover
    existing components before inventing new UI.
    """
    return [
        component
        for name in find_components(pattern, category=category)
        if (component := get_component(name)) is not None
    ]


def autodiscover() -> None:
    """Auto-discover and register all components."""
    try:
        from faststrap import components

        # Recursively import all component modules
        for module_info in pkgutil.walk_packages(
            components.__path__, prefix="faststrap.components."
        ):
            try:
                # Safely access module name attribute
                module_name = getattr(module_info, "name", None)
                if module_name:
                    importlib.import_module(module_name)
                else:
                    warnings.warn(
                        f"Module info missing 'name' attribute: {module_info}",
                        ImportWarning,
                        stacklevel=2,
                    )
            except ImportError as e:
                # Get module name safely for error message
                module_name = getattr(module_info, "name", "unknown")
                warnings.warn(
                    f"Could not import {module_name}: {e}",
                    ImportWarning,
                    stacklevel=2,
                )

    except ImportError:
        pass  # Components not yet installed


def ensure_autodiscovered() -> None:
    """Run component autodiscovery only once, on first registry access."""
    global _autodiscovered
    if _autodiscovered:
        return
    with _autodiscover_lock:
        if _autodiscovered:
            return
        autodiscover()
        _autodiscovered = True
