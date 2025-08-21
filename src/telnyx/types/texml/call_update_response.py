# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallUpdateResponse", "Data"]


class Data(BaseModel):
    sid: Optional[str] = None

    status: Optional[str] = None


class CallUpdateResponse(BaseModel):
    data: Optional[Data] = None
