# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AutoRechargePrefUpdateParams"]


class AutoRechargePrefUpdateParams(TypedDict, total=False):
    enabled: bool
    """Whether auto recharge is enabled."""

    invoice_enabled: bool

    preference: Literal["credit_paypal", "ach"]
    """The payment preference for auto recharge."""

    recharge_amount: str
    """
    The amount to recharge the account, the actual recharge amount will be the
    amount necessary to reach the threshold amount plus the recharge amount.
    """

    threshold_amount: str
    """The threshold amount at which the account will be recharged."""
