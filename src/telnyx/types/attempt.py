# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .http import HTTP
from .._models import BaseModel

__all__ = ["Attempt"]


class Attempt(BaseModel):
    """Webhook delivery attempt details."""

    errors: Optional[List[int]] = None
    """Webhook delivery error codes."""

    finished_at: Optional[datetime] = None
    """ISO 8601 timestamp indicating when the attempt has finished."""

    http: Optional[HTTP] = None
    """HTTP request and response information."""

    started_at: Optional[datetime] = None
    """ISO 8601 timestamp indicating when the attempt was initiated."""

    status: Optional[Literal["delivered", "failed"]] = None
