# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    about: str

    address: str

    category: str

    description: str

    display_name: str

    email: str

    profile_id: str
    """Messaging profile ID for inbound messages"""

    website: str
