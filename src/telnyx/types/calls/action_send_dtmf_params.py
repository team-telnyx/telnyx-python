# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionSendDtmfParams"]


class ActionSendDtmfParams(TypedDict, total=False):
    digits: Required[str]
    """DTMF digits to send.

    Valid digits are 0-9, A-D, \\**, and #. Pauses can be added using w (0.5s) and W
    (1s).
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

    duration_millis: int
    """
    Specifies for how many milliseconds each digit will be played in the audio
    stream. Ranges from 100 to 500ms
    """
