# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .terms_of_service.tos_product_type import TosProductType

__all__ = ["TermsOfServiceRetrieveInfoParams"]


class TermsOfServiceRetrieveInfoParams(TypedDict, total=False):
    product_type: TosProductType
    """Optional product filter. Omit to return info for all products."""
