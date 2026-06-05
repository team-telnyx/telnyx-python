# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TermsOfServiceStatusParams"]


class TermsOfServiceStatusParams(TypedDict, total=False):
    product_type: Literal["branded_calling", "number_reputation"]
    """Which product's ToS to check.

    Defaults to `branded_calling`; pass `number_reputation` to check the Number
    Reputation Terms of Service.
    """
