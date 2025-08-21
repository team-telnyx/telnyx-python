# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["SiprecSiprecSidJsonResponse"]


class SiprecSiprecSidJsonResponse(BaseModel):
    account_sid: Optional[str] = None
    """The id of the account the resource belongs to."""

    call_sid: Optional[str] = None
    """The id of the call the resource belongs to."""

    date_updated: Optional[str] = None
    """The date and time the siprec session was last updated."""

    error_code: Optional[str] = None
    """The error code of the siprec session."""

    sid: Optional[str] = None
    """The SID of the siprec session."""

    status: Optional[Literal["in-progress", "stopped"]] = None
    """The status of the siprec session."""

    uri: Optional[str] = None
    """The URI of the siprec session."""
