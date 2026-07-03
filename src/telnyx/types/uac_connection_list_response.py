# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .fqdn import Fqdn
from .._models import BaseModel
from .dtmf_type import DtmfType
from .encrypted_media import EncryptedMedia
from .anchorsite_override import AnchorsiteOverride
from .connection_rtcp_settings import ConnectionRtcpSettings
from .shared.connection_jitter_buffer import ConnectionJitterBuffer
from .shared.connection_noise_suppression_details import ConnectionNoiseSuppressionDetails

__all__ = ["UacConnectionListResponse", "ExternalUacSettings", "Inbound", "InternalUacSettings", "Outbound"]


class ExternalUacSettings(BaseModel):
    """
    External SIP peer settings used by Telnyx when registering to your PBX and routing outbound calls.
    """

    auth_username: Optional[str] = None
    """The authentication username used in SIP digest authentication.

    If not set, the Username value will be used.
    """

    expiration_sec: Optional[int] = None
    """
    The registration interval, in seconds, indicating how often the system refreshes
    the SIP registration with the external SIP peer.
    """

    from_user: Optional[str] = None
    """The user portion of the SIP From header used in outbound requests.

    This controls the caller identity presented to the external SIP peer.
    """

    outbound_proxy: Optional[str] = None
    """
    An optional SIP proxy used to route outbound requests before reaching the
    external SIP peer.
    """

    password: Optional[str] = None
    """The SIP password used for digest authentication with the external SIP peer."""

    proxy: Optional[str] = None
    """
    The SIP proxy address of the external SIP peer used for registrations and
    outbound call routing.
    """

    transport: Optional[Literal["UDP", "TLS", "TCP"]] = None
    """
    The transport protocol used for SIP signaling when communicating with the
    external SIP peer. One of UDP, TLS, or TCP.
    """

    username: Optional[str] = None
    """
    The SIP username used to authenticate with the external SIP peer for
    registrations and outbound calls. Must start with a letter or number and contain
    only letters, numbers, hyphens, and underscores.
    """


class Inbound(BaseModel):
    ani_number_format: Optional[Literal["+E.164", "E.164", "+E.164-national", "E.164-national"]] = None
    """
    This setting allows you to set the format with which the caller's number (ANI)
    is sent for inbound phone calls.
    """

    channel_limit: Optional[int] = None
    """
    When set, this will limit the total number of inbound calls to phone numbers
    associated with this connection.
    """

    codecs: Optional[List[str]] = None
    """
    Defines the list of codecs that Telnyx will send for inbound calls to a specific
    number on your portal account, in priority order. This only works when the
    Connection the number is assigned to uses Media Handling mode: default. OPUS and
    H.264 codecs are available only when using TCP or TLS transport for SIP.
    """

    default_routing_method: Optional[Literal["sequential", "round-robin"]] = None
    """
    Default routing method to be used when a number is associated with the
    connection. Must be one of the routing method types or left blank, other values
    are not allowed.
    """

    dnis_number_format: Optional[Literal["+e164", "e164", "national", "sip_username"]] = None

    generate_ringback_tone: Optional[bool] = None
    """Generate ringback tone through 183 session progress message with early media."""

    isup_headers_enabled: Optional[bool] = None
    """When set, inbound phone calls will receive ISUP parameters via SIP headers.

    (Only when available and only when using TCP or TLS transport.)
    """

    prack_enabled: Optional[bool] = None
    """Enable PRACK messages as defined in RFC3262."""

    shaken_stir_enabled: Optional[bool] = None
    """
    When enabled the SIP Connection will receive the Identity header with
    Shaken/Stir data in the SIP INVITE message of inbound calls, even when using UDP
    transport.
    """

    simultaneous_ringing: Optional[Literal["disabled", "enabled"]] = None
    """When enabled, allows multiple devices to ring simultaneously on incoming calls."""

    sip_compact_headers_enabled: Optional[bool] = None
    """Defaults to true."""

    sip_region: Optional[Literal["US", "Europe", "Australia"]] = None
    """Selects which `sip_region` to receive inbound calls from.

    If null, the default region (US) will be used.
    """

    sip_subdomain: Optional[str] = None
    """The Telnyx-generated SIP subdomain for this UAC connection."""

    sip_subdomain_receive_settings: Optional[Literal["only_my_connections", "from_anyone"]] = None
    """Controls which SIP URI callers may reach this connection."""

    timeout_1xx_secs: Optional[int] = None
    """Time(sec) before aborting if connection is not made."""

    timeout_2xx_secs: Optional[int] = None
    """Time(sec) before aborting if call is unanswered (min: 1, max: 600)."""


