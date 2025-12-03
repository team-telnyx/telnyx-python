# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["BulkSimCardActionListResponse", "Data", "DataSimCardActionsSummary"]


class DataSimCardActionsSummary(BaseModel):
    count: Optional[int] = None

    status: Optional[Literal["in-progress", "completed", "failed", "interrupted"]] = None


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    action_type: Optional[Literal["bulk_set_public_ips"]] = None
    """The operation type. It can be one of the following: <br/>

    <ul>
    <li><code>bulk_set_public_ips</code> - set a public IP for each specified SIM card.</li>
    </ul>
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    record_type: Optional[str] = None

    settings: Optional[Dict[str, object]] = None
    """A JSON object representation of the bulk action payload."""

    sim_card_actions_summary: Optional[List[DataSimCardActionsSummary]] = None

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class BulkSimCardActionListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
