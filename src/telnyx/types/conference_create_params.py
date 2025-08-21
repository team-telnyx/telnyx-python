# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConferenceCreateParams"]


class ConferenceCreateParams(TypedDict, total=False):
    call_control_id: Required[str]
    """Unique identifier and token for controlling the call"""

    name: Required[str]
    """Name of the conference"""

    beep_enabled: Literal["always", "never", "on_enter", "on_exit"]
    """
    Whether a beep sound should be played when participants join and/or leave the
    conference.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string. The client_state will be updated for
    the creator call leg and will be used for all webhooks related to the created
    conference.
    """

    comfort_noise: bool
    """Toggle background comfort noise."""

    command_id: str
    """Use this field to avoid execution of duplicate commands.

    Telnyx will ignore subsequent commands with the same `command_id` as one that
    has already been executed.
    """

    duration_minutes: int
    """Time length (minutes) after which the conference will end."""

    hold_audio_url: str
    """The URL of a file to be played to participants joining the conference.

    The URL can point to either a WAV or MP3 file. hold_media_name and
    hold_audio_url cannot be used together in one request. Takes effect only when
    "start_conference_on_create" is set to "false".
    """

    hold_media_name: str
    """The media_name of a file to be played to participants joining the conference.

    The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file. Takes effect only when "start_conference_on_create" is set to
    "false".
    """

    max_participants: int
    """The maximum number of active conference participants to allow.

    Must be between 2 and 800. Defaults to 250
    """

    start_conference_on_create: bool
    """Whether the conference should be started on creation.

    If the conference isn't started all participants that join are automatically put
    on hold. Defaults to "true".
    """
