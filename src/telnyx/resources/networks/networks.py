# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import network_list_params, network_create_params, network_update_params, network_list_interfaces_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from .default_gateway import (
    DefaultGatewayResource,
    AsyncDefaultGatewayResource,
    DefaultGatewayResourceWithRawResponse,
    AsyncDefaultGatewayResourceWithRawResponse,
    DefaultGatewayResourceWithStreamingResponse,
    AsyncDefaultGatewayResourceWithStreamingResponse,
)
from ...types.network_list_response import NetworkListResponse
from ...types.network_create_response import NetworkCreateResponse
from ...types.network_delete_response import NetworkDeleteResponse
from ...types.network_update_response import NetworkUpdateResponse
from ...types.network_retrieve_response import NetworkRetrieveResponse
from ...types.network_list_interfaces_response import NetworkListInterfacesResponse

__all__ = ["NetworksResource", "AsyncNetworksResource"]


class NetworksResource(SyncAPIResource):
    @cached_property
    def default_gateway(self) -> DefaultGatewayResource:
        return DefaultGatewayResource(self._client)

    @cached_property
    def with_raw_response(self) -> NetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NetworksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkCreateResponse:
        """
        Create a new Network.

        Args:
          name: A user specified name for the network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/networks",
            body=maybe_transform({"name": name}, network_create_params.NetworkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkCreateResponse,
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
    ) -> NetworkRetrieveResponse:
        """
        Retrieve a Network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRetrieveResponse,
        )

    def update(
        self,
        network_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkUpdateResponse:
        """
        Update a Network.

        Args:
          name: A user specified name for the network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return self._patch(
            f"/networks/{network_id}",
            body=maybe_transform({"name": name}, network_update_params.NetworkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkUpdateResponse,
        )

    def list(
        self,
        *,
        filter: network_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[NetworkListResponse]:
        """
        List all Networks.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/networks",
            page=SyncDefaultFlatPagination[NetworkListResponse],
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
                    network_list_params.NetworkListParams,
                ),
            ),
            model=NetworkListResponse,
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
    ) -> NetworkDeleteResponse:
        """
        Delete a Network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkDeleteResponse,
        )

    def list_interfaces(
        self,
        id: str,
        *,
        filter: network_list_interfaces_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[NetworkListInterfacesResponse]:
        """
        List all Interfaces for a Network.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name],
              filter[type], filter[status]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/networks/{id}/network_interfaces",
            page=SyncDefaultFlatPagination[NetworkListInterfacesResponse],
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
                    network_list_interfaces_params.NetworkListInterfacesParams,
                ),
            ),
            model=NetworkListInterfacesResponse,
        )


class AsyncNetworksResource(AsyncAPIResource):
    @cached_property
    def default_gateway(self) -> AsyncDefaultGatewayResource:
        return AsyncDefaultGatewayResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNetworksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNetworksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkCreateResponse:
        """
        Create a new Network.

        Args:
          name: A user specified name for the network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/networks",
            body=await async_maybe_transform({"name": name}, network_create_params.NetworkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkCreateResponse,
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
    ) -> NetworkRetrieveResponse:
        """
        Retrieve a Network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRetrieveResponse,
        )

    async def update(
        self,
        network_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkUpdateResponse:
        """
        Update a Network.

        Args:
          name: A user specified name for the network.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network_id:
            raise ValueError(f"Expected a non-empty value for `network_id` but received {network_id!r}")
        return await self._patch(
            f"/networks/{network_id}",
            body=await async_maybe_transform({"name": name}, network_update_params.NetworkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkUpdateResponse,
        )

    def list(
        self,
        *,
        filter: network_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NetworkListResponse, AsyncDefaultFlatPagination[NetworkListResponse]]:
        """
        List all Networks.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/networks",
            page=AsyncDefaultFlatPagination[NetworkListResponse],
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
                    network_list_params.NetworkListParams,
                ),
            ),
            model=NetworkListResponse,
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
    ) -> NetworkDeleteResponse:
        """
        Delete a Network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/networks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkDeleteResponse,
        )

    def list_interfaces(
        self,
        id: str,
        *,
        filter: network_list_interfaces_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NetworkListInterfacesResponse, AsyncDefaultFlatPagination[NetworkListInterfacesResponse]]:
        """
        List all Interfaces for a Network.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name],
              filter[type], filter[status]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/networks/{id}/network_interfaces",
            page=AsyncDefaultFlatPagination[NetworkListInterfacesResponse],
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
                    network_list_interfaces_params.NetworkListInterfacesParams,
                ),
            ),
            model=NetworkListInterfacesResponse,
        )


class NetworksResourceWithRawResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_raw_response_wrapper(
            networks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            networks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            networks.update,
        )
        self.list = to_raw_response_wrapper(
            networks.list,
        )
        self.delete = to_raw_response_wrapper(
            networks.delete,
        )
        self.list_interfaces = to_raw_response_wrapper(
            networks.list_interfaces,
        )

    @cached_property
    def default_gateway(self) -> DefaultGatewayResourceWithRawResponse:
        return DefaultGatewayResourceWithRawResponse(self._networks.default_gateway)


class AsyncNetworksResourceWithRawResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_raw_response_wrapper(
            networks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            networks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            networks.update,
        )
        self.list = async_to_raw_response_wrapper(
            networks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            networks.delete,
        )
        self.list_interfaces = async_to_raw_response_wrapper(
            networks.list_interfaces,
        )

    @cached_property
    def default_gateway(self) -> AsyncDefaultGatewayResourceWithRawResponse:
        return AsyncDefaultGatewayResourceWithRawResponse(self._networks.default_gateway)


class NetworksResourceWithStreamingResponse:
    def __init__(self, networks: NetworksResource) -> None:
        self._networks = networks

        self.create = to_streamed_response_wrapper(
            networks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            networks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            networks.update,
        )
        self.list = to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = to_streamed_response_wrapper(
            networks.delete,
        )
        self.list_interfaces = to_streamed_response_wrapper(
            networks.list_interfaces,
        )

    @cached_property
    def default_gateway(self) -> DefaultGatewayResourceWithStreamingResponse:
        return DefaultGatewayResourceWithStreamingResponse(self._networks.default_gateway)


class AsyncNetworksResourceWithStreamingResponse:
    def __init__(self, networks: AsyncNetworksResource) -> None:
        self._networks = networks

        self.create = async_to_streamed_response_wrapper(
            networks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            networks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            networks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            networks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            networks.delete,
        )
        self.list_interfaces = async_to_streamed_response_wrapper(
            networks.list_interfaces,
        )

    @cached_property
    def default_gateway(self) -> AsyncDefaultGatewayResourceWithStreamingResponse:
        return AsyncDefaultGatewayResourceWithStreamingResponse(self._networks.default_gateway)
