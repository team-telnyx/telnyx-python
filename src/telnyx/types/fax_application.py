# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .anchorsite_override import AnchorsiteOverride

__all__ = ["FaxApplication", "Inbound", "Outbound"]


class Inbound(BaseModel):
    channel_limit: Optional[int] = None
    """
    When set, this will limit the number of concurrent inbound calls to phone
    numbers associated with this connection.
    """

    sip_subdomain: Optional[str] = None
    """
    Specifies a subdomain that can be used to receive Inbound calls to a Connection,
    in the same way a phone number is used, from a SIP endpoint. Example: the
    subdomain "example.sip.telnyx.com" can be called from any SIP endpoint by using
    the SIP URI "sip:@example.sip.telnyx.com" where the user part can be any
    alphanumeric value. Please note TLS encrypted calls are not allowed for
    subdomain calls.
    """

    sip_subdomain_receive_settings: Optional[Literal["only_my_connections", "from_anyone"]] = None
    """
    This option can be enabled to receive calls from: "Anyone" (any SIP endpoint in
    the public Internet) or "Only my connections" (any connection assigned to the
    same Telnyx user).
    """


class Outbound(BaseModel):
    channel_limit: Optional[int] = None
    """
    When set, this will limit the number of concurrent outbound calls to phone
    numbers associated with this connection.
    """

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""


class FaxApplication(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the resource."""

    active: Optional[bool] = None
    """Specifies whether the connection can be used."""

    anchorsite_override: Optional[AnchorsiteOverride] = None
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    application_name: Optional[str] = None
    """A user-assigned name to help manage the application."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    inbound: Optional[Inbound] = None

    outbound: Optional[Outbound] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    tags: Optional[List[str]] = None
    """Tags associated with the Fax Application."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

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
