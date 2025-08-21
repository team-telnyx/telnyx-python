# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .media_resource import MediaResource

__all__ = ["MediaUpdateResponse"]


class MediaUpdateResponse(BaseModel):
    data: Optional[MediaResource] = None
