# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentCreateStoredPaymentTransactionResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    amount_cents: Optional[int] = None

    amount_currency: Optional[str] = None

    auto_recharge: Optional[bool] = None

    created_at: Optional[datetime] = None

    processor_status: Optional[str] = None

    record_type: Optional[Literal["transaction"]] = None

    transaction_processing_type: Optional[Literal["stored_payment"]] = None


class PaymentCreateStoredPaymentTransactionResponse(BaseModel):
    data: Optional[Data] = None
