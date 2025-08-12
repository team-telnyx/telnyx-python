# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallControlApplicationOutboundParam"]


class CallControlApplicationOutboundParam(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the total number of outbound calls to phone numbers
    associated with this connection.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""
