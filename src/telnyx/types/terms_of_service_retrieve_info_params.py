# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TermsOfServiceRetrieveInfoParams"]


class TermsOfServiceRetrieveInfoParams(TypedDict, total=False):
    product_type: Literal["branded_calling", "number_reputation"]
    """Optional product filter. Omit to return info for all products."""
