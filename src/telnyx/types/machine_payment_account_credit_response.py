# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MachinePaymentAccountCreditResponse", "Data"]


class Data(BaseModel):
    """An account-credit transaction settled through the Machine Payment Protocol."""

    id: str
    """Unique identifier of the account-credit transaction."""

    account_id: str
    """Identifier of the credited Telnyx account.

    Derived from the authenticated user on the initial request and from the verified
    payment credential on a paid retry — never from the request body.
    """

    amount: str
    """Credited amount as a decimal string with two fractional digits."""

    currency: str
    """ISO 4217 currency code of the credited amount (currently always USD)."""

    payment_source: Literal["machine_payment"]
    """
    Payment source identifier distinguishing machine payments from other
    account-credit sources.
    """

    record_type: Literal["machine_payment_account_credit"]
    """Record type identifier."""

    created: Optional[bool] = None
    """
    True when this response created a new account credit, false when an existing
    transaction was returned for a duplicate paid retry.
    """

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the transaction was created."""

    mpp_resource: Optional[str] = None
    """
    Machine Payment Protocol resource identifier the payment credential was bound
    to.
    """

    payment_intent_id: Optional[str] = None
    """Stripe PaymentIntent identifier for Stripe settlements.

    Absent for Tempo settlements.
    """

    payment_method: Optional[Literal["stripe_spt", "tempo_usdc"]] = None
    """
    Payment method used by the provider: `stripe_spt` for Stripe Shared Payment
    Token payments, `tempo_usdc` for Tempo USDC payments.
    """

    provider: Optional[Literal["stripe", "tempo"]] = None
    """Upstream payment provider that settled the payment."""

    receipt_reference: Optional[str] = None
    """
    Provider receipt reference: the Stripe PaymentIntent identifier for Stripe
    settlements, or the on-chain transaction hash for Tempo settlements.
    """

    status: Optional[Literal["new", "processing", "settled", "expired", "invalid"]] = None
    """Status of the transaction.

    Successful machine payment credits are recorded as `settled`.
    """


class MachinePaymentAccountCreditResponse(BaseModel):
    data: Optional[Data] = None
    """An account-credit transaction settled through the Machine Payment Protocol."""
