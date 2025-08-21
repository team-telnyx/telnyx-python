# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["GlobalIPCreateParams"]


class GlobalIPCreateParams(TypedDict, total=False):
    description: str
    """A user specified description for the address."""

    name: str
    """A user specified name for the address."""

    ports: Dict[str, object]
    """A Global IP ports grouped by protocol code."""
