# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.netapps_location import NetappsLocation

__all__ = ["VirtualCrossConnectsCoverageListResponse"]


class VirtualCrossConnectsCoverageListResponse(BaseModel):
    available_bandwidth: Optional[List[float]] = None
    """
    The available throughput in Megabits per Second (Mbps) for your Virtual Cross
    Connect.
    """

    cloud_provider: Optional[Literal["aws", "azure", "gce"]] = None
    """
    The Virtual Private Cloud with which you would like to establish a cross
    connect.
    """

    cloud_provider_region: Optional[str] = None
    """The region where your Virtual Private Cloud hosts are located.

    Should be identical to how the cloud provider names region, i.e. us-east-1 for
    AWS but Frankfurt for Azure
    """

    location: Optional[NetappsLocation] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""
