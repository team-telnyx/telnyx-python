# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BrowserSessionRetrieveArtifactResponse", "Data"]


class Data(BaseModel):
    id: str

    action_id: str

    checksum: str

    content_type: str

    created_at: datetime

    download_url: str
    """Signed relative path (starts with /v2/artifact_downloads/).

    Prepend your API host, e.g. https://api.telnyx.com, before calling it.
    """

    expires_at: datetime

    session_id: str

    size_bytes: int

    type: str


class BrowserSessionRetrieveArtifactResponse(BaseModel):
    data: Optional[Data] = None
