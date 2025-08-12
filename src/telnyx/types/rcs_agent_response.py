# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .rcs_agent import RcsAgent

__all__ = ["RcsAgentResponse"]


class RcsAgentResponse(BaseModel):
    data: Optional[RcsAgent] = None
