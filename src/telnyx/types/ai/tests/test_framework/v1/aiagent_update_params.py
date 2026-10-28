# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AiagentUpdateParams"]


class AiagentUpdateParams(TypedDict, total=False):
    agent_name: str
    """Name of the test agent."""

    assistant_id: str
    """ID of the Telnyx AI assistant under test."""

    auto_fetch_calls_enabled: bool

    auto_sync_prompt_enabled: bool

    auto_update_dropoff_nodes: bool

    auto_update_topic_nodes: bool

    contact_number: str

    description: str

    inbound: bool

    language: str
    """ISO language code the test agent converses in."""

    llm_max_tokens: int

    llm_model: str

    llm_system_prompt: str

    llm_temperature: float

    outbound_auto_call: bool

    sip_endpoint: str
