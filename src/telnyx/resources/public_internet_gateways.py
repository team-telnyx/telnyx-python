# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import public_internet_gateway_list_params, public_internet_gateway_create_params
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
from ..types.public_internet_gateway_list_response import PublicInternetGatewayListResponse
from ..types.public_internet_gateway_create_response import PublicInternetGatewayCreateResponse
from ..types.public_internet_gateway_delete_response import PublicInternetGatewayDeleteResponse
from ..types.public_internet_gateway_retrieve_response import PublicInternetGatewayRetrieveResponse

__all__ = ["PublicInternetGatewaysResource", "AsyncPublicInternetGatewaysResource"]


class PublicInternetGatewaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublicInternetGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PublicInternetGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublicInternetGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PublicInternetGatewaysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicInternetGatewayCreateResponse:
        """
        Create a new Public Internet Gateway.

        Args:
          name: A user specified name for the interface.

          network_id: The id of the network associated with the interface.

          region_code: The region the interface should be deployed to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/public_internet_gateways",
            body=maybe_transform(
                {
                    "name": name,
                    "network_id": network_id,
                    "region_code": region_code,
                },
                public_internet_gateway_create_params.PublicInternetGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicInternetGatewayCreateResponse,
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
    ) -> PublicInternetGatewayRetrieveResponse:
        """
        Retrieve a Public Internet Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/public_internet_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicInternetGatewayRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: public_internet_gateway_list_params.Filter | NotGiven = NOT_GIVEN,
        page: public_internet_gateway_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicInternetGatewayListResponse:
        """
        List all Public Internet Gateways.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/public_internet_gateways",
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
                    public_internet_gateway_list_params.PublicInternetGatewayListParams,
                ),
            ),
            cast_to=PublicInternetGatewayListResponse,
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
    ) -> PublicInternetGatewayDeleteResponse:
        """
        Delete a Public Internet Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/public_internet_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicInternetGatewayDeleteResponse,
        )


class AsyncPublicInternetGatewaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublicInternetGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublicInternetGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublicInternetGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPublicInternetGatewaysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        network_id: str | NotGiven = NOT_GIVEN,
        region_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicInternetGatewayCreateResponse:
        """
        Create a new Public Internet Gateway.

        Args:
          name: A user specified name for the interface.

          network_id: The id of the network associated with the interface.

          region_code: The region the interface should be deployed to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/public_internet_gateways",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network_id": network_id,
                    "region_code": region_code,
                },
                public_internet_gateway_create_params.PublicInternetGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicInternetGatewayCreateResponse,
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
    ) -> PublicInternetGatewayRetrieveResponse:
        """
        Retrieve a Public Internet Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/public_internet_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicInternetGatewayRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: public_internet_gateway_list_params.Filter | NotGiven = NOT_GIVEN,
        page: public_internet_gateway_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicInternetGatewayListResponse:
        """
        List all Public Internet Gateways.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/public_internet_gateways",
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
                    public_internet_gateway_list_params.PublicInternetGatewayListParams,
                ),
            ),
            cast_to=PublicInternetGatewayListResponse,
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
    ) -> PublicInternetGatewayDeleteResponse:
        """
        Delete a Public Internet Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/public_internet_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicInternetGatewayDeleteResponse,
        )


class PublicInternetGatewaysResourceWithRawResponse:
    def __init__(self, public_internet_gateways: PublicInternetGatewaysResource) -> None:
        self._public_internet_gateways = public_internet_gateways

        self.create = to_raw_response_wrapper(
            public_internet_gateways.create,
        )
        self.retrieve = to_raw_response_wrapper(
            public_internet_gateways.retrieve,
        )
        self.list = to_raw_response_wrapper(
            public_internet_gateways.list,
        )
        self.delete = to_raw_response_wrapper(
            public_internet_gateways.delete,
        )


class AsyncPublicInternetGatewaysResourceWithRawResponse:
    def __init__(self, public_internet_gateways: AsyncPublicInternetGatewaysResource) -> None:
        self._public_internet_gateways = public_internet_gateways

        self.create = async_to_raw_response_wrapper(
            public_internet_gateways.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            public_internet_gateways.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            public_internet_gateways.list,
        )
        self.delete = async_to_raw_response_wrapper(
            public_internet_gateways.delete,
        )


class PublicInternetGatewaysResourceWithStreamingResponse:
    def __init__(self, public_internet_gateways: PublicInternetGatewaysResource) -> None:
        self._public_internet_gateways = public_internet_gateways

        self.create = to_streamed_response_wrapper(
            public_internet_gateways.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            public_internet_gateways.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            public_internet_gateways.list,
        )
        self.delete = to_streamed_response_wrapper(
            public_internet_gateways.delete,
        )


class AsyncPublicInternetGatewaysResourceWithStreamingResponse:
    def __init__(self, public_internet_gateways: AsyncPublicInternetGatewaysResource) -> None:
        self._public_internet_gateways = public_internet_gateways

        self.create = async_to_streamed_response_wrapper(
            public_internet_gateways.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            public_internet_gateways.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            public_internet_gateways.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            public_internet_gateways.delete,
        )
