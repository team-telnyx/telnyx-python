# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["VoicemailUpdateParams", "Greeting"]


class VoicemailUpdateParams(TypedDict, total=False):
    enabled: bool
    """Whether voicemail is enabled."""

    greeting: Greeting
    """Controls the greeting a caller hears before leaving a voicemail.

    Set `mode` to `default` to play the standard system greeting, or to
    `custom_greeting` to play your own audio. When `mode` is `custom_greeting`,
    `media_name` is required and must reference an audio file already uploaded to
    your account through the Media Storage API.
    """

    pin: str
    """The pin used for voicemail"""


class Greeting(TypedDict, total=False):
    """Controls the greeting a caller hears before leaving a voicemail.

    Set `mode` to `default` to play the standard system greeting, or to `custom_greeting` to play your own audio. When `mode` is `custom_greeting`, `media_name` is required and must reference an audio file already uploaded to your account through the Media Storage API.
    """

    media_name: Optional[str]
    """The name of the media file to play as the greeting.

    Required when `mode` is `custom_greeting`; ignored when `mode` is `default`. The
    value must match the `media_name` of a file you previously uploaded with the
    Media Storage API (`POST /v2/media`).
    """

    mode: Literal["default", "custom_greeting"]
    """The greeting mode.

    `default` plays the standard system greeting. `custom_greeting` plays the audio
    referenced by `media_name`.
    """
