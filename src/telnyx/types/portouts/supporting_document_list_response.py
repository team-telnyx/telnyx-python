# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SupportingDocumentListResponse", "Data"]


class Data(BaseModel):
    id: str

    created_at: str
    """Supporting document creation timestamp in ISO 8601 format"""

    document_id: str
    """Identifies the associated document"""

    portout_id: str
    """Identifies the associated port request"""

    record_type: str
    """Identifies the type of the resource."""

    type: Literal["loa", "invoice"]
    """Identifies the type of the document"""

    updated_at: str
    """Supporting document last changed timestamp in ISO 8601 format"""


class SupportingDocumentListResponse(BaseModel):
    data: Optional[List[Data]] = None
