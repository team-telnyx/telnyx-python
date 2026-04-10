# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .check_availability_tool_params import CheckAvailabilityToolParams

__all__ = ["CheckAvailabilityTool"]


class CheckAvailabilityTool(BaseModel):
    check_availability: CheckAvailabilityToolParams

    type: Literal["check_availability"]
