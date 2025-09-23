# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["NumberLookupCreateParams"]


class NumberLookupCreateParams(TypedDict, total=False):
    aggregation_type: Annotated[Literal["ALL", "BY_ORGANIZATION_MEMBER"], PropertyInfo(alias="aggregationType")]
    """Type of aggregation for the report"""

    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """End date for the usage report"""

    managed_accounts: Annotated[SequenceNotStr[str], PropertyInfo(alias="managedAccounts")]
    """List of managed accounts to include in the report"""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Start date for the usage report"""
