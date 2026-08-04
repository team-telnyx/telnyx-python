# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .mdr_usage_report_list_params import MdrUsageReportListParams as MdrUsageReportListParams
from .mdr_usage_report_create_params import MdrUsageReportCreateParams as MdrUsageReportCreateParams
from .cdr_usage_report_fetch_sync_params import CdrUsageReportFetchSyncParams as CdrUsageReportFetchSyncParams
from .mdr_usage_report_fetch_sync_params import MdrUsageReportFetchSyncParams as MdrUsageReportFetchSyncParams

if TYPE_CHECKING:
    from .mdr_usage_report import MdrUsageReport as MdrUsageReport
    from .mdr_usage_report_create_response import MdrUsageReportCreateResponse as MdrUsageReportCreateResponse
    from .mdr_usage_report_delete_response import MdrUsageReportDeleteResponse as MdrUsageReportDeleteResponse
    from .mdr_usage_report_retrieve_response import MdrUsageReportRetrieveResponse as MdrUsageReportRetrieveResponse
    from .cdr_usage_report_fetch_sync_response import CdrUsageReportFetchSyncResponse as CdrUsageReportFetchSyncResponse
    from .mdr_usage_report_fetch_sync_response import MdrUsageReportFetchSyncResponse as MdrUsageReportFetchSyncResponse
    from .reporting_pagination_meta_77109e5d17 import (
        ReportingPaginationMeta77109e5d17 as ReportingPaginationMeta77109e5d17,
    )


def __getattr__(name: str) -> Any:
    if name == "CdrUsageReportFetchSyncResponse":
        from .cdr_usage_report_fetch_sync_response import CdrUsageReportFetchSyncResponse

        return CdrUsageReportFetchSyncResponse
    if name == "MdrUsageReport":
        from .mdr_usage_report import MdrUsageReport

        return MdrUsageReport
    if name == "ReportingPaginationMeta77109e5d17":
        from .reporting_pagination_meta_77109e5d17 import ReportingPaginationMeta77109e5d17

        return ReportingPaginationMeta77109e5d17
    if name == "MdrUsageReportCreateResponse":
        from .mdr_usage_report_create_response import MdrUsageReportCreateResponse

        return MdrUsageReportCreateResponse
    if name == "MdrUsageReportRetrieveResponse":
        from .mdr_usage_report_retrieve_response import MdrUsageReportRetrieveResponse

        return MdrUsageReportRetrieveResponse
    if name == "MdrUsageReportDeleteResponse":
        from .mdr_usage_report_delete_response import MdrUsageReportDeleteResponse

        return MdrUsageReportDeleteResponse
    if name == "MdrUsageReportFetchSyncResponse":
        from .mdr_usage_report_fetch_sync_response import MdrUsageReportFetchSyncResponse

        return MdrUsageReportFetchSyncResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
