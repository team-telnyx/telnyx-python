# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VoiceSettingsParam",
    "BackgroundAudio",
    "BackgroundAudioPredefinedMedia",
    "BackgroundAudioMediaURL",
    "BackgroundAudioMediaName",
]


class BackgroundAudioPredefinedMedia(TypedDict, total=False):
    type: Required[Literal["predefined_media"]]
    """Select from predefined media options."""

    value: Required[Literal["silence", "office"]]
    """The predefined media to use. `silence` disables background audio."""


class BackgroundAudioMediaURL(TypedDict, total=False):
    type: Required[Literal["media_url"]]
    """Provide a direct URL to an MP3 file. The audio will loop during the call."""

    value: Required[str]
    """HTTPS URL to an MP3 file."""


class BackgroundAudioMediaName(TypedDict, total=False):
    type: Required[Literal["media_name"]]
    """Reference a previously uploaded media by its name from Telnyx Media Storage."""

    value: Required[str]
    """
    The `name` of a media asset created via
    [Media Storage API](https://developers.telnyx.com/api/media-storage/create-media-storage).
    The audio will loop during the call.
    """


BackgroundAudio: TypeAlias = Union[BackgroundAudioPredefinedMedia, BackgroundAudioMediaURL, BackgroundAudioMediaName]


class VoiceSettingsParam(TypedDict, total=False):
    voice: Required[str]
    """The voice to be used by the voice assistant.

    Check the full list of
    [available voices](https://developers.telnyx.com/api/call-control/list-text-to-speech-voices)
    via our voices API. To use ElevenLabs, you must reference your ElevenLabs API
    key as an integration secret under the `api_key_ref` field. See
    [integration secrets documentation](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    for details. For Telnyx voices, use `Telnyx.<model_id>.<voice_id>` (e.g.
    Telnyx.KokoroTTS.af_heart)
    """

    api_key_ref: str
    """
    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your ElevenLabs API key. Warning: Free plans are unlikely to work
    with this integration.
    """

    background_audio: BackgroundAudio
    """Optional background audio to play on the call.

    Use a predefined media bed, or supply a looped MP3 URL. If a media URL is chosen
    in the portal, customers can preview it before saving.
    """

    similarity_boost: float
    """
    Determines how closely the AI should adhere to the original voice when
    attempting to replicate it. Only applicable when using ElevenLabs.
    """

    speed: float
    """Adjusts speech velocity.

    1.0 is default speed; values less than 1.0 slow speech; values greater than 1.0
    accelerate it. Only applicable when using ElevenLabs.
    """

    style: float
    """Determines the style exaggeration of the voice.

    Amplifies speaker style but consumes additional resources when set above 0. Only
    applicable when using ElevenLabs.
    """

    temperature: float
    """Determines how stable the voice is and the randomness between each generation.

    Lower values create a broader emotional range; higher values produce more
    consistent, monotonous output. Only applicable when using ElevenLabs.
    """

    use_speaker_boost: bool
    """Amplifies similarity to the original speaker voice.

    Increases computational load and latency slightly. Only applicable when using
    ElevenLabs.
    """

    voice_speed: float
    """The speed of the voice in the range [0.25, 2.0].

    1.0 is deafult speed. Larger numbers make the voice faster, smaller numbers make
    it slower. This is only applicable for Telnyx Natural voices.
    """
