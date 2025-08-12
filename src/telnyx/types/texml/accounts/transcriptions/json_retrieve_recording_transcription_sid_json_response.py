# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["JsonRetrieveRecordingTranscriptionSidJsonResponse"]


class JsonRetrieveRecordingTranscriptionSidJsonResponse(BaseModel):
    account_sid: Optional[str] = None

    api_version: Optional[str] = None
    """The version of the API that was used to make the request."""

    call_sid: Optional[str] = None

    date_created: Optional[datetime] = None

    date_updated: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration of this recording, given in seconds."""

    recording_sid: Optional[str] = None
    """Identifier of a resource."""

    sid: Optional[str] = None
    """Identifier of a resource."""

    status: Optional[Literal["in-progress", "completed"]] = None
    """The status of the recording transcriptions.

    The transcription text will be available only when the status is completed.
    """

    transcription_text: Optional[str] = None
    """The recording's transcribed text"""

    uri: Optional[str] = None
    """The relative URI for the recording transcription resource."""
