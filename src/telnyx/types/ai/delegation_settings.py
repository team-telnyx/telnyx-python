# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .external_llm import ExternalLlm

__all__ = ["DelegationSettings"]


class DelegationSettings(BaseModel):
    """
    Splits the conversation between a frontend model that talks to the caller and a backend model that does the work. On the GPT-Live route the frontend model cannot call tools at all — when it needs something done it raises a delegation and waits. On the chat completion route the frontend keeps a single `delegate` tool that returns immediately, so the conversation carries on while the backend works. Either way the backend's answer is spoken as commentary or kept as silent context, depending on `speak_results`. Beta feature.
    """

    enabled: Optional[bool] = None
    """Whether the assistant delegates work to a backend model.

    Defaults to `true`: a GPT-Live assistant with delegation disabled can hold a
    conversation but can never look anything up or run a tool.
    """

    external_llm: Optional[ExternalLlm] = None
    """
    Run the backend on your own OpenAI-compatible endpoint instead of a
    Telnyx-hosted model. As above, a raw `api_key` here is rejected — reference an
    integration secret with `external_llm.llm_api_key_ref` instead.
    """

    instructions: Optional[str] = None
    """Extra instructions for the backend model, in addition to the assistant's own.

    Use this for the business rules the backend needs and the talking model does
    not.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the backend model's API key.

    Required for models from providers other than Telnyx, OpenAI and Anthropic. A
    raw `api_key` is rejected rather than ignored, so that no plaintext credential
    is stored on the assistant.
    """

    mode: Optional[Literal["telnyx", "client"]] = None
    """Who answers a delegation.

    `telnyx` runs the backend model on Telnyx with the assistant's own tools, MCP
    servers and observability. `client` relays the delegation to a server you host
    over the WebSocket configured in `websocket_settings`: Telnyx sends a
    `session.delegation.created` frame and waits for your
    `session.delegation.completed` answer. That answer is text only, since the
    socket offers no tool vocabulary. If no socket is connected the delegation is
    refused and the assistant tells the caller it cannot look things up right now.
    Defaults to `telnyx`.
    """

    model: Optional[str] = None
    """The backend model that answers delegations.

    Must be a model available for AI Assistants. When enabling `telnyx` delegation,
    explicitly set this field or `external_llm.model`; a configuration without
    either backend model is rejected. Only applies when `mode` is `telnyx`.
    """

    speak_results: Optional[bool] = None
    """Whether the backend's answer is spoken to the caller.

    When `true` the result is appended as commentary and paraphrased aloud; when
    `false` it is kept as silent context that informs later answers without being
    read out. Defaults to `true`.
    """
