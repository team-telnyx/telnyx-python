# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .interface_status import InterfaceStatus

__all__ = ["PublicInternetGatewayListResponse"]


class PublicInternetGatewayListResponse(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    name: Optional[str] = None
    """A user specified name for the interface."""

    network_id: Optional[str] = None
    """The id of the network associated with the interface."""

    public_ip: Optional[str] = None
    """The publically accessible ip for this interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    region_code: Optional[str] = None
    """The region interface is deployed to."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""
