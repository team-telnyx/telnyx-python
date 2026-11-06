# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentGatewayRetrieveSpendLogsResponse", "Data", "Meta"]


class Data(BaseModel):
    """One request the instance served."""

    id: str
    """The request's ID."""

    completion_tokens: int
    """Output tokens, reasoning included."""

    duration_ms: Optional[int] = None
    """How long the request took, in milliseconds."""

    ended_at: Optional[datetime] = None
    """When the request ended."""

    key_id: Optional[str] = None
    """The key the request used."""

    model: Optional[str] = None
    """The Telnyx Inference model that answered, such as `zai-org/GLM-5.3-Flash`.

    For an MCP tool request, `MCP: ` and the tool's name.
    """

    operation: str
    """The request type.

    `acompletion` is a chat completion, `aresponses` a response,
    `anthropic_messages` a message, `call_mcp_tool` an MCP tool request, and
    `list_mcp_tools` an MCP tool list.
    """

    prompt_tokens: int
    """Input tokens."""

    spend: float
    """What the request cost, in USD, with its tokens at Telnyx Inference prices."""

    started_at: datetime
    """When the request started."""

    status: Optional[str] = None
    """`success` or `failure`."""

    team_id: Optional[str] = None
    """The key's team."""

    total_tokens: int
    """Input and output tokens."""


class Meta(BaseModel):
    page_number: int
    """The page returned, counting from 1."""

    page_size: int
    """Results per page."""

    total_pages: int
    """Pages that can be requested; 0 when nothing matched."""

    total_results: int
    """Results across every page."""

    total_results_capped: bool
    """`true` when the window holds more than 10,000 rows.

    The two totals are then lower bounds: narrow the window, or page until a page
    comes back empty.
    """


class AgentGatewayRetrieveSpendLogsResponse(BaseModel):
    data: List[Data]

    meta: Meta
