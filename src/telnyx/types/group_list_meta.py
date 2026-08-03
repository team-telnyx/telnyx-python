# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["GroupListMeta"]


class GroupListMeta(BaseModel):
    """Group list `meta` (consistent with `GET /v2/email_blocks`)."""

    page_number: int

    page_size: int

    total_pages: int

    total_results: int
