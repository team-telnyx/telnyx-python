# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .anchorsite_override import AnchorsiteOverride

__all__ = ["ConnectionRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the specific resource."""

    active: Optional[bool] = None
    """Defaults to true"""

    anchorsite_override: Optional[AnchorsiteOverride] = None
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    connection_name: Optional[str] = None

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    tags: Optional[List[str]] = None
    """Tags associated with the connection."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    webhook_api_version: Optional[Literal["1", "2"]] = None
    """Determines which webhook format will be used, Telnyx API v1 or v2."""

    webhook_event_failover_url: Optional[str] = None
    """
    The failover URL where webhooks related to this connection will be sent if
    sending to the primary URL fails.
    """

    webhook_event_url: Optional[str] = None
    """The URL where webhooks related to this connection will be sent."""


class ConnectionRetrieveResponse(BaseModel):
    data: Optional[Data] = None
