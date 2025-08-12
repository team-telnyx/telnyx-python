# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RcsCapabilities"]


class RcsCapabilities(BaseModel):
    agent_id: Optional[str] = None
    """RCS agent ID"""

    agent_name: Optional[str] = None
    """RCS agent name"""

    features: Optional[List[str]] = None
    """List of RCS capabilities"""

    phone_number: Optional[str] = None
    """Phone number"""

    record_type: Optional[Literal["rcs.capabilities"]] = None
    """Identifies the type of the resource"""
