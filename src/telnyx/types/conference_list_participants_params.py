# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConferenceListParticipantsParams", "Filter"]


class ConferenceListParticipantsParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[muted], filter[on_hold], filter[whispering]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    region: Literal["Australia", "Europe", "Middle East", "US"]
    """Region where the conference data is located"""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[muted], filter[on_hold], filter[whispering]
    """

    muted: bool
    """If present, participants will be filtered to those who are/are not muted"""

    on_hold: bool
    """If present, participants will be filtered to those who are/are not put on hold"""

    whispering: bool
    """
    If present, participants will be filtered to those who are whispering or are not
    """
