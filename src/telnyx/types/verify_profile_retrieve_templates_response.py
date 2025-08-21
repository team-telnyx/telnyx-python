# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VerifyProfileRetrieveTemplatesResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    text: Optional[str] = None


class VerifyProfileRetrieveTemplatesResponse(BaseModel):
    data: List[Data]
