# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RecursiveCluster", "Node"]


class Node(BaseModel):
    filename: str
    """
    The corresponding source file of your embedded storage bucket that the node is
    from.
    """

    text: str
    """The text of the node."""


class RecursiveCluster(BaseModel):
    cluster_id: str

    cluster_summary: str

    total_number_of_nodes: int

    cluster_header: Optional[str] = None

    nodes: Optional[List[Node]] = None

    subclusters: Optional[List["RecursiveCluster"]] = None
