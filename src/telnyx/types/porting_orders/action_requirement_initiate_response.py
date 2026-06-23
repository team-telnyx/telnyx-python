# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .porting_action_requirement import PortingActionRequirement

__all__ = ["ActionRequirementInitiateResponse"]


class ActionRequirementInitiateResponse(BaseModel):
    data: Optional[PortingActionRequirement] = None
