# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActionEnqueueResponse", "Data"]


class Data(BaseModel):
    result: Optional[str] = None


class ActionEnqueueResponse(BaseModel):
    data: Optional[Data] = None
