# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .global_ip_assignment import GlobalIPAssignment

__all__ = ["GlobalIPAssignmentRetrieveResponse"]


class GlobalIPAssignmentRetrieveResponse(BaseModel):
    data: Optional[GlobalIPAssignment] = None
