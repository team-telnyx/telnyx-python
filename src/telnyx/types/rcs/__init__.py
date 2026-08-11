# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .rcs_agent import RcsAgent as RcsAgent
    from .rcs_agent_response import RcsAgentResponse as RcsAgentResponse


def __getattr__(name: str) -> Any:
    if name == "RcsAgent":
        from .rcs_agent import RcsAgent

        return RcsAgent
    if name == "RcsAgentResponse":
        from .rcs_agent_response import RcsAgentResponse

        return RcsAgentResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
