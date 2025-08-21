# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DialogflowConfigParam"]


class DialogflowConfigParam(TypedDict, total=False):
    analyze_sentiment: bool
    """Enable sentiment analysis from Dialogflow."""

    partial_automated_agent_reply: bool
    """Enable partial automated agent reply from Dialogflow."""
