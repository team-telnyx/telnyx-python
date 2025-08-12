# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .dtmf_type import DtmfType
from .encrypted_media import EncryptedMedia
from .outbound_ip_param import OutboundIPParam
from .anchorsite_override import AnchorsiteOverride
from .connection_rtcp_settings_param import ConnectionRtcpSettingsParam

__all__ = ["IPConnectionCreateParams", "Inbound"]


class IPConnectionCreateParams(TypedDict, total=False):
    active: bool
    """Defaults to true"""

    anchorsite_override: AnchorsiteOverride
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    android_push_credential_id: Optional[str]
    """The uuid of the push credential for Android"""

    connection_name: str

    default_on_hold_comfort_noise_enabled: bool
    """When enabled, Telnyx will generate comfort noise when you place the call on
    hold.

    If disabled, you will need to generate comfort noise or on hold music to avoid
    RTP timeout.
    """

    dtmf_type: DtmfType
    """Sets the type of DTMF digits sent from Telnyx to this Connection.

    Note that DTMF digits sent to Telnyx will be accepted in all formats.
    """

    encode_contact_header_enabled: bool
    """
    Encode the SIP contact header sent by Telnyx to avoid issues for NAT or ALG
    scenarios.
    """

    encrypted_media: Optional[EncryptedMedia]
    """Enable use of SRTP for encryption.

    Cannot be set if the transport_portocol is TLS.
    """

    inbound: Inbound

    ios_push_credential_id: Optional[str]
    """The uuid of the push credential for Ios"""

    onnet_t38_passthrough_enabled: bool
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: OutboundIPParam

    rtcp_settings: ConnectionRtcpSettingsParam

    tags: List[str]
    """Tags associated with the connection."""

    transport_protocol: Literal["UDP", "TCP", "TLS"]
    """One of UDP, TLS, or TCP.

    Applies only to connections with IP authentication or FQDN authentication.
    """

    webhook_api_version: Literal["1", "2"]
    """Determines which webhook format will be used, Telnyx API v1 or v2."""

    webhook_event_failover_url: Optional[str]
    """
    The failover URL where webhooks related to this connection will be sent if
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: str
    """The URL where webhooks related to this connection will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int]
    """Specifies how many seconds to wait before timing out a webhook."""


class Inbound(TypedDict, total=False):
    ani_number_format: Literal["+E.164", "E.164", "+E.164-national", "E.164-national"]
    """
    This setting allows you to set the format with which the caller's number (ANI)
    is sent for inbound phone calls.
    """

    channel_limit: int
    """
    When set, this will limit the total number of inbound calls to phone numbers
    associated with this connection.
    """

    codecs: List[str]
    """
    Defines the list of codecs that Telnyx will send for inbound calls to a specific
    number on your portal account, in priority order. This only works when the
    Connection the number is assigned to uses Media Handling mode: default. OPUS and
    H.264 codecs are available only when using TCP or TLS transport for SIP.
    """

    default_routing_method: Literal["sequential", "round-robin"]
    """
    Default routing method to be used when a number is associated with the
    connection. Must be one of the routing method types or left blank, other values
    are not allowed.
    """

    dnis_number_format: Literal["+e164", "e164", "national", "sip_username"]

    generate_ringback_tone: bool
    """Generate ringback tone through 183 session progress message with early media."""

    isup_headers_enabled: bool
    """When set, inbound phone calls will receive ISUP parameters via SIP headers.

    (Only when available and only when using TCP or TLS transport.)
    """

    prack_enabled: bool
    """Enable PRACK messages as defined in RFC3262."""

    shaken_stir_enabled: bool
    """
    When enabled the SIP Connection will receive the Identity header with
    Shaken/Stir data in the SIP INVITE message of inbound calls, even when using UDP
    transport.
    """

    sip_compact_headers_enabled: bool
    """Defaults to true."""

    sip_region: Literal["US", "Europe", "Australia"]
    """Selects which `sip_region` to receive inbound calls from.

    If null, the default region (US) will be used.
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

    timeout_1xx_secs: int
    """Time(sec) before aborting if connection is not made."""

    timeout_2xx_secs: int
    """Time(sec) before aborting if call is unanswered (min: 1, max: 600)."""
