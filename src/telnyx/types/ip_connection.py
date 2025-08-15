# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .dtmf_type import DtmfType
from .inbound_ip import InboundIP
from .outbound_ip import OutboundIP
from .encrypted_media import EncryptedMedia
from .anchorsite_override import AnchorsiteOverride
from .connection_rtcp_settings import ConnectionRtcpSettings

__all__ = ["IPConnection"]


class IPConnection(BaseModel):
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

    connection_name: Optional[str] = None

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

    inbound: Optional[InboundIP] = None

    onnet_t38_passthrough_enabled: Optional[bool] = None
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: Optional[OutboundIP] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    rtcp_settings: Optional[ConnectionRtcpSettings] = None

    tags: Optional[List[str]] = None
    """Tags associated with the connection."""

    transport_protocol: Optional[Literal["UDP", "TCP", "TLS"]] = None
    """One of UDP, TLS, or TCP.

    Applies only to connections with IP authentication or FQDN authentication.
    """

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
