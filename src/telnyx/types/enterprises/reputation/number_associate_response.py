# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["NumberAssociateResponse", "Data", "Meta"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    created_at: Optional[datetime] = None
    """When the number was associated"""

    enterprise_id: Optional[str] = None
    """ID of the associated enterprise"""

    phone_number: Optional[str] = None
    """Phone number in E.164 format"""

    updated_at: Optional[datetime] = None
    """When the record was last updated"""


class Meta(BaseModel):
    page_number: Optional[int] = None
    """Current page number"""

    page_size: Optional[int] = None
    """Items per page"""

    total_pages: Optional[int] = None
    """Total number of pages"""

    total_results: Optional[int] = None
    """Total number of results"""


class NumberAssociateResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
