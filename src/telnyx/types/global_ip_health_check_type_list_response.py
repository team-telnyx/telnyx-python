# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["GlobalIPHealthCheckTypeListResponse", "Data"]


class Data(BaseModel):
    health_check_params: Optional[Dict[str, object]] = None
    """Global IP Health check params."""

    health_check_type: Optional[str] = None
    """Global IP Health check type."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class GlobalIPHealthCheckTypeListResponse(BaseModel):
    data: Optional[List[Data]] = None
