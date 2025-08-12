# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from .dtmf_type import DtmfType
from .encrypted_media import EncryptedMedia
from .anchorsite_override import AnchorsiteOverride
from .credential_inbound_param import CredentialInboundParam
from .credential_outbound_param import CredentialOutboundParam
from .connection_rtcp_settings_param import ConnectionRtcpSettingsParam

__all__ = ["CredentialConnectionUpdateParams"]


class CredentialConnectionUpdateParams(TypedDict, total=False):
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
    """A user-assigned name to help manage the connection."""

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

    inbound: CredentialInboundParam

    ios_push_credential_id: Optional[str]
    """The uuid of the push credential for Ios"""

    onnet_t38_passthrough_enabled: bool
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: CredentialOutboundParam

    password: str
    """The password to be used as part of the credentials.

    Must be 8 to 128 characters long.
    """

    rtcp_settings: ConnectionRtcpSettingsParam

    sip_uri_calling_preference: Literal["disabled", "unrestricted", "internal"]
    """This feature enables inbound SIP URI calls to your Credential Auth Connection.

    If enabled for all (unrestricted) then anyone who calls the SIP URI
    <your-username>@telnyx.com will be connected to your Connection. You can also
    choose to allow only calls that are originated on any Connections under your
    account (internal).
    """

    tags: List[str]
    """Tags associated with the connection."""

    user_name: str
    """The user name to be used as part of the credentials.

    Must be 4-32 characters long and alphanumeric values only (no spaces or special
    characters).
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
