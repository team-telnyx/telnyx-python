# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..external_voice_integrations_pagination_meta import ExternalVoiceIntegrationsPaginationMeta

__all__ = ["LogMessageListResponse", "LogMessage", "LogMessageMeta", "LogMessageSource"]


class LogMessageMeta(BaseModel):
    external_connection_id: Optional[str] = None
    """The external connection the log message is associated with, if any."""

    telephone_number: Optional[str] = None
    """The telephone number the log message is associated with, if any."""

    ticket_id: Optional[str] = None
    """The ticket ID for an operation that generated the log message, if any."""


class LogMessageSource(BaseModel):
    pointer: Optional[str] = None
    """JSON pointer (RFC6901) to the offending entity."""


class LogMessage(BaseModel):
    code: str

    title: str

    detail: Optional[str] = None

    meta: Optional[LogMessageMeta] = None

    source: Optional[LogMessageSource] = None


class LogMessageListResponse(BaseModel):
    log_messages: Optional[List[LogMessage]] = None

    meta: Optional[ExternalVoiceIntegrationsPaginationMeta] = None
