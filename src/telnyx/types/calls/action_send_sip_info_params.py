# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionSendSipInfoParams"]


class ActionSendSipInfoParams(TypedDict, total=False):
    body: Required[str]
    """Content of the SIP INFO"""

    content_type: Required[str]
    """Content type of the INFO body.

    Must be MIME type compliant. There is a 1,400 bytes limit
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
