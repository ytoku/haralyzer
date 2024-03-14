"""Provides compatibility layer"""

from typing import TYPE_CHECKING

# Since functools.cached_property is supported in python >= 3.8,
# we use cached_property package alternatively.
# However pyright does not handle it correctly, we make a type checker
# treat cached_property.cached_property as functools.cached_property.

if TYPE_CHECKING:
    from functools import cached_property
else:
    from cached_property import cached_property


__all__ = [
    "cached_property",
]
