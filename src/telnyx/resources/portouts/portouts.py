# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ...types import portout_list_params, portout_update_status_params, portout_list_rejection_codes_params
from .reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .supporting_documents import (
    SupportingDocumentsResource,
    AsyncSupportingDocumentsResource,
    SupportingDocumentsResourceWithRawResponse,
    AsyncSupportingDocumentsResourceWithRawResponse,
    SupportingDocumentsResourceWithStreamingResponse,
    AsyncSupportingDocumentsResourceWithStreamingResponse,
)
from ...types.portout_list_response import PortoutListResponse
from ...types.portout_retrieve_response import PortoutRetrieveResponse
from ...types.portout_update_status_response import PortoutUpdateStatusResponse
from ...types.portout_list_rejection_codes_response import PortoutListRejectionCodesResponse

__all__ = ["PortoutsResource", "AsyncPortoutsResource"]


class PortoutsResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def supporting_documents(self) -> SupportingDocumentsResource:
        return SupportingDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PortoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PortoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PortoutsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutRetrieveResponse:
        """
        Returns the portout request based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/portouts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortoutRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: portout_list_params.Filter | NotGiven = NOT_GIVEN,
        page: portout_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutListResponse:
        """
        Returns the portout requests according to filters

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[carrier_name], filter[country_code], filter[country_code_in],
              filter[foc_date], filter[inserted_at], filter[phone_number], filter[pon],
              filter[ported_out_at], filter[spid], filter[status], filter[status_in],
              filter[support_key]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/portouts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    portout_list_params.PortoutListParams,
                ),
            ),
            cast_to=PortoutListResponse,
        )

    def list_rejection_codes(
        self,
        portout_id: str,
        *,
        filter: portout_list_rejection_codes_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutListRejectionCodesResponse:
        """
        Given a port-out ID, list rejection codes that are eligible for that port-out

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[code],
              filter[code][in]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portout_id:
            raise ValueError(f"Expected a non-empty value for `portout_id` but received {portout_id!r}")
        return self._get(
            f"/portouts/rejections/{portout_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter}, portout_list_rejection_codes_params.PortoutListRejectionCodesParams
                ),
            ),
            cast_to=PortoutListRejectionCodesResponse,
        )

    def update_status(
        self,
        status: Literal["authorized", "rejected-pending"],
        *,
        id: str,
        reason: str,
        host_messaging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutUpdateStatusResponse:
        """
        Authorize or reject portout request

        Args:
          reason: Provide a reason if rejecting the port out request

          host_messaging: Indicates whether messaging services should be maintained with Telnyx after the
              port out completes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return self._patch(
            f"/portouts/{id}/{status}",
            body=maybe_transform(
                {
                    "reason": reason,
                    "host_messaging": host_messaging,
                },
                portout_update_status_params.PortoutUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortoutUpdateStatusResponse,
        )


class AsyncPortoutsResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def supporting_documents(self) -> AsyncSupportingDocumentsResource:
        return AsyncSupportingDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPortoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPortoutsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutRetrieveResponse:
        """
        Returns the portout request based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/portouts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortoutRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: portout_list_params.Filter | NotGiven = NOT_GIVEN,
        page: portout_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutListResponse:
        """
        Returns the portout requests according to filters

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[carrier_name], filter[country_code], filter[country_code_in],
              filter[foc_date], filter[inserted_at], filter[phone_number], filter[pon],
              filter[ported_out_at], filter[spid], filter[status], filter[status_in],
              filter[support_key]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/portouts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    portout_list_params.PortoutListParams,
                ),
            ),
            cast_to=PortoutListResponse,
        )

    async def list_rejection_codes(
        self,
        portout_id: str,
        *,
        filter: portout_list_rejection_codes_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutListRejectionCodesResponse:
        """
        Given a port-out ID, list rejection codes that are eligible for that port-out

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[code],
              filter[code][in]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portout_id:
            raise ValueError(f"Expected a non-empty value for `portout_id` but received {portout_id!r}")
        return await self._get(
            f"/portouts/rejections/{portout_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, portout_list_rejection_codes_params.PortoutListRejectionCodesParams
                ),
            ),
            cast_to=PortoutListRejectionCodesResponse,
        )

    async def update_status(
        self,
        status: Literal["authorized", "rejected-pending"],
        *,
        id: str,
        reason: str,
        host_messaging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortoutUpdateStatusResponse:
        """
        Authorize or reject portout request

        Args:
          reason: Provide a reason if rejecting the port out request

          host_messaging: Indicates whether messaging services should be maintained with Telnyx after the
              port out completes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not status:
            raise ValueError(f"Expected a non-empty value for `status` but received {status!r}")
        return await self._patch(
            f"/portouts/{id}/{status}",
            body=await async_maybe_transform(
                {
                    "reason": reason,
                    "host_messaging": host_messaging,
                },
                portout_update_status_params.PortoutUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortoutUpdateStatusResponse,
        )


class PortoutsResourceWithRawResponse:
    def __init__(self, portouts: PortoutsResource) -> None:
        self._portouts = portouts

        self.retrieve = to_raw_response_wrapper(
            portouts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            portouts.list,
        )
        self.list_rejection_codes = to_raw_response_wrapper(
            portouts.list_rejection_codes,
        )
        self.update_status = to_raw_response_wrapper(
            portouts.update_status,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._portouts.events)

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._portouts.reports)

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._portouts.comments)

    @cached_property
    def supporting_documents(self) -> SupportingDocumentsResourceWithRawResponse:
        return SupportingDocumentsResourceWithRawResponse(self._portouts.supporting_documents)


