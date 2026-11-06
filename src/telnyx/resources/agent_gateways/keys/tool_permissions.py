# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agent_gateways.keys import tool_permission_create_params
from ....types.agent_gateways.keys.agent_gateway_tool_permissions_response import AgentGatewayToolPermissionsResponse

__all__ = ["ToolPermissionsResource", "AsyncToolPermissionsResource"]


class ToolPermissionsResource(SyncAPIResource):
    """The MCP servers and tools a key or team may use."""

    @cached_property
    def with_raw_response(self) -> ToolPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ToolPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ToolPermissionsResourceWithStreamingResponse(self)

    def create(
        self,
        key_id: str,
        *,
        instance_id: str,
        servers: Iterable[tool_permission_create_params.Server],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayToolPermissionsResponse:
        """Replaces the grant whole and returns it.

        Every server must be one of the
        instance's MCP servers or APIs, named once. A key reaches the servers granted to
        it or to its team, and the servers open to every key; when both grant, only the
        servers in both. The instance must be `ready`; otherwise the request answers
        `409`.

        Args:
          servers: The servers granted, each with its tools. `[]` grants none.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._put(
            path_template(
                "/agent_gateways/{instance_id}/keys/{key_id}/tool_permissions", instance_id=instance_id, key_id=key_id
            ),
            body=maybe_transform({"servers": servers}, tool_permission_create_params.ToolPermissionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayToolPermissionsResponse,
        )

    def list(
        self,
        key_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayToolPermissionsResponse:
        """
        Returns the MCP servers and APIs the key may use, and the tools within each.
        `servers: []` means none. The instance must be `ready`; otherwise the request
        answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._get(
            path_template(
                "/agent_gateways/{instance_id}/keys/{key_id}/tool_permissions", instance_id=instance_id, key_id=key_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayToolPermissionsResponse,
        )


class AsyncToolPermissionsResource(AsyncAPIResource):
    """The MCP servers and tools a key or team may use."""

    @cached_property
    def with_raw_response(self) -> AsyncToolPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncToolPermissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        key_id: str,
        *,
        instance_id: str,
        servers: Iterable[tool_permission_create_params.Server],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayToolPermissionsResponse:
        """Replaces the grant whole and returns it.

        Every server must be one of the
        instance's MCP servers or APIs, named once. A key reaches the servers granted to
        it or to its team, and the servers open to every key; when both grant, only the
        servers in both. The instance must be `ready`; otherwise the request answers
        `409`.

        Args:
          servers: The servers granted, each with its tools. `[]` grants none.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._put(
            path_template(
                "/agent_gateways/{instance_id}/keys/{key_id}/tool_permissions", instance_id=instance_id, key_id=key_id
            ),
            body=await async_maybe_transform(
                {"servers": servers}, tool_permission_create_params.ToolPermissionCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayToolPermissionsResponse,
        )

    async def list(
        self,
        key_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayToolPermissionsResponse:
        """
        Returns the MCP servers and APIs the key may use, and the tools within each.
        `servers: []` means none. The instance must be `ready`; otherwise the request
        answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._get(
            path_template(
                "/agent_gateways/{instance_id}/keys/{key_id}/tool_permissions", instance_id=instance_id, key_id=key_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayToolPermissionsResponse,
        )


class ToolPermissionsResourceWithRawResponse:
    def __init__(self, tool_permissions: ToolPermissionsResource) -> None:
        self._tool_permissions = tool_permissions

        self.create = to_raw_response_wrapper(
            tool_permissions.create,
        )
        self.list = to_raw_response_wrapper(
            tool_permissions.list,
        )


class AsyncToolPermissionsResourceWithRawResponse:
    def __init__(self, tool_permissions: AsyncToolPermissionsResource) -> None:
        self._tool_permissions = tool_permissions

        self.create = async_to_raw_response_wrapper(
            tool_permissions.create,
        )
        self.list = async_to_raw_response_wrapper(
            tool_permissions.list,
        )


class ToolPermissionsResourceWithStreamingResponse:
    def __init__(self, tool_permissions: ToolPermissionsResource) -> None:
        self._tool_permissions = tool_permissions

        self.create = to_streamed_response_wrapper(
            tool_permissions.create,
        )
        self.list = to_streamed_response_wrapper(
            tool_permissions.list,
        )


class AsyncToolPermissionsResourceWithStreamingResponse:
    def __init__(self, tool_permissions: AsyncToolPermissionsResource) -> None:
        self._tool_permissions = tool_permissions

        self.create = async_to_streamed_response_wrapper(
            tool_permissions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tool_permissions.list,
        )
