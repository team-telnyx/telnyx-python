# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel
from .network_interface import NetworkInterface

__all__ = ["PublicInternetGatewayRetrieveResponse", "Data"]


class Data(Record, NetworkInterface):
    public_ip: Optional[str] = None
    """The publically accessible ip for this interface."""

    region_code: Optional[str] = None
    """The region interface is deployed to."""


class PublicInternetGatewayRetrieveResponse(BaseModel):
    data: Optional[Data] = None
