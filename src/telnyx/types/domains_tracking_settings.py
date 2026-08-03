# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["DomainsTrackingSettings"]


class DomainsTrackingSettings(BaseModel):
    click_tracking: Optional[bool] = None
    """Rewrite HTML links through a tracking redirect to record click events."""

    open_tracking: Optional[bool] = None
    """Inject a tracking pixel into HTML messages to record open events."""

    unsubscribe_tracking: Optional[bool] = None
    """Add RFC 8058 List-Unsubscribe headers with a signed one-click unsubscribe URL.

    Enabled by default; Gmail/Yahoo bulk-sender rules require one-click unsubscribe
    support.
    """
