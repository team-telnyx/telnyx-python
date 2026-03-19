# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoiceCloneCreateFromDesignParams"]


class VoiceCloneCreateFromDesignParams(TypedDict, total=False):
    gender: Required[Literal["male", "female", "neutral"]]
    """Gender of the voice clone."""

    language: Required[str]
    """ISO 639-1 language code for the clone (e.g. `en`, `fr`, `de`)."""

    name: Required[str]
    """Name for the voice clone."""

    voice_design_id: Required[str]
    """UUID of the source voice design to clone."""
