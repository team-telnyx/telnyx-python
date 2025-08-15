# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .texml_recording_subresources_uris import TexmlRecordingSubresourcesUris

__all__ = ["TexmlGetCallRecordingResponseBody"]


class TexmlGetCallRecordingResponseBody(BaseModel):
    account_sid: Optional[str] = None

    call_sid: Optional[str] = None

    channels: Optional[Literal[1, 2]] = None

    conference_sid: Optional[str] = None

    date_created: Optional[datetime] = None

    date_updated: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration of this recording, given in seconds."""

    error_code: Optional[str] = None

    media_url: Optional[str] = None

    sid: Optional[str] = None
    """Identifier of a resource."""

    source: Optional[
        Literal[
            "StartCallRecordingAPI",
            "StartConferenceRecordingAPI",
            "OutboundAPI",
            "DialVerb",
            "Conference",
            "RecordVerb",
            "Trunking",
        ]
    ] = None
    """Defines how the recording was created."""

    start_time: Optional[datetime] = None

    status: Optional[Literal["in-progress", "completed", "paused", "stopped"]] = None

    subresources_uris: Optional[TexmlRecordingSubresourcesUris] = None
    """Subresources details for a recording if available."""

    uri: Optional[str] = None
    """The relative URI for this recording resource."""