class InternalUacSettings(BaseModel):
    """Internal Telnyx-side settings for a UAC connection."""

    destination_uri: Optional[str] = None
    """
    The SIP URI that Telnyx will call when handling an inbound request from the
    external peer. Do not include a `sip:` prefix. The value must be in the format
    `userinfo@<subdomain.>sip.telnyx.com` or
    `userinfo@<subdomain.>sipdev.telnyx.com`; the userinfo portion may contain only
    letters, digits, hyphens, and underscores.
    """


class Outbound(BaseModel):
    ani_override: Optional[str] = None
    """
    Set a phone number as the ani_override value to override caller id number on
    outbound calls.
    """

    ani_override_type: Optional[Literal["always", "normal", "emergency"]] = None
    """Specifies when we apply your ani_override setting.

    Only applies when ani_override is not blank.
    """

    call_parking_enabled: Optional[bool] = None
    """
    Forces all SIP calls originated on this connection to be "parked" instead of
    "bridged" to the destination specified on the URI. Parked calls will return
    ringback to the caller and will await for a Call Control command to define which
    action will be taken next.
    """

    channel_limit: Optional[int] = None
    """
    When set, this will limit the total number of outbound calls to phone numbers
    associated with this connection.
    """

    generate_ringback_tone: Optional[bool] = None
    """Generate ringback tone through 183 session progress message with early media."""

    instant_ringback_enabled: Optional[bool] = None
    """
    When set, ringback will not wait for indication before sending ringback tone to
    calling party.
    """

    localization: Optional[str] = None
    """
    A 2-character country code specifying the country whose national dialing rules
    should be used. For example, if set to `US` then any US number can be dialed
    without preprending +1 to the number. When left blank, Telnyx will try US and GB
    dialing rules, in that order, by default.
    """

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""

    t38_reinvite_source: Optional[
        Literal["telnyx", "customer", "disabled", "passthru", "caller-passthru", "callee-passthru"]
    ] = None
    """This setting only affects connections with Fax-type Outbound Voice Profiles.

    The setting dictates whether or not Telnyx sends a t.38 reinvite.<br/><br/> By
    default, Telnyx will send the re-invite. If set to `customer`, the caller is
    expected to send the t.38 reinvite.
    """


