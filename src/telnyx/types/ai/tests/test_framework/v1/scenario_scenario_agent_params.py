# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ScenarioScenarioAgentParams", "Context"]


class ScenarioScenarioAgentParams(TypedDict, total=False):
    scenarios: Required[Union[Iterable[object], str]]
    """Scenario IDs to improve, or the literal string 'all'."""

    user_message: Required[str]
    """What the assistant should improve about the selected scenarios."""

    agent_id: Optional[int]

    agent_resolution_response: str

    apply_changes: bool

    context: Optional[Iterable[Context]]

    knowledge_base: Iterable[int]

    num_scenarios: int

    pending_tool_calls: Optional[Iterable[Dict[str, object]]]

    scenarios_needing_agent: Iterable[int]

    session_id: Optional[int]

    updated_scenarios: Iterable[Dict[str, object]]


class Context(TypedDict, total=False):
    content: str

    role: str

    timestamp: str
