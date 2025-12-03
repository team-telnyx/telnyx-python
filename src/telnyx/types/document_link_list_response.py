# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["DocumentLinkListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    document_id: Optional[str] = None
    """Identifies the associated document."""

    linked_record_type: Optional[str] = None
    """The linked resource's record type."""

    linked_resource_id: Optional[str] = None
    """Identifies the linked resource."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class DocumentLinkListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
