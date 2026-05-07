# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AIRetrieveModelsResponse", "Data"]


class Data(BaseModel):
    id: str

    created: int

    owned_by: str

    object: Optional[str] = None


class AIRetrieveModelsResponse(BaseModel):
    data: List[Data]

    object: Optional[str] = None
