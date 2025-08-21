# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.networks import default_gateway_create_params
from ...types.networks.default_gateway_create_response import DefaultGatewayCreateResponse
from ...types.networks.default_gateway_delete_response import DefaultGatewayDeleteResponse
from ...types.networks.default_gateway_retrieve_response import DefaultGatewayRetrieveResponse

__all__ = ["DefaultGatewayResource", "AsyncDefaultGatewayResource"]


class DefaultGatewayResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DefaultGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DefaultGatewayResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        wireguard_peer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultGatewayCreateResponse:
        """
        Create Default Gateway.

        Args:
          wireguard_peer_id: Wireguard peer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/networks/{id}/default_gateway",
            body=maybe_transform(
                {"wireguard_peer_id": wireguard_peer_id}, default_gateway_create_params.DefaultGatewayCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultGatewayCreateResponse,
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
    ) -> DefaultGatewayRetrieveResponse:
        """
        Get Default Gateway status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/networks/{id}/default_gateway",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultGatewayRetrieveResponse,
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
    ) -> DefaultGatewayDeleteResponse:
        """
        Delete Default Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/networks/{id}/default_gateway",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultGatewayDeleteResponse,
        )


class AsyncDefaultGatewayResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDefaultGatewayResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        wireguard_peer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultGatewayCreateResponse:
        """
        Create Default Gateway.

        Args:
          wireguard_peer_id: Wireguard peer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/networks/{id}/default_gateway",
            body=await async_maybe_transform(
                {"wireguard_peer_id": wireguard_peer_id}, default_gateway_create_params.DefaultGatewayCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultGatewayCreateResponse,
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
    ) -> DefaultGatewayRetrieveResponse:
        """
        Get Default Gateway status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/networks/{id}/default_gateway",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultGatewayRetrieveResponse,
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
    ) -> DefaultGatewayDeleteResponse:
        """
        Delete Default Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/networks/{id}/default_gateway",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefaultGatewayDeleteResponse,
        )


class DefaultGatewayResourceWithRawResponse:
    def __init__(self, default_gateway: DefaultGatewayResource) -> None:
        self._default_gateway = default_gateway

        self.create = to_raw_response_wrapper(
            default_gateway.create,
        )
        self.retrieve = to_raw_response_wrapper(
            default_gateway.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            default_gateway.delete,
        )


class AsyncDefaultGatewayResourceWithRawResponse:
    def __init__(self, default_gateway: AsyncDefaultGatewayResource) -> None:
        self._default_gateway = default_gateway

        self.create = async_to_raw_response_wrapper(
            default_gateway.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            default_gateway.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            default_gateway.delete,
        )


class DefaultGatewayResourceWithStreamingResponse:
    def __init__(self, default_gateway: DefaultGatewayResource) -> None:
        self._default_gateway = default_gateway

        self.create = to_streamed_response_wrapper(
            default_gateway.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            default_gateway.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            default_gateway.delete,
        )


class AsyncDefaultGatewayResourceWithStreamingResponse:
    def __init__(self, default_gateway: AsyncDefaultGatewayResource) -> None:
        self._default_gateway = default_gateway

        self.create = async_to_streamed_response_wrapper(
            default_gateway.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            default_gateway.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            default_gateway.delete,
        )
