# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionStartNoiseSuppressionParams"]


class ActionStartNoiseSuppressionParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    direction: Literal["inbound", "outbound", "both"]
    """The direction of the audio stream to be noise suppressed."""

    noise_suppression_engine: Literal["A", "B"]
    """The engine to use for noise suppression.

    A - rnnoise engine B - deepfilter engine.
    """
