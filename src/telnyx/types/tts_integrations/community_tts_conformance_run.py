# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CommunityTtsConformanceRun"]


class CommunityTtsConformanceRun(BaseModel):
    """One recorded run of `test_connection`."""

    id: str

    checks: Dict[str, Literal["ok", "failed", "skipped"]]
    """
    Each check is `ok`, `failed` or `skipped`: `voices_url_reachable`,
    `voices_schema_valid`, `handshake`, `auth`, `init_accepted`, `audio_received`,
    `final_frame_received`, `clean_close`.
    """

    kind: Literal["test_connection", "conformance"]
    """`test_connection`: run by the owner.

    `conformance`: run by Telnyx during review.
    """

    success: bool
    """`true` when every check is `ok`."""

    error: Optional[str] = None
    """The first failure, in words."""

    latency_ms: Optional[int] = None
    """How long the whole run took."""

    started_at: Optional[datetime] = None

    time_to_first_audio_ms: Optional[int] = None

    voice_id: Optional[str] = None
