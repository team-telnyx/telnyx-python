# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RimeVoiceSettings"]


class RimeVoiceSettings(BaseModel):
    type: Literal["rime"]
    """Voice settings provider type"""

    api_key_ref: Optional[str] = None
    """
    The `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Rime API key. Only required when using your own Rime
    account.
    """

    voice_speed: Optional[float] = None
    """Speech speed multiplier. Default is 1.0."""
