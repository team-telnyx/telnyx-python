# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OtaUpdateListParams", "Filter", "Page"]


class OtaUpdateListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for OTA updates (deepObject style).

    Originally: filter[status], filter[sim_card_id], filter[type]
    """

    page: Page
    """Consolidated pagination parameter (deepObject style).

    Originally: page[number], page[size]
    """


class Filter(TypedDict, total=False):
    sim_card_id: str
    """The SIM card identification UUID."""

    status: Literal["in-progress", "completed", "failed"]
    """Filter by a specific status of the resource's lifecycle."""

    type: Literal["sim_card_network_preferences"]
    """Filter by type."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""
