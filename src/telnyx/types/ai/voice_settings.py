# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceSettings"]


class VoiceSettings(BaseModel):
    voice: str
    """The voice to be used by the voice assistant.

    Check the full list of
    [available voices](https://developers.telnyx.com/api/call-control/list-text-to-speech-voices)
    via our voices API. To use ElevenLabs, you must reference your ElevenLabs API
    key as an integration secret under the `api_key_ref` field. See
    [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    for details. For Telnyx voices, use `Telnyx.<model_id>.<voice_id>` (e.g.
    Telnyx.KokoroTTS.af_heart)
    """

    api_key_ref: Optional[str] = None
    """
    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your ElevenLabs API key. Warning: Free plans are unlikely to work
    with this integration.
    """

    voice_speed: Optional[float] = None
    """The speed of the voice in the range [0.25, 2.0].

    1.0 is deafult speed. Larger numbers make the voice faster, smaller numbers make
    it slower. This is only applicable for Telnyx Natural voices.
    """
