# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SqldbCreateParams"]


class SqldbCreateParams(TypedDict, total=False):
    name: Required[str]
    """Database name.

    Lowercase letters, numbers, and hyphens only; must start and end with a letter
    or number.
    """
