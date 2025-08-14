# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionStopStreamingResponse", "Data"]


class Data(BaseModel):
    result: Optional[str] = None


class ActionStopStreamingResponse(BaseModel):
    data: Optional[Data] = None
