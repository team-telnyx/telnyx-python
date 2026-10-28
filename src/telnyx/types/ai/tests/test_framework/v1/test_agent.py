# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime

from ......_models import BaseModel

__all__ = ["TestAgent"]


class TestAgent(BaseModel):
    __test__ = False
    id: int

    agent_name: str
    """Name of the test agent."""

    assistant_id: str
    """ID of the Telnyx AI assistant under test."""

    created_at: datetime

    updated_at: datetime

    auto_update_dropoff_nodes: Optional[bool] = None

    auto_update_topic_nodes: Optional[bool] = None

    chat_assistant_id: Optional[str] = None
    """ID of the chat assistant under test, when testing text channels."""

    contact_number: Optional[str] = None
    """Contact phone number for the test agent."""

    description: Optional[str] = None

    enabled_personalities: Optional[List[int]] = None
    """IDs of the test personalities enabled for this agent."""

    hallucination_metric_kb_files: Optional[List[int]] = None

    inbound: Optional[bool] = None
    """Whether the test agent accepts inbound calls."""

    knowledge_base_files: Optional[List[object]] = None
    """Knowledge-base files associated with the test agent."""

    language: Optional[str] = None
    """ISO language code the test agent converses in."""

    llm_max_tokens: Optional[int] = None

    llm_model: Optional[str] = None
    """Model used to drive the test agent's side of the conversation."""

    llm_system_prompt: Optional[str] = None

    llm_temperature: Optional[float] = None

    outbound_auto_call: Optional[bool] = None

    outbound_numbers: Optional[List[object]] = None
    """Outbound numbers associated with the test agent."""

    sip_auth: Optional[Dict[str, str]] = None

    sip_endpoint: Optional[str] = None
