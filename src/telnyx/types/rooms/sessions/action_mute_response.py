# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ActionMuteResponse", "Data"]


class Data(BaseModel):
    result: Optional[str] = None


class ActionMuteResponse(BaseModel):
    data: Optional[Data] = None
