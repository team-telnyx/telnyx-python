# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeetingSessionRecordingExport"]


class MeetingSessionRecordingExport(BaseModel):
    """Customer Storage recording reference.

    Pending is not downloadable; exported means upload was verified; failed is terminal. Download with ordinary Storage authorization. No presigned URL is returned.
    """

    bucket: str

    bytes: Optional[int] = None

    exported_at: Optional[datetime] = None

    key: str

    region: str

    status: Literal["pending", "exported", "failed"]

    type: Literal["video"]
