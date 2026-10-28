# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import tunnel_list_params, tunnel_create_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tunnel_list_response import TunnelListResponse
from ...types.tunnel_create_response import TunnelCreateResponse
from ...types.tunnel_retrieve_response import TunnelRetrieveResponse

__all__ = ["TunnelsResource", "AsyncTunnelsResource"]


class TunnelsResource(SyncAPIResource):
    """
    Tunnels connect a Network to hosts behind a tunnel process within the user's network.
    """

    @cached_property
    def actions(self) -> ActionsResource:
        """
        Tunnels connect a Network to hosts behind a tunnel process within the user's network.
        """
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TunnelsResourceWithStreamingResponse(self)

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
    ) -> TunnelCreateResponse:
        """Creates a tunnel and returns its `tunnel_token`.

        The token is the only
        credential the tunnel process needs, and this response and
        `POST /tunnels/{id}/actions/rotate_token` are the only ones that return it. A
        new tunnel is `inactive` until a tunnel process connects with the token.

        Args:
          name: A user specified name for the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tunnels",
            body=maybe_transform({"name": name}, tunnel_create_params.TunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TunnelCreateResponse,
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
    ) -> TunnelRetrieveResponse:
        """Retrieves a tunnel with its status and the tunnel processes connected to it.

        The
        response never includes `tunnel_token`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tunnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TunnelRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: tunnel_list_params.Filter | Omit = omit,
        page: tunnel_list_params.Page | Omit = omit,
        sort: Literal["name", "-name", "status", "-status", "created_at", "-created_at", "updated_at", "-updated_at"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TunnelListResponse:
        """
        Lists the tunnels on the account with their status and connected tunnel
        processes. Responses never include `tunnel_token`.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name],
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
            "/tunnels",
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
                    tunnel_list_params.TunnelListParams,
                ),
            ),
            cast_to=TunnelListResponse,
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
        """Deletes a tunnel.

        A tunnel that a route names as its next hop cannot be deleted;
        delete those routes first. Connected tunnel processes are disconnected and
        cannot reconnect with the tunnel's token.

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
            path_template("/tunnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTunnelsResource(AsyncAPIResource):
    """
    Tunnels connect a Network to hosts behind a tunnel process within the user's network.
    """

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Tunnels connect a Network to hosts behind a tunnel process within the user's network.
        """
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTunnelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTunnelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTunnelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTunnelsResourceWithStreamingResponse(self)

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
    ) -> TunnelCreateResponse:
        """Creates a tunnel and returns its `tunnel_token`.

        The token is the only
        credential the tunnel process needs, and this response and
        `POST /tunnels/{id}/actions/rotate_token` are the only ones that return it. A
        new tunnel is `inactive` until a tunnel process connects with the token.

        Args:
          name: A user specified name for the tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tunnels",
            body=await async_maybe_transform({"name": name}, tunnel_create_params.TunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TunnelCreateResponse,
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
    ) -> TunnelRetrieveResponse:
        """Retrieves a tunnel with its status and the tunnel processes connected to it.

        The
        response never includes `tunnel_token`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tunnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TunnelRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: tunnel_list_params.Filter | Omit = omit,
        page: tunnel_list_params.Page | Omit = omit,
        sort: Literal["name", "-name", "status", "-status", "created_at", "-created_at", "updated_at", "-updated_at"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TunnelListResponse:
        """
        Lists the tunnels on the account with their status and connected tunnel
        processes. Responses never include `tunnel_token`.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name],
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
            "/tunnels",
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
                    tunnel_list_params.TunnelListParams,
                ),
            ),
            cast_to=TunnelListResponse,
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
        """Deletes a tunnel.

        A tunnel that a route names as its next hop cannot be deleted;
        delete those routes first. Connected tunnel processes are disconnected and
        cannot reconnect with the tunnel's token.

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
            path_template("/tunnels/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TunnelsResourceWithRawResponse:
    def __init__(self, tunnels: TunnelsResource) -> None:
        self._tunnels = tunnels

        self.create = to_raw_response_wrapper(
            tunnels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tunnels.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tunnels.list,
        )
        self.delete = to_raw_response_wrapper(
            tunnels.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """
        Tunnels connect a Network to hosts behind a tunnel process within the user's network.
        """
        return ActionsResourceWithRawResponse(self._tunnels.actions)


class AsyncTunnelsResourceWithRawResponse:
    def __init__(self, tunnels: AsyncTunnelsResource) -> None:
        self._tunnels = tunnels

        self.create = async_to_raw_response_wrapper(
            tunnels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tunnels.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tunnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tunnels.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """
        Tunnels connect a Network to hosts behind a tunnel process within the user's network.
        """
        return AsyncActionsResourceWithRawResponse(self._tunnels.actions)


class TunnelsResourceWithStreamingResponse:
    def __init__(self, tunnels: TunnelsResource) -> None:
        self._tunnels = tunnels

        self.create = to_streamed_response_wrapper(
            tunnels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tunnels.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tunnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            tunnels.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """
        Tunnels connect a Network to hosts behind a tunnel process within the user's network.
        """
        return ActionsResourceWithStreamingResponse(self._tunnels.actions)


class AsyncTunnelsResourceWithStreamingResponse:
    def __init__(self, tunnels: AsyncTunnelsResource) -> None:
        self._tunnels = tunnels

        self.create = async_to_streamed_response_wrapper(
            tunnels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tunnels.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tunnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tunnels.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        Tunnels connect a Network to hosts behind a tunnel process within the user's network.
        """
        return AsyncActionsResourceWithStreamingResponse(self._tunnels.actions)
