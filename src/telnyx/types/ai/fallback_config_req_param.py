# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .external_llm_req_param import ExternalLlmReqParam

__all__ = ["FallbackConfigReqParam"]


class FallbackConfigReqParam(TypedDict, total=False):
    external_llm: ExternalLlmReqParam

    llm_api_key_ref: str
    """Integration secret identifier for the fallback model API key."""

    model: str
    """
    Fallback Telnyx-hosted model to use when the primary LLM provider is
    unavailable.
    """
