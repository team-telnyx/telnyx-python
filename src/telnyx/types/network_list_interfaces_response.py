# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .interface_status import InterfaceStatus

__all__ = ["NetworkListInterfacesResponse", "Region"]


class Region(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class NetworkListInterfacesResponse(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    name: Optional[str] = None
    """A user specified name for the interface."""

    network_id: Optional[str] = None
    """The id of the network associated with the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    region: Optional[Region] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    type: Optional[str] = None
    """Identifies the type of the interface."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""
