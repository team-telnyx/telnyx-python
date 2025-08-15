# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .sim_card_data_usage_notification import SimCardDataUsageNotification

__all__ = ["SimCardDataUsageNotificationCreateResponse"]


class SimCardDataUsageNotificationCreateResponse(BaseModel):
    data: Optional[SimCardDataUsageNotification] = None
    """The SIM card individual data usage notification information."""
