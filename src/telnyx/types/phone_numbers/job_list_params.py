# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["JobListParams", "Filter"]


class JobListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[type], filter[phone_number], filter[phone_number][],
    filter[status][]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["created_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[type], filter[phone_number], filter[phone_number][], filter[status][]
    """

    phone_number: Union[str, SequenceNotStr[str]]
    """Returns jobs that targeted any of the supplied account-owned phone numbers.

    Values beginning with `+` must contain 1 to 20 digits after the plus sign. The
    10-value limit is enforced before duplicate values are removed. Unmatched or
    non-account-owned identifiers return an empty result. Phone-number filtering
    must be enabled for the account.
    """

    status: List[Literal["pending", "in_progress", "completed", "failed", "expired"]]
    """Returns jobs with any of the supplied statuses.

    Use repeated `filter[status][]` parameters; scalar and comma-separated status
    values are not accepted.
    """

    type: Literal["update_emergency_settings", "delete_phone_numbers", "update_phone_numbers"]
    """Identifies the type of the background job."""
