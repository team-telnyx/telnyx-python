# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NumberBlockOrderCreateParams"]


class NumberBlockOrderCreateParams(TypedDict, total=False):
    range: Required[int]
    """The phone number range included in the block."""

    starting_number: Required[str]
    """Starting phone number block"""

    connection_id: str
    """Identifies the connection associated with this phone number."""

    customer_reference: str
    """A customer reference string for customer look ups."""

    messaging_profile_id: str
    """Identifies the messaging profile associated with the phone number."""
