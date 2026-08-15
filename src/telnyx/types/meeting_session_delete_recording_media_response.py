# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeetingSessionDeleteRecordingMediaResponse", "Data"]


class Data(BaseModel):
    deletion_status: Literal["requested", "already_in_progress"]

    meeting_session_id: str
    """The account-scoped Meeting Session identifier."""

    provider: Literal["recall"]

    scope: Literal["provider_recording_media"]


class MeetingSessionDeleteRecordingMediaResponse(BaseModel):
    data: Data
