# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionUnmuteResponse", "Data"]


class Data(BaseModel):
    result: str


class ActionUnmuteResponse(BaseModel):
    data: Optional[Data] = None
