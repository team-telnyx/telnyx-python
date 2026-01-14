# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionListParams", "Filter"]


class ActionListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for SIM card actions (deepObject style).

    Originally: filter[sim_card_id], filter[status],
    filter[bulk_sim_card_action_id], filter[action_type]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter for SIM card actions (deepObject style).

    Originally: filter[sim_card_id], filter[status], filter[bulk_sim_card_action_id], filter[action_type]
    """

    action_type: Literal[
        "enable", "enable_standby_sim_card", "disable", "set_standby", "remove_public_ip", "set_public_ip"
    ]
    """Filter by action type."""

    bulk_sim_card_action_id: str
    """Filter by a bulk SIM card action ID."""

    sim_card_id: str
    """A valid SIM card ID."""

    status: Literal["in-progress", "completed", "failed"]
    """Filter by a specific status of the resource's lifecycle."""
