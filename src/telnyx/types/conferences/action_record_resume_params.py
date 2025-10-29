# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionRecordResumeParams"]


class ActionRecordResumeParams(TypedDict, total=False):
    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    recording_id: str
    """Use this field to resume specific recording."""

    region: Literal["Australia", "Europe", "Middle East", "US"]
    """Region where the conference data is located.

    Defaults to the region defined in user's data locality settings (Europe or US).
    """
