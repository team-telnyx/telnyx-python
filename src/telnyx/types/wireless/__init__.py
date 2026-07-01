# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .detail_records_report_list_params import DetailRecordsReportListParams as DetailRecordsReportListParams
from .detail_records_report_create_params import DetailRecordsReportCreateParams as DetailRecordsReportCreateParams

if TYPE_CHECKING:
    from .wdr_report import WdrReport as WdrReport
    from .detail_records_report_list_response import DetailRecordsReportListResponse as DetailRecordsReportListResponse
    from .detail_records_report_create_response import (
        DetailRecordsReportCreateResponse as DetailRecordsReportCreateResponse,
    )
    from .detail_records_report_delete_response import (
        DetailRecordsReportDeleteResponse as DetailRecordsReportDeleteResponse,
    )
    from .detail_records_report_retrieve_response import (
        DetailRecordsReportRetrieveResponse as DetailRecordsReportRetrieveResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "WdrReport":
        from .wdr_report import WdrReport

        return WdrReport
    if name == "DetailRecordsReportCreateResponse":
        from .detail_records_report_create_response import DetailRecordsReportCreateResponse

        return DetailRecordsReportCreateResponse
    if name == "DetailRecordsReportRetrieveResponse":
        from .detail_records_report_retrieve_response import DetailRecordsReportRetrieveResponse

        return DetailRecordsReportRetrieveResponse
    if name == "DetailRecordsReportListResponse":
        from .detail_records_report_list_response import DetailRecordsReportListResponse

        return DetailRecordsReportListResponse
    if name == "DetailRecordsReportDeleteResponse":
        from .detail_records_report_delete_response import DetailRecordsReportDeleteResponse

        return DetailRecordsReportDeleteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
