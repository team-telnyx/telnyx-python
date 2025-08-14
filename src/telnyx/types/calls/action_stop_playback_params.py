# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionStopPlaybackParams"]


class ActionStopPlaybackParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    overlay: bool
    """When enabled, it stops the audio being played in the overlay queue."""

    stop: str
    """Use `current` to stop the current audio being played.

    Use `all` to stop the current audio file being played and clear all audio files
    from the queue.
    """
