# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ActionRequirementListParams", "Filter", "Sort"]


class ActionRequirementListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[id][in][], filter[requirement_type_id], filter[action_type],
    filter[status]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Sort
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[id][in][], filter[requirement_type_id], filter[action_type], filter[status]
    """

    id: SequenceNotStr[str]
    """Filter action requirements by a list of IDs"""

    action_type: Literal["au_id_verification"]
    """Filter action requirements by action type"""

    requirement_type_id: str
    """Filter action requirements by requirement type ID"""

    status: Literal["created", "pending", "completed", "cancelled", "failed"]
    """Filter action requirements by status"""


class Sort(TypedDict, total=False):
    """Consolidated sort parameter (deepObject style). Originally: sort[value]"""

    value: Literal["created_at", "-created_at", "updated_at", "-updated_at"]
    """Specifies the sort order for results.

    If not given, results are sorted by created_at in descending order.
    """
