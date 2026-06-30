# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .credit_account_settle_params import CreditAccountSettleParams as CreditAccountSettleParams
from .credit_account_create_quote_params import CreditAccountCreateQuoteParams as CreditAccountCreateQuoteParams

if TYPE_CHECKING:
    from .credit_account_settle_response import CreditAccountSettleResponse as CreditAccountSettleResponse
    from .credit_account_create_quote_response import (
        CreditAccountCreateQuoteResponse as CreditAccountCreateQuoteResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "CreditAccountCreateQuoteResponse":
        from .credit_account_create_quote_response import CreditAccountCreateQuoteResponse

        return CreditAccountCreateQuoteResponse
    if name == "CreditAccountSettleResponse":
        from .credit_account_settle_response import CreditAccountSettleResponse

        return CreditAccountSettleResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
