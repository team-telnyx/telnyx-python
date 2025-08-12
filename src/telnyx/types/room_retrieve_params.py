# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RoomRetrieveParams"]


class RoomRetrieveParams(TypedDict, total=False):
    include_sessions: bool
    """To decide if room sessions should be included in the response."""
