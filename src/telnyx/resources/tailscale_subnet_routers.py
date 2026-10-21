# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    tailscale_subnet_router_list_params,
    tailscale_subnet_router_create_params,
    tailscale_subnet_router_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.tailscale_subnet_router import TailscaleSubnetRouter
from ..types.tailscale_subnet_router_create_response import TailscaleSubnetRouterCreateResponse
from ..types.tailscale_subnet_router_delete_response import TailscaleSubnetRouterDeleteResponse
from ..types.tailscale_subnet_router_update_response import TailscaleSubnetRouterUpdateResponse
from ..types.tailscale_subnet_router_retrieve_response import TailscaleSubnetRouterRetrieveResponse

__all__ = ["TailscaleSubnetRoutersResource", "AsyncTailscaleSubnetRoutersResource"]


class TailscaleSubnetRoutersResource(SyncAPIResource):
    """Tailscale Subnet Router operations"""

    @cached_property
    def with_raw_response(self) -> TailscaleSubnetRoutersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TailscaleSubnetRoutersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TailscaleSubnetRoutersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TailscaleSubnetRoutersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        advertised_routes: SequenceNotStr[str],
        auth_key: str,
        name: str,
        network_id: str,
        region_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TailscaleSubnetRouterCreateResponse:
        """
        Creates a Tailscale Subnet Router on a Network and enrolls it in the user's
        tailnet with the auth key. The response returns the router with `status`
        `provisioning`. Poll `GET /tailscale_subnet_routers/{id}` until it is
        `provisioned`. Then approve its routes in the tailnet, unless an auto-approver
        covers them.

        Args:
          advertised_routes: IPv4 subnets of the Network that the router advertises to the tailnet. Each
              entry is a canonical CIDR that the Network routes. Default, loopback,
              link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
              are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.

          auth_key: A Tailscale auth key that enrolls the router in the user's tailnet: reusable,
              pre-approved, tagged, and not ephemeral. Telnyx stores it encrypted until
              enrollment succeeds, then discards it. It is never returned.

          name: A user specified name for the router.

          network_id: The id of the Network to attach the router to.

          region_code: The code of the region to create the router in. `GET /network_coverage` lists
              the regions whose `available_services` include `tailscale_subnet_router`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tailscale_subnet_routers",
            body=maybe_transform(
                {
                    "advertised_routes": advertised_routes,
                    "auth_key": auth_key,
                    "name": name,
                    "network_id": network_id,
                    "region_code": region_code,
                },
                tailscale_subnet_router_create_params.TailscaleSubnetRouterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterCreateResponse,
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
    ) -> TailscaleSubnetRouterRetrieveResponse:
        """
        Returns the details of a single Tailscale Subnet Router by its identifier,
        including its enrollment state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tailscale_subnet_routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        advertised_routes: SequenceNotStr[str] | Omit = omit,
        auth_key: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TailscaleSubnetRouterUpdateResponse:
        """
        Renames the router, changes its advertised routes, or retries a failed
        enrollment. Any change queues a new provisioning run and returns the router with
        `status` `provisioning`. The router keeps its machine identity on the tailnet.
        Send an empty object to retry a `failed` router with its stored auth key.
        Include a new `auth_key` only while the router has never enrolled. The router's
        Network and region cannot change: create a new router instead.

        Args:
          advertised_routes: IPv4 subnets of the Network that the router advertises to the tailnet. Each
              entry is a canonical CIDR that the Network routes. Default, loopback,
              link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
              are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.

          auth_key: A replacement Tailscale auth key. Accepted only while the router has never
              enrolled, for example after a `failed` enrollment. Never returned.

          name: A user specified name for the router.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/tailscale_subnet_routers/{id}", id=id),
            body=maybe_transform(
                {
                    "advertised_routes": advertised_routes,
                    "auth_key": auth_key,
                    "name": name,
                },
                tailscale_subnet_router_update_params.TailscaleSubnetRouterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterUpdateResponse,
        )

    def list(
        self,
        *,
        filter: tailscale_subnet_router_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[TailscaleSubnetRouter]:
        """
        Returns a paginated list of the Tailscale Subnet Routers on the account, with
        support for filtering by Network.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/tailscale_subnet_routers",
            page=SyncDefaultFlatPagination[TailscaleSubnetRouter],
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
                    tailscale_subnet_router_list_params.TailscaleSubnetRouterListParams,
                ),
            ),
            model=TailscaleSubnetRouter,
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
    ) -> TailscaleSubnetRouterDeleteResponse:
        """Removes the router from the Network and logs it out of the tailnet.

        The response
        returns the router with `status` `deleting`. The record disappears once removal
        completes. A machine entry can remain in the tailnet's admin console until it is
        removed there.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/tailscale_subnet_routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterDeleteResponse,
        )


class AsyncTailscaleSubnetRoutersResource(AsyncAPIResource):
    """Tailscale Subnet Router operations"""

    @cached_property
    def with_raw_response(self) -> AsyncTailscaleSubnetRoutersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTailscaleSubnetRoutersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTailscaleSubnetRoutersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTailscaleSubnetRoutersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        advertised_routes: SequenceNotStr[str],
        auth_key: str,
        name: str,
        network_id: str,
        region_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TailscaleSubnetRouterCreateResponse:
        """
        Creates a Tailscale Subnet Router on a Network and enrolls it in the user's
        tailnet with the auth key. The response returns the router with `status`
        `provisioning`. Poll `GET /tailscale_subnet_routers/{id}` until it is
        `provisioned`. Then approve its routes in the tailnet, unless an auto-approver
        covers them.

        Args:
          advertised_routes: IPv4 subnets of the Network that the router advertises to the tailnet. Each
              entry is a canonical CIDR that the Network routes. Default, loopback,
              link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
              are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.

          auth_key: A Tailscale auth key that enrolls the router in the user's tailnet: reusable,
              pre-approved, tagged, and not ephemeral. Telnyx stores it encrypted until
              enrollment succeeds, then discards it. It is never returned.

          name: A user specified name for the router.

          network_id: The id of the Network to attach the router to.

          region_code: The code of the region to create the router in. `GET /network_coverage` lists
              the regions whose `available_services` include `tailscale_subnet_router`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tailscale_subnet_routers",
            body=await async_maybe_transform(
                {
                    "advertised_routes": advertised_routes,
                    "auth_key": auth_key,
                    "name": name,
                    "network_id": network_id,
                    "region_code": region_code,
                },
                tailscale_subnet_router_create_params.TailscaleSubnetRouterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterCreateResponse,
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
    ) -> TailscaleSubnetRouterRetrieveResponse:
        """
        Returns the details of a single Tailscale Subnet Router by its identifier,
        including its enrollment state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tailscale_subnet_routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        advertised_routes: SequenceNotStr[str] | Omit = omit,
        auth_key: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TailscaleSubnetRouterUpdateResponse:
        """
        Renames the router, changes its advertised routes, or retries a failed
        enrollment. Any change queues a new provisioning run and returns the router with
        `status` `provisioning`. The router keeps its machine identity on the tailnet.
        Send an empty object to retry a `failed` router with its stored auth key.
        Include a new `auth_key` only while the router has never enrolled. The router's
        Network and region cannot change: create a new router instead.

        Args:
          advertised_routes: IPv4 subnets of the Network that the router advertises to the tailnet. Each
              entry is a canonical CIDR that the Network routes. Default, loopback,
              link-local, multicast, and Tailscale (`100.64.0.0/10`) ranges are rejected. So
              are ranges that overlap the router's own, `172.27.254.0/24` and `198.18.0.0/20`.

          auth_key: A replacement Tailscale auth key. Accepted only while the router has never
              enrolled, for example after a `failed` enrollment. Never returned.

          name: A user specified name for the router.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/tailscale_subnet_routers/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "advertised_routes": advertised_routes,
                    "auth_key": auth_key,
                    "name": name,
                },
                tailscale_subnet_router_update_params.TailscaleSubnetRouterUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterUpdateResponse,
        )

    def list(
        self,
        *,
        filter: tailscale_subnet_router_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TailscaleSubnetRouter, AsyncDefaultFlatPagination[TailscaleSubnetRouter]]:
        """
        Returns a paginated list of the Tailscale Subnet Routers on the account, with
        support for filtering by Network.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/tailscale_subnet_routers",
            page=AsyncDefaultFlatPagination[TailscaleSubnetRouter],
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
                    tailscale_subnet_router_list_params.TailscaleSubnetRouterListParams,
                ),
            ),
            model=TailscaleSubnetRouter,
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
    ) -> TailscaleSubnetRouterDeleteResponse:
        """Removes the router from the Network and logs it out of the tailnet.

        The response
        returns the router with `status` `deleting`. The record disappears once removal
        completes. A machine entry can remain in the tailnet's admin console until it is
        removed there.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/tailscale_subnet_routers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TailscaleSubnetRouterDeleteResponse,
        )


