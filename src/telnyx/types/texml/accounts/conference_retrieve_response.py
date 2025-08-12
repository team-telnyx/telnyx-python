# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ConferenceRetrieveResponse"]


class ConferenceRetrieveResponse(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    api_version: Optional[str] = None
    """The version of the API that was used to make the request."""

    call_sid_ending_conference: Optional[str] = None
    """Caller ID, if present."""

    date_created: Optional[str] = None
    """The timestamp of when the resource was created."""

    date_updated: Optional[str] = None
    """The timestamp of when the resource was last updated."""

    friendly_name: Optional[str] = None
    """A string that you assigned to describe this conference room."""

    reason_conference_ended: Optional[
        Literal[
            "participant-with-end-conference-on-exit-left",
            "last-participant-left",
            "conference-ended-via-api",
            "time-exceeded",
        ]
    ] = None
    """The reason why a conference ended.

    When a conference is in progress, will be null.
    """

    region: Optional[str] = None
    """A string representing the region where the conference is hosted."""

    sid: Optional[str] = None
    """The unique identifier of the conference."""

    status: Optional[Literal["init", "in-progress", "completed"]] = None
    """The status of this conference."""

    subresource_uris: Optional[Dict[str, object]] = None
    """A list of related resources identified by their relative URIs."""

    uri: Optional[str] = None
    """The relative URI for this conference."""