class UacConnectionListResponse(BaseModel):
    """
    A UAC (User Agent Client) Connection registers Telnyx to your PBX — the opposite of a standard SIP trunk, where the PBX registers to Telnyx. Use UAC when your PBX doesn’t support outbound SIP registration or you need Telnyx to maintain the registration.
    """

    id: Optional[str] = None
    """Identifies the type of resource."""

    active: Optional[bool] = None
    """Defaults to true"""

    anchorsite_override: Optional[AnchorsiteOverride] = None
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    android_push_credential_id: Optional[str] = None
    """The uuid of the push credential for Android"""

    authentication: Optional[Literal["uac-authentication"]] = None
    """The authentication strategy used by this connection."""

    call_cost_in_webhooks: Optional[bool] = None
    """Specifies if call cost webhooks should be sent for this connection."""

    connection_name: Optional[str] = None

    created_at: Optional[str] = None
    """ISO-8601 formatted date indicating when the resource was created."""

    default_on_hold_comfort_noise_enabled: Optional[bool] = None
    """When enabled, Telnyx will generate comfort noise when you place the call on
    hold.

    If disabled, you will need to generate comfort noise or on hold music to avoid
    RTP timeout.
    """

    dtmf_type: Optional[DtmfType] = None
    """Sets the type of DTMF digits sent from Telnyx to this Connection.

    Note that DTMF digits sent to Telnyx will be accepted in all formats.
    """

    encode_contact_header_enabled: Optional[bool] = None
    """
    Encode the SIP contact header sent by Telnyx to avoid issues for NAT or ALG
    scenarios.
    """

    encrypted_media: Optional[EncryptedMedia] = None
    """Enable use of SRTP for encryption.

    Cannot be set if the transport_portocol is TLS.
    """

    external_uac_settings: Optional[ExternalUacSettings] = None
    """
    External SIP peer settings used by Telnyx when registering to your PBX and
    routing outbound calls.
    """

    fqdn: Optional[str] = None
    """The Telnyx-managed FQDN generated for the UAC connection."""

    fqdn_outbound_authentication: Optional[Literal["credential-authentication"]] = None
    """The fixed outbound authentication mode used by UAC FQDN records."""

    fqdns: Optional[List[Fqdn]] = None
    """FQDN records managed automatically by the UAC connection lifecycle."""

    inbound: Optional[Inbound] = None

    internal_uac_settings: Optional[InternalUacSettings] = None
    """Internal Telnyx-side settings for a UAC connection."""

    ios_push_credential_id: Optional[str] = None
    """The uuid of the push credential for Ios"""

    jitter_buffer: Optional[ConnectionJitterBuffer] = None
    """Configuration options for Jitter Buffer.

    Enables Jitter Buffer for RTP streams of SIP Trunking calls. The feature is off
    unless enabled. You may define min and max values in msec for customized
    buffering behaviors. Larger values add latency but tolerate more jitter, while
    smaller values reduce latency but are more sensitive to jitter and reordering.
    """

    noise_suppression: Optional[Literal["inbound", "outbound", "both", "disabled"]] = None
    """Controls when noise suppression is applied to calls.

    When set to 'inbound', noise suppression is applied to incoming audio. When set
    to 'outbound', it's applied to outgoing audio. When set to 'both', it's applied
    in both directions. When set to 'disabled', noise suppression is turned off.
    """

    noise_suppression_details: Optional[ConnectionNoiseSuppressionDetails] = None
    """Configuration options for noise suppression.

    These settings are stored regardless of the noise_suppression value, but only
    take effect when noise_suppression is not 'disabled'. If you disable noise
    suppression and later re-enable it, the previously configured settings will be
    used.
    """

    onnet_t38_passthrough_enabled: Optional[bool] = None
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: Optional[Outbound] = None

    password: Optional[str] = None
    """The password to be used as part of the credentials.

    Must be 8 to 128 characters long.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    registration_status: Optional[str] = None
    """The most recently known SIP registration status for this UAC connection."""

    registration_status_updated_at: Optional[str] = None
    """
    ISO 8601 formatted date indicating when the registration status was last
    updated.
    """

    rtcp_settings: Optional[ConnectionRtcpSettings] = None

    sip_uri_calling_preference: Optional[Literal["disabled", "unrestricted", "internal"]] = None
    """This feature enables inbound SIP URI calls to your Credential Auth Connection.

    If enabled for all (unrestricted) then anyone who calls the SIP URI
    <your-username>@telnyx.com will be connected to your Connection. You can also
    choose to allow only calls that are originated on any Connections under your
    account (internal).
    """

    tags: Optional[List[str]] = None
    """Tags associated with the connection."""

    updated_at: Optional[str] = None
    """ISO-8601 formatted date indicating when the resource was updated."""

    user_name: Optional[str] = None
    """The user name to be used as part of the credentials.

    Must be 4-32 characters long and alphanumeric values only (no spaces or special
    characters). At least one of the first 5 characters must be a letter.
    """

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