class AsyncPortoutsResourceWithRawResponse:
    def __init__(self, portouts: AsyncPortoutsResource) -> None:
        self._portouts = portouts

        self.retrieve = async_to_raw_response_wrapper(
            portouts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            portouts.list,
        )
        self.list_rejection_codes = async_to_raw_response_wrapper(
            portouts.list_rejection_codes,
        )
        self.update_status = async_to_raw_response_wrapper(
            portouts.update_status,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._portouts.events)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._portouts.reports)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._portouts.comments)

    @cached_property
    def supporting_documents(self) -> AsyncSupportingDocumentsResourceWithRawResponse:
        return AsyncSupportingDocumentsResourceWithRawResponse(self._portouts.supporting_documents)


class PortoutsResourceWithStreamingResponse:
    def __init__(self, portouts: PortoutsResource) -> None:
        self._portouts = portouts

        self.retrieve = to_streamed_response_wrapper(
            portouts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            portouts.list,
        )
        self.list_rejection_codes = to_streamed_response_wrapper(
            portouts.list_rejection_codes,
        )
        self.update_status = to_streamed_response_wrapper(
            portouts.update_status,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._portouts.events)

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._portouts.reports)

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._portouts.comments)

    @cached_property
    def supporting_documents(self) -> SupportingDocumentsResourceWithStreamingResponse:
        return SupportingDocumentsResourceWithStreamingResponse(self._portouts.supporting_documents)


class AsyncPortoutsResourceWithStreamingResponse:
    def __init__(self, portouts: AsyncPortoutsResource) -> None:
        self._portouts = portouts

        self.retrieve = async_to_streamed_response_wrapper(
            portouts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            portouts.list,
        )
        self.list_rejection_codes = async_to_streamed_response_wrapper(
            portouts.list_rejection_codes,
        )
        self.update_status = async_to_streamed_response_wrapper(
            portouts.update_status,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._portouts.events)

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._portouts.reports)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._portouts.comments)

    @cached_property
    def supporting_documents(self) -> AsyncSupportingDocumentsResourceWithStreamingResponse:
        return AsyncSupportingDocumentsResourceWithStreamingResponse(self._portouts.supporting_documents)
