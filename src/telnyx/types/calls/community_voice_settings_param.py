# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommunityVoiceSettingsParam"]


class CommunityVoiceSettingsParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Settings for a community text-to-speech engine voice (`<EngineName>.<VoiceId>`).

    `api_key_ref` is required. Every other key is a setting the engine declares in its `voice_settings_schema`, and is passed to the engine as sent. See the [Community TTS engines guide](/docs/voice/tts/community-engines).
    """

    api_key_ref: Required[str]
    """The `identifier` of an integration secret that holds your key for the engine.

    See
    [integration secrets documentation](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    for details.
    """
