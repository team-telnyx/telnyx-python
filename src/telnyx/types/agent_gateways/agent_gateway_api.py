# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .agent_gateway_shown_auth import AgentGatewayShownAuth

__all__ = ["AgentGatewayAPI"]


class AgentGatewayAPI(BaseModel):
    id: str
    """Identifies the API."""

    auth: AgentGatewayShownAuth
    """The server's outbound authentication method. Credentials are never returned."""

    base_url: Optional[str] = None
    """Where the gateway sends the API's requests.

    `null` takes the description's first `servers` entry.
    """

    created_at: Optional[datetime] = None

    forwarded_headers: List[str]
    """Headers copied from the agent's request, by name."""

    name: str
    """
    A name for the API, unique on the instance across MCP servers and APIs,
    regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
    API's tools with it and a hyphen.
    """

    open_to_every_key: bool
    """`true` lets every key on the instance use the server, granted or not."""

    spec_url: str
    """The URL of the API's OpenAPI description."""

    static_headers: Dict[str, str]
    """Headers sent on every request."""

    tools: List[str]
    """The operations the API exposes as tools, by tool name.

    `[]` exposes every operation.
    """

    updated_at: Optional[datetime] = None
