# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TrackingSettingsParam"]


class TrackingSettingsParam(TypedDict, total=False):
    """Per-send open and click tracking overrides.

    Omitted properties inherit the sender domain's tracking settings.
    """

    click_tracking: bool
    """Whether to rewrite links for click tracking in this message."""

    open_tracking: bool
    """Whether to inject an open-tracking pixel for this message."""
