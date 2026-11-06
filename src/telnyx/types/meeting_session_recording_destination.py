# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["MeetingSessionRecordingDestination"]


class MeetingSessionRecordingDestination(BaseModel):
    """Customer-owned Telnyx Storage destination for recording exports.

    Uses the authenticated organization and user; do not supply credentials, region, organization ID or object key.
    """

    bucket: str
    """Existing accessible bucket.

    Consecutive dots and IPv4-address names are rejected.
    """

    prefix: Optional[str] = None
    """Optional object-key prefix.

    One trailing slash is normalized. Empty path segments, . and .. segments are
    rejected.
    """
