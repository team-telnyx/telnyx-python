# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["AgentGatewayShownAuth"]


class AgentGatewayShownAuth(BaseModel):
    """The server's outbound authentication method. Credentials are never returned."""

    type: str
    """The method's `type`."""
