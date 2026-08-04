# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailEventListParams"]


class EmailEventListParams(TypedDict, total=False):
    email_id: str
    """Filter events for a specific email message UUID.

    Invalid UUID values are silently ignored (no filter applied).
    """

    event_type: Union[str, SequenceNotStr[str]]
    """Comma-separated list of event types to include.

    Also accepts repeated query parameters (e.g.
    event_type=delivered&event_type=bounced). Unknown values return no matches.
    """

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Inclusive ISO 8601 start timestamp. Defaults to 30 days ago when omitted."""

    page_cursor: str
    """Opaque URL-safe Base64 cursor returned by a previous list response."""

    page_size: int
    """Number of results to return.

    Defaults to 25; maximum is 100. Invalid values are clamped to the valid range.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Inclusive ISO 8601 end timestamp.

    When `from` is provided without `to`, defaults to `from + 30 days`.
    """
