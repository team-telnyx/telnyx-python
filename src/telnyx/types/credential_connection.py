# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .dtmf_type import DtmfType
from .encrypted_media import EncryptedMedia
from .credential_inbound import CredentialInbound
from .anchorsite_override import AnchorsiteOverride
from .credential_outbound import CredentialOutbound
from .connection_rtcp_settings import ConnectionRtcpSettings

__all__ = ["CredentialConnection"]


class CredentialConnection(BaseModel):
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

    inbound: Optional[CredentialInbound] = None

    onnet_t38_passthrough_enabled: Optional[bool] = None
    """
    Enable on-net T38 if you prefer the sender and receiver negotiating T38 directly
    if both are on the Telnyx network. If this is disabled, Telnyx will be able to
    use T38 on just one leg of the call depending on each leg's settings.
    """

    outbound: Optional[CredentialOutbound] = None

    password: Optional[str] = None
    """The password to be used as part of the credentials.

    Must be 8 to 128 characters long.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

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
