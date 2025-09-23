# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["MessagingListResponse", "Data", "DataFilter", "Meta"]


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
    """Identifies the resource"""

    connections: Optional[List[int]] = None

    created_at: Optional[datetime] = None

    directions: Optional[List[Literal["INBOUND", "OUTBOUND"]]] = None

    end_date: Optional[datetime] = None

    filters: Optional[List[DataFilter]] = None

    profiles: Optional[List[str]] = None
    """List of messaging profile IDs"""

    record_type: Optional[str] = None

    record_types: Optional[List[Literal["INCOMPLETE", "COMPLETED", "ERRORS"]]] = None

    report_name: Optional[str] = None

    report_url: Optional[str] = None

    start_date: Optional[datetime] = None

    status: Optional[Literal["PENDING", "COMPLETE", "FAILED", "EXPIRED"]] = None

    updated_at: Optional[datetime] = None


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class MessagingListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
