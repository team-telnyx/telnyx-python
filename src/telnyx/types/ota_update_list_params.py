# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OtaUpdateListParams", "Filter"]


class OtaUpdateListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for OTA updates (deepObject style).

    Originally: filter[status], filter[sim_card_id], filter[type]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter for OTA updates (deepObject style).

    Originally: filter[status], filter[sim_card_id], filter[type]
    """

    sim_card_id: str
    """The SIM card identification UUID."""

    status: Literal["in-progress", "completed", "failed"]
    """Filter by a specific status of the resource's lifecycle."""

    type: Literal["sim_card_network_preferences"]
    """Filter by type."""
