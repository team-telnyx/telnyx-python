# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .doc_service_record import DocServiceRecord

__all__ = ["DocServiceDocument", "DocServiceDocumentSize"]


class DocServiceDocumentSize(BaseModel):
    """Indicates the document's filesize"""

    amount: Optional[int] = None
    """The number of bytes"""

    unit: Optional[str] = None
    """Identifies the unit"""


class DocServiceDocument(DocServiceRecord):
    av_scan_status: Optional[Literal["scanned", "infected", "pending_scan", "not_scanned"]] = None
    """The antivirus scan status of the document."""

    content_type: Optional[str] = None
    """The document's content_type."""

    customer_reference: Optional[str] = None
    """Optional reference string for customer tracking."""

    filename: Optional[str] = None
    """The filename of the document."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    sha256: Optional[str] = None
    """The document's SHA256 hash provided for optional verification purposes."""

    size: Optional[DocServiceDocumentSize] = None
    """Indicates the document's filesize"""

    status: Optional[Literal["pending", "verified", "denied"]] = None
    """Indicates the current document reviewing status"""
