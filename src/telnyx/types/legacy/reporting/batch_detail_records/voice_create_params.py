# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo
from ..filter_param import FilterParam

__all__ = ["VoiceCreateParams"]


class VoiceCreateParams(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End time in ISO format"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start time in ISO format"""

    call_types: Iterable[int]
    """List of call types to filter by (Inbound = 1, Outbound = 2)"""

    connections: Iterable[int]
    """List of connections to filter by"""

    fields: SequenceNotStr[str]
    """Set of fields to include in the report"""

    filters: Iterable[FilterParam]
    """List of filters to apply"""

    include_all_metadata: bool
    """Whether to include all metadata"""

    managed_accounts: SequenceNotStr[str]
    """List of managed accounts to include"""

    record_types: Iterable[int]
    """List of record types to filter by (Complete = 1, Incomplete = 2, Errors = 3)"""

    report_name: str
    """Name of the report"""

    select_all_managed_accounts: bool
    """Whether to select all managed accounts"""

    source: str
    """Source of the report.

    Valid values: calls (default), call-control, fax-api, webrtc
    """

    timezone: str
    """Timezone for the report"""
