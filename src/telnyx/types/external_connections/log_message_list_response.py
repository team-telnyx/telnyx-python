# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LogMessageListResponse", "Meta", "Source"]


class Meta(BaseModel):
    external_connection_id: Optional[str] = None
    """The external connection the log message is associated with, if any."""

    telephone_number: Optional[str] = None
    """The telephone number the log message is associated with, if any."""

    ticket_id: Optional[str] = None
    """The ticket ID for an operation that generated the log message, if any."""


class Source(BaseModel):
    pointer: Optional[str] = None
    """JSON pointer (RFC6901) to the offending entity."""


class LogMessageListResponse(BaseModel):
    code: str

    title: str

    detail: Optional[str] = None

    meta: Optional[Meta] = None

    source: Optional[Source] = None
