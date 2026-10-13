# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageRetrieveSummaryParams"]


class UsageRetrieveSummaryParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    token_group_id: Required[str]

    metadata: Dict[str, str]
    """Request tag filters as metadata[<key>]=<value>, at most 5, combined with AND.

    A value matches the tag's text form exactly (booleans as true/false, integers in
    decimal), so metadata[flag]=true matches both boolean true and the string
    "true". Keys are case-sensitive; reserved-prefix keys are rejected. Unindexed:
    bounded by the account, the date range and the report timeout.
    """
