# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FuncRetrieveMetricAggregatesParams"]


class FuncRetrieveMetricAggregatesParams(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Exclusive window end, UTC ISO 8601 with milliseconds"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive window start, UTC ISO 8601 with milliseconds"""

    filter_edge_site: Annotated[str, PropertyInfo(alias="filter[edge_site]")]
    """Edge site filter"""

    filter_namespace: Annotated[str, PropertyInfo(alias="filter[namespace]")]
    """Kubernetes namespace filter"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
