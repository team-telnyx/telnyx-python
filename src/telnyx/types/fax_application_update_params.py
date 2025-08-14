# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .anchorsite_override import AnchorsiteOverride

__all__ = ["FaxApplicationUpdateParams", "Inbound", "Outbound"]


class FaxApplicationUpdateParams(TypedDict, total=False):
    application_name: Required[str]
    """A user-assigned name to help manage the application."""

    webhook_event_url: Required[str]
    """The URL where webhooks related to this connection will be sent.

    Must include a scheme, such as 'https'.
    """

    active: bool
    """Specifies whether the connection can be used."""

    anchorsite_override: AnchorsiteOverride
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    fax_email_recipient: Optional[str]
    """
    Specifies an email address where faxes sent to this application will be
    forwarded to (as pdf or tiff attachments)
    """

    inbound: Inbound

    outbound: Outbound

    tags: List[str]
    """Tags associated with the Fax Application."""

    webhook_event_failover_url: Optional[str]
    """
    The failover URL where webhooks related to this connection will be sent if
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int]
    """Specifies how many seconds to wait before timing out a webhook."""


class Inbound(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the number of concurrent inbound calls to phone
    numbers associated with this connection.
    """

    sip_subdomain: str
    """
    Specifies a subdomain that can be used to receive Inbound calls to a Connection,
    in the same way a phone number is used, from a SIP endpoint. Example: the
    subdomain "example.sip.telnyx.com" can be called from any SIP endpoint by using
    the SIP URI "sip:@example.sip.telnyx.com" where the user part can be any
    alphanumeric value. Please note TLS encrypted calls are not allowed for
    subdomain calls.
    """

    sip_subdomain_receive_settings: Literal["only_my_connections", "from_anyone"]
    """
    This option can be enabled to receive calls from: "Anyone" (any SIP endpoint in
    the public Internet) or "Only my connections" (any connection assigned to the
    same Telnyx user).
    """


class Outbound(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the number of concurrent outbound calls to phone
    numbers associated with this connection.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""
