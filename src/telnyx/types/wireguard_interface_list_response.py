# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .record import Record
from .._models import BaseModel
from .interface import Interface
from .pagination_meta import PaginationMeta

__all__ = ["WireguardInterfaceListResponse", "Data", "DataRegion"]


class DataRegion(BaseModel):
    code: Optional[str] = None
    """Region code of the interface."""

    name: Optional[str] = None
    """Region name of the interface."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class Data(Record, Interface):
    enable_sip_trunking: Optional[bool] = None
    """Enable SIP traffic forwarding over VPN interface."""

    endpoint: Optional[str] = None
    """The Telnyx WireGuard peers `Peer.endpoint` value."""

    public_key: Optional[str] = None
    """The Telnyx WireGuard peers `Peer.PublicKey`."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    region: Optional[DataRegion] = None

    region_code: Optional[str] = None
    """The region interface is deployed to."""


class WireguardInterfaceListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
