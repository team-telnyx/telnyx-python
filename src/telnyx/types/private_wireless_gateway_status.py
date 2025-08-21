# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PrivateWirelessGatewayStatus"]


class PrivateWirelessGatewayStatus(BaseModel):
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
