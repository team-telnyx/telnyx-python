# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocServiceDocument", "Size"]


class Size(BaseModel):
    amount: Optional[int] = None
    """The number of bytes"""

    unit: Optional[str] = None
    """Identifies the unit"""


class DocServiceDocument(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    content_type: Optional[str] = None
    """The document's content_type."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """Optional reference string for customer tracking."""

    filename: Optional[str] = None
    """The filename of the document."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    sha256: Optional[str] = None
    """The document's SHA256 hash provided for optional verification purposes."""

    size: Optional[Size] = None
    """Indicates the document's filesize"""

    status: Optional[Literal["pending", "verified", "denied"]] = None
    """Indicates the current document reviewing status"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""
