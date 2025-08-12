# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SipHeaderParam"]


class SipHeaderParam(TypedDict, total=False):
    name: Required[Literal["User-to-User"]]
    """The name of the header to add."""

    value: Required[str]
    """The value of the header."""
