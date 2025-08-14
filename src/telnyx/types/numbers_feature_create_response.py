# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["NumbersFeatureCreateResponse", "Data"]


class Data(BaseModel):
    features: List[str]

    phone_number: str


class NumbersFeatureCreateResponse(BaseModel):
    data: Optional[List[Data]] = None
