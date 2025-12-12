# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel
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
