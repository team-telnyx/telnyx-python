# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CallStreamsJsonResponse"]


class CallStreamsJsonResponse(BaseModel):
    account_sid: Optional[str] = None

    call_sid: Optional[str] = None

    date_updated: Optional[datetime] = None

    name: Optional[str] = None
    """The user specified name of Stream."""

    sid: Optional[str] = None
    """Identifier of a resource."""

    status: Optional[Literal["in-progress"]] = None
    """The status of the streaming."""

    uri: Optional[str] = None
    """The relative URI for this streaming resource."""
