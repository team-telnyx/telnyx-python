# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionRejectParams"]


class ActionRejectParams(TypedDict, total=False):
    cause: Required[Literal["CALL_REJECTED", "NOT_FOUND", "TEMPORARILY_UNAVAILABLE", "USER_BUSY"]]
    """Cause for call rejection.

    The cause sets the SIP response the caller receives: `USER_BUSY` sends 486 User
    Busy, `CALL_REJECTED` sends 603 Decline, `NOT_FOUND` sends 404 Not Found, and
    `TEMPORARILY_UNAVAILABLE` sends 480 Temporarily Unavailable.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """
