# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CredentialInboundParam"]


class CredentialInboundParam(TypedDict, total=False):
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

    timeout_1xx_secs: int
    """Time(sec) before aborting if connection is not made."""

    timeout_2xx_secs: int
    """Time(sec) before aborting if call is unanswered (min: 1, max: 600)."""
