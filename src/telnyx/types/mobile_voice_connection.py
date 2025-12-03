# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MobileVoiceConnection", "Inbound", "Outbound"]


class Inbound(BaseModel):
    channel_limit: Optional[int] = None


class Outbound(BaseModel):
    channel_limit: Optional[int] = None

    outbound_voice_profile_id: Optional[str] = None


class MobileVoiceConnection(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    active: Optional[bool] = None
    """Indicates if the connection is active."""

    connection_name: Optional[str] = None
    """The name of the connection."""

    created_at: Optional[datetime] = None

    inbound: Optional[Inbound] = None

    outbound: Optional[Outbound] = None

    record_type: Optional[Literal["mobile_voice_connection"]] = None
    """Identifies the type of the resource."""

    tags: Optional[List[str]] = None
    """A list of tags associated with the connection."""

    updated_at: Optional[datetime] = None

    webhook_api_version: Optional[Literal["1", "2"]] = None
    """The API version for webhooks."""

    webhook_event_failover_url: Optional[str] = None
    """The failover URL where webhooks are sent."""

    webhook_event_url: Optional[str] = None
    """The URL where webhooks are sent."""

    webhook_timeout_secs: Optional[int] = None
    """The timeout for webhooks in seconds."""
