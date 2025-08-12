# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ElevenLabsVoiceSettingsParam"]


class ElevenLabsVoiceSettingsParam(TypedDict, total=False):
    api_key_ref: str
    """
    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your ElevenLabs API key. Warning: Free plans are unlikely to work
    with this integration.
    """
