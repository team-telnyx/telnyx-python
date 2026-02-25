# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentCreateStoredPaymentTransactionParams"]


class PaymentCreateStoredPaymentTransactionParams(TypedDict, total=False):
    amount: Required[str]
    """Amount in dollars and cents, e.g. "120.00" """
