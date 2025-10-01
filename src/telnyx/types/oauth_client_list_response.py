# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .oauth_client import OAuthClient

__all__ = ["OAuthClientListResponse", "Meta"]


class Meta(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Number of items per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    total_results: Optional[int] = None
    """Total number of results"""


class OAuthClientListResponse(BaseModel):
    data: Optional[List[OAuthClient]] = None

    meta: Optional[Meta] = None
