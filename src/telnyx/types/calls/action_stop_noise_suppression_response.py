# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionStopNoiseSuppressionResponse", "Data"]


class Data(BaseModel):
    result: Optional[str] = None


class ActionStopNoiseSuppressionResponse(BaseModel):
    data: Optional[Data] = None
