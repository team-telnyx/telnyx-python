# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PrivateWirelessGatewayDeleteResponse", "Data", "DataAssignedResource", "DataStatus"]


class DataAssignedResource(BaseModel):
    count: Optional[int] = None
    """The current count of a resource type assigned to the Private Wireless Gateway."""

    record_type: Optional[str] = None
    """The type of the resource assigned to the Private Wireless Gateway."""


class DataStatus(BaseModel):
    error_code: Optional[str] = None
    """
    This attribute is an [error code](https://developers.telnyx.com/api/errors)
    related to the failure reason.
    """

    error_description: Optional[str] = None
    """This attribute provides a human-readable explanation of why a failure happened."""

    value: Optional[Literal["provisioning", "provisioned", "failed", "decommissioning"]] = None
    """The current status or failure details of the Private Wireless Gateway. <ul>

     <li><code>provisioning</code> - the Private Wireless Gateway is being provisioned.</li>
     <li><code>provisioned</code> - the Private Wireless Gateway was provisioned and able to receive connections.</li>
     <li><code>failed</code> - the provisioning had failed for a reason and it requires an intervention.</li>
     <li><code>decommissioning</code> - the Private Wireless Gateway is being removed from the network.</li>
     </ul>
     Transitioning between the provisioning and provisioned states may take some time.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    assigned_resources: Optional[List[DataAssignedResource]] = None
    """
    A list of the resources that have been assigned to the Private Wireless Gateway.
    """

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    ip_range: Optional[str] = None
    """IP block used to assign IPs to the SIM cards in the Private Wireless Gateway."""

    name: Optional[str] = None
    """The private wireless gateway name."""

    network_id: Optional[str] = None
    """The identification of the related network resource."""

    record_type: Optional[str] = None

    region_code: Optional[str] = None
    """The name of the region where the Private Wireless Gateway is deployed."""

    status: Optional[DataStatus] = None
    """The current status or failure details of the Private Wireless Gateway."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""


class PrivateWirelessGatewayDeleteResponse(BaseModel):
    data: Optional[Data] = None
