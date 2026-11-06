# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CalendarRetrieveOAuthCallbackParams"]


class CalendarRetrieveOAuthCallbackParams(TypedDict, total=False):
    code: str
    """Authorization code supplied by the calendar provider."""

    error: str
    """Authorization error supplied by the calendar provider, such as access_denied."""

    state: str
    """Unmodified signed state from the authorization URL."""
