# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .call_control_command_result import CallControlCommandResult

__all__ = ["ActionStopNoiseSuppressionResponse"]


class ActionStopNoiseSuppressionResponse(BaseModel):
    data: Optional[CallControlCommandResult] = None
