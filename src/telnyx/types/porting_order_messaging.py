# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PortingOrderMessaging"]


class PortingOrderMessaging(BaseModel):
    enable_messaging: Optional[bool] = None
    """
    Indicates whether Telnyx will port messaging capabilities from the losing
    carrier. If false, any messaging capabilities will stay with their current
    provider.
    """

    messaging_capable: Optional[bool] = None
    """Indicates whether the porting order can also port messaging capabilities."""

    messaging_port_completed: Optional[bool] = None
    """Indicates whether the messaging porting has been completed."""

    messaging_port_status: Optional[
        Literal["not_applicable", "pending", "activating", "exception", "canceled", "partial_port_complete", "ported"]
    ] = None
    """The current status of the messaging porting."""
