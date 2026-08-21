# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .external_llm import ExternalLlm
from .node_position import NodePosition
from .assistant_tool import AssistantTool
from .voice_settings import VoiceSettings
from .transcription_settings import TranscriptionSettings

__all__ = ["FlowNode"]


class FlowNode(BaseModel):
    """One step in a conversation flow, as returned by the API."""

    id: str
    """Caller-supplied unique identifier for this node within the flow."""

    instructions: str
    """Prompt that drives the LLM while this node is active. Required."""

    external_llm: Optional[ExternalLlm] = None
    """Override for `Assistant.external_llm` while this node is active.

    Use this to route a node's turns to a different external LLM (different `model`,
    `base_url`, credentials). Part of the LLM bundle — see `model` for cascade
    semantics. Mutually exclusive with `model` on the node (a single LLM identity
    per node).
    """

    instructions_mode: Optional[Literal["replace", "append"]] = None
    """How `instructions` combine with the assistant-level instructions.

    `replace` (default): the node's instructions are used alone. `append`: the
    node's instructions are concatenated after the assistant's instructions.
    """

    llm_api_key_ref: Optional[str] = None
    """Override for `Assistant.llm_api_key_ref` while this node is active.

    Part of the LLM bundle — see `model` for cascade semantics.
    """

    model: Optional[str] = None
    """Override for `Assistant.model` while this node is active.

    Part of the LLM bundle (`model` + `llm_api_key_ref` + `external_llm`): when any
    of the three is set on the node, all three are taken from the node and the
    assistant-level LLM identity is not consulted. When none of the three is set,
    the assistant's bundle cascades unchanged.
    """

    name: Optional[str] = None
    """Optional human-readable label, displayed in authoring UIs."""

    position: Optional[NodePosition] = None
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    shared_tool_ids: Optional[List[str]] = None
    """IDs of shared (org-level) tools available at this node.

    Knowledge bases are attached the same way — via a shared retrieval tool. Tools
    not listed here are not callable while this node is active.
    """

    tools: Optional[List[List[AssistantTool]]] = None
    """Full tool definitions for this node, resolved from `shared_tool_ids`
    server-side.

    Populated on responses so clients can render the flow without a follow-up fetch
    per shared tool. Ignored on input — set `shared_tool_ids` to configure a node's
    tools.
    """

    tools_mode: Optional[Literal["replace", "append"]] = None
    """How `shared_tool_ids` combine with the assistant-level tool set.

    `replace` (default): only the node's tools are callable. `append`: the node's
    tools are added to the assistant's tools. Ignored when `shared_tool_ids` is
    null.
    """

    transcription: Optional[TranscriptionSettings] = None
    """Per-node transcription override (response form)."""

    type: Optional[Literal["prompt"]] = None
    """Node kind discriminator. `prompt` is an LLM-driven step."""

    voice_settings: Optional[VoiceSettings] = None
    """Per-node voice override (response form)."""
