# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AgentGatewayToolPermissions", "Server"]


class Server(BaseModel):
    id: str
    """An MCP server's or API's `id` on the instance."""

    tools: Optional[List[str]] = None
    """The tools the grant covers, by name without the server prefix.

    `[]` covers every tool the server exposes.
    """


class AgentGatewayToolPermissions(BaseModel):
    servers: List[Server]
    """The servers granted, each with its tools. `[]` grants none."""
