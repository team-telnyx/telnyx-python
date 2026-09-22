# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FuncLogExportConfigResponse", "Data"]


class Data(BaseModel):
    """Metadata-only view of a function's log export destination.

    Header values are write-only (encrypted server-side) and never appear in any response.
    """

    id: Optional[str] = None
    """Configuration record ID"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether export is enabled for this function"""

    endpoint: Optional[str] = None
    """HTTPS OTLP endpoint URL logs are pushed to"""

    func_id: Optional[str] = None
    """Function ID this configuration belongs to"""

    invocation_export_enabled: Optional[bool] = None
    """Whether invocation records (one per HTTP request) are exported"""

    record_type: Optional[Literal["compute_func_log_export_config"]] = None

    runtime_export_enabled: Optional[bool] = None
    """Whether runtime logs (function stdout/stderr) are exported"""

    updated_at: Optional[datetime] = None


class FuncLogExportConfigResponse(BaseModel):
    data: Optional[Data] = None
    """Metadata-only view of a function's log export destination.

    Header values are write-only (encrypted server-side) and never appear in any
    response.
    """
