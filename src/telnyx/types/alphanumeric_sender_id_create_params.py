# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AlphanumericSenderIDCreateParams"]


class AlphanumericSenderIDCreateParams(TypedDict, total=False):
    alphanumeric_sender_id: Required[str]
    """The alphanumeric sender ID string."""

    messaging_profile_id: Required[str]
    """The messaging profile to associate the sender ID with."""

    us_long_code_fallback: str
    """A US long code number to use as fallback when sending to US destinations."""
