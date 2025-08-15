# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import global_ip_list_params, global_ip_create_params
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
from ..types.global_ip_list_response import GlobalIPListResponse
from ..types.global_ip_create_response import GlobalIPCreateResponse
from ..types.global_ip_delete_response import GlobalIPDeleteResponse
from ..types.global_ip_retrieve_response import GlobalIPRetrieveResponse

__all__ = ["GlobalIPsResource", "AsyncGlobalIPsResource"]


class GlobalIPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ports: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPCreateResponse:
        """
        Create a Global IP.

        Args:
          description: A user specified description for the address.

          name: A user specified name for the address.

          ports: A Global IP ports grouped by protocol code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/global_ips",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "ports": ports,
                },
                global_ip_create_params.GlobalIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPCreateResponse,
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
    ) -> GlobalIPRetrieveResponse:
        """
        Retrieve a Global IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/global_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPRetrieveResponse,
        )

    def list(
        self,
        *,
        page: global_ip_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPListResponse:
        """
        List all Global IPs.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/global_ips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, global_ip_list_params.GlobalIPListParams),
            ),
            cast_to=GlobalIPListResponse,
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
    ) -> GlobalIPDeleteResponse:
        """
        Delete a Global IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/global_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPDeleteResponse,
        )


class AsyncGlobalIPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ports: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPCreateResponse:
        """
        Create a Global IP.

        Args:
          description: A user specified description for the address.

          name: A user specified name for the address.

          ports: A Global IP ports grouped by protocol code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/global_ips",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "ports": ports,
                },
                global_ip_create_params.GlobalIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPCreateResponse,
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
    ) -> GlobalIPRetrieveResponse:
        """
        Retrieve a Global IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/global_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: global_ip_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPListResponse:
        """
        List all Global IPs.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/global_ips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, global_ip_list_params.GlobalIPListParams),
            ),
            cast_to=GlobalIPListResponse,
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
    ) -> GlobalIPDeleteResponse:
        """
        Delete a Global IP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/global_ips/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPDeleteResponse,
        )


class GlobalIPsResourceWithRawResponse:
    def __init__(self, global_ips: GlobalIPsResource) -> None:
        self._global_ips = global_ips

        self.create = to_raw_response_wrapper(
            global_ips.create,
        )
        self.retrieve = to_raw_response_wrapper(
            global_ips.retrieve,
        )
        self.list = to_raw_response_wrapper(
            global_ips.list,
        )
        self.delete = to_raw_response_wrapper(
            global_ips.delete,
        )


class AsyncGlobalIPsResourceWithRawResponse:
    def __init__(self, global_ips: AsyncGlobalIPsResource) -> None:
        self._global_ips = global_ips

        self.create = async_to_raw_response_wrapper(
            global_ips.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            global_ips.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            global_ips.list,
        )
        self.delete = async_to_raw_response_wrapper(
            global_ips.delete,
        )


class GlobalIPsResourceWithStreamingResponse:
    def __init__(self, global_ips: GlobalIPsResource) -> None:
        self._global_ips = global_ips

        self.create = to_streamed_response_wrapper(
            global_ips.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            global_ips.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            global_ips.list,
        )
        self.delete = to_streamed_response_wrapper(
            global_ips.delete,
        )


class AsyncGlobalIPsResourceWithStreamingResponse:
    def __init__(self, global_ips: AsyncGlobalIPsResource) -> None:
        self._global_ips = global_ips

        self.create = async_to_streamed_response_wrapper(
            global_ips.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            global_ips.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            global_ips.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            global_ips.delete,
        )
