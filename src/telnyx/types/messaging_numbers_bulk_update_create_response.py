# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessagingNumbersBulkUpdateCreateResponse", "Data"]


class Data(BaseModel):
    failed: Optional[List[str]] = None
    """Phone numbers that failed to update."""

    order_id: Optional[str] = None
    """Order ID to verify bulk update status."""

    pending: Optional[List[str]] = None
    """Phone numbers pending to be updated."""

    record_type: Optional[Literal["messaging_numbers_bulk_update"]] = None
    """Identifies the type of the resource."""

    success: Optional[List[str]] = None
    """Phoned numbers updated successfully."""


class MessagingNumbersBulkUpdateCreateResponse(BaseModel):
    data: Optional[Data] = None
