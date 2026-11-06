# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentGatewayPassthroughAuthParam"]


class AgentGatewayPassthroughAuthParam(TypedDict, total=False):
    """
    The gateway forwards the agent's own `Authorization` header to the server unchanged.
    """

    type: Literal["passthrough"]
