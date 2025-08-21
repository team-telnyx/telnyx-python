# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ota_update_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ota_update_list_response import OtaUpdateListResponse
from ..types.ota_update_retrieve_response import OtaUpdateRetrieveResponse

__all__ = ["OtaUpdatesResource", "AsyncOtaUpdatesResource"]


class OtaUpdatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OtaUpdatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OtaUpdatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OtaUpdatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OtaUpdatesResourceWithStreamingResponse(self)

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
    ) -> OtaUpdateRetrieveResponse:
        """
        This API returns the details of an Over the Air (OTA) update.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ota_updates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtaUpdateRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: ota_update_list_params.Filter | NotGiven = NOT_GIVEN,
        page: ota_update_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OtaUpdateListResponse:
        """
        List OTA updates

        Args:
          filter:
              Consolidated filter parameter for OTA updates (deepObject style). Originally:
              filter[status], filter[sim_card_id], filter[type]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ota_updates",
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
                    ota_update_list_params.OtaUpdateListParams,
                ),
            ),
            cast_to=OtaUpdateListResponse,
        )


class AsyncOtaUpdatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOtaUpdatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOtaUpdatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOtaUpdatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOtaUpdatesResourceWithStreamingResponse(self)

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
    ) -> OtaUpdateRetrieveResponse:
        """
        This API returns the details of an Over the Air (OTA) update.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ota_updates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtaUpdateRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: ota_update_list_params.Filter | NotGiven = NOT_GIVEN,
        page: ota_update_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OtaUpdateListResponse:
        """
        List OTA updates

        Args:
          filter:
              Consolidated filter parameter for OTA updates (deepObject style). Originally:
              filter[status], filter[sim_card_id], filter[type]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ota_updates",
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
                    ota_update_list_params.OtaUpdateListParams,
                ),
            ),
            cast_to=OtaUpdateListResponse,
        )


class OtaUpdatesResourceWithRawResponse:
    def __init__(self, ota_updates: OtaUpdatesResource) -> None:
        self._ota_updates = ota_updates

        self.retrieve = to_raw_response_wrapper(
            ota_updates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ota_updates.list,
        )


class AsyncOtaUpdatesResourceWithRawResponse:
    def __init__(self, ota_updates: AsyncOtaUpdatesResource) -> None:
        self._ota_updates = ota_updates

        self.retrieve = async_to_raw_response_wrapper(
            ota_updates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ota_updates.list,
        )


class OtaUpdatesResourceWithStreamingResponse:
    def __init__(self, ota_updates: OtaUpdatesResource) -> None:
        self._ota_updates = ota_updates

        self.retrieve = to_streamed_response_wrapper(
            ota_updates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ota_updates.list,
        )


class AsyncOtaUpdatesResourceWithStreamingResponse:
    def __init__(self, ota_updates: AsyncOtaUpdatesResource) -> None:
        self._ota_updates = ota_updates

        self.retrieve = async_to_streamed_response_wrapper(
            ota_updates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ota_updates.list,
        )
