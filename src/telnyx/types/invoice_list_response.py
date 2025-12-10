# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from .._models import BaseModel

__all__ = ["InvoiceListResponse"]


class InvoiceListResponse(BaseModel):
    file_id: Optional[str] = None

    invoice_id: Optional[str] = None

    paid: Optional[bool] = None

    period_end: Optional[date] = None

    period_start: Optional[date] = None

    url: Optional[str] = None
