# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ActionDeleteParams"]


class ActionDeleteParams(TypedDict, total=False):
    ids: Required[List[str]]
    """List of call recording IDs to delete."""
