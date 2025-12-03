# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from ..task_status import TaskStatus
from .assistants.tests.test_suites.meta import Meta

__all__ = ["ClusterListResponse", "Data"]


class Data(BaseModel):
    bucket: str

    created_at: datetime

    finished_at: datetime

    min_cluster_size: int

    min_subcluster_size: int

    status: TaskStatus

    task_id: str


class ClusterListResponse(BaseModel):
    data: List[Data]

    meta: Meta
