# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RcsSuggestionParam",
    "Action",
    "ActionCreateCalendarEventAction",
    "ActionDialAction",
    "ActionOpenURLAction",
    "ActionViewLocationAction",
    "ActionViewLocationActionLatLong",
    "Reply",
]


class ActionCreateCalendarEventAction(TypedDict, total=False):
    description: str
    """Event description. Maximum 500 characters."""

    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    title: str
    """Event title. Maximum 100 characters."""


class ActionDialAction(TypedDict, total=False):
    phone_number: Required[str]
    """Phone number in +E.164 format"""


class ActionOpenURLAction(TypedDict, total=False):
    application: Required[Literal["OPEN_URL_APPLICATION_UNSPECIFIED", "BROWSER", "WEBVIEW"]]
    """URL open application, browser or webview."""

    url: Required[str]

    webview_view_mode: Required[Literal["WEBVIEW_VIEW_MODE_UNSPECIFIED", "FULL", "HALF", "TALL"]]

    description: str
    """Accessbility description for webview."""


class ActionViewLocationActionLatLong(TypedDict, total=False):
    latitude: Required[float]
    """The latitude in degrees. It must be in the range [-90.0, +90.0]."""

    longitude: Required[float]
    """The longitude in degrees. It must be in the range [-180.0, +180.0]."""


class ActionViewLocationAction(TypedDict, total=False):
    label: str
    """The label of the pin dropped"""

    lat_long: ActionViewLocationActionLatLong

    query: str
    """query string (Android only)"""


class Action(TypedDict, total=False):
    create_calendar_event_action: ActionCreateCalendarEventAction
    """
    Opens the user's default calendar app and starts the new calendar event flow
    with the agent-specified event data pre-filled.
    """

    dial_action: ActionDialAction
    """
    Opens the user's default dialer app with the agent-specified phone number filled
    in.
    """

    fallback_url: str
    """Fallback URL to use if a client doesn't support a suggested action.

    Fallback URLs open in new browser windows. Maximum 2048 characters.
    """

    open_url_action: ActionOpenURLAction
    """Opens the user's default web browser app to the specified URL."""

    postback_data: str
    """
    Payload (base64 encoded) that will be sent to the agent in the user event that
    results when the user taps the suggested action. Maximum 2048 characters.
    """

    share_location_action: object
    """
    Opens the RCS app's location chooser so the user can pick a location to send
    back to the agent.
    """

    text: str
    """Text that is shown in the suggested action. Maximum 25 characters."""

    view_location_action: ActionViewLocationAction
    """Opens the user's default map app and selects the agent-specified location."""


class Reply(TypedDict, total=False):
    postback_data: str
    """
    Payload (base64 encoded) that will be sent to the agent in the user event that
    results when the user taps the suggested action. Maximum 2048 characters.
    """

    text: str
    """Text that is shown in the suggested reply (maximum 25 characters)"""


class RcsSuggestionParam(TypedDict, total=False):
    action: Action
    """When tapped, initiates the corresponding native action on the device."""

    reply: Reply
