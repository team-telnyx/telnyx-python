# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["OpenAICreateResponseParams"]


class OpenAICreateResponseParams(TypedDict, total=False):
    conversation: str
    """Optional Telnyx Conversation ID from `POST /ai/conversations`.

    When provided, Telnyx stores this turn on that conversation and uses the
    conversation's prior messages as context. Reuse the same ID for subsequent turns
    and tool-result followups. Omit it for a non-persisted, stateless response.
    """

    input: Dict[str, object]
    """The input items for this turn, using the OpenAI Responses API input format."""

    instructions: str
    """Optional system/developer instructions for the model.

    When used with a persisted `conversation`, send these on the first request that
    creates the thread; subsequent turns can rely on the stored history.
    """

    model: str
    """
    Model identifier to use for the response, for example `zai-org/GLM-5.1-FP8` or
    another model available from the Telnyx OpenAI-compatible models endpoint.
    """

    stream: bool
    """
    Set to `true` to stream Server-Sent Events, matching OpenAI's Responses
    streaming format.
    """
