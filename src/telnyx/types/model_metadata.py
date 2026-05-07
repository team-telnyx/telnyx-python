# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ModelMetadata"]


class ModelMetadata(BaseModel):
    id: str

    created: int

    owned_by: str

    object: Optional[str] = None
