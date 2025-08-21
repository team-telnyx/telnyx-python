# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AutoRechargePrefUpdateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the auto recharge preference."""

    enabled: Optional[bool] = None
    """Whether auto recharge is enabled."""

    invoice_enabled: Optional[bool] = None

    preference: Optional[Literal["credit_paypal", "ach"]] = None
    """The payment preference for auto recharge."""

    recharge_amount: Optional[str] = None
    """
    The amount to recharge the account, the actual recharge amount will be the
    amount necessary to reach the threshold amount plus the recharge amount.
    """

    record_type: Optional[str] = None
    """The record type."""

    threshold_amount: Optional[str] = None
    """The threshold amount at which the account will be recharged."""


class AutoRechargePrefUpdateResponse(BaseModel):
    data: Optional[Data] = None
