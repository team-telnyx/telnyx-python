# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundIP"]


class InboundIP(BaseModel):
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

    default_primary_ip_id: Optional[str] = None
    """The default primary IP to use for the number.

    Only settable if the connection is of IP authentication type. Value must be the
    ID of an authorized IP set on the connection.
    """

    default_routing_method: Optional[Literal["sequential", "round-robin"]] = None
    """
    Default routing method to be used when a number is associated with the
    connection. Must be one of the routing method types or left blank, other values
    are not allowed.
    """

    default_secondary_ip_id: Optional[str] = None
    """The default secondary IP to use for the number.

    Only settable if the connection is of IP authentication type. Value must be the
    ID of an authorized IP set on the connection.
    """

    default_tertiary_ip_id: Optional[str] = None
    """The default tertiary IP to use for the number.

    Only settable if the connection is of IP authentication type. Value must be the
    ID of an authorized IP set on the connection.
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

    sip_compact_headers_enabled: Optional[bool] = None
    """Defaults to true."""

    sip_region: Optional[Literal["US", "Europe", "Australia"]] = None
    """Selects which `sip_region` to receive inbound calls from.

    If null, the default region (US) will be used.
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

    timeout_1xx_secs: Optional[int] = None
    """Time(sec) before aborting if connection is not made."""

    timeout_2xx_secs: Optional[int] = None
    """Time(sec) before aborting if call is unanswered (min: 1, max: 600)."""
