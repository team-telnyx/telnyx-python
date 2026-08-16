# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SqldbDeleteParams"]


class SqldbDeleteParams(TypedDict, total=False):
    force: bool
    """Delete the database even when functions still bind it.

    Their bindings stop resolving.
    """
