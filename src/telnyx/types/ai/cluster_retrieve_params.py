# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClusterRetrieveParams"]


class ClusterRetrieveParams(TypedDict, total=False):
    show_subclusters: bool
    """Whether or not to include subclusters and their nodes in the response."""

    top_n_nodes: int
    """The number of nodes in the cluster to return in the response.

    Nodes will be sorted by their centrality within the cluster.
    """
