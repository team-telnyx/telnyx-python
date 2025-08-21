# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .loopcount_param import LoopcountParam

__all__ = ["ActionStartPlaybackParams"]


class ActionStartPlaybackParams(TypedDict, total=False):
    audio_type: Literal["mp3", "wav"]
    """Specifies the type of audio provided in `audio_url` or `playback_content`."""

    audio_url: str
    """The URL of a file to be played back on the call.

    The URL can point to either a WAV or MP3 file. media_name and audio_url cannot
    be used together in one request.
    """

    cache_audio: bool
    """Caches the audio file.

    Useful when playing the same audio file multiple times during the call.
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

    loop: LoopcountParam
    """The number of times the audio file should be played.

    If supplied, the value must be an integer between 1 and 100, or the special
    string `infinity` for an endless loop.
    """

    media_name: str
    """The media_name of a file to be played back on the call.

    The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """

    overlay: bool
    """
    When enabled, audio will be mixed on top of any other audio that is actively
    being played back. Note that `overlay: true` will only work if there is another
    audio file already being played on the call.
    """

    playback_content: str
    """Allows a user to provide base64 encoded mp3 or wav.

    Note: when using this parameter, `media_url` and `media_name` in the
    `playback_started` and `playback_ended` webhooks will be empty
    """

    stop: str
    """When specified, it stops the current audio being played.

    Specify `current` to stop the current audio being played, and to play the next
    file in the queue. Specify `all` to stop the current audio file being played and
    to also clear all audio files from the queue.
    """

    target_legs: str
    """Specifies the leg or legs on which audio will be played.

    If supplied, the value must be either `self`, `opposite` or `both`.
    """
