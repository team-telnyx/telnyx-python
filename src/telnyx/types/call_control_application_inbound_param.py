# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CallControlApplicationInboundParam"]


class CallControlApplicationInboundParam(TypedDict, total=False):
    channel_limit: int
    """
    When set, this will limit the total number of inbound calls to phone numbers
    associated with this connection.
    """

    shaken_stir_enabled: bool
    """
    When enabled Telnyx will include Shaken/Stir data in the Webhook for new inbound
    calls.
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
