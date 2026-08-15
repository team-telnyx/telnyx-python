# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MeetingSessionListParams"]


class MeetingSessionListParams(TypedDict, total=False):
    status: Literal[
        "scheduled", "joining", "waiting_for_admission", "active", "leaving", "ended", "failed", "admission_denied"
    ]
    """Filter meeting sessions by current status."""
