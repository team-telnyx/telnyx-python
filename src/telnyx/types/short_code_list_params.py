# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ShortCodeListParams", "Filter", "Page"]


class ShortCodeListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[messaging_profile_id]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """


class Filter(TypedDict, total=False):
    messaging_profile_id: str
    """Filter by Messaging Profile ID.

    Use the string `null` for phone numbers without assigned profiles. A synonym for
    the `/messaging_profiles/{id}/short_codes` endpoint when querying about an
    extant profile.
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