class TailscaleSubnetRoutersResourceWithRawResponse:
    def __init__(self, tailscale_subnet_routers: TailscaleSubnetRoutersResource) -> None:
        self._tailscale_subnet_routers = tailscale_subnet_routers

        self.create = to_raw_response_wrapper(
            tailscale_subnet_routers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tailscale_subnet_routers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tailscale_subnet_routers.update,
        )
        self.list = to_raw_response_wrapper(
            tailscale_subnet_routers.list,
        )
        self.delete = to_raw_response_wrapper(
            tailscale_subnet_routers.delete,
        )


class AsyncTailscaleSubnetRoutersResourceWithRawResponse:
    def __init__(self, tailscale_subnet_routers: AsyncTailscaleSubnetRoutersResource) -> None:
        self._tailscale_subnet_routers = tailscale_subnet_routers

        self.create = async_to_raw_response_wrapper(
            tailscale_subnet_routers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tailscale_subnet_routers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tailscale_subnet_routers.update,
        )
        self.list = async_to_raw_response_wrapper(
            tailscale_subnet_routers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tailscale_subnet_routers.delete,
        )


class TailscaleSubnetRoutersResourceWithStreamingResponse:
    def __init__(self, tailscale_subnet_routers: TailscaleSubnetRoutersResource) -> None:
        self._tailscale_subnet_routers = tailscale_subnet_routers

        self.create = to_streamed_response_wrapper(
            tailscale_subnet_routers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tailscale_subnet_routers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tailscale_subnet_routers.update,
        )
        self.list = to_streamed_response_wrapper(
            tailscale_subnet_routers.list,
        )
        self.delete = to_streamed_response_wrapper(
            tailscale_subnet_routers.delete,
        )


class AsyncTailscaleSubnetRoutersResourceWithStreamingResponse:
    def __init__(self, tailscale_subnet_routers: AsyncTailscaleSubnetRoutersResource) -> None:
        self._tailscale_subnet_routers = tailscale_subnet_routers

        self.create = async_to_streamed_response_wrapper(
            tailscale_subnet_routers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tailscale_subnet_routers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tailscale_subnet_routers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tailscale_subnet_routers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tailscale_subnet_routers.delete,
        )
