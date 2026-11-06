# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MeetingSessionRecordingDestinationParam"]


class MeetingSessionRecordingDestinationParam(TypedDict, total=False):
    """Customer-owned Telnyx Storage destination for recording exports.

    Uses the authenticated organization and user; do not supply credentials, region, organization ID or object key.
    """

    bucket: Required[str]
    """Existing accessible bucket.

    Consecutive dots and IPv4-address names are rejected.
    """

    prefix: str
    """Optional object-key prefix.

    One trailing slash is normalized. Empty path segments, . and .. segments are
    rejected.
    """
