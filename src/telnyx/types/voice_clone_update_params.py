# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VoiceCloneUpdateParams"]


class VoiceCloneUpdateParams(TypedDict, total=False):
    name: Required[str]
    """New name for the voice clone."""

    gender: Literal["male", "female", "neutral"]
    """Updated gender for the voice clone."""

    language: str
    """Updated ISO 639-1 language code or `auto`."""
