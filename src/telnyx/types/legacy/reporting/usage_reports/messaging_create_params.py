# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["MessagingCreateParams"]


class MessagingCreateParams(TypedDict, total=False):
    aggregation_type: Required[int]
    """Aggregation type: No aggregation = 0, By Messaging Profile = 1, By Tags = 2"""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    managed_accounts: SequenceNotStr[str]
    """List of managed accounts to include"""

    profiles: SequenceNotStr[str]
    """List of messaging profile IDs to filter by"""

    select_all_managed_accounts: bool

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
