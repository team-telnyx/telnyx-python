# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .comment_type import CommentType

__all__ = ["DirComment"]


class DirComment(BaseModel):
    id: Optional[str] = None

    author_name: Optional[str] = None
    """Display name of the author. May be `null`."""

    author_role: Optional[Literal["customer", "admin"]] = None
    """Who wrote the comment. `admin` covers the Telnyx vetting team."""

    comment_type: Optional[CommentType] = None
    """Comment categorisation.

    Customers post `customer_inquiry`. The Telnyx team posts `vetting_comment`,
    `rejection_reason`, `notification`, `status_update`, or `admin_response`.
    `internal_note` is filtered out of customer-visible responses.
    """

    content: Optional[str] = None

    created_at: Optional[datetime] = None

    entity_type: Optional[Literal["dir"]] = None
    """Resource the comment is attached to. Always `dir` on this endpoint."""

    visibility: Optional[Literal["customer"]] = None
    """Always `customer` on this endpoint - internal-only comments are filtered out."""
