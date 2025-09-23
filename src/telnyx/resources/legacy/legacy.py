# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .reporting.reporting import (
    ReportingResource,
    AsyncReportingResource,
    ReportingResourceWithRawResponse,
    AsyncReportingResourceWithRawResponse,
    ReportingResourceWithStreamingResponse,
    AsyncReportingResourceWithStreamingResponse,
)

__all__ = ["LegacyResource", "AsyncLegacyResource"]


class LegacyResource(SyncAPIResource):
    @cached_property
    def reporting(self) -> ReportingResource:
        return ReportingResource(self._client)

    @cached_property
    def with_raw_response(self) -> LegacyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LegacyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LegacyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LegacyResourceWithStreamingResponse(self)


class AsyncLegacyResource(AsyncAPIResource):
    @cached_property
    def reporting(self) -> AsyncReportingResource:
        return AsyncReportingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLegacyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLegacyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLegacyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLegacyResourceWithStreamingResponse(self)


class LegacyResourceWithRawResponse:
    def __init__(self, legacy: LegacyResource) -> None:
        self._legacy = legacy

    @cached_property
    def reporting(self) -> ReportingResourceWithRawResponse:
        return ReportingResourceWithRawResponse(self._legacy.reporting)


class AsyncLegacyResourceWithRawResponse:
    def __init__(self, legacy: AsyncLegacyResource) -> None:
        self._legacy = legacy

    @cached_property
    def reporting(self) -> AsyncReportingResourceWithRawResponse:
        return AsyncReportingResourceWithRawResponse(self._legacy.reporting)


class LegacyResourceWithStreamingResponse:
    def __init__(self, legacy: LegacyResource) -> None:
        self._legacy = legacy

    @cached_property
    def reporting(self) -> ReportingResourceWithStreamingResponse:
        return ReportingResourceWithStreamingResponse(self._legacy.reporting)


class AsyncLegacyResourceWithStreamingResponse:
    def __init__(self, legacy: AsyncLegacyResource) -> None:
        self._legacy = legacy

    @cached_property
    def reporting(self) -> AsyncReportingResourceWithStreamingResponse:
        return AsyncReportingResourceWithStreamingResponse(self._legacy.reporting)
