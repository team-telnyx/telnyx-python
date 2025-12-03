# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel
from .network_interface import NetworkInterface

__all__ = ["PublicInternetGatewayCreateResponse", "Data", "DataRegion"]


class DataRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class Data(Record, NetworkInterface):
    public_ip: Optional[str] = None
    """The publically accessible ip for this interface."""

    region: Optional[DataRegion] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""


class PublicInternetGatewayCreateResponse(BaseModel):
    data: Optional[Data] = None
