# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RegulatoryRequirementRetrieveParams", "Filter"]


class RegulatoryRequirementRetrieveParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[phone_number], filter[requirement_group_id],
    filter[country_code], filter[phone_number_type], filter[action]
    """


class Filter(TypedDict, total=False):
    action: Literal["ordering", "porting", "action"]
    """Action to check requirements for"""

    country_code: str
    """Country code(iso2) to check requirements for"""

    phone_number: str
    """Phone number to check requirements for"""

    phone_number_type: Literal["local", "toll_free", "mobile", "national", "shared_cost"]
    """Phone number type to check requirements for"""

    requirement_group_id: str
    """ID of requirement group to check requirements for"""
