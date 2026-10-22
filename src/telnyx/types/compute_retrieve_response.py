# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ComputeRetrieveResponse", "Data", "DataPlacement", "DataPlacementClusterResult"]


class DataPlacementClusterResult(BaseModel):
    cluster_id: Optional[str] = None
    """Public region, or unknown when no mapping exists"""

    error: Optional[str] = None

    error_code: Optional[str] = None

    status: Optional[str] = None

    success: Optional[bool] = None


class DataPlacement(BaseModel):
    """Last deployment fan-out report, not a live probe.

    Omitted on actor types without a placement-aware deployment.
    """

    cluster_results: Optional[List[DataPlacementClusterResult]] = None

    clusters: Optional[List[str]] = None
    """Public regions with successful deployment"""

    excluded_clusters: Optional[List[str]] = None

    observed_at: Optional[str] = None
    """Optional ISO-8601 millisecond timestamp"""

    partial: Optional[bool] = None

    policy: Optional[Literal["everywhere", "single_site"]] = None

    unchecked_clusters: Optional[List[str]] = None


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    owner_function_id: Optional[str] = None
    """ID of the function that owns and ships this actor type.

    Empty when the type is unowned.
    """

    placement: Optional[DataPlacement] = None
    """Last deployment fan-out report, not a live probe.

    Omitted on actor types without a placement-aware deployment.
    """

    record_type: Optional[str] = None

    status: Optional[str] = None

    type: Optional[str] = None

    updated_at: Optional[str] = None


class ComputeRetrieveResponse(BaseModel):
    data: Optional[Data] = None
