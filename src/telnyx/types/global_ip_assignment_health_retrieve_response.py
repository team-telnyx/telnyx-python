# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GlobalIPAssignmentHealthRetrieveResponse",
    "Data",
    "DataGlobalIP",
    "DataGlobalIPAssignment",
    "DataGlobalIPAssignmentWireguardPeer",
    "DataHealth",
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


class DataHealth(BaseModel):
    fail: Optional[float] = None
    """The number of failed health checks."""

    pass_: Optional[float] = FieldInfo(alias="pass", default=None)
    """The number of successful health checks."""


class Data(BaseModel):
    global_ip: Optional[DataGlobalIP] = None

    global_ip_assignment: Optional[DataGlobalIPAssignment] = None

    health: Optional[DataHealth] = None

    timestamp: Optional[datetime] = None
    """The timestamp of the metric."""


class GlobalIPAssignmentHealthRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
