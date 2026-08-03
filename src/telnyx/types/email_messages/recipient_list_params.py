# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RecipientListParams"]


class RecipientListParams(TypedDict, total=False):
    kind: Literal["to", "cc", "bcc"]
    """Filter recipients by address kind."""

    page_cursor: str
    """Opaque URL-safe Base64 cursor returned by a previous list response."""

    page_size: int
    """Number of results to return.

    Defaults to 25; maximum is 100. Invalid values are clamped to the valid range.
    """

    status: Literal["queued", "sending", "sent", "deferred", "delivered", "bounced", "failed", "gw_reject", "cancelled"]
    """Filter recipients by status."""
