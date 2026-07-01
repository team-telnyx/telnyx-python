# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .porting_report import PortingReport

__all__ = ["ReportRetrieveResponse"]


class ReportRetrieveResponse(BaseModel):
    data: Optional[PortingReport] = None
