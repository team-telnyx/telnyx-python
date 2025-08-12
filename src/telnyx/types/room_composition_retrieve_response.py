# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RoomCompositionRetrieveResponse", "Data", "DataVideoLayout"]


class DataVideoLayout(BaseModel):
    height: Optional[int] = None
    """Height of the video region"""

    max_columns: Optional[int] = None
    """Maximum number of columns of the region's placement grid.

    By default, the region has as many columns as needed to layout all the specified
    video sources.
    """

    max_rows: Optional[int] = None
    """Maximum number of rows of the region's placement grid.

    By default, the region has as many rows as needed to layout all the specified
    video sources.
    """

    video_sources: Optional[List[str]] = None
    """Array of video recording ids to be composed in the region.

    Can be "\\**" to specify all video recordings in the session
    """

    width: Optional[int] = None
    """Width of the video region"""

    x_pos: Optional[int] = None
    """
    X axis value (in pixels) of the region's upper left corner relative to the upper
    left corner of the whole room composition viewport.
    """

    y_pos: Optional[int] = None
    """
    Y axis value (in pixels) of the region's upper left corner relative to the upper
    left corner of the whole room composition viewport.
    """

    z_pos: Optional[int] = None
    """
    Regions with higher z_pos values are stacked on top of regions with lower z_pos
    values
    """


class Data(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the room composition."""

    completed_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room composition has completed."""

    created_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room composition was created."""

    download_url: Optional[str] = None
    """Url to download the composition."""

    duration_secs: Optional[int] = None
    """Shows the room composition duration in seconds."""

    ended_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room composition has ended."""

    format: Optional[Literal["mp4"]] = None
    """Shows format of the room composition."""

    record_type: Optional[str] = None

    room_id: Optional[str] = None
    """Identify the room associated with the room composition."""

    session_id: Optional[str] = None
    """Identify the room session associated with the room composition."""

    size_mb: Optional[float] = None
    """Shows the room composition size in MB."""

    started_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room composition has stated."""

    status: Optional[Literal["completed", "enqueued", "processing"]] = None
    """Shows the room composition status."""

    updated_at: Optional[datetime] = None
    """ISO 8601 timestamp when the room composition was updated."""

    user_id: Optional[str] = None
    """Identify the user associated with the room composition."""

    video_layout: Optional[Dict[str, DataVideoLayout]] = None
    """Describes the video layout of the room composition in terms of regions.

    Limited to 2 regions.
    """

    webhook_event_failover_url: Optional[str] = None
    """
    The failover URL where webhooks related to this room composition will be sent if
    sending to the primary URL fails. Must include a scheme, such as 'https'.
    """

    webhook_event_url: Optional[str] = None
    """The URL where webhooks related to this room composition will be sent.

    Must include a scheme, such as 'https'.
    """

    webhook_timeout_secs: Optional[int] = None
    """Specifies how many seconds to wait before timing out a webhook."""


class RoomCompositionRetrieveResponse(BaseModel):
    data: Optional[Data] = None
