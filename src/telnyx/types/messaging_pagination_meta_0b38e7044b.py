# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["MessagingPaginationMeta0b38e7044b"]


class MessagingPaginationMeta0b38e7044b(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int
