# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .meeting_session import MeetingSession

__all__ = ["MeetingSessionResponse"]


class MeetingSessionResponse(BaseModel):
    data: MeetingSession
    """Represents a meeting session.

    Core serializer fields are required; platform-specific fields are optional.
    Nullable fields use null when absent. No actor, provider-bot, idempotency,
    routing, key, or internal fields are exposed.
    """
