# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NumberOrderPhoneNumberListParams", "Filter"]


class NumberOrderPhoneNumberListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[country_code]
    """


class Filter(TypedDict, total=False):
    country_code: str
    """Country code of the order phone number."""
