# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreditAccountSettlePaymentResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique transaction identifier."""

    amount: Optional[str] = None
    """The transaction amount in the specified currency."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the transaction was created."""

    currency: Optional[str] = None
    """The currency of the transaction amount (e.g. USD)."""

    quote_id: Optional[str] = None
    """The original quote ID associated with this transaction."""

    record_type: Optional[Literal["x402_transaction"]] = None

    status: Optional[Literal["settled"]] = None
    """The settlement status of the transaction."""

    tx_hash: Optional[str] = None
    """The on-chain transaction hash, if available."""


class CreditAccountSettlePaymentResponse(BaseModel):
    data: Optional[Data] = None
