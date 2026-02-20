# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionGatherDtmfAudioParams"]


class ActionGatherDtmfAudioParams(TypedDict, total=False):
    call_control_id: Required[str]
    """
    Unique identifier and token for controlling the call leg that will receive the
    gather prompt.
    """

    audio_url: str
    """The URL of the audio file to play as the gather prompt.

    Must be WAV or MP3 format.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    Must be a valid Base-64 encoded string.
    """

    gather_id: str
    """Identifier for this gather command.

    Will be included in the gather ended webhook. Maximum 100 characters.
    """

    initial_timeout_millis: int
    """Duration in milliseconds to wait for the first digit before timing out."""

    inter_digit_timeout_millis: int
    """Duration in milliseconds to wait between digits."""

    invalid_audio_url: str
    """URL of audio file to play when invalid input is received."""

    invalid_media_name: str
    """Name of media file to play when invalid input is received."""

    maximum_digits: int
    """Maximum number of digits to gather."""

    maximum_tries: int
    """Maximum number of times to play the prompt if no input is received."""

    media_name: str
    """
    The name of the media file uploaded to the Media Storage API to play as the
    gather prompt.
    """

    minimum_digits: int
    """Minimum number of digits to gather."""

    stop_playback_on_dtmf: bool
    """Whether to stop the audio playback when a DTMF digit is received."""

    terminating_digit: str
    """Digit that terminates gathering."""

    timeout_millis: int
    """Duration in milliseconds to wait for input before timing out."""

    valid_digits: str
    """Digits that are valid for gathering. All other digits will be ignored."""
