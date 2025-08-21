# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import connection_list_params, connection_list_active_calls_params
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
from ..types.connection_list_response import ConnectionListResponse
from ..types.connection_retrieve_response import ConnectionRetrieveResponse
from ..types.connection_list_active_calls_response import ConnectionListActiveCallsResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ConnectionsResourceWithStreamingResponse(self)

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
    ) -> ConnectionRetrieveResponse:
        """Retrieves the high-level details of an existing connection.

        To retrieve specific
        authentication information, use the endpoint for the specific connection type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: connection_list_params.Filter | NotGiven = NOT_GIVEN,
        page: connection_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "connection_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionListResponse:
        """
        Returns a list of your connections irrespective of type.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_name], filter[fqdn], filter[outbound_voice_profile_id],
              filter[outbound.outbound_voice_profile_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in ascending order.
                </li>

                <li>
                  <code>-connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connections",
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
                    connection_list_params.ConnectionListParams,
                ),
            ),
            cast_to=ConnectionListResponse,
        )

    def list_active_calls(
        self,
        connection_id: str,
        *,
        page: connection_list_active_calls_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionListActiveCallsResponse:
        """Lists all active calls for given connection.

        Acceptable connections are either
        SIP connections with webhook_url or xml_request_url, call control or texml.
        Returned results are cursor paginated.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[before], page[limit], page[size], page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/connections/{connection_id}/active_calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page}, connection_list_active_calls_params.ConnectionListActiveCallsParams
                ),
            ),
            cast_to=ConnectionListActiveCallsResponse,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncConnectionsResourceWithStreamingResponse(self)

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
    ) -> ConnectionRetrieveResponse:
        """Retrieves the high-level details of an existing connection.

        To retrieve specific
        authentication information, use the endpoint for the specific connection type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: connection_list_params.Filter | NotGiven = NOT_GIVEN,
        page: connection_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "connection_name", "active"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionListResponse:
        """
        Returns a list of your connections irrespective of type.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_name], filter[fqdn], filter[outbound_voice_profile_id],
              filter[outbound.outbound_voice_profile_id]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in ascending order.
                </li>

                <li>
                  <code>-connection_name</code>: sorts the result by the
                  <code>connection_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connections",
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
                    connection_list_params.ConnectionListParams,
                ),
            ),
            cast_to=ConnectionListResponse,
        )

    async def list_active_calls(
        self,
        connection_id: str,
        *,
        page: connection_list_active_calls_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionListActiveCallsResponse:
        """Lists all active calls for given connection.

        Acceptable connections are either
        SIP connections with webhook_url or xml_request_url, call control or texml.
        Returned results are cursor paginated.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[after],
              page[before], page[limit], page[size], page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/connections/{connection_id}/active_calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, connection_list_active_calls_params.ConnectionListActiveCallsParams
                ),
            ),
            cast_to=ConnectionListActiveCallsResponse,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = to_raw_response_wrapper(
            connections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.list_active_calls = to_raw_response_wrapper(
            connections.list_active_calls,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = async_to_raw_response_wrapper(
            connections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.list_active_calls = async_to_raw_response_wrapper(
            connections.list_active_calls,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.list_active_calls = to_streamed_response_wrapper(
            connections.list_active_calls,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = async_to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.list_active_calls = async_to_streamed_response_wrapper(
            connections.list_active_calls,
        )
