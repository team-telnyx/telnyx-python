# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .log_message import LogMessage

__all__ = ["LogMessageRetrieveResponse"]


class LogMessageRetrieveResponse(BaseModel):
    log_messages: Optional[List[LogMessage]] = None
