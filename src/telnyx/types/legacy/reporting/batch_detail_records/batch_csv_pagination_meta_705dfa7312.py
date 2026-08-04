# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ....._models import BaseModel

__all__ = ["BatchCsvPaginationMeta705dfa7312"]


class BatchCsvPaginationMeta705dfa7312(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
