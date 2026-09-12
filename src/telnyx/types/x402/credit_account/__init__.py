# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .payment_list_params import PaymentListParams as PaymentListParams

if TYPE_CHECKING:
    from .x402_transaction_record import X402TransactionRecord as X402TransactionRecord
    from .payment_retrieve_response import PaymentRetrieveResponse as PaymentRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "X402TransactionRecord":
        from .x402_transaction_record import X402TransactionRecord

        return X402TransactionRecord
    if name == "PaymentRetrieveResponse":
        from .payment_retrieve_response import PaymentRetrieveResponse

        return PaymentRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
