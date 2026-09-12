# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .functions_observability_pagination_meta import FunctionsObservabilityPaginationMeta

__all__ = ["FuncRetrieveMetricAggregatesResponse", "Data"]


class Data(BaseModel):
    cpu_used_cores_avg: Optional[float] = None

    cpu_used_cores_max: Optional[float] = None

    end_time: Optional[datetime] = None

    function_id: Optional[str] = None

    function_name: Optional[str] = None

    memory_used_bytes_avg: Optional[float] = None

    memory_used_bytes_max: Optional[float] = None

    product: Optional[str] = None

    record_type: Optional[str] = None

    request_client_error_rate: Optional[float] = None

    request_count: Optional[float] = None

    request_error_rate: Optional[float] = None

    request_latency_avg_ms: Optional[float] = None

    request_latency_p50_ms: Optional[float] = None

    request_latency_p95_ms: Optional[float] = None

    request_latency_p99_ms: Optional[float] = None

    request_success_rate: Optional[float] = None

    start_time: Optional[datetime] = None


class FuncRetrieveMetricAggregatesResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[FunctionsObservabilityPaginationMeta] = None
