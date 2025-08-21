# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .portout_report import PortoutReport

__all__ = ["ReportCreateResponse"]


class ReportCreateResponse(BaseModel):
    data: Optional[PortoutReport] = None
