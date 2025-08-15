# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .dtmf_type import DtmfType
from .anchorsite_override import AnchorsiteOverride

__all__ = ["TexmlApplication", "Inbound", "Outbound"]


class Inbound(BaseModel):
    channel_limit: Optional[int] = None
    """
    When set, this will limit the total number of inbound calls to phone numbers
    associated with this connection.
    """

    shaken_stir_enabled: Optional[bool] = None
    """
    When enabled Telnyx will include Shaken/Stir data in the Webhook for new inbound
    calls.
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
    When set, this will limit the total number of outbound calls to phone numbers
    associated with this connection.
    """

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""


class TexmlApplication(BaseModel):
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

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    dtmf_type: Optional[DtmfType] = None
    """Sets the type of DTMF digits sent from Telnyx to this Connection.

    Note that DTMF digits sent to Telnyx will be accepted in all formats.
    """

    first_command_timeout: Optional[bool] = None
    """
    Specifies whether calls to phone numbers associated with this connection should
    hangup after timing out.
    """

    first_command_timeout_secs: Optional[int] = None
    """Specifies how many seconds to wait before timing out a dial command."""

    friendly_name: Optional[str] = None
    """A user-assigned name to help manage the application."""

    inbound: Optional[Inbound] = None

    outbound: Optional[Outbound] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status_callback: Optional[str] = None
    """
    URL for Telnyx to send requests to containing information about call progress
    events.
    """

    status_callback_method: Optional[Literal["get", "post"]] = None
    """HTTP request method Telnyx should use when requesting the status_callback URL."""

    tags: Optional[List[str]] = None
    """Tags associated with the Texml Application."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    voice_fallback_url: Optional[str] = None
    """
    URL to which Telnyx will deliver your XML Translator webhooks if we get an error
    response from your voice_url.
    """

    voice_method: Optional[Literal["get", "post"]] = None
    """
    HTTP request method Telnyx will use to interact with your XML Translator
    webhooks. Either 'get' or 'post'.
    """

    voice_url: Optional[str] = None
    """URL to which Telnyx will deliver your XML Translator webhooks."""
