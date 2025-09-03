# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MessagingHostedNumberOrderCreateParams"]


class MessagingHostedNumberOrderCreateParams(TypedDict, total=False):
    messaging_profile_id: str
    """
    Automatically associate the number with this messaging profile ID when the order
    is complete.
    """

    phone_numbers: SequenceNotStr[str]
    """Phone numbers to be used for hosted messaging."""
