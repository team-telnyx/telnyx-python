# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .func_log_export_config import FuncLogExportConfig

__all__ = ["FuncLogExportConfigResponse"]


class FuncLogExportConfigResponse(BaseModel):
    data: Optional[FuncLogExportConfig] = None
    """Metadata-only view of a function's log export destination.

    Header values are write-only (encrypted server-side) and never appear in any
    response.
    """
