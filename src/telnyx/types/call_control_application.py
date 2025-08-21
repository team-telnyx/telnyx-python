# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .call_control_application_inbound import CallControlApplicationInbound
from .call_control_application_outbound import CallControlApplicationOutbound

__all__ = ["CallControlApplication"]


class CallControlApplication(BaseModel):
    id: Optional[str] = None

    active: Optional[bool] = None
    """Specifies whether the connection can be used."""

    anchorsite_override: Optional[Literal['"Latency"', '"Chicago, IL"', '"Ashburn, VA"', '"San Jose, CA"']] = None
    """
    `Latency` directs Telnyx to route media through the site with the lowest
    round-trip time to the user's connection. Telnyx calculates this time using ICMP
    ping messages. This can be disabled by specifying a site to handle all media.
    """

    application_name: Optional[str] = None
    """A user-assigned name to help manage the application."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date of when the resource was created"""

    dtmf_type: Optional[Literal["RFC 2833", "Inband", "SIP INFO"]] = None
    """Sets the type of DTMF digits sent from Telnyx to this Connection.

    Note that DTMF digits sent to Telnyx will be accepted in all formats.
    """

    first_command_timeout: Optional[bool] = None
    """
    Specifies whether calls to phone numbers associated with this connection should
    hangup after timing out.
    """

    first_command_timeout_secs: Optional[int] = None
    """Specifies how many seconds to wait before timing out a dial command."""

    inbound: Optional[CallControlApplicationInbound] = None

    outbound: Optional[CallControlApplicationOutbound] = None

    record_type: Optional[Literal["call_control_application"]] = None

    redact_dtmf_debug_logging: Optional[bool] = None
    """
    When enabled, DTMF digits entered by users will be redacted in debug logs to
    protect PII data entered through IVR interactions.
    """

    tags: Optional[List[str]] = None
    """Tags assigned to the Call Control Application."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date of when the resource was last updated"""

    webhook_api_version: Optional[Literal["1", "2"]] = None
    """Determines which webhook format will be used, Telnyx API v1 or v2."""

    webhook_event_failover_url: Optional[str] = None
    """
    The failover URL where webhooks related to this connection will be sent if
    sending to the primary URL fails. Must include a scheme, such as `https`.
    """

    webhook_event_url: Optional[str] = None
    """The URL where webhooks related to this connection will be sent.

    Must include a scheme, such as `https`.
    """

    webhook_timeout_secs: Optional[int] = None
