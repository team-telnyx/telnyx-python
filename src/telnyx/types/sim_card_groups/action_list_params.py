# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionListParams"]


class ActionListParams(TypedDict, total=False):
    filter_sim_card_group_id: Annotated[str, PropertyInfo(alias="filter[sim_card_group_id]")]
    """A valid SIM card group ID."""

    filter_status: Annotated[Literal["in-progress", "completed", "failed"], PropertyInfo(alias="filter[status]")]
    """Filter by a specific status of the resource's lifecycle."""

    filter_type: Annotated[
        Literal[
            "set_private_wireless_gateway",
            "remove_private_wireless_gateway",
            "set_wireless_blocklist",
            "remove_wireless_blocklist",
        ],
        PropertyInfo(alias="filter[type]"),
    ]
    """Filter by action type."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""
