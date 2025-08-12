# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ClusterComputeParams"]


class ClusterComputeParams(TypedDict, total=False):
    bucket: Required[str]
    """The embedded storage bucket to compute the clusters from.

    The bucket must already be
    [embedded](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding).
    """

    files: List[str]
    """Array of files to filter which are included."""

    min_cluster_size: int
    """Smallest number of related text chunks to qualify as a cluster.

    Top-level clusters should be thought of as identifying broad themes in your
    data.
    """

    min_subcluster_size: int
    """Smallest number of related text chunks to qualify as a sub-cluster.

    Sub-clusters should be thought of as identifying more specific topics within a
    broader theme.
    """

    prefix: str
    """Prefix to filter whcih files in the buckets are included."""
