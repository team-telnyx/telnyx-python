# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AttachmentRequestParam"]


class AttachmentRequestParam(TypedDict, total=False):
    content: str
    """Attachment content, typically Base64-encoded.

    Defaults to empty string when omitted.
    """

    content_id: Optional[str]
    """MIME Content-ID used to reference an inline attachment."""

    content_type: str
    """MIME content type. Defaults to "application/octet-stream" when omitted."""

    disposition: str
    """MIME disposition (`attachment` or `inline`)."""

    filename: str
    """Attachment filename. Defaults to "attachment" when omitted."""
