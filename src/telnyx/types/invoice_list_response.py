# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel

__all__ = ["InvoiceListResponse", "Data", "Meta"]


class Data(BaseModel):
    file_id: Optional[str] = None

    invoice_id: Optional[str] = None

    paid: Optional[bool] = None

    period_end: Optional[date] = None

    period_start: Optional[date] = None

    url: Optional[str] = None


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class InvoiceListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
