# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UsageReportListParams", "Page"]


class UsageReportListParams(TypedDict, total=False):
    dimensions: Required[List[str]]
    """Breakout by specified product dimensions"""

    metrics: Required[List[str]]
    """Specified product usage values"""

    product: Required[str]
    """Telnyx product"""

    date_range: str
    """A more user-friendly way to specify the timespan you want to filter by.

    More options can be found in the Telnyx API Reference docs.
    """

    end_date: str
    """The end date for the time range you are interested in.

    The maximum time range is 31 days. Format: YYYY-MM-DDTHH:mm:ssZ
    """

    filter: str
    """Filter records on dimensions"""

    format: Literal["csv", "json"]
    """Specify the response format (csv or json).

    JSON is returned by default, even if not specified.
    """

    managed_accounts: bool
    """
    Return the aggregations for all Managed Accounts under the user making the
    request.
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    sort: List[str]
    """Specifies the sort order for results"""

    start_date: str
    """The start date for the time range you are interested in.

    The maximum time range is 31 days. Format: YYYY-MM-DDTHH:mm:ssZ
    """

    authorization_bearer: str
    """Authenticates the request with your Telnyx API V2 KEY"""


class Page(TypedDict, total=False):
    number: int

    size: int
