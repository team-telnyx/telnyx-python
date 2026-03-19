# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TrafficPolicyProfileCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    domains: Optional[List[str]] = None
    """Array of domain names."""

    ip_ranges: Optional[List[str]] = None
    """Array of IP ranges in CIDR notation."""

    limit_bw_kbps: Optional[int] = None
    """Bandwidth limit in kbps."""

    record_type: Optional[str] = None

    services: Optional[List[str]] = None
    """Array of PCEF service IDs included in the profile."""

    type: Optional[Literal["whitelist", "blacklist", "throttling"]] = None
    """The type of the traffic policy profile."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class TrafficPolicyProfileCreateResponse(BaseModel):
    data: Optional[Data] = None
