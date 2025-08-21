# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RecordingsJsonRecordingsJsonResponse"]


class RecordingsJsonRecordingsJsonResponse(BaseModel):
    account_sid: Optional[str] = None

    call_sid: Optional[str] = None

    channels: Optional[Literal[1, 2]] = None

    conference_sid: Optional[str] = None

    date_created: Optional[datetime] = None

    date_updated: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration of this recording, given in seconds."""

    error_code: Optional[str] = None

    price: Optional[str] = None
    """The price of this recording, the currency is specified in the price_unit field."""

    price_unit: Optional[str] = None
    """The unit in which the price is given."""

    sid: Optional[str] = None
    """Identifier of a resource."""

    source: Optional[
        Literal[
            "StartCallRecordingAPI",
            "StartConferenceRecordingAPI",
            "OutboundAPI",
            "DialVerb",
            "Conference",
            "RecordVerb",
            "Trunking",
        ]
    ] = None
    """Defines how the recording was created."""

    start_time: Optional[datetime] = None

    track: Optional[Literal["inbound", "outbound", "both"]] = None
    """The audio track to record for the call. The default is `both`."""

    uri: Optional[str] = None
    """The relative URI for this recording resource."""
