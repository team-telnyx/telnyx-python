# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .x402_transaction_record import X402TransactionRecord

__all__ = ["PaymentRetrieveResponse"]


class PaymentRetrieveResponse(BaseModel):
    data: Optional[X402TransactionRecord] = None
    """An x402 payment transaction."""
