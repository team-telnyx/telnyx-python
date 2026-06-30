# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..messaging_10dlc.task_status import TaskStatus

__all__ = ["ClusterListResponse"]


class ClusterListResponse(BaseModel):
    bucket: str

    created_at: datetime

    finished_at: datetime

    min_cluster_size: int

    min_subcluster_size: int

    status: TaskStatus

    task_id: str
