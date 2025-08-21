# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["RequirementListParams", "Filter", "Page"]


class RequirementListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for requirements (deepObject style).

    Originally: filter[country_code], filter[phone_number_type], filter[action]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    sort: List[
        Literal[
            "created_at",
            "updated_at",
            "country_code",
            "phone_number_type",
            "-created_at",
            "-updated_at",
            "-country_code",
            "-phone_number_type",
        ]
    ]
    """Consolidated sort parameter for requirements (deepObject style).

    Originally: sort[]
    """


class Filter(TypedDict, total=False):
    action: Literal["branded_calling", "ordering", "porting"]
    """Filters requirements to those applying to a specific action."""

    country_code: str
    """
    Filters results to those applying to a 2-character (ISO 3166-1 alpha-2) country
    code
    """

    phone_number_type: Literal["local", "national", "toll_free"]
    """Filters results to those applying to a specific phone_number_type"""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
