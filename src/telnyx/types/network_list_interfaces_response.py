# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel
from .network_interface import NetworkInterface

__all__ = ["NetworkListInterfacesResponse", "NetworkListInterfacesResponseRegion"]


class NetworkListInterfacesResponseRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class NetworkListInterfacesResponse(Record, NetworkInterface):
    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    region: Optional[NetworkListInterfacesResponseRegion] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""

    type: Optional[str] = None
    """Identifies the type of the interface."""
