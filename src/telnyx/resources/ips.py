# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ip_list_params, ip_create_params, ip_update_params
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
from ..types.ip_list_response import IPListResponse
from ..types.ip_create_response import IPCreateResponse
from ..types.ip_delete_response import IPDeleteResponse
from ..types.ip_update_response import IPUpdateResponse
from ..types.ip_retrieve_response import IPRetrieveResponse

__all__ = ["IPsResource", "AsyncIPsResource"]


class IPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return IPsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ip_address: str,
        connection_id: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPCreateResponse:
        """
        Create a new IP object.

        Args:
          ip_address: IP adddress represented by this resource.

          connection_id: ID of the IP Connection to which this IP should be attached.

          port: Port to use when connecting to this IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ips",
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "connection_id": connection_id,
                    "port": port,
                },
                ip_create_params.IPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRetrieveResponse:
        """
        Return the details regarding a specific IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        ip_address: str,
        connection_id: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPUpdateResponse:
        """
        Update the details of a specific IP.

        Args:
          ip_address: IP adddress represented by this resource.

          connection_id: ID of the IP Connection to which this IP should be attached.

          port: Port to use when connecting to this IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/ips/{id}",
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "connection_id": connection_id,
                    "port": port,
                },
                ip_update_params.IPUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPUpdateResponse,
        )

    def list(
        self,
        *,
        filter: ip_list_params.Filter | NotGiven = NOT_GIVEN,
        page: ip_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPListResponse:
        """
        Get all IPs belonging to the user that match the given filters.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_id], filter[ip_address], filter[port]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ips",
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
                    ip_list_params.IPListParams,
                ),
            ),
            cast_to=IPListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPDeleteResponse:
        """
        Delete an IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPDeleteResponse,
        )


class AsyncIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncIPsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ip_address: str,
        connection_id: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPCreateResponse:
        """
        Create a new IP object.

        Args:
          ip_address: IP adddress represented by this resource.

          connection_id: ID of the IP Connection to which this IP should be attached.

          port: Port to use when connecting to this IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ips",
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "connection_id": connection_id,
                    "port": port,
                },
                ip_create_params.IPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPRetrieveResponse:
        """
        Return the details regarding a specific IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        ip_address: str,
        connection_id: str | NotGiven = NOT_GIVEN,
        port: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPUpdateResponse:
        """
        Update the details of a specific IP.

        Args:
          ip_address: IP adddress represented by this resource.

          connection_id: ID of the IP Connection to which this IP should be attached.

          port: Port to use when connecting to this IP.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/ips/{id}",
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "connection_id": connection_id,
                    "port": port,
                },
                ip_update_params.IPUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: ip_list_params.Filter | NotGiven = NOT_GIVEN,
        page: ip_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPListResponse:
        """
        Get all IPs belonging to the user that match the given filters.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_id], filter[ip_address], filter[port]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ips",
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
                    ip_list_params.IPListParams,
                ),
            ),
            cast_to=IPListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IPDeleteResponse:
        """
        Delete an IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPDeleteResponse,
        )


class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.create = to_raw_response_wrapper(
            ips.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ips.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ips.update,
        )
        self.list = to_raw_response_wrapper(
            ips.list,
        )
        self.delete = to_raw_response_wrapper(
            ips.delete,
        )


class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.create = async_to_raw_response_wrapper(
            ips.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ips.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ips.update,
        )
        self.list = async_to_raw_response_wrapper(
            ips.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ips.delete,
        )


class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.create = to_streamed_response_wrapper(
            ips.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ips.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ips.update,
        )
        self.list = to_streamed_response_wrapper(
            ips.list,
        )
        self.delete = to_streamed_response_wrapper(
            ips.delete,
        )


class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.create = async_to_streamed_response_wrapper(
            ips.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ips.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ips.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ips.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ips.delete,
        )
