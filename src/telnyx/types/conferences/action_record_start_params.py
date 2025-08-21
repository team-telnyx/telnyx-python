# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionRecordStartParams"]


class ActionRecordStartParams(TypedDict, total=False):
    format: Required[Literal["wav", "mp3"]]
    """The audio file format used when storing the conference recording.

    Can be either `mp3` or `wav`.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `conference_id`.
    """

    custom_file_name: str
    """The custom recording file name to be used instead of the default `call_leg_id`.

    Telnyx will still add a Unix timestamp suffix.
    """

    play_beep: bool
    """If enabled, a beep sound will be played at the start of a recording."""

    trim: Literal["trim-silence"]
    """
    When set to `trim-silence`, silence will be removed from the beginning and end
    of the recording.
    """
