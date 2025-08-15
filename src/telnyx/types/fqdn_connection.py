# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .dtmf_type import DtmfType
from .inbound_fqdn import InboundFqdn
from .outbound_fqdn import OutboundFqdn
from .encrypted_media import EncryptedMedia
from .transport_protocol import TransportProtocol
from .anchorsite_override import AnchorsiteOverride
from .webhook_api_version import WebhookAPIVersion
from .connection_rtcp_settings import ConnectionRtcpSettings

__all__ = ["FqdnConnection"]


class FqdnConnection(BaseModel):
    connection_name: str
    """A user-assigned name to help manage the connection."""

    id: Optional[str] = None
    """Identifies the resource."""

    active: Optional[bool] = None
    """Defaults to true"""

    adjust_dtmf_timestamp: Optional[bool] = None
    """Indicates whether DTMF timestamp adjustment is enabled."""

    anchorsite_override: Optional[AnchorsiteOverride] = None
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    call_cost_enabled: Optional[bool] = None
    """Indicates whether call cost calculation is enabled."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

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

    ignore_dtmf_duration: Optional[bool] = None
    """Indicates whether DTMF duration should be ignored."""

    ignore_mark_bit: Optional[bool] = None
    """Indicates whether the mark bit should be ignored."""

    inbound: Optional[InboundFqdn] = None

    microsoft_teams_sbc: Optional[bool] = None
    """The connection is enabled for Microsoft Teams Direct Routing."""

    noise_suppression: Optional[bool] = None
    """Indicates whether noise suppression is enabled."""

    onnet_t38_passthrough_enabled: Optional[bool] = None
    """
    Enable on-net T38 if you prefer that the sender and receiver negotiate T38
    directly when both are on the Telnyx network. If this is disabled, Telnyx will
    be able to use T38 on just one leg of the call according to each leg's settings.
    """

    outbound: Optional[OutboundFqdn] = None

    password: Optional[str] = None
    """The password for the FQDN connection."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    rtcp_settings: Optional[ConnectionRtcpSettings] = None

    rtp_pass_codecs_on_stream_change: Optional[bool] = None
    """Defines if codecs should be passed on stream change."""

    send_normalized_timestamps: Optional[bool] = None
    """Indicates whether normalized timestamps should be sent."""

    tags: Optional[List[str]] = None
    """Tags associated with the connection."""

    third_party_control_enabled: Optional[bool] = None
    """Indicates whether third-party control is enabled."""

    transport_protocol: Optional[TransportProtocol] = None
    """One of UDP, TLS, or TCP.

    Applies only to connections with IP authentication or FQDN authentication.
    """

    txt_name: Optional[str] = None
    """The name for the TXT record associated with the FQDN connection."""

    txt_ttl: Optional[int] = None
    """The time to live for the TXT record associated with the FQDN connection."""

    txt_value: Optional[str] = None
    """The value for the TXT record associated with the FQDN connection."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""

    user_name: Optional[str] = None
    """The username for the FQDN connection."""

    webhook_api_version: Optional[WebhookAPIVersion] = None
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
