# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionStopRecordingResponse", "Data"]


class Data(BaseModel):
    result: Optional[str] = None


class ActionStopRecordingResponse(BaseModel):
    data: Optional[Data] = None
