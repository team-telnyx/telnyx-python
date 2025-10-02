# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["MessagingCreateParams", "Filter"]


class MessagingCreateParams(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End time in ISO format.

    Note: If end time includes the last 4 hours, some MDRs might not appear in this
    report, due to wait time for downstream message delivery confirmation
    """

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start time in ISO format"""

    connections: Iterable[int]
    """List of connections to filter by"""

    directions: Iterable[int]
    """List of directions to filter by (Inbound = 1, Outbound = 2)"""

    filters: Iterable[Filter]
    """List of filters to apply"""

    include_message_body: bool
    """Whether to include message body in the report"""

    managed_accounts: SequenceNotStr[str]
    """List of managed accounts to include"""

    profiles: SequenceNotStr[str]
    """List of messaging profile IDs to filter by"""

    record_types: Iterable[int]
    """List of record types to filter by (Complete = 1, Incomplete = 2, Errors = 3)"""

    report_name: str
    """Name of the report"""

    select_all_managed_accounts: bool
    """Whether to select all managed accounts"""

    timezone: str
    """Timezone for the report"""


class Filter(TypedDict, total=False):
    billing_group: str
    """Billing group UUID to filter by"""

    cld: str
    """Called line identification (destination number)"""

    cld_filter: Literal["contains", "starts_with", "ends_with"]
    """Filter type for CLD matching"""

    cli: str
    """Calling line identification (caller ID)"""

    cli_filter: Literal["contains", "starts_with", "ends_with"]
    """Filter type for CLI matching"""

    filter_type: Literal["and", "or"]
    """Logical operator for combining filters"""

    tags_list: str
    """Tag name to filter by"""
