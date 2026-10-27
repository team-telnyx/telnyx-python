# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DedicatedIPListParams"]


class DedicatedIPListParams(TypedDict, total=False):
    filter_pool_id: Annotated[str, PropertyInfo(alias="filter[pool_id]")]
    """Return only IPs in this pool (exact match on `pool_id`).

    A value that is not a UUID returns an empty list. An empty value applies no
    filter.
    """

    filter_region: Annotated[str, PropertyInfo(alias="filter[region]")]
    """Return only IPs in this region (exact, case-sensitive match on `region`).

    An empty value applies no filter.
    """

    filter_status: Annotated[
        Literal["provisioning", "warming_up", "active", "suspended", "released"], PropertyInfo(alias="filter[status]")
    ]
    """Return only IPs in this lifecycle status (exact match).

    Any other value returns an empty list. An empty value applies no filter.
    """
