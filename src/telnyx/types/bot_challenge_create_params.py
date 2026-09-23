# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BotChallengeCreateParams"]


class BotChallengeCreateParams(TypedDict, total=False):
    llm_model_name: str
    """Name of the LLM the client is using."""

    llm_parameter_count: str
    """Parameter count of the client LLM."""

    llm_quantization: str
    """Quantization of the client LLM."""
