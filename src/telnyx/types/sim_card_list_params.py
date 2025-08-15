# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SimCardListParams", "Filter", "Page"]


class SimCardListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for SIM cards (deepObject style).

    Originally: filter[tags], filter[iccid], filter[status]
    """

    filter_sim_card_group_id: Annotated[str, PropertyInfo(alias="filter[sim_card_group_id]")]
    """A valid SIM card group ID."""

    include_sim_card_group: bool
    """It includes the associated SIM card group object in the response when present."""

    page: Page
    """Consolidated pagination parameter (deepObject style).

    Originally: page[number], page[size]
    """

    sort: Literal["current_billing_period_consumed_data.amount"]
    """Sorts SIM cards by the given field.

    Defaults to ascending order unless field is prefixed with a minus sign.
    """


class Filter(TypedDict, total=False):
    iccid: str
    """A search string to partially match for the SIM card's ICCID."""

    status: List[Literal["enabled", "disabled", "standby", "data_limit_exceeded", "unauthorized_imei"]]
    """Filter by a SIM card's status."""

    tags: List[str]
    """
    A list of SIM card tags to filter on.<br/><br/> If the SIM card contains
    <b><i>all</i></b> of the given <code>tags</code> they will be found.<br/><br/>
    For example, if the SIM cards have the following tags: <ul>

      <li><code>['customers', 'staff', 'test']</code>
      <li><code>['test']</code></li>
      <li><code>['customers']</code></li>
    </ul>
    Searching for <code>['customers', 'test']</code> returns only the first because it's the only one with both tags.<br/> Searching for <code>test</code> returns the first two SIMs, because both of them have such tag.<br/> Searching for <code>customers</code> returns the first and last SIMs.<br/>
    """


class Page(TypedDict, total=False):
    number: int
    """The page number to load."""

    size: int
    """The size of the page."""
