# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VoicemailCreateParams"]


class VoicemailCreateParams(TypedDict, total=False):
    enabled: bool
    """Whether voicemail is enabled."""

    pin: str
    """The pin used for voicemail"""
