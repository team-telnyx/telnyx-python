# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionShareResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this sharing token"""

    token: Optional[str] = None
    """A signed JWT token that can be used to access the shared resource"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    expires_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the sharing token expires."""

    expires_in_seconds: Optional[int] = None
    """The number of seconds until the sharing token expires"""

    permissions: Optional[List[Literal["porting_order.document.read", "porting_order.document.update"]]] = None
    """The permissions granted to the sharing token"""

    porting_order_id: Optional[str] = None
    """Identifies the porting order resource being shared"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class ActionShareResponse(BaseModel):
    data: Optional[Data] = None
