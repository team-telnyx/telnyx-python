# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .external_llm import ExternalLlm

__all__ = ["FallbackConfig"]


class FallbackConfig(BaseModel):
    external_llm: Optional[ExternalLlm] = None

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the fallback model API key."""

    model: Optional[str] = None
    """
    Fallback Telnyx-hosted model to use when the primary LLM provider is
    unavailable.
    """
