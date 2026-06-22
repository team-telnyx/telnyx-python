# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .doc_service_record import DocServiceRecord

__all__ = ["DocumentLinkListResponse"]


class DocumentLinkListResponse(DocServiceRecord):
    document_id: Optional[str] = None
    """Identifies the associated document."""

    linked_record_type: Optional[str] = None
    """The linked resource's record type."""

    linked_resource_id: Optional[str] = None
    """Identifies the linked resource."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""
