# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .logs_meta import LogsMeta

__all__ = [
    "FuncRetrieveLogsResponse",
    "FuncRuntimeLogsResponse",
    "FuncRuntimeLogsResponseData",
    "FuncInvocationLogsResponse",
    "FuncInvocationLogsResponseData",
]


class FuncRuntimeLogsResponseData(BaseModel):
    level: Optional[str] = None

    message: Optional[str] = None

    record_type: Optional[Literal["compute_func_runtime_log"]] = None

    timestamp: Optional[datetime] = None


class FuncRuntimeLogsResponse(BaseModel):
    data: Optional[List[FuncRuntimeLogsResponseData]] = None

    meta: Optional[LogsMeta] = None


class FuncInvocationLogsResponseData(BaseModel):
    duration_ms: Optional[float] = None

    method: Optional[str] = None

    path: Optional[str] = None

    record_type: Optional[Literal["compute_func_invocation_log"]] = None

    region: Optional[str] = None

    request_size_bytes: Optional[int] = None

    response_size_bytes: Optional[int] = None

    status_code: Optional[int] = None

    timestamp: Optional[datetime] = None


class FuncInvocationLogsResponse(BaseModel):
    data: Optional[List[FuncInvocationLogsResponseData]] = None

    meta: Optional[LogsMeta] = None


FuncRetrieveLogsResponse: TypeAlias = Union[FuncRuntimeLogsResponse, FuncInvocationLogsResponse]
