# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["VerifyMeta"]


class VerifyMeta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int
