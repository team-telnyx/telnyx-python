# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "RcsSuggestion",
    "Action",
    "ActionCreateCalendarEventAction",
    "ActionDialAction",
    "ActionOpenURLAction",
    "ActionViewLocationAction",
    "ActionViewLocationActionLatLong",
    "Reply",
]


class ActionCreateCalendarEventAction(BaseModel):
    description: Optional[str] = None
    """Event description. Maximum 500 characters."""

    end_time: Optional[datetime] = None

    start_time: Optional[datetime] = None

    title: Optional[str] = None
    """Event title. Maximum 100 characters."""


class ActionDialAction(BaseModel):
    phone_number: str
    """Phone number in +E.164 format"""


class ActionOpenURLAction(BaseModel):
    application: Literal["OPEN_URL_APPLICATION_UNSPECIFIED", "BROWSER", "WEBVIEW"]
    """URL open application, browser or webview."""

    url: str

    webview_view_mode: Literal["WEBVIEW_VIEW_MODE_UNSPECIFIED", "FULL", "HALF", "TALL"]

    description: Optional[str] = None
    """Accessbility description for webview."""


class ActionViewLocationActionLatLong(BaseModel):
    latitude: float
    """The latitude in degrees. It must be in the range [-90.0, +90.0]."""

    longitude: float
    """The longitude in degrees. It must be in the range [-180.0, +180.0]."""


class ActionViewLocationAction(BaseModel):
    label: Optional[str] = None
    """The label of the pin dropped"""

    lat_long: Optional[ActionViewLocationActionLatLong] = None

    query: Optional[str] = None
    """query string (Android only)"""


class Action(BaseModel):
    create_calendar_event_action: Optional[ActionCreateCalendarEventAction] = None
    """
    Opens the user's default calendar app and starts the new calendar event flow
    with the agent-specified event data pre-filled.
    """

    dial_action: Optional[ActionDialAction] = None
    """
    Opens the user's default dialer app with the agent-specified phone number filled
    in.
    """

    fallback_url: Optional[str] = None
    """Fallback URL to use if a client doesn't support a suggested action.

    Fallback URLs open in new browser windows. Maximum 2048 characters.
    """

    open_url_action: Optional[ActionOpenURLAction] = None
    """Opens the user's default web browser app to the specified URL."""

    postback_data: Optional[str] = None
    """
    Payload (base64 encoded) that will be sent to the agent in the user event that
    results when the user taps the suggested action. Maximum 2048 characters.
    """

    share_location_action: Optional[object] = None
    """
    Opens the RCS app's location chooser so the user can pick a location to send
    back to the agent.
    """

    text: Optional[str] = None
    """Text that is shown in the suggested action. Maximum 25 characters."""

    view_location_action: Optional[ActionViewLocationAction] = None
    """Opens the user's default map app and selects the agent-specified location."""


class Reply(BaseModel):
    postback_data: Optional[str] = None
    """
    Payload (base64 encoded) that will be sent to the agent in the user event that
    results when the user taps the suggested action. Maximum 2048 characters.
    """

    text: Optional[str] = None
    """Text that is shown in the suggested reply (maximum 25 characters)"""


class RcsSuggestion(BaseModel):
    action: Optional[Action] = None
    """When tapped, initiates the corresponding native action on the device."""

    reply: Optional[Reply] = None
