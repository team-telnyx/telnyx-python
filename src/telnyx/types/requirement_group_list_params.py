# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RequirementGroupListParams", "Filter"]


class RequirementGroupListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[country_code], filter[phone_number_type], filter[action],
    filter[status], filter[customer_reference]
    """


class Filter(TypedDict, total=False):
    action: Literal["ordering", "porting", "action"]
    """Filter requirement groups by action type"""

    country_code: str
    """Filter requirement groups by country code (iso alpha 2)"""

    customer_reference: str
    """Filter requirement groups by customer reference"""

    phone_number_type: Literal["local", "toll_free", "mobile", "national", "shared_cost"]
    """Filter requirement groups by phone number type."""

    status: Literal["approved", "unapproved", "pending-approval", "declined"]
    """Filter requirement groups by status"""
