# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionJoinParams"]


class ActionJoinParams(TypedDict, total=False):
    call_control_id: Required[str]
    """Unique identifier and token for controlling the call"""

    beep_enabled: Literal["always", "never", "on_enter", "on_exit"]
    """
    Whether a beep sound should be played when the participant joins and/or leaves
    the conference. Can be used to override the conference-level setting.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string. Please note that the client_state
    will be updated for the participient call leg and the change will not affect
    conferencing webhooks unless the participient is the owner of the conference.
    """

    command_id: str
    """Use this field to avoid execution of duplicate commands.

    Telnyx will ignore subsequent commands with the same `command_id` as one that
    has already been executed.
    """

    end_conference_on_exit: bool
    """
    Whether the conference should end and all remaining participants be hung up
    after the participant leaves the conference. Defaults to "false".
    """

    hold: bool
    """
    Whether the participant should be put on hold immediately after joining the
    conference. Defaults to "false".
    """

    hold_audio_url: str
    """
    The URL of a file to be played to the participant when they are put on hold
    after joining the conference. hold_media_name and hold_audio_url cannot be used
    together in one request. Takes effect only when "start_conference_on_create" is
    set to "false". This property takes effect only if "hold" is set to "true".
    """

    hold_media_name: str
    """
    The media_name of a file to be played to the participant when they are put on
    hold after joining the conference. The media_name must point to a file
    previously uploaded to api.telnyx.com/v2/media by the same user/organization.
    The file must either be a WAV or MP3 file. Takes effect only when
    "start_conference_on_create" is set to "false". This property takes effect only
    if "hold" is set to "true".
    """

    mute: bool
    """Whether the participant should be muted immediately after joining the
    conference.

    Defaults to "false".
    """

    soft_end_conference_on_exit: bool
    """Whether the conference should end after the participant leaves the conference.

    NOTE this doesn't hang up the other participants. Defaults to "false".
    """

    start_conference_on_enter: bool
    """
    Whether the conference should be started after the participant joins the
    conference. Defaults to "false".
    """

    supervisor_role: Literal["barge", "monitor", "none", "whisper"]
    """Sets the joining participant as a supervisor for the conference.

    A conference can have multiple supervisors. "barge" means the supervisor enters
    the conference as a normal participant. This is the same as "none". "monitor"
    means the supervisor is muted but can hear all participants. "whisper" means
    that only the specified "whisper_call_control_ids" can hear the supervisor.
    Defaults to "none".
    """

    whisper_call_control_ids: List[str]
    """Array of unique call_control_ids the joining supervisor can whisper to.

    If none provided, the supervisor will join the conference as a monitoring
    participant only.
    """
