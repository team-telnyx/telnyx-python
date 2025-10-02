# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["VoiceCreateResponse", "Data", "DataFilter"]


class DataFilter(BaseModel):
    billing_group: Optional[str] = None
    """Billing group UUID to filter by"""

    cld: Optional[str] = None
    """Called line identification (destination number)"""

    cld_filter: Optional[Literal["contains", "starts_with", "ends_with"]] = None
    """Filter type for CLD matching"""

    cli: Optional[str] = None
    """Calling line identification (caller ID)"""

    cli_filter: Optional[Literal["contains", "starts_with", "ends_with"]] = None
    """Filter type for CLI matching"""

    filter_type: Optional[Literal["and", "or"]] = None
    """Logical operator for combining filters"""

    tags_list: Optional[str] = None
    """Tag name to filter by"""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the report"""

    call_types: Optional[List[int]] = None
    """List of call types (Inbound = 1, Outbound = 2)"""

    connections: Optional[List[int]] = None
    """List of connections"""

    created_at: Optional[str] = None
    """Creation date of the report"""

    end_time: Optional[str] = None
    """End time in ISO format"""

    filters: Optional[List[DataFilter]] = None
    """List of filters"""

    managed_accounts: Optional[List[str]] = None
    """List of managed accounts"""

    record_type: Optional[str] = None

    record_types: Optional[List[int]] = None
    """List of record types (Complete = 1, Incomplete = 2, Errors = 3)"""

    report_name: Optional[str] = None
    """Name of the report"""

    report_url: Optional[str] = None
    """URL to download the report"""

    retry: Optional[int] = None
    """Number of retries"""

    source: Optional[str] = None
    """Source of the report.

    Valid values: calls (default), call-control, fax-api, webrtc
    """

    start_time: Optional[str] = None
    """Start time in ISO format"""

    status: Optional[int] = None
    """Status of the report (Pending = 1, Complete = 2, Failed = 3, Expired = 4)"""

    timezone: Optional[str] = None
    """Timezone for the report"""

    updated_at: Optional[str] = None
    """Last update date of the report"""


class VoiceCreateResponse(BaseModel):
    data: Optional[Data] = None
    """Response object for CDR detailed report"""
