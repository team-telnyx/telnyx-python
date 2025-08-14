# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .dtmf_type import DtmfType
from .encrypted_media import EncryptedMedia
from .inbound_fqdn_param import InboundFqdnParam
from .transport_protocol import TransportProtocol
from .anchorsite_override import AnchorsiteOverride
from .outbound_fqdn_param import OutboundFqdnParam
from .webhook_api_version import WebhookAPIVersion
from .connection_rtcp_settings_param import ConnectionRtcpSettingsParam

__all__ = ["FqdnConnectionCreateParams"]


class FqdnConnectionCreateParams(TypedDict, total=False):
    connection_name: Required[str]
    """A user-assigned name to help manage the connection."""

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

    inbound: InboundFqdnParam

    ios_push_credential_id: Optional[str]
    """The uuid of the push credential for Ios"""

    microsoft_teams_sbc: bool
    """When enabled, the connection will be created for Microsoft Teams Direct Routing.

    A \\**.mstsbc.telnyx.tech FQDN will be created for the connection automatically.
    """

    onnet_t38_passthrough_enabled: bool
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: OutboundFqdnParam

    rtcp_settings: ConnectionRtcpSettingsParam

    tags: List[str]
    """Tags associated with the connection."""

    transport_protocol: TransportProtocol
    """One of UDP, TLS, or TCP.

    Applies only to connections with IP authentication or FQDN authentication.
    """

    webhook_api_version: WebhookAPIVersion
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
