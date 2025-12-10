# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..record import Record
from ..._models import BaseModel
from ..pagination_meta import PaginationMeta
from ..interface_status import InterfaceStatus

__all__ = ["DefaultGatewayCreateResponse", "Data"]


class Data(Record):
    network_id: Optional[str] = None
    """Network ID."""

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    status: Optional[InterfaceStatus] = None
    """The current status of the interface deployment."""

    wireguard_peer_id: Optional[str] = None
    """Wireguard peer ID."""


class DefaultGatewayCreateResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
