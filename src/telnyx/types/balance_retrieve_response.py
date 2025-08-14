# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BalanceRetrieveResponse", "Data"]


class Data(BaseModel):
    available_credit: Optional[str] = None
    """Available amount to spend (balance + credit limit)"""

    balance: Optional[str] = None
    """The account's current balance."""

    credit_limit: Optional[str] = None
    """The account's credit limit."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""

    pending: Optional[str] = None
    """The account’s pending amount."""

    record_type: Optional[Literal["balance"]] = None
    """Identifies the type of the resource."""


class BalanceRetrieveResponse(BaseModel):
    data: Optional[Data] = None
