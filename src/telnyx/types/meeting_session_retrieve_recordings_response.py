# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .meeting_session_recording_export import MeetingSessionRecordingExport

__all__ = ["MeetingSessionRetrieveRecordingsResponse", "Data"]


class Data(BaseModel):
    expires_at: Optional[datetime] = None

    type: str

    url: str


class MeetingSessionRetrieveRecordingsResponse(BaseModel):
    data: List[Data]
    """
    Temporary download URLs for recordings held by the Meeting service, including
    Zoom and existing Google Meet and Teams recordings. Empty for customer Storage
    exports; use recording_export instead. Choose the download method from these
    fields rather than the platform alone.
    """

    recording_export: Optional[MeetingSessionRecordingExport] = None
    """Customer Storage recording reference.

    Pending is not downloadable; exported means upload was verified; failed is
    terminal. Download with ordinary Storage authorization. No presigned URL is
    returned.
    """
