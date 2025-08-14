# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimCardDataUsageNotificationListParams"]


class SimCardDataUsageNotificationListParams(TypedDict, total=False):
    filter_sim_card_id: Annotated[str, PropertyInfo(alias="filter[sim_card_id]")]
    """A valid SIM card ID."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""
