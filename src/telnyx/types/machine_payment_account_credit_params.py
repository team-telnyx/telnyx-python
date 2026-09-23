# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MachinePaymentAccountCreditParams"]


class MachinePaymentAccountCreditParams(TypedDict, total=False):
    amount_usd: Required[str]
    """
    Amount to credit in USD, as a decimal string with up to two fractional digits
    (by default between 5.00 and 500.00). The request body is required on the
    initial challenge request and remains required on a paid retry, where you
    re-send the identical body plus the payment credential — the credential, not the
    body, selects the payment, and the retried body is not re-validated.
    """
