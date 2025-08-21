# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionRecordPauseParams"]


class ActionRecordPauseParams(TypedDict, total=False):
    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    recording_id: str
    """Use this field to pause specific recording."""
