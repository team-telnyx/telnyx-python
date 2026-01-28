# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "VoiceSettings",
    "BackgroundAudio",
    "BackgroundAudioPredefinedMedia",
    "BackgroundAudioMediaURL",
    "BackgroundAudioMediaName",
]


class BackgroundAudioPredefinedMedia(BaseModel):
    type: Literal["predefined_media"]
    """Select from predefined media options."""

    value: Literal["silence", "office"]
    """The predefined media to use. `silence` disables background audio."""


class BackgroundAudioMediaURL(BaseModel):
    type: Literal["media_url"]
    """Provide a direct URL to an MP3 file. The audio will loop during the call."""

    value: str
    """HTTPS URL to an MP3 file."""


class BackgroundAudioMediaName(BaseModel):
    type: Literal["media_name"]
    """Reference a previously uploaded media by its name from Telnyx Media Storage."""

    value: str
    """
    The `name` of a media asset created via
    [Media Storage API](https://developers.telnyx.com/api/media-storage/create-media-storage).
    The audio will loop during the call.
    """


BackgroundAudio: TypeAlias = Annotated[
    Union[BackgroundAudioPredefinedMedia, BackgroundAudioMediaURL, BackgroundAudioMediaName],
    PropertyInfo(discriminator="type"),
]


class VoiceSettings(BaseModel):
    voice: str
    """The voice to be used by the voice assistant.

    Check the full list of
    [available voices](https://developers.telnyx.com/api/call-control/list-text-to-speech-voices)
    via our voices API. To use ElevenLabs, you must reference your ElevenLabs API
    key as an integration secret under the `api_key_ref` field. See
    [integration secrets documentation](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    for details. For Telnyx voices, use `Telnyx.<model_id>.<voice_id>` (e.g.
    Telnyx.KokoroTTS.af_heart)
    """

    api_key_ref: Optional[str] = None
    """
    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    that refers to your ElevenLabs API key. Warning: Free plans are unlikely to work
    with this integration.
    """

    background_audio: Optional[BackgroundAudio] = None
    """Optional background audio to play on the call.

    Use a predefined media bed, or supply a looped MP3 URL. If a media URL is chosen
    in the portal, customers can preview it before saving.
    """

    similarity_boost: Optional[float] = None
    """
    Determines how closely the AI should adhere to the original voice when
    attempting to replicate it. Only applicable when using ElevenLabs.
    """

    speed: Optional[float] = None
    """Adjusts speech velocity.

    1.0 is default speed; values less than 1.0 slow speech; values greater than 1.0
    accelerate it. Only applicable when using ElevenLabs.
    """

    style: Optional[float] = None
    """Determines the style exaggeration of the voice.

    Amplifies speaker style but consumes additional resources when set above 0. Only
    applicable when using ElevenLabs.
    """

    temperature: Optional[float] = None
    """Determines how stable the voice is and the randomness between each generation.

    Lower values create a broader emotional range; higher values produce more
    consistent, monotonous output. Only applicable when using ElevenLabs.
    """

    use_speaker_boost: Optional[bool] = None
    """Amplifies similarity to the original speaker voice.

    Increases computational load and latency slightly. Only applicable when using
    ElevenLabs.
    """

    voice_speed: Optional[float] = None
    """The speed of the voice in the range [0.25, 2.0].

    1.0 is deafult speed. Larger numbers make the voice faster, smaller numbers make
    it slower. This is only applicable for Telnyx Natural voices.
    """
