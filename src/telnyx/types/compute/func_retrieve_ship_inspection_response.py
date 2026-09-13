# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FuncRetrieveShipInspectionResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = None

    reason: Optional[str] = None

    record_type: Optional[Literal["build_log_inspection"]] = None
    """Stable record type retained by both inspection path aliases."""

    runtime: Optional[str] = None

    snippet: Optional[str] = None

    stage: Optional[Literal["build", "platform", "pre_build", "deploy", "security_review", "none", "pending"]] = None


class FuncRetrieveShipInspectionResponse(BaseModel):
    data: Optional[Data] = None
