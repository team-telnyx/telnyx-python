# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import network_route_list_params, network_route_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.network_route_list_response import NetworkRouteListResponse
from ..types.network_route_create_response import NetworkRouteCreateResponse
from ..types.network_route_retrieve_response import NetworkRouteRetrieveResponse

__all__ = ["NetworkRoutesResource", "AsyncNetworkRoutesResource"]


class NetworkRoutesResource(SyncAPIResource):
    """Routes on a Network that send a CIDR to a next hop, such as a tunnel."""

    @cached_property
    def with_raw_response(self) -> NetworkRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NetworkRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NetworkRoutesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        cidr: str,
        network_id: str,
        next_hop: network_route_create_params.NextHop,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkRouteCreateResponse:
        """Adds a route to a Network.

        Traffic on the Network to an address in `cidr` goes
        via `next_hop`. With a tunnel as the next hop, functions on the Network reach
        the CIDR through the tunnel without a redeploy. A Network holds each CIDR once.

        Args:
          cidr: The IPv4 subnet to route, such as a subnet behind the tunnel. It must be a
              canonical CIDR. Default, loopback, link-local, multicast, and shared address
              space (`100.64.0.0/10`) ranges are rejected. So are ranges that overlap the
              Tailscale Subnet Router ranges, `172.27.254.0/24` and `198.18.0.0/20`, or a
              subnet already on the Network.

          network_id: The id of the Network to add the route to.

          next_hop: Where the Network sends traffic for `cidr`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/network_routes",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "network_id": network_id,
                    "next_hop": next_hop,
                },
                network_route_create_params.NetworkRouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRouteCreateResponse,
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
    ) -> NetworkRouteRetrieveResponse:
        """
        Retrieves a route and its status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/network_routes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRouteRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: network_route_list_params.Filter,
        page: network_route_list_params.Page | Omit = omit,
        sort: Literal["cidr", "-cidr", "status", "-status", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkRouteListResponse:
        """Lists the routes of the account's Networks.

        A Network's list is its effective
        route table: the routes added with `POST /network_routes` (`origin` `static`)
        and the routes that its attachments install (`origin` `attachment`). Lookup is
        longest prefix within the Network.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[network_id], filter[origin], filter[next_hop.type], filter[cidr],
              filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[limit]

          sort: Sorts the results by a field, ascending, or descending with a leading `-`. The
              default is `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/network_routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    network_route_list_params.NetworkRouteListParams,
                ),
            ),
            cast_to=NetworkRouteListResponse,
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
    ) -> None:
        """Deletes a route that was added with `POST /network_routes`.

        Traffic to its CIDR
        stops going via the next hop at once. Routes that an attachment installs
        (`origin` `attachment`) leave with the attachment and cannot be deleted here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/network_routes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNetworkRoutesResource(AsyncAPIResource):
    """Routes on a Network that send a CIDR to a next hop, such as a tunnel."""

    @cached_property
    def with_raw_response(self) -> AsyncNetworkRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNetworkRoutesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        cidr: str,
        network_id: str,
        next_hop: network_route_create_params.NextHop,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkRouteCreateResponse:
        """Adds a route to a Network.

        Traffic on the Network to an address in `cidr` goes
        via `next_hop`. With a tunnel as the next hop, functions on the Network reach
        the CIDR through the tunnel without a redeploy. A Network holds each CIDR once.

        Args:
          cidr: The IPv4 subnet to route, such as a subnet behind the tunnel. It must be a
              canonical CIDR. Default, loopback, link-local, multicast, and shared address
              space (`100.64.0.0/10`) ranges are rejected. So are ranges that overlap the
              Tailscale Subnet Router ranges, `172.27.254.0/24` and `198.18.0.0/20`, or a
              subnet already on the Network.

          network_id: The id of the Network to add the route to.

          next_hop: Where the Network sends traffic for `cidr`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/network_routes",
            body=await async_maybe_transform(
                {
                    "cidr": cidr,
                    "network_id": network_id,
                    "next_hop": next_hop,
                },
                network_route_create_params.NetworkRouteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRouteCreateResponse,
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
    ) -> NetworkRouteRetrieveResponse:
        """
        Retrieves a route and its status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/network_routes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkRouteRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: network_route_list_params.Filter,
        page: network_route_list_params.Page | Omit = omit,
        sort: Literal["cidr", "-cidr", "status", "-status", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NetworkRouteListResponse:
        """Lists the routes of the account's Networks.

        A Network's list is its effective
        route table: the routes added with `POST /network_routes` (`origin` `static`)
        and the routes that its attachments install (`origin` `attachment`). Lookup is
        longest prefix within the Network.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[network_id], filter[origin], filter[next_hop.type], filter[cidr],
              filter[status]

          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[limit]

          sort: Sorts the results by a field, ascending, or descending with a leading `-`. The
              default is `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/network_routes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    network_route_list_params.NetworkRouteListParams,
                ),
            ),
            cast_to=NetworkRouteListResponse,
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
    ) -> None:
        """Deletes a route that was added with `POST /network_routes`.

        Traffic to its CIDR
        stops going via the next hop at once. Routes that an attachment installs
        (`origin` `attachment`) leave with the attachment and cannot be deleted here.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/network_routes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NetworkRoutesResourceWithRawResponse:
    def __init__(self, network_routes: NetworkRoutesResource) -> None:
        self._network_routes = network_routes

        self.create = to_raw_response_wrapper(
            network_routes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            network_routes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            network_routes.list,
        )
        self.delete = to_raw_response_wrapper(
            network_routes.delete,
        )


class AsyncNetworkRoutesResourceWithRawResponse:
    def __init__(self, network_routes: AsyncNetworkRoutesResource) -> None:
        self._network_routes = network_routes

        self.create = async_to_raw_response_wrapper(
            network_routes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            network_routes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            network_routes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            network_routes.delete,
        )


class NetworkRoutesResourceWithStreamingResponse:
    def __init__(self, network_routes: NetworkRoutesResource) -> None:
        self._network_routes = network_routes

        self.create = to_streamed_response_wrapper(
            network_routes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            network_routes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            network_routes.list,
        )
        self.delete = to_streamed_response_wrapper(
            network_routes.delete,
        )


class AsyncNetworkRoutesResourceWithStreamingResponse:
    def __init__(self, network_routes: AsyncNetworkRoutesResource) -> None:
        self._network_routes = network_routes

        self.create = async_to_streamed_response_wrapper(
            network_routes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            network_routes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            network_routes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            network_routes.delete,
        )
