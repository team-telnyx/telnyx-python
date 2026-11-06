# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .agent_gateway_shown_auth import AgentGatewayShownAuth

__all__ = ["AgentGatewayMcpServer"]


class AgentGatewayMcpServer(BaseModel):
    id: str
    """Identifies the server."""

    auth: AgentGatewayShownAuth
    """The server's outbound authentication method. Credentials are never returned."""

    created_at: Optional[datetime] = None

    forwarded_headers: List[str]
    """Headers copied from the agent's request, by name."""

    name: str
    """
    A name for the server, unique on the instance across MCP servers and APIs,
    regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
    server's tools with it and a hyphen.
    """

    open_to_every_key: bool
    """`true` lets every key on the instance use the server, granted or not."""

    static_headers: Dict[str, str]
    """Headers sent on every request."""

    tools: List[str]
    """The tools the server exposes to every key, by name. `[]` exposes every tool."""

    transport: Literal["http", "sse"]
    """`http` for Streamable HTTP, or `sse` for Server-Sent Events."""

    updated_at: Optional[datetime] = None

    url: str
    """The server's MCP endpoint."""
