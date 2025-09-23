# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .usage_reports.usage_reports import (
    UsageReportsResource,
    AsyncUsageReportsResource,
    UsageReportsResourceWithRawResponse,
    AsyncUsageReportsResourceWithRawResponse,
    UsageReportsResourceWithStreamingResponse,
    AsyncUsageReportsResourceWithStreamingResponse,
)
from .batch_detail_records.batch_detail_records import (
    BatchDetailRecordsResource,
    AsyncBatchDetailRecordsResource,
    BatchDetailRecordsResourceWithRawResponse,
    AsyncBatchDetailRecordsResourceWithRawResponse,
    BatchDetailRecordsResourceWithStreamingResponse,
    AsyncBatchDetailRecordsResourceWithStreamingResponse,
)

__all__ = ["ReportingResource", "AsyncReportingResource"]


class ReportingResource(SyncAPIResource):
    @cached_property
    def batch_detail_records(self) -> BatchDetailRecordsResource:
        return BatchDetailRecordsResource(self._client)

    @cached_property
    def usage_reports(self) -> UsageReportsResource:
        return UsageReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ReportingResourceWithStreamingResponse(self)


class AsyncReportingResource(AsyncAPIResource):
    @cached_property
    def batch_detail_records(self) -> AsyncBatchDetailRecordsResource:
        return AsyncBatchDetailRecordsResource(self._client)

    @cached_property
    def usage_reports(self) -> AsyncUsageReportsResource:
        return AsyncUsageReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncReportingResourceWithStreamingResponse(self)


class ReportingResourceWithRawResponse:
    def __init__(self, reporting: ReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def batch_detail_records(self) -> BatchDetailRecordsResourceWithRawResponse:
        return BatchDetailRecordsResourceWithRawResponse(self._reporting.batch_detail_records)

    @cached_property
    def usage_reports(self) -> UsageReportsResourceWithRawResponse:
        return UsageReportsResourceWithRawResponse(self._reporting.usage_reports)


class AsyncReportingResourceWithRawResponse:
    def __init__(self, reporting: AsyncReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def batch_detail_records(self) -> AsyncBatchDetailRecordsResourceWithRawResponse:
        return AsyncBatchDetailRecordsResourceWithRawResponse(self._reporting.batch_detail_records)

    @cached_property
    def usage_reports(self) -> AsyncUsageReportsResourceWithRawResponse:
        return AsyncUsageReportsResourceWithRawResponse(self._reporting.usage_reports)


class ReportingResourceWithStreamingResponse:
    def __init__(self, reporting: ReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def batch_detail_records(self) -> BatchDetailRecordsResourceWithStreamingResponse:
        return BatchDetailRecordsResourceWithStreamingResponse(self._reporting.batch_detail_records)

    @cached_property
    def usage_reports(self) -> UsageReportsResourceWithStreamingResponse:
        return UsageReportsResourceWithStreamingResponse(self._reporting.usage_reports)


class AsyncReportingResourceWithStreamingResponse:
    def __init__(self, reporting: AsyncReportingResource) -> None:
        self._reporting = reporting

    @cached_property
    def batch_detail_records(self) -> AsyncBatchDetailRecordsResourceWithStreamingResponse:
        return AsyncBatchDetailRecordsResourceWithStreamingResponse(self._reporting.batch_detail_records)

    @cached_property
    def usage_reports(self) -> AsyncUsageReportsResourceWithStreamingResponse:
        return AsyncUsageReportsResourceWithStreamingResponse(self._reporting.usage_reports)
