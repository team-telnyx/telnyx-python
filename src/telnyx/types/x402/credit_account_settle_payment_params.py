# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditAccountSettlePaymentParams"]


class CreditAccountSettlePaymentParams(TypedDict, total=False):
    id: Required[str]
    """The quote ID to settle."""

    body_payment_signature: Annotated[str, PropertyInfo(alias="payment_signature")]
    """Base64-encoded signed payment authorization (x402 PaymentPayload).

    Can alternatively be provided via the PAYMENT-SIGNATURE header.
    """

    header_payment_signature: Annotated[str, PropertyInfo(alias="PAYMENT-SIGNATURE")]
