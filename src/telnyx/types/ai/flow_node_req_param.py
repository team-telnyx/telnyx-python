# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .node_position_param import NodePositionParam
from .voice_settings_param import VoiceSettingsParam
from .external_llm_req_param import ExternalLlmReqParam
from .transcription_settings_param import TranscriptionSettingsParam

__all__ = ["FlowNodeReqParam"]


class FlowNodeReqParam(TypedDict, total=False):
    """One step in a conversation flow, as supplied by API clients.

    Each node carries the prompt, tool scope, and optional overrides for
    model/voice/transcription. Unset overrides cascade from the assistant.
    """

    id: Required[str]
    """Caller-supplied unique identifier for this node within the flow."""

    instructions: Required[str]
    """Prompt that drives the LLM while this node is active. Required."""

    external_llm: ExternalLlmReqParam
    """Override for `Assistant.external_llm` while this node is active.

    Use this to route a node's turns to a different external LLM (different `model`,
    `base_url`, credentials). Part of the LLM bundle — see `model` for cascade
    semantics. Mutually exclusive with `model` on the node (a single LLM identity
    per node).
    """

    instructions_mode: Literal["replace", "append"]
    """How `instructions` combine with the assistant-level instructions.

    `replace` (default): the node's instructions are used alone. `append`: the
    node's instructions are concatenated after the assistant's instructions.
    """

    llm_api_key_ref: str
    """Override for `Assistant.llm_api_key_ref` while this node is active.

    Part of the LLM bundle — see `model` for cascade semantics.
    """

    model: str
    """Override for `Assistant.model` while this node is active.

    Part of the LLM bundle (`model` + `llm_api_key_ref` + `external_llm`): when any
    of the three is set on the node, all three are taken from the node and the
    assistant-level LLM identity is not consulted. When none of the three is set,
    the assistant's bundle cascades unchanged.
    """

    name: str
    """Optional human-readable label, displayed in authoring UIs."""

    position: NodePositionParam
    """Optional canvas coordinates used by authoring UIs to lay out the graph.

    Ignored by the runtime; round-trips so frontends can persist graph layout across
    reloads.
    """

    shared_tool_ids: SequenceNotStr[str]
    """IDs of shared (org-level) tools available at this node.

    Knowledge bases are attached the same way — via a shared retrieval tool. Tools
    not listed here are not callable while this node is active.
    """

    tools_mode: Literal["replace", "append"]
    """How `shared_tool_ids` combine with the assistant-level tool set.

    `replace` (default): only the node's tools are callable. `append`: the node's
    tools are added to the assistant's tools. Ignored when `shared_tool_ids` is
    null.
    """

    transcription: TranscriptionSettingsParam
    """Per-node transcription override (model/language/region).

    Unset fields cascade from the assistant-level transcription.
    """

    type: Literal["prompt"]
    """Node kind discriminator.

    `prompt` (default) is an LLM-driven step; `tool` is a standalone tool execution
    (see `ToolNodeReq`).
    """

    voice_settings: VoiceSettingsParam
    """Per-node voice override.

    Only fields set here override the assistant-level voice settings; unset fields
    cascade.
    """
