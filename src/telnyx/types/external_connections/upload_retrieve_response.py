# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .upload import Upload
from ..._models import BaseModel

__all__ = ["UploadRetrieveResponse"]


class UploadRetrieveResponse(BaseModel):
    data: Optional[Upload] = None
