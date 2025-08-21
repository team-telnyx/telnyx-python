# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_control_application import CallControlApplication

__all__ = ["CallControlApplicationDeleteResponse"]


class CallControlApplicationDeleteResponse(BaseModel):
    data: Optional[CallControlApplication] = None
