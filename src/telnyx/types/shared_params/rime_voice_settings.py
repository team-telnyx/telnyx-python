# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RimeVoiceSettings"]


class RimeVoiceSettings(TypedDict, total=False):
    type: Required[Literal["rime"]]
    """Voice settings provider type"""

    api_key_ref: str
    """
    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Rime API key. Only required when using your own Rime
    account.
    """

    voice_speed: float
    """Speech speed multiplier. Default is 1.0."""
