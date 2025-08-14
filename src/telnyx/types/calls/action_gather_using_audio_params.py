# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionGatherUsingAudioParams"]


class ActionGatherUsingAudioParams(TypedDict, total=False):
    audio_url: str
    """The URL of a file to be played back at the beginning of each prompt.

    The URL can point to either a WAV or MP3 file. media_name and audio_url cannot
    be used together in one request.
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

    inter_digit_timeout_millis: int
    """The number of milliseconds to wait for input between digits."""

    invalid_audio_url: str
    """
    The URL of a file to play when digits don't match the `valid_digits` parameter
    or the number of digits is not between `min` and `max`. The URL can point to
    either a WAV or MP3 file. invalid_media_name and invalid_audio_url cannot be
    used together in one request.
    """

    invalid_media_name: str
    """
    The media_name of a file to be played back when digits don't match the
    `valid_digits` parameter or the number of digits is not between `min` and `max`.
    The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """

    maximum_digits: int
    """The maximum number of digits to fetch.

    This parameter has a maximum value of 128.
    """

    maximum_tries: int
    """
    The maximum number of times the file should be played if there is no input from
    the user on the call.
    """

    media_name: str
    """The media_name of a file to be played back at the beginning of each prompt.

    The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """

    minimum_digits: int
    """The minimum number of digits to fetch. This parameter has a minimum value of 1."""

    terminating_digit: str
    """
    The digit used to terminate input if fewer than `maximum_digits` digits have
    been gathered.
    """

    timeout_millis: int
    """
    The number of milliseconds to wait for a DTMF response after file playback ends
    before a replaying the sound file.
    """

    valid_digits: str
    """A list of all digits accepted as valid."""
