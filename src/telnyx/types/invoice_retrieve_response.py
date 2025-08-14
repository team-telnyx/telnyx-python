# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from .._models import BaseModel

__all__ = ["InvoiceRetrieveResponse", "Data"]


class Data(BaseModel):
    download_url: Optional[str] = None
    """Present only if the query parameter `action=link` is set."""

    file_id: Optional[str] = None

    invoice_id: Optional[str] = None

    paid: Optional[bool] = None

    period_end: Optional[date] = None

    period_start: Optional[date] = None

    url: Optional[str] = None


class InvoiceRetrieveResponse(BaseModel):
    data: Optional[Data] = None
