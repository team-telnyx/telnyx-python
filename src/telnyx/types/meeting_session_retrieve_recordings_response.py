# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MeetingSessionRetrieveRecordingsResponse", "Data"]


class Data(BaseModel):
    expires_at: Optional[str] = None
    """Expiry timestamp when supplied by the provider, or null.

    The current adapter returns null.
    """

    type: str

    url: str
    """Current provider download URL.

    The API does not guarantee URL lifetime or refresh behavior.
    """


class MeetingSessionRetrieveRecordingsResponse(BaseModel):
    data: List[Data]
