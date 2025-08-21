# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["BucketCreatePresignedURLResponse", "Content"]


class Content(BaseModel):
    token: Optional[str] = None
    """The token for the object"""

    expires_at: Optional[datetime] = None
    """The expiration time of the token"""

    presigned_url: Optional[str] = None
    """The presigned URL for the object"""


class BucketCreatePresignedURLResponse(BaseModel):
    content: Optional[Content] = None
