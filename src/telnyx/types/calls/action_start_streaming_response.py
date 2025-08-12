# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionStartStreamingResponse", "Data"]


class Data(BaseModel):
    result: Optional[str] = None


class ActionStartStreamingResponse(BaseModel):
    data: Optional[Data] = None
