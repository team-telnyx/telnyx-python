# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .dtmf_type import DtmfType
from .encrypted_media import EncryptedMedia
from .inbound_ip_param import InboundIPParam
from .outbound_ip_param import OutboundIPParam
from .anchorsite_override import AnchorsiteOverride
from .connection_rtcp_settings_param import ConnectionRtcpSettingsParam
from .shared_params.connection_noise_suppression_details import ConnectionNoiseSuppressionDetails

__all__ = ["IPConnectionUpdateParams", "JitterBuffer"]


class IPConnectionUpdateParams(TypedDict, total=False):
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

    call_cost_in_webhooks: bool
    """Specifies if call cost webhooks should be sent for this connection."""

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

    inbound: InboundIPParam

    ios_push_credential_id: Optional[str]
    """The uuid of the push credential for Ios"""

    jitter_buffer: JitterBuffer
    """Configuration options for Jitter Buffer.

    Enables Jitter Buffer for RTP streams of SIP Trunking calls. The feature is off
    unless enabled. You may define min and max values in msec for customized
    buffering behaviors. Larger values add latency but tolerate more jitter, while
    smaller values reduce latency but are more sensitive to jitter and reordering.
    """

    noise_suppression: Literal["inbound", "outbound", "both", "disabled"]
    """Controls when noise suppression is applied to calls.

    When set to 'inbound', noise suppression is applied to incoming audio. When set
    to 'outbound', it's applied to outgoing audio. When set to 'both', it's applied
    in both directions. When set to 'disabled', noise suppression is turned off.
    """

    noise_suppression_details: ConnectionNoiseSuppressionDetails
    """Configuration options for noise suppression.

    These settings are stored regardless of the noise_suppression value, but only
    take effect when noise_suppression is not 'disabled'. If you disable noise
    suppression and later re-enable it, the previously configured settings will be
    used.
    """

    onnet_t38_passthrough_enabled: bool
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: OutboundIPParam

    rtcp_settings: ConnectionRtcpSettingsParam

    tags: SequenceNotStr[str]
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


class JitterBuffer(TypedDict, total=False):
    """Configuration options for Jitter Buffer.

    Enables Jitter Buffer for RTP streams of SIP Trunking calls. The feature is off unless enabled. You may define min and max values in msec for customized buffering behaviors. Larger values add latency but tolerate more jitter, while smaller values reduce latency but are more sensitive to jitter and reordering.
    """

    enable_jitter_buffer: bool
    """Enables Jitter Buffer for RTP streams of SIP Trunking calls.

    The feature is off unless enabled.
    """

    jitterbuffer_msec_max: int
    """The maximum jitter buffer size in milliseconds.

    Must be between 40 and 400. Has no effect if enable_jitter_buffer is not true.
    """

    jitterbuffer_msec_min: int
    """The minimum jitter buffer size in milliseconds.

    Must be between 40 and 400. Has no effect if enable_jitter_buffer is not true.
    """
