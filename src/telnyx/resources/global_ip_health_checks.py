# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import global_ip_health_check_list_params, global_ip_health_check_create_params
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
from ..types.global_ip_health_check_list_response import GlobalIPHealthCheckListResponse
from ..types.global_ip_health_check_create_response import GlobalIPHealthCheckCreateResponse
from ..types.global_ip_health_check_delete_response import GlobalIPHealthCheckDeleteResponse
from ..types.global_ip_health_check_retrieve_response import GlobalIPHealthCheckRetrieveResponse

__all__ = ["GlobalIPHealthChecksResource", "AsyncGlobalIPHealthChecksResource"]


class GlobalIPHealthChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPHealthChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPHealthChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPHealthChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPHealthChecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        global_ip_id: str | NotGiven = NOT_GIVEN,
        health_check_params: Dict[str, object] | NotGiven = NOT_GIVEN,
        health_check_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPHealthCheckCreateResponse:
        """
        Create a Global IP health check.

        Args:
          global_ip_id: Global IP ID.

          health_check_params: A Global IP health check params.

          health_check_type: The Global IP health check type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/global_ip_health_checks",
            body=maybe_transform(
                {
                    "global_ip_id": global_ip_id,
                    "health_check_params": health_check_params,
                    "health_check_type": health_check_type,
                },
                global_ip_health_check_create_params.GlobalIPHealthCheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckCreateResponse,
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
    ) -> GlobalIPHealthCheckRetrieveResponse:
        """
        Retrieve a Global IP health check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/global_ip_health_checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckRetrieveResponse,
        )

    def list(
        self,
        *,
        page: global_ip_health_check_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPHealthCheckListResponse:
        """
        List all Global IP health checks.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/global_ip_health_checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, global_ip_health_check_list_params.GlobalIPHealthCheckListParams),
            ),
            cast_to=GlobalIPHealthCheckListResponse,
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
    ) -> GlobalIPHealthCheckDeleteResponse:
        """
        Delete a Global IP health check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/global_ip_health_checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckDeleteResponse,
        )


class AsyncGlobalIPHealthChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPHealthChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPHealthChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPHealthChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPHealthChecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        global_ip_id: str | NotGiven = NOT_GIVEN,
        health_check_params: Dict[str, object] | NotGiven = NOT_GIVEN,
        health_check_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPHealthCheckCreateResponse:
        """
        Create a Global IP health check.

        Args:
          global_ip_id: Global IP ID.

          health_check_params: A Global IP health check params.

          health_check_type: The Global IP health check type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/global_ip_health_checks",
            body=await async_maybe_transform(
                {
                    "global_ip_id": global_ip_id,
                    "health_check_params": health_check_params,
                    "health_check_type": health_check_type,
                },
                global_ip_health_check_create_params.GlobalIPHealthCheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckCreateResponse,
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
    ) -> GlobalIPHealthCheckRetrieveResponse:
        """
        Retrieve a Global IP health check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/global_ip_health_checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: global_ip_health_check_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPHealthCheckListResponse:
        """
        List all Global IP health checks.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/global_ip_health_checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, global_ip_health_check_list_params.GlobalIPHealthCheckListParams
                ),
            ),
            cast_to=GlobalIPHealthCheckListResponse,
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
    ) -> GlobalIPHealthCheckDeleteResponse:
        """
        Delete a Global IP health check.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/global_ip_health_checks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPHealthCheckDeleteResponse,
        )


class GlobalIPHealthChecksResourceWithRawResponse:
    def __init__(self, global_ip_health_checks: GlobalIPHealthChecksResource) -> None:
        self._global_ip_health_checks = global_ip_health_checks

        self.create = to_raw_response_wrapper(
            global_ip_health_checks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            global_ip_health_checks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            global_ip_health_checks.list,
        )
        self.delete = to_raw_response_wrapper(
            global_ip_health_checks.delete,
        )


class AsyncGlobalIPHealthChecksResourceWithRawResponse:
    def __init__(self, global_ip_health_checks: AsyncGlobalIPHealthChecksResource) -> None:
        self._global_ip_health_checks = global_ip_health_checks

        self.create = async_to_raw_response_wrapper(
            global_ip_health_checks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            global_ip_health_checks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            global_ip_health_checks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            global_ip_health_checks.delete,
        )


class GlobalIPHealthChecksResourceWithStreamingResponse:
    def __init__(self, global_ip_health_checks: GlobalIPHealthChecksResource) -> None:
        self._global_ip_health_checks = global_ip_health_checks

        self.create = to_streamed_response_wrapper(
            global_ip_health_checks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            global_ip_health_checks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            global_ip_health_checks.list,
        )
        self.delete = to_streamed_response_wrapper(
            global_ip_health_checks.delete,
        )


class AsyncGlobalIPHealthChecksResourceWithStreamingResponse:
    def __init__(self, global_ip_health_checks: AsyncGlobalIPHealthChecksResource) -> None:
        self._global_ip_health_checks = global_ip_health_checks

        self.create = async_to_streamed_response_wrapper(
            global_ip_health_checks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            global_ip_health_checks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            global_ip_health_checks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            global_ip_health_checks.delete,
        )
