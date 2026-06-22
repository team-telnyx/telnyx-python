# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .porting_order_activation_status import PortingOrderActivationStatus

__all__ = ["PortingOrderActivationSettings"]


class PortingOrderActivationSettings(BaseModel):
    activation_status: Optional[PortingOrderActivationStatus] = None
    """Activation status"""

    fast_port_eligible: Optional[bool] = None
    """Indicates whether this porting order is eligible for FastPort"""

    foc_datetime_actual: Optional[datetime] = None
    """ISO 8601 formatted Date/Time of the FOC date"""

    foc_datetime_requested: Optional[datetime] = None
    """ISO 8601 formatted Date/Time requested for the FOC date"""
