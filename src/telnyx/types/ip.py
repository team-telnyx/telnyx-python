# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IP"]


class IP(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    connection_id: Optional[str] = None
    """ID of the IP Connection to which this IP should be attached."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    ip_address: Optional[str] = None
    """IP adddress represented by this resource."""

    port: Optional[int] = None
    """Port to use when connecting to this IP."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
