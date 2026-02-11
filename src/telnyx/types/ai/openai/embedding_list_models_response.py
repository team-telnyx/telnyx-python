# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["EmbeddingListModelsResponse", "Data"]


class Data(BaseModel):
    id: str
    """The model identifier"""

    created: int
    """Unix timestamp of when the model was created"""

    object: str
    """The object type, always 'model'"""

    owned_by: str
    """The organization that owns the model"""


class EmbeddingListModelsResponse(BaseModel):
    data: List[Data]
    """List of available embedding models"""

    object: str
    """The object type, always 'list'"""
