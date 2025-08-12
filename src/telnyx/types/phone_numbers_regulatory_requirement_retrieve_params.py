# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhoneNumbersRegulatoryRequirementRetrieveParams", "Filter"]


class PhoneNumbersRegulatoryRequirementRetrieveParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number]
    """


class Filter(TypedDict, total=False):
    phone_number: str
    """Record type phone number/ phone numbers"""
