# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CalendarConnectionCreateResponse", "Data"]


class Data(BaseModel):
    oauth_url: str
    """Open in a browser to authorize calendar access."""

    platform: Literal["google_calendar", "microsoft_outlook"]
    """Calendar provider: Google Calendar or Microsoft Outlook."""

    status: Literal["pending_oauth"]
    """Authorization has not completed."""


class CalendarConnectionCreateResponse(BaseModel):
    data: Data
