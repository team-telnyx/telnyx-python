# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InworldVoiceSettings"]


class InworldVoiceSettings(TypedDict, total=False):
    type: Required[Literal["inworld"]]
    """Voice settings provider type"""

    delivery_mode: Literal["STABLE", "BALANCED", "CREATIVE"]
    """
    Controls the expressiveness and consistency of the Inworld `TTS2` model's speech
    synthesis. `STABLE` favors consistent, predictable output, `CREATIVE` allows
    more expressive variation, and `BALANCED` sits in between. Optional and only
    supported by `TTS2`; when omitted, the provider default applies.
    """
