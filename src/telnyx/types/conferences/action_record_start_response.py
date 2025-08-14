# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionRecordStartResponse", "Data"]


class Data(BaseModel):
    result: str


class ActionRecordStartResponse(BaseModel):
    data: Optional[Data] = None
