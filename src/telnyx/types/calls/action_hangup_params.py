# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ..custom_sip_header_param import CustomSipHeaderParam

__all__ = ["ActionHangupParams"]


class ActionHangupParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP BYE message."""

    reason: str
    """
    Text for the SIP `Reason` header (RFC 3326) sent when cancelling an unanswered
    outbound leg. The SIP CANCEL carries `Reason: SIP;cause=200;text="<reason>"`;
    phones such as Poly and Yealink use it to suppress the missed-call entry for a
    call answered elsewhere. Has no effect on an answered leg or an inbound leg. A
    hangup sent before the leg's `call.initiated` webhook still hangs up the leg,
    but without the `Reason` header. Must not contain `"`, `\\``, control characters,
    or characters outside the Basic Multilingual Plane (such as emoji); invalid
    values are rejected with a 422.
    """
