# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .call_control_application_inbound_param import CallControlApplicationInboundParam
from .call_control_application_outbound_param import CallControlApplicationOutboundParam

__all__ = ["CallControlApplicationCreateParams"]


class CallControlApplicationCreateParams(TypedDict, total=False):
    application_name: Required[str]
    """A user-assigned name to help manage the application."""

    webhook_event_url: Required[str]
    """The URL where webhooks related to this connection will be sent.

    Must include a scheme, such as 'https'.
    """

    active: bool
    """Specifies whether the connection can be used."""

    anchorsite_override: Literal['"Latency"', '"Chicago, IL"', '"Ashburn, VA"', '"San Jose, CA"']
    """
    <code>Latency</code> directs Telnyx to route media through the site with the
    lowest round-trip time to the user's connection. Telnyx calculates this time
    using ICMP ping messages. This can be disabled by specifying a site to handle
    all media.
    """

    dtmf_type: Literal["RFC 2833", "Inband", "SIP INFO"]
    """Sets the type of DTMF digits sent from Telnyx to this Connection.

    Note that DTMF digits sent to Telnyx will be accepted in all formats.
    """

    first_command_timeout: bool
    """
    Specifies whether calls to phone numbers associated with this connection should
    hangup after timing out.
    """

    first_command_timeout_secs: int
    """Specifies how many seconds to wait before timing out a dial command."""

    inbound: CallControlApplicationInboundParam

    outbound: CallControlApplicationOutboundParam

    redact_dtmf_debug_logging: bool
    """
    When enabled, DTMF digits entered by users will be redacted in debug logs to
    protect PII data entered through IVR interactions.
    """

    webhook_api_version: Literal["1", "2"]
    """Determines which webhook format will be used, Telnyx API v1 or v2."""

    webhook_event_failover_url: Optional[str]
    """
    The failover URL where webhooks related to this connection will be sent if
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int]
    """Specifies how many seconds to wait before timing out a webhook."""
