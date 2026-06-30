# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel
from .run_status import RunStatus

__all__ = ["MissionRunData"]


class MissionRunData(BaseModel):
    mission_id: str

    run_id: str

    started_at: datetime

    status: RunStatus

    updated_at: datetime

    error: Optional[str] = None

    finished_at: Optional[datetime] = None

    input: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None

    result_payload: Optional[Dict[str, object]] = None

    result_summary: Optional[str] = None
