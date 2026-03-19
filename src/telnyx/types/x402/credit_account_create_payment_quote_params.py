# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditAccountCreatePaymentQuoteParams"]


class CreditAccountCreatePaymentQuoteParams(TypedDict, total=False):
    amount_usd: Required[str]
    """Amount in USD to fund (minimum 5.00, maximum 10000.00)."""
