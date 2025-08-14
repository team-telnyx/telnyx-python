# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["RcsAgent"]


class RcsAgent(BaseModel):
    agent_id: Optional[str] = None
    """RCS Agent ID"""

    agent_name: Optional[str] = None
    """Human readable agent name"""

    created_at: Optional[datetime] = None
    """Date and time when the resource was created"""

    enabled: Optional[bool] = None
    """Specifies whether the agent is enabled"""

    profile_id: Optional[str] = None
    """Messaging profile ID associated with the RCS Agent"""

    updated_at: Optional[datetime] = None
    """Date and time when the resource was updated"""

    user_id: Optional[str] = None
    """User ID associated with the RCS Agent"""

    webhook_failover_url: Optional[str] = None
    """Failover URL to receive RCS events"""

    webhook_url: Optional[str] = None
    """URL to receive RCS events"""
