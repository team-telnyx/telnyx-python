# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProductRetrieveParams"]


class ProductRetrieveParams(TypedDict, total=False):
    filter_country_iso: Annotated[Optional[str], PropertyInfo(alias="filter[country_iso]")]

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number (1-based)."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of items per page (max 100)."""
