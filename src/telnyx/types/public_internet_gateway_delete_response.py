# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel
from .interface import Interface

__all__ = ["PublicInternetGatewayDeleteResponse", "Data", "DataRegion"]


class DataRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class Data(Record, Interface):
    public_ip: Optional[str] = None
    """The publically accessible ip for this interface."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    region: Optional[DataRegion] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""


class PublicInternetGatewayDeleteResponse(BaseModel):
    data: Optional[Data] = None
