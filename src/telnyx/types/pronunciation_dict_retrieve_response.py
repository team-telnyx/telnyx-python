# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .pronunciation_dict_data import PronunciationDictData

__all__ = ["PronunciationDictRetrieveResponse"]


class PronunciationDictRetrieveResponse(BaseModel):
    """Response containing a single pronunciation dictionary."""

    data: Optional[PronunciationDictData] = None
    """A pronunciation dictionary record."""
