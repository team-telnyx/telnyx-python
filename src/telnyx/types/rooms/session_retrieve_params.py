# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionRetrieveParams"]


class SessionRetrieveParams(TypedDict, total=False):
    include_participants: bool
    """To decide if room participants should be included in the response."""
