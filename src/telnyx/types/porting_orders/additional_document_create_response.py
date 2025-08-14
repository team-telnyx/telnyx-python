# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AdditionalDocumentCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this additional document"""

    content_type: Optional[str] = None
    """The content type of the related document."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    document_id: Optional[str] = None
    """Identifies the associated document"""

    document_type: Optional[Literal["loa", "invoice", "csr", "other"]] = None
    """Identifies the type of additional document"""

    filename: Optional[str] = None
    """The filename of the related document."""

    porting_order_id: Optional[str] = None
    """Identifies the associated porting order"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class AdditionalDocumentCreateResponse(BaseModel):
    data: Optional[List[Data]] = None
