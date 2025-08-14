# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionUnholdResponse", "Data"]


class Data(BaseModel):
    result: str


class ActionUnholdResponse(BaseModel):
    data: Optional[Data] = None
