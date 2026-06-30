# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..messaging_10dlc.task_status import TaskStatus

__all__ = ["ClusterRetrieveResponse", "Data"]


class Data(BaseModel):
    bucket: str

    clusters: List["RecursiveCluster"]

    status: TaskStatus


class ClusterRetrieveResponse(BaseModel):
    data: Data


from .recursive_cluster import RecursiveCluster
