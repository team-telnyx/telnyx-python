# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .model_metadata import ModelMetadata

__all__ = ["ModelsResponse"]


class ModelsResponse(BaseModel):
    data: List[ModelMetadata]

    object: Optional[str] = None
