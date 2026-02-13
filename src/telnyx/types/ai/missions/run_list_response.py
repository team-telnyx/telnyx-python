# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    mission_id: str

    run_id: str

    started_at: datetime

    status: Literal["pending", "running", "paused", "succeeded", "failed", "cancelled"]

    updated_at: datetime

    error: Optional[str] = None

    finished_at: Optional[datetime] = None

    input: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None

    result_payload: Optional[Dict[str, object]] = None

    result_summary: Optional[str] = None
