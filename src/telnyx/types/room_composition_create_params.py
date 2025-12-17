# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .video_region_param import VideoRegionParam

__all__ = ["RoomCompositionCreateParams"]


class RoomCompositionCreateParams(TypedDict, total=False):
    format: str
    """The desired format of the room composition."""

    resolution: str
    """
    The desired resolution (width/height in pixels) of the resulting video of the
    room composition. Both width and height are required to be between 16 and 1280;
    and width _ height should not exceed 1280 _ 720
    """

    session_id: str
    """id of the room session associated with the room composition."""

    video_layout: Dict[str, VideoRegionParam]
    """Describes the video layout of the room composition in terms of regions."""

    webhook_event_failover_url: str
    """
    The failover URL where webhooks related to this room composition will be sent if
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: str
    """The URL where webhooks related to this room composition will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: int
    """Specifies how many seconds to wait before timing out a webhook."""
