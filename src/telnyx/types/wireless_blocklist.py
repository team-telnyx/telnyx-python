# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WirelessBlocklist"]


class WirelessBlocklist(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    name: Optional[str] = None
    """The wireless blocklist name."""

    record_type: Optional[str] = None

    type: Optional[Literal["country", "mcc", "plmn"]] = None
    """The type of the wireless blocklist."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""

    values: Optional[List[str]] = None
    """Values to block. The values here depend on the `type` of Wireless Blocklist."""
