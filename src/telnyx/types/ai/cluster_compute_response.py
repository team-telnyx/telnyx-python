# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["ClusterComputeResponse", "Data"]


class Data(BaseModel):
    task_id: str


class ClusterComputeResponse(BaseModel):
    data: Data
