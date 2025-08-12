# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ManagedAccountUpdateParams"]


class ManagedAccountUpdateParams(TypedDict, total=False):
    managed_account_allow_custom_pricing: bool
    """
    Boolean value that indicates if the managed account is able to have custom
    pricing set for it or not. If false, uses the pricing of the manager account.
    Defaults to false. This value may be changed, but there may be time lag between
    when the value is changed and pricing changes take effect.
    """
