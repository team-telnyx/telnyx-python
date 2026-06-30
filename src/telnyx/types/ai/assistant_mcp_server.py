# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AssistantMcpServer"]


class AssistantMcpServer(BaseModel):
    """Reference to an MCP server attached to an assistant.

    Create and manage MCP servers with the `/ai/mcp_servers` endpoints, then attach them to assistants by ID.
    """

    id: str
    """ID of the MCP server to attach.

    This must be the `id` of an MCP server returned by the `/ai/mcp_servers`
    endpoints.
    """

    allowed_tools: Optional[List[str]] = None
    """Optional per-assistant allowlist of MCP tool names.

    When omitted, the assistant uses the MCP server's configured `allowed_tools`.
    """
