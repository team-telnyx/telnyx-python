# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from ..task_status import TaskStatus

__all__ = ["ClusterRetrieveResponse", "Data"]


class Data(BaseModel):
    bucket: str

    clusters: List["RecursiveCluster"]

    status: TaskStatus


class ClusterRetrieveResponse(BaseModel):
    data: Data


from .recursive_cluster import RecursiveCluster
