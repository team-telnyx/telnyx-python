# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .global_ip_health_check import GlobalIPHealthCheck

__all__ = ["GlobalIPHealthCheckDeleteResponse"]


class GlobalIPHealthCheckDeleteResponse(BaseModel):
    data: Optional[GlobalIPHealthCheck] = None
