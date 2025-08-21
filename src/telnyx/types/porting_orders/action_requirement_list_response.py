# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta

__all__ = ["ActionRequirementListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the action requirement"""

    action_type: Optional[str] = None
    """The type of action required"""

    action_url: Optional[str] = None
    """Optional URL for the action"""

    cancel_reason: Optional[str] = None
    """Reason for cancellation if status is 'cancelled'"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date-time indicating when the resource was created"""

    porting_order_id: Optional[str] = None
    """The ID of the porting order this action requirement belongs to"""

    record_type: Optional[Literal["porting_action_requirement"]] = None
    """Identifies the type of the resource"""

    requirement_type_id: Optional[str] = None
    """The ID of the requirement type"""

    status: Optional[Literal["created", "pending", "completed", "cancelled", "failed"]] = None
    """Current status of the action requirement"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date-time indicating when the resource was updated"""


class ActionRequirementListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
