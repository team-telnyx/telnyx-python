# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ModelMetadata"]


class ModelMetadata(BaseModel):
    """Metadata for a model available on Telnyx Inference.

    Returned by `GET /v2/ai/openai/models` (and the deprecated `GET /v2/ai/models`). Open-source models live under their Hugging Face organization (e.g. `moonshotai/Kimi-K2.6`, `zai-org/GLM-5.1-FP8`, `MiniMaxAI/MiniMax-M2.7`); fine-tuned models are owned by the Telnyx organization that trained them.
    """

    id: str
    """Model identifier.

    For open-source models, follows the `{organization}/{model_name}` convention
    from Hugging Face (e.g. `moonshotai/Kimi-K2.6`).
    """

    context_length: int
    """
    Maximum total tokens (prompt + completion) supported by the model in a single
    request.
    """

    created: datetime
    """Timestamp at which the model was registered on Telnyx Inference (ISO 8601)."""

    languages: List[str]
    """ISO language codes the model supports (e.g. `en`, `es`)."""

    license: str
    """License the model is distributed under, e.g.

    `Apache 2.0`, `MIT`, `Llama 3 Community License`.
    """

    organization: str
    """
    Organization that originally published the model, matching the prefix of `id`
    for open-source models.
    """

    owned_by: str
    """Owner of the model.

    `Telnyx` for Telnyx-hosted open-source models, the upstream provider name for
    proxied models, or the Telnyx organization id for fine-tuned models.
    """

    parameters: int
    """Total parameter count of the model."""

    tier: Literal["small", "medium", "large", "unlisted"]
    """Billing tier the model belongs to.

    Used together with `pricing` to determine cost per 1M tokens.
    """

    base_model: Optional[str] = None
    """Base model the fine-tuned model was trained from.

    Only set for fine-tuned models.
    """

    description: Optional[str] = None
    """Short, human-readable summary of what the model is best suited for."""

    is_fine_tunable: Optional[bool] = None
    """
    Whether the model can be used as a base for a fine-tuning job via
    `POST /v2/ai/fine_tuning/jobs`.
    """

    is_vision_supported: Optional[bool] = None
    """
    Whether the model accepts image inputs in chat completions (multimodal vision
    support).
    """

    max_completion_tokens: Optional[int] = None
    """Maximum number of completion (output) tokens the model will generate per
    request.

    `null` if unconstrained beyond `context_length`.
    """

    object: Optional[str] = None
    """Object type. Always `model`."""

    parameters_str: Optional[str] = None
    """Human-readable parameter count, e.g. `1.0T`, `753.9B`, `8B`."""

    pricing: Optional[Dict[str, str]] = None
    """Mapping of token kind to price, as strings to preserve precision.

    Typical keys are `prompt`, `cached_prompt`, and `completion`. When pricing is
    available the block also includes `currency` (ISO 4217 code matching the
    account's configured billing currency) and `unit` (the denomination the prices
    are quoted in, currently always `1M_tokens` for token-priced models).
    """

    recommended_for_assistants: Optional[bool] = None
    """
    Whether Telnyx currently recommends this model as the LLM powering a Telnyx AI
    Assistant.
    """

    regions: Optional[List[str]] = None
    """Public region names where the model is currently deployed (e.g.

    `us-central-1`, `eu-central-1`).
    """

    task: Optional[str] = None
    """Primary task the model is intended for, e.g.

    `text-generation`, `audio-text-to-text`, `feature-extraction` (embeddings).
    """
