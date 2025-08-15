# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExternalConnection", "Inbound", "Outbound"]


class Inbound(BaseModel):
    channel_limit: Optional[int] = None
    """
    When set, this will limit the number of concurrent inbound calls to phone
    numbers associated with this connection.
    """


class Outbound(BaseModel):
    channel_limit: Optional[int] = None
    """
    When set, this will limit the number of concurrent outbound calls to phone
    numbers associated with this connection.
    """

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""


class ExternalConnection(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the resource."""

    active: Optional[bool] = None
    """Specifies whether the connection can be used."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    credential_active: Optional[bool] = None
    """If the credential associated with this service is active."""

    external_sip_connection: Optional[Literal["zoom", "operator_connect"]] = None
    """The service that will be consuming this connection."""

    inbound: Optional[Inbound] = None

    outbound: Optional[Outbound] = None

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
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: Optional[str] = None
    """The URL where webhooks related to this connection will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int] = None
    """Specifies how many seconds to wait before timing out a webhook."""
