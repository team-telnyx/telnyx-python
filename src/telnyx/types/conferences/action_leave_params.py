# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionLeaveParams"]


class ActionLeaveParams(TypedDict, total=False):
    call_control_id: Required[str]
    """Unique identifier and token for controlling the call"""

    beep_enabled: Literal["always", "never", "on_enter", "on_exit"]
    """Whether a beep sound should be played when the participant leaves the
    conference.

    Can be used to override the conference-level setting.
    """

    command_id: str
    """Use this field to avoid execution of duplicate commands.

    Telnyx will ignore subsequent commands with the same `command_id` as one that
    has already been executed.
    """
