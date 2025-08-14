# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubNumberOrderRetrieveParams", "Filter"]


class SubNumberOrderRetrieveParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[include_phone_numbers]
    """


class Filter(TypedDict, total=False):
    include_phone_numbers: bool
    """Include the first 50 phone number objects in the results"""
