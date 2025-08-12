# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CommentListResponse", "Data", "Meta"]


class Data(BaseModel):
    id: str

    body: str
    """Comment body"""

    created_at: str
    """Comment creation timestamp in ISO 8601 format"""

    user_id: str
    """Identifies the user who created the comment.

    Will be null if created by Telnyx Admin
    """

    portout_id: Optional[str] = None
    """Identifies the associated port request"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class Meta(BaseModel):
    page_number: Optional[float] = None
    """Current Page based on pagination settings (included when defaults are used.)"""

    page_size: Optional[float] = None
    """
    Number of results to return per page based on pagination settings (included when
    defaults are used.)
    """

    total_pages: Optional[float] = None
    """Total number of pages based on pagination settings"""

    total_results: Optional[float] = None
    """Total number of results"""


class CommentListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
