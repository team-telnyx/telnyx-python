# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    profile_id: Optional[str]
    """Messaging profile ID associated with the RCS Agent"""

    webhook_failover_url: Optional[str]
    """Failover URL to receive RCS events"""

    webhook_url: Optional[str]
    """URL to receive RCS events"""
