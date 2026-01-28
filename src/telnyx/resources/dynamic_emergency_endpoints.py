# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import dynamic_emergency_endpoint_list_params, dynamic_emergency_endpoint_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.dynamic_emergency_endpoint import DynamicEmergencyEndpoint
from ..types.dynamic_emergency_endpoint_create_response import DynamicEmergencyEndpointCreateResponse
from ..types.dynamic_emergency_endpoint_delete_response import DynamicEmergencyEndpointDeleteResponse
from ..types.dynamic_emergency_endpoint_retrieve_response import DynamicEmergencyEndpointRetrieveResponse

__all__ = ["DynamicEmergencyEndpointsResource", "AsyncDynamicEmergencyEndpointsResource"]


class DynamicEmergencyEndpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DynamicEmergencyEndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DynamicEmergencyEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DynamicEmergencyEndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DynamicEmergencyEndpointsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        callback_number: str,
        caller_name: str,
        dynamic_emergency_address_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicEmergencyEndpointCreateResponse:
        """
        Creates a dynamic emergency endpoints.

        Args:
          dynamic_emergency_address_id: An id of a currently active dynamic emergency location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dynamic_emergency_endpoints",
            body=maybe_transform(
                {
                    "callback_number": callback_number,
                    "caller_name": caller_name,
                    "dynamic_emergency_address_id": dynamic_emergency_address_id,
                },
                dynamic_emergency_endpoint_create_params.DynamicEmergencyEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyEndpointCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicEmergencyEndpointRetrieveResponse:
        """
        Returns the dynamic emergency endpoint based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/dynamic_emergency_endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyEndpointRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: dynamic_emergency_endpoint_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[DynamicEmergencyEndpoint]:
        """
        Returns the dynamic emergency endpoints according to filters

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[country_code]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dynamic_emergency_endpoints",
            page=SyncDefaultFlatPagination[DynamicEmergencyEndpoint],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    dynamic_emergency_endpoint_list_params.DynamicEmergencyEndpointListParams,
                ),
            ),
            model=DynamicEmergencyEndpoint,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicEmergencyEndpointDeleteResponse:
        """
        Deletes the dynamic emergency endpoint based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/dynamic_emergency_endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyEndpointDeleteResponse,
        )


class AsyncDynamicEmergencyEndpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDynamicEmergencyEndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDynamicEmergencyEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        callback_number: str,
        caller_name: str,
        dynamic_emergency_address_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicEmergencyEndpointCreateResponse:
        """
        Creates a dynamic emergency endpoints.

        Args:
          dynamic_emergency_address_id: An id of a currently active dynamic emergency location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dynamic_emergency_endpoints",
            body=await async_maybe_transform(
                {
                    "callback_number": callback_number,
                    "caller_name": caller_name,
                    "dynamic_emergency_address_id": dynamic_emergency_address_id,
                },
                dynamic_emergency_endpoint_create_params.DynamicEmergencyEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyEndpointCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicEmergencyEndpointRetrieveResponse:
        """
        Returns the dynamic emergency endpoint based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/dynamic_emergency_endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyEndpointRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: dynamic_emergency_endpoint_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DynamicEmergencyEndpoint, AsyncDefaultFlatPagination[DynamicEmergencyEndpoint]]:
        """
        Returns the dynamic emergency endpoints according to filters

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[country_code]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dynamic_emergency_endpoints",
            page=AsyncDefaultFlatPagination[DynamicEmergencyEndpoint],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    dynamic_emergency_endpoint_list_params.DynamicEmergencyEndpointListParams,
                ),
            ),
            model=DynamicEmergencyEndpoint,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicEmergencyEndpointDeleteResponse:
        """
        Deletes the dynamic emergency endpoint based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/dynamic_emergency_endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyEndpointDeleteResponse,
        )


class DynamicEmergencyEndpointsResourceWithRawResponse:
    def __init__(self, dynamic_emergency_endpoints: DynamicEmergencyEndpointsResource) -> None:
        self._dynamic_emergency_endpoints = dynamic_emergency_endpoints

        self.create = to_raw_response_wrapper(
            dynamic_emergency_endpoints.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dynamic_emergency_endpoints.retrieve,
        )
        self.list = to_raw_response_wrapper(
            dynamic_emergency_endpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            dynamic_emergency_endpoints.delete,
        )


class AsyncDynamicEmergencyEndpointsResourceWithRawResponse:
    def __init__(self, dynamic_emergency_endpoints: AsyncDynamicEmergencyEndpointsResource) -> None:
        self._dynamic_emergency_endpoints = dynamic_emergency_endpoints

        self.create = async_to_raw_response_wrapper(
            dynamic_emergency_endpoints.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dynamic_emergency_endpoints.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            dynamic_emergency_endpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dynamic_emergency_endpoints.delete,
        )


class DynamicEmergencyEndpointsResourceWithStreamingResponse:
    def __init__(self, dynamic_emergency_endpoints: DynamicEmergencyEndpointsResource) -> None:
        self._dynamic_emergency_endpoints = dynamic_emergency_endpoints

        self.create = to_streamed_response_wrapper(
            dynamic_emergency_endpoints.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dynamic_emergency_endpoints.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            dynamic_emergency_endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            dynamic_emergency_endpoints.delete,
        )


class AsyncDynamicEmergencyEndpointsResourceWithStreamingResponse:
    def __init__(self, dynamic_emergency_endpoints: AsyncDynamicEmergencyEndpointsResource) -> None:
        self._dynamic_emergency_endpoints = dynamic_emergency_endpoints

        self.create = async_to_streamed_response_wrapper(
            dynamic_emergency_endpoints.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dynamic_emergency_endpoints.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            dynamic_emergency_endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dynamic_emergency_endpoints.delete,
        )
