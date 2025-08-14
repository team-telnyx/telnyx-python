# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectionRtcpSettings"]


class ConnectionRtcpSettings(BaseModel):
    capture_enabled: Optional[bool] = None
    """
    BETA - Enable the capture and storage of RTCP messages to create QoS reports on
    the Telnyx Mission Control Portal.
    """

    port: Optional[Literal["rtcp-mux", "rtp+1"]] = None
    """RTCP port by default is rtp+1, it can also be set to rtcp-mux"""

    report_frequency_secs: Optional[int] = None
    """RTCP reports are sent to customers based on the frequency set.

    Frequency is in seconds and it can be set to values from 5 to 3000 seconds.
    """
