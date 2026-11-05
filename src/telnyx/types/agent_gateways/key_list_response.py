# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .agent_gateway_key import AgentGatewayKey

__all__ = ["KeyListResponse"]


class KeyListResponse(BaseModel):
    data: List[AgentGatewayKey]
