# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .func_retrieve_logs_params import FuncRetrieveLogsParams as FuncRetrieveLogsParams
from .func_retrieve_logs_response import FuncRetrieveLogsResponse as FuncRetrieveLogsResponse
from .func_retrieve_revisions_params import FuncRetrieveRevisionsParams as FuncRetrieveRevisionsParams
from .func_retrieve_metric_aggregates_params import (
    FuncRetrieveMetricAggregatesParams as FuncRetrieveMetricAggregatesParams,
)

if TYPE_CHECKING:
    from .logs_meta import LogsMeta as LogsMeta
    from .func_retrieve_revisions_response import FuncRetrieveRevisionsResponse as FuncRetrieveRevisionsResponse
    from .func_retrieve_ship_inspection_response import (
        FuncRetrieveShipInspectionResponse as FuncRetrieveShipInspectionResponse,
    )
    from .functions_observability_pagination_meta import (
        FunctionsObservabilityPaginationMeta as FunctionsObservabilityPaginationMeta,
    )
    from .func_retrieve_metric_aggregates_response import (
        FuncRetrieveMetricAggregatesResponse as FuncRetrieveMetricAggregatesResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "FunctionsObservabilityPaginationMeta":
        from .functions_observability_pagination_meta import FunctionsObservabilityPaginationMeta

        return FunctionsObservabilityPaginationMeta
    if name == "LogsMeta":
        from .logs_meta import LogsMeta

        return LogsMeta
    if name == "FuncRetrieveMetricAggregatesResponse":
        from .func_retrieve_metric_aggregates_response import FuncRetrieveMetricAggregatesResponse

        return FuncRetrieveMetricAggregatesResponse
    if name == "FuncRetrieveRevisionsResponse":
        from .func_retrieve_revisions_response import FuncRetrieveRevisionsResponse

        return FuncRetrieveRevisionsResponse
    if name == "FuncRetrieveShipInspectionResponse":
        from .func_retrieve_ship_inspection_response import FuncRetrieveShipInspectionResponse

        return FuncRetrieveShipInspectionResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
