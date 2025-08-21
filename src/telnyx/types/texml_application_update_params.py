# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .dtmf_type import DtmfType
from .anchorsite_override import AnchorsiteOverride

__all__ = ["TexmlApplicationUpdateParams", "Inbound", "Outbound"]


class TexmlApplicationUpdateParams(TypedDict, total=False):
    friendly_name: Required[str]
    """A user-assigned name to help manage the application."""

    voice_url: Required[str]
    """URL to which Telnyx will deliver your XML Translator webhooks."""

    active: bool
    """Specifies whether the connection can be used."""

    anchorsite_override: AnchorsiteOverride
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    dtmf_type: DtmfType
    """Sets the type of DTMF digits sent from Telnyx to this Connection.

    Note that DTMF digits sent to Telnyx will be accepted in all formats.
    """

    first_command_timeout: bool
    """
    Specifies whether calls to phone numbers associated with this connection should
    hangup after timing out.
    """

    first_command_timeout_secs: int
    """Specifies how many seconds to wait before timing out a dial command."""

    inbound: Inbound

    outbound: Outbound

    status_callback: str
    """
    URL for Telnyx to send requests to containing information about call progress
    events.
    """

    status_callback_method: Literal["get", "post"]
    """HTTP request method Telnyx should use when requesting the status_callback URL."""

    tags: List[str]
    """Tags associated with the Texml Application."""

    voice_fallback_url: str
    """
    URL to which Telnyx will deliver your XML Translator webhooks if we get an error
    response from your voice_url.
    """

    voice_method: Literal["get", "post"]
    """
    HTTP request method Telnyx will use to interact with your XML Translator
    webhooks. Either 'get' or 'post'.
    """


class Inbound(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the total number of inbound calls to phone numbers
    associated with this connection.
    """

    shaken_stir_enabled: bool
    """
    When enabled Telnyx will include Shaken/Stir data in the Webhook for new inbound
    calls.
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
    When set, this will limit the total number of outbound calls to phone numbers
    associated with this connection.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""
