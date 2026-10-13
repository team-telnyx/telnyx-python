# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SpendRetrieveEventsParams"]


class SpendRetrieveEventsParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    end_user_id: str

    metadata: Dict[str, str]
    """Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND.

    A value matches the tag's text form exactly (booleans as true/false, integers in
    decimal), so metadata[flag]=true matches both boolean true and the string
    "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
    bounded by the account, the date range and the report timeout.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    page_snapshot: Annotated[str, PropertyInfo(alias="page[snapshot]")]
    """
    Required after page 1; account/filter-bound 15-minute stable snapshot;
    expired/mismatch 409.
    """

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    token_group_id: str

    token_key_id: str

    token_user_id: str
