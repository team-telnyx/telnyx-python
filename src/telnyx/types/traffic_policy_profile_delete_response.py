# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TrafficPolicyProfileDeleteResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""


class TrafficPolicyProfileDeleteResponse(BaseModel):
    data: Optional[Data] = None
