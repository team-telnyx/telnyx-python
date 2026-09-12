# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .functions_observability_pagination_meta import FunctionsObservabilityPaginationMeta

__all__ = ["FuncRetrieveRevisionsResponse", "Data"]


class Data(BaseModel):
    active: Optional[bool] = None

    build_ok_at: Optional[datetime] = None

    build_status: Optional[str] = None

    commit_sha: Optional[str] = None

    deploy_status: Optional[str] = None

    failure_reason: Optional[str] = None

    failure_stage: Optional[str] = None

    image: Optional[str] = None

    record_type: Optional[str] = None

    revision_id: Optional[str] = None

    shipped_at: Optional[datetime] = None

    shipped_by: Optional[str] = None


class FuncRetrieveRevisionsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[FunctionsObservabilityPaginationMeta] = None
