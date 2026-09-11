# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["OpenAICreateResponseParams", "Reasoning"]


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

    mode: Literal["preferred", "strict"]
    """How strictly `region` is applied.

    `preferred` (the default when `region` is set) tries that region first and falls
    back to another when the model cannot be served there, so a request that would
    have succeeded still succeeds. `strict` pins the request: it is served from that
    region or it fails with a 422, never redirected to another region. Requires
    `region`.
    """

    model: str
    """
    Model identifier to use for the response, for example `zai-org/GLM-5.1-FP8` or
    another model available from the Telnyx OpenAI-compatible models endpoint.
    """

    reasoning: Reasoning

    region: Literal["USA", "EU", "AUS", "UAE"]
    """
    Optional data-residency region the request should be served from, using the same
    vocabulary as your account's Data Locality setting. Behavior depends on `mode`.
    Supported for Telnyx-hosted models only: a request routed to an external
    provider never passes through Telnyx model routing, so a region cannot be
    enforced for it. Omit for today's latency-based routing.
    """

    service_tier: str
    """The service tier to use for this request.

    Supported values vary by model; use `GET /v2/ai/openai/models` and inspect the
    model's `service_tiers` field. If omitted, Telnyx-hosted models use `default`.
    """

    stream: bool
    """
    Set to `true` to stream Server-Sent Events, matching OpenAI's Responses
    streaming format.
    """


class Reasoning(TypedDict, total=False):
    effort: Literal["none", "minimal", "low", "medium", "high", "xhigh", "max"]
    """Controls the reasoning effort for models that support it.

    Same values and semantics as reasoning_effort on Chat Completions.
    """
