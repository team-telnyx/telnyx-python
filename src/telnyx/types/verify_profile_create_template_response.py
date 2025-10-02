# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VerifyProfileCreateTemplateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    text: Optional[str] = None


class VerifyProfileCreateTemplateResponse(BaseModel):
    data: Optional[Data] = None
