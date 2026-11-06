# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.agent_gateways import mcp_server_create_params, mcp_server_update_params
from ...types.agent_gateways.mcp_server_list_response import McpServerListResponse
from ...types.agent_gateways.agent_gateway_mcp_server_response import AgentGatewayMcpServerResponse

__all__ = ["McpServersResource", "AsyncMcpServersResource"]


class McpServersResource(SyncAPIResource):
    """MCP servers on an instance, served to agents at one MCP endpoint."""

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
        instance_id: str,
        *,
        name: str,
        url: str,
        auth: mcp_server_create_params.Auth | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        transport: Literal["http", "sse"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayMcpServerResponse:
        """Adds an MCP server.

        The instance serves its tools at `{gateway_url}/mcp`, each
        named with the server's `name` and a hyphen, to the keys granted the server and,
        with `open_to_every_key`, to every key. The instance must be `ready`; otherwise
        the request answers `409`.

        Args:
          name: A name for the server, unique on the instance across MCP servers and APIs,
              regardless of case. Up to 100 letters, digits, `_`, and `.`. The gateway
              prefixes the server's tools with it and a hyphen.

          url: The server's MCP endpoint, `http` or `https`.

          auth: How the gateway authenticates to the server. Replaced whole on an update;
              `{"type": "none"}` removes the credential.

          forwarded_headers: Headers copied from the agent's request, by name.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          static_headers: Headers sent on every request.

          tools: The tools the server exposes to every key, by name. `[]` exposes every tool.

          transport: `http` for Streamable HTTP, or `sse` for Server-Sent Events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/mcp_servers", instance_id=instance_id),
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "auth": auth,
                    "forwarded_headers": forwarded_headers,
                    "open_to_every_key": open_to_every_key,
                    "static_headers": static_headers,
                    "tools": tools,
                    "transport": transport,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayMcpServerResponse,
        )

    def update(
        self,
        server_id: str,
        *,
        instance_id: str,
        auth: mcp_server_update_params.Auth | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        transport: Literal["http", "sse"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayMcpServerResponse:
        """Changes an MCP server's settings.

        A field left out stays as it is. `auth` is
        replaced whole, `tools: []` exposes every tool, and `static_headers: {}` clears
        the headers. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          auth: How the gateway authenticates to the server. Replaced whole on an update;
              `{"type": "none"}` removes the credential.

          forwarded_headers: Headers copied from the agent's request, by name.

          name: A name for the server, unique on the instance across MCP servers and APIs,
              regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
              server's tools with it and a hyphen.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          static_headers: Headers sent on every request.

          tools: The tools the server exposes to every key, by name. `[]` exposes every tool.

          transport: `http` for Streamable HTTP, or `sse` for Server-Sent Events.

          url: The server's MCP endpoint, `http` or `https`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._patch(
            path_template(
                "/agent_gateways/{instance_id}/mcp_servers/{server_id}", instance_id=instance_id, server_id=server_id
            ),
            body=maybe_transform(
                {
                    "auth": auth,
                    "forwarded_headers": forwarded_headers,
                    "name": name,
                    "open_to_every_key": open_to_every_key,
                    "static_headers": static_headers,
                    "tools": tools,
                    "transport": transport,
                    "url": url,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayMcpServerResponse,
        )

    def list(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """
        Lists the MCP servers the instance serves at `{gateway_url}/mcp`, without their
        credentials. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/mcp_servers", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )

    def delete(
        self,
        server_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayMcpServerResponse:
        """Removes an MCP server and returns it as it was.

        Its `id` stays in the tool
        permissions that name it until they are next set. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return self._delete(
            path_template(
                "/agent_gateways/{instance_id}/mcp_servers/{server_id}", instance_id=instance_id, server_id=server_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayMcpServerResponse,
        )


class AsyncMcpServersResource(AsyncAPIResource):
    """MCP servers on an instance, served to agents at one MCP endpoint."""

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
        instance_id: str,
        *,
        name: str,
        url: str,
        auth: mcp_server_create_params.Auth | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        transport: Literal["http", "sse"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayMcpServerResponse:
        """Adds an MCP server.

        The instance serves its tools at `{gateway_url}/mcp`, each
        named with the server's `name` and a hyphen, to the keys granted the server and,
        with `open_to_every_key`, to every key. The instance must be `ready`; otherwise
        the request answers `409`.

        Args:
          name: A name for the server, unique on the instance across MCP servers and APIs,
              regardless of case. Up to 100 letters, digits, `_`, and `.`. The gateway
              prefixes the server's tools with it and a hyphen.

          url: The server's MCP endpoint, `http` or `https`.

          auth: How the gateway authenticates to the server. Replaced whole on an update;
              `{"type": "none"}` removes the credential.

          forwarded_headers: Headers copied from the agent's request, by name.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          static_headers: Headers sent on every request.

          tools: The tools the server exposes to every key, by name. `[]` exposes every tool.

          transport: `http` for Streamable HTTP, or `sse` for Server-Sent Events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/mcp_servers", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "auth": auth,
                    "forwarded_headers": forwarded_headers,
                    "open_to_every_key": open_to_every_key,
                    "static_headers": static_headers,
                    "tools": tools,
                    "transport": transport,
                },
                mcp_server_create_params.McpServerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayMcpServerResponse,
        )

    async def update(
        self,
        server_id: str,
        *,
        instance_id: str,
        auth: mcp_server_update_params.Auth | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        transport: Literal["http", "sse"] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayMcpServerResponse:
        """Changes an MCP server's settings.

        A field left out stays as it is. `auth` is
        replaced whole, `tools: []` exposes every tool, and `static_headers: {}` clears
        the headers. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          auth: How the gateway authenticates to the server. Replaced whole on an update;
              `{"type": "none"}` removes the credential.

          forwarded_headers: Headers copied from the agent's request, by name.

          name: A name for the server, unique on the instance across MCP servers and APIs,
              regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
              server's tools with it and a hyphen.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          static_headers: Headers sent on every request.

          tools: The tools the server exposes to every key, by name. `[]` exposes every tool.

          transport: `http` for Streamable HTTP, or `sse` for Server-Sent Events.

          url: The server's MCP endpoint, `http` or `https`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._patch(
            path_template(
                "/agent_gateways/{instance_id}/mcp_servers/{server_id}", instance_id=instance_id, server_id=server_id
            ),
            body=await async_maybe_transform(
                {
                    "auth": auth,
                    "forwarded_headers": forwarded_headers,
                    "name": name,
                    "open_to_every_key": open_to_every_key,
                    "static_headers": static_headers,
                    "tools": tools,
                    "transport": transport,
                    "url": url,
                },
                mcp_server_update_params.McpServerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayMcpServerResponse,
        )

    async def list(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """
        Lists the MCP servers the instance serves at `{gateway_url}/mcp`, without their
        credentials. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/mcp_servers", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )

    async def delete(
        self,
        server_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayMcpServerResponse:
        """Removes an MCP server and returns it as it was.

        Its `id` stays in the tool
        permissions that name it until they are next set. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not server_id:
            raise ValueError(f"Expected a non-empty value for `server_id` but received {server_id!r}")
        return await self._delete(
            path_template(
                "/agent_gateways/{instance_id}/mcp_servers/{server_id}", instance_id=instance_id, server_id=server_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayMcpServerResponse,
        )


class McpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.create = to_raw_response_wrapper(
            mcp_servers.create,
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
        self.update = async_to_streamed_response_wrapper(
            mcp_servers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mcp_servers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mcp_servers.delete,
        )
