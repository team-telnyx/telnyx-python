# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DomainsTrackingSettingsParam"]


class DomainsTrackingSettingsParam(TypedDict, total=False):
    click_tracking: bool
    """Rewrite HTML links through a tracking redirect to record click events."""

    open_tracking: bool
    """Inject a tracking pixel into HTML messages to record open events."""

    unsubscribe_tracking: bool
    """Add RFC 8058 List-Unsubscribe headers with a signed one-click unsubscribe URL.

    Enabled by default; Gmail/Yahoo bulk-sender rules require one-click unsubscribe
    support.
    """
