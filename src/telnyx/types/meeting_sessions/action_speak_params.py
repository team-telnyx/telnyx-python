# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionSpeakParams"]


class ActionSpeakParams(TypedDict, total=False):
    text: Required[str]
    """Text for the bot to speak."""

    interrupt: bool
    """If true, interrupt any currently playing audio to speak this text immediately."""

    voice: str
    """Voice identifier to use for this utterance.

    When supplied, it overrides the session-default voice configured at creation;
    otherwise the speak action uses that session default.
    """
