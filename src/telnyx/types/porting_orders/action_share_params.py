# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionShareParams"]


class ActionShareParams(TypedDict, total=False):
    expires_in_seconds: int
    """The number of seconds the token will be valid for"""

    permissions: Literal["porting_order.document.read", "porting_order.document.update"]
    """The permissions the token will have"""
