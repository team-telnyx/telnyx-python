# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AgreementListParams"]


class AgreementListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""

    product_type: Literal["branded_calling", "number_reputation"]
    """Optional filter.

    Omit to list the user's agreements for **every** product (branded_calling and
    number_reputation); pass a value to return only that product's agreements.
    """
