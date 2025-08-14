# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CallControlApplicationOutbound"]


class CallControlApplicationOutbound(BaseModel):
    channel_limit: Optional[int] = None
    """
    When set, this will limit the total number of outbound calls to phone numbers
    associated with this connection.
    """

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""
