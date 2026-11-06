# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .agent_gateway_api import AgentGatewayAPI

__all__ = ["APIListResponse"]


class APIListResponse(BaseModel):
    data: List[AgentGatewayAPI]
