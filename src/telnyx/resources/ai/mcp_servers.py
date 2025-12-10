# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import mcp_server_list_params, mcp_server_create_params, mcp_server_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPaginationTopLevelArray, AsyncDefaultFlatPaginationTopLevelArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.ai.mcp_server_list_response import McpServerListResponse
from ...types.ai.mcp_server_create_response import McpServerCreateResponse
from ...types.ai.mcp_server_update_response import McpServerUpdateResponse
from ...types.ai.mcp_server_retrieve_response import McpServerRetrieveResponse

__all__ = ["McpServersResource", "AsyncMcpServersResource"]


class McpServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return McpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return McpServersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: str,
        url: str,
        allowed_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        api_key_ref: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Create a new MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/mcp_servers",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "url": url,
                    "allowed_tools": allowed_tools,
                    "api_key_ref": api_key_ref,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerCreateResponse,
        )

    def retrieve(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerRetrieveResponse:
        """
        Retrieve details for a specific MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return self._get(
            f"/ai/mcp_servers/{mcp_server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerRetrieveResponse,
        )

    def update(
        self,
        mcp_server_id: str,
        *,
        id: str | Omit = omit,
        allowed_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        api_key_ref: Optional[str] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        type: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return self._put(
            f"/ai/mcp_servers/{mcp_server_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "allowed_tools": allowed_tools,
                    "api_key_ref": api_key_ref,
                    "created_at": created_at,
                    "name": name,
                    "type": type,
                    "url": url,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        type: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPaginationTopLevelArray[McpServerListResponse]:
        """
        Retrieve a list of MCP servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/mcp_servers",
            page=SyncDefaultFlatPaginationTopLevelArray[McpServerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "type": type,
                        "url": url,
                    },
                    mcp_server_list_params.McpServerListParams,
                ),
            ),
            model=McpServerListResponse,
        )

    def delete(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/mcp_servers/{mcp_server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMcpServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMcpServersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: str,
        url: str,
        allowed_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        api_key_ref: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerCreateResponse:
        """
        Create a new MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/mcp_servers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "url": url,
                    "allowed_tools": allowed_tools,
                    "api_key_ref": api_key_ref,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerCreateResponse,
        )

    async def retrieve(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerRetrieveResponse:
        """
        Retrieve details for a specific MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return await self._get(
            f"/ai/mcp_servers/{mcp_server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerRetrieveResponse,
        )

    async def update(
        self,
        mcp_server_id: str,
        *,
        id: str | Omit = omit,
        allowed_tools: Optional[SequenceNotStr[str]] | Omit = omit,
        api_key_ref: Optional[str] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        type: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerUpdateResponse:
        """
        Update an existing MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        return await self._put(
            f"/ai/mcp_servers/{mcp_server_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "allowed_tools": allowed_tools,
                    "api_key_ref": api_key_ref,
                    "created_at": created_at,
                    "name": name,
                    "type": type,
                    "url": url,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        type: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[McpServerListResponse, AsyncDefaultFlatPaginationTopLevelArray[McpServerListResponse]]:
        """
        Retrieve a list of MCP servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/mcp_servers",
            page=AsyncDefaultFlatPaginationTopLevelArray[McpServerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "type": type,
                        "url": url,
                    },
                    mcp_server_list_params.McpServerListParams,
                ),
            ),
            model=McpServerListResponse,
        )

    async def delete(
        self,
        mcp_server_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a specific MCP server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mcp_server_id:
            raise ValueError(f"Expected a non-empty value for `mcp_server_id` but received {mcp_server_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/mcp_servers/{mcp_server_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class McpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_raw_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mcp_servers.update,
        )
        self.list = to_raw_response_wrapper(
            mcp_servers.list,
        )
        self.delete = to_raw_response_wrapper(
            mcp_servers.delete,
        )


class AsyncMcpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = async_to_raw_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_raw_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mcp_servers.delete,
        )


class McpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_streamed_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = to_streamed_response_wrapper(
            mcp_servers.delete,
        )


class AsyncMcpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = async_to_streamed_response_wrapper(
            mcp_servers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mcp_servers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp_servers.delete,
        )
