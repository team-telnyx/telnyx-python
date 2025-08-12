# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "GlobalIPAssignmentsUsageRetrieveResponse",
    "Data",
    "DataGlobalIP",
    "DataGlobalIPAssignment",
    "DataGlobalIPAssignmentWireguardPeer",
    "DataReceived",
    "DataTransmitted",
]


class DataGlobalIP(BaseModel):
    id: Optional[str] = None
    """Global IP ID."""

    ip_address: Optional[str] = None
    """The Global IP address."""


class DataGlobalIPAssignmentWireguardPeer(BaseModel):
    ip_address: Optional[str] = None
    """The IP address of the interface."""

    name: Optional[str] = None
    """A user specified name for the interface."""


class DataGlobalIPAssignment(BaseModel):
    id: Optional[str] = None
    """Global IP assignment ID."""

    wireguard_peer: Optional[DataGlobalIPAssignmentWireguardPeer] = None

    wireguard_peer_id: Optional[str] = None
    """Wireguard peer ID."""


class DataReceived(BaseModel):
    amount: Optional[float] = None
    """The amount of data received."""

    unit: Optional[str] = None
    """The unit of the amount of data received."""


class DataTransmitted(BaseModel):
    amount: Optional[float] = None
    """The amount of data transmitted."""

    unit: Optional[str] = None
    """The unit of the amount of data transmitted."""


class Data(BaseModel):
    global_ip: Optional[DataGlobalIP] = None

    global_ip_assignment: Optional[DataGlobalIPAssignment] = None

    received: Optional[DataReceived] = None

    timestamp: Optional[datetime] = None
    """The timestamp of the metric."""

    transmitted: Optional[DataTransmitted] = None


class GlobalIPAssignmentsUsageRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
