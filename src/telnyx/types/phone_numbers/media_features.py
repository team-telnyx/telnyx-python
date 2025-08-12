# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MediaFeatures"]


class MediaFeatures(BaseModel):
    accept_any_rtp_packets_enabled: Optional[bool] = None
    """
    When enabled, Telnyx will accept RTP packets from any customer-side IP address
    and port, not just those to which Telnyx is sending RTP.
    """

    rtp_auto_adjust_enabled: Optional[bool] = None
    """
    When RTP Auto-Adjust is enabled, the destination RTP address port will be
    automatically changed to match the source of the incoming RTP packets.
    """

    t38_fax_gateway_enabled: Optional[bool] = None
    """Controls whether Telnyx will accept a T.38 re-INVITE for this phone number.

    Note that Telnyx will not send a T.38 re-INVITE; this option only controls
    whether one will be accepted.
    """
