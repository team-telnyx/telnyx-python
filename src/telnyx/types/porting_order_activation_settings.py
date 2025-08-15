# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PortingOrderActivationSettings"]


class PortingOrderActivationSettings(BaseModel):
    activation_status: Optional[
        Literal[
            "New",
            "Pending",
            "Conflict",
            "Cancel Pending",
            "Failed",
            "Concurred",
            "Activate RDY",
            "Disconnect Pending",
            "Concurrence Sent",
            "Old",
            "Sending",
            "Active",
            "Cancelled",
        ]
    ] = None
    """Activation status"""

    fast_port_eligible: Optional[bool] = None
    """Indicates whether this porting order is eligible for FastPort"""

    foc_datetime_actual: Optional[datetime] = None
    """ISO 8601 formatted Date/Time of the FOC date"""

    foc_datetime_requested: Optional[datetime] = None
    """ISO 8601 formatted Date/Time requested for the FOC date"""
