# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectionRtcpSettingsParam"]


class ConnectionRtcpSettingsParam(TypedDict, total=False):
    capture_enabled: bool
    """
    BETA - Enable the capture and storage of RTCP messages to create QoS reports on
    the Telnyx Mission Control Portal.
    """

    port: Literal["rtcp-mux", "rtp+1"]
    """RTCP port by default is rtp+1, it can also be set to rtcp-mux"""

    report_frequency_secs: int
    """RTCP reports are sent to customers based on the frequency set.

    Frequency is in seconds and it can be set to values from 5 to 3000 seconds.
    """
