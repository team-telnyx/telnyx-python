# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VoicemailPrefResponse", "Greeting"]


class Greeting(BaseModel):
    """Controls the greeting a caller hears before leaving a voicemail.

    Set `mode` to `default` to play the standard system greeting, or to `custom_greeting` to play your own audio. When `mode` is `custom_greeting`, `media_name` is required and must reference an audio file already uploaded to your account through the Media Storage API.
    """

    media_name: Optional[str] = None
    """The name of the media file to play as the greeting.

    Required when `mode` is `custom_greeting`; ignored when `mode` is `default`. The
    value must match the `media_name` of a file you previously uploaded with the
    Media Storage API (`POST /v2/media`).
    """

    mode: Optional[Literal["default", "custom_greeting"]] = None
    """The greeting mode.

    `default` plays the standard system greeting. `custom_greeting` plays the audio
    referenced by `media_name`.
    """


class VoicemailPrefResponse(BaseModel):
    enabled: Optional[bool] = None
    """Whether voicemail is enabled."""

    greeting: Optional[Greeting] = None
    """Controls the greeting a caller hears before leaving a voicemail.

    Set `mode` to `default` to play the standard system greeting, or to
    `custom_greeting` to play your own audio. When `mode` is `custom_greeting`,
    `media_name` is required and must reference an audio file already uploaded to
    your account through the Media Storage API.
    """

    pin: Optional[str] = None
    """The pin used for the voicemail."""
