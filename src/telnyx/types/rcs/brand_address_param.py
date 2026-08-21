# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BrandAddressParam"]


class BrandAddressParam(TypedDict, total=False):
    administrative_area: Required[str]

    city: Required[str]

    country_code: Required[str]
    """The two-letter ISO 3166-1 country code."""

    line_1: Required[str]

    postal_code: Required[str]

    line_2: Optional[str]
