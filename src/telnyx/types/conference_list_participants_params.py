# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConferenceListParticipantsParams", "Filter", "Page"]


class ConferenceListParticipantsParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[muted], filter[on_hold], filter[whispering]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[before], page[limit], page[size], page[number]
    """


class Filter(TypedDict, total=False):
    muted: bool
    """If present, participants will be filtered to those who are/are not muted"""

    on_hold: bool
    """If present, participants will be filtered to those who are/are not put on hold"""

    whispering: bool
    """
    If present, participants will be filtered to those who are whispering or are not
    """


class Page(TypedDict, total=False):
    after: str
    """Opaque identifier of next page"""

    before: str
    """Opaque identifier of previous page"""

    limit: int
    """Limit of records per single page"""

    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
