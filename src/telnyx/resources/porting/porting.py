# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .loa_configurations import (
    LoaConfigurationsResource,
    AsyncLoaConfigurationsResource,
    LoaConfigurationsResourceWithRawResponse,
    AsyncLoaConfigurationsResourceWithRawResponse,
    LoaConfigurationsResourceWithStreamingResponse,
    AsyncLoaConfigurationsResourceWithStreamingResponse,
)
from ...types.porting_list_uk_carriers_response import PortingListUkCarriersResponse

__all__ = ["PortingResource", "AsyncPortingResource"]


class PortingResource(SyncAPIResource):
    """Endpoints related to porting orders management."""

    @cached_property
    def events(self) -> EventsResource:
        """Endpoints related to porting orders management."""
        return EventsResource(self._client)

    @cached_property
    def reports(self) -> ReportsResource:
        """Endpoints related to porting orders management."""
        return ReportsResource(self._client)

    @cached_property
    def loa_configurations(self) -> LoaConfigurationsResource:
        """Endpoints related to porting orders management."""
        return LoaConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PortingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PortingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PortingResourceWithStreamingResponse(self)

    def list_uk_carriers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortingListUkCarriersResponse:
        """List available carriers in the UK."""
        return self._get(
            "/porting/uk_carriers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingListUkCarriersResponse,
        )


class AsyncPortingResource(AsyncAPIResource):
    """Endpoints related to porting orders management."""

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Endpoints related to porting orders management."""
        return AsyncEventsResource(self._client)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        """Endpoints related to porting orders management."""
        return AsyncReportsResource(self._client)

    @cached_property
    def loa_configurations(self) -> AsyncLoaConfigurationsResource:
        """Endpoints related to porting orders management."""
        return AsyncLoaConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPortingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPortingResourceWithStreamingResponse(self)

    async def list_uk_carriers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortingListUkCarriersResponse:
        """List available carriers in the UK."""
        return await self._get(
            "/porting/uk_carriers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingListUkCarriersResponse,
        )


class PortingResourceWithRawResponse:
    def __init__(self, porting: PortingResource) -> None:
        self._porting = porting

        self.list_uk_carriers = to_raw_response_wrapper(
            porting.list_uk_carriers,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        return EventsResourceWithRawResponse(self._porting.events)

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        return ReportsResourceWithRawResponse(self._porting.reports)

    @cached_property
    def loa_configurations(self) -> LoaConfigurationsResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        return LoaConfigurationsResourceWithRawResponse(self._porting.loa_configurations)


class AsyncPortingResourceWithRawResponse:
    def __init__(self, porting: AsyncPortingResource) -> None:
        self._porting = porting

        self.list_uk_carriers = async_to_raw_response_wrapper(
            porting.list_uk_carriers,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        return AsyncEventsResourceWithRawResponse(self._porting.events)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        return AsyncReportsResourceWithRawResponse(self._porting.reports)

    @cached_property
    def loa_configurations(self) -> AsyncLoaConfigurationsResourceWithRawResponse:
        """Endpoints related to porting orders management."""
        return AsyncLoaConfigurationsResourceWithRawResponse(self._porting.loa_configurations)


class PortingResourceWithStreamingResponse:
    def __init__(self, porting: PortingResource) -> None:
        self._porting = porting

        self.list_uk_carriers = to_streamed_response_wrapper(
            porting.list_uk_carriers,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        return EventsResourceWithStreamingResponse(self._porting.events)

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        return ReportsResourceWithStreamingResponse(self._porting.reports)

    @cached_property
    def loa_configurations(self) -> LoaConfigurationsResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        return LoaConfigurationsResourceWithStreamingResponse(self._porting.loa_configurations)


class AsyncPortingResourceWithStreamingResponse:
    def __init__(self, porting: AsyncPortingResource) -> None:
        self._porting = porting

        self.list_uk_carriers = async_to_streamed_response_wrapper(
            porting.list_uk_carriers,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        return AsyncEventsResourceWithStreamingResponse(self._porting.events)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        return AsyncReportsResourceWithStreamingResponse(self._porting.reports)

    @cached_property
    def loa_configurations(self) -> AsyncLoaConfigurationsResourceWithStreamingResponse:
        """Endpoints related to porting orders management."""
        return AsyncLoaConfigurationsResourceWithStreamingResponse(self._porting.loa_configurations)
