# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ...types.agent_gateways import api_create_params, api_update_params
from ...types.agent_gateways.api_list_response import APIListResponse
from ...types.agent_gateways.agent_gateway_api_response import AgentGatewayAPIResponse

__all__ = ["APIsResource", "AsyncAPIsResource"]


class APIsResource(SyncAPIResource):
    """REST APIs on an instance, served to agents as tools."""

    @cached_property
    def with_raw_response(self) -> APIsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return APIsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return APIsResourceWithStreamingResponse(self)

    def create(
        self,
        instance_id: str,
        *,
        name: str,
        spec_url: str,
        auth: api_create_params.Auth | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayAPIResponse:
        """Adds a REST API by its OpenAPI description.

        Each operation becomes a tool at
        `{gateway_url}/mcp`, named with the API's `name`, a hyphen, and the lowercased
        `operationId`. A description the gateway cannot fetch yields an API with no
        tools. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          name: A name for the API, unique on the instance across MCP servers and APIs,
              regardless of case. Up to 100 letters, digits, `_`, and `.`. The gateway
              prefixes the API's tools with it and a hyphen.

          spec_url: The URL of the API's OpenAPI description: OpenAPI 3.0, OpenAPI 3.1, or Swagger
              2.0.

          auth: How the gateway authenticates to the API. AWS Signature Version 4 is for MCP
              servers only. Replaced whole on an update.

          base_url: Where the gateway sends the API's requests. Without it, the gateway takes the
              description's first `servers` entry.

          forwarded_headers: Headers copied from the agent's request, by name.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          static_headers: Headers sent on every request.

          tools: The operations the API exposes as tools, by tool name. `[]` exposes every
              operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/apis", instance_id=instance_id),
            body=maybe_transform(
                {
                    "name": name,
                    "spec_url": spec_url,
                    "auth": auth,
                    "base_url": base_url,
                    "forwarded_headers": forwarded_headers,
                    "open_to_every_key": open_to_every_key,
                    "static_headers": static_headers,
                    "tools": tools,
                },
                api_create_params.APICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayAPIResponse,
        )

    def update(
        self,
        api_id: str,
        *,
        instance_id: str,
        auth: api_update_params.Auth | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        spec_url: str | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayAPIResponse:
        """Changes an API's settings.

        A field left out stays as it is, `"base_url": null`
        clears the base URL, and `auth` is replaced whole. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          auth: How the gateway authenticates to the API. AWS Signature Version 4 is for MCP
              servers only. Replaced whole on an update.

          base_url: Where the gateway sends the API's requests. Without it, the gateway takes the
              description's first `servers` entry.

          forwarded_headers: Headers copied from the agent's request, by name.

          name: A name for the API, unique on the instance across MCP servers and APIs,
              regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
              API's tools with it and a hyphen.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          spec_url: The URL of the API's OpenAPI description: OpenAPI 3.0, OpenAPI 3.1, or Swagger
              2.0.

          static_headers: Headers sent on every request.

          tools: The operations the API exposes as tools, by tool name. `[]` exposes every
              operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not api_id:
            raise ValueError(f"Expected a non-empty value for `api_id` but received {api_id!r}")
        return self._patch(
            path_template("/agent_gateways/{instance_id}/apis/{api_id}", instance_id=instance_id, api_id=api_id),
            body=maybe_transform(
                {
                    "auth": auth,
                    "base_url": base_url,
                    "forwarded_headers": forwarded_headers,
                    "name": name,
                    "open_to_every_key": open_to_every_key,
                    "spec_url": spec_url,
                    "static_headers": static_headers,
                    "tools": tools,
                },
                api_update_params.APIUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayAPIResponse,
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
    ) -> APIListResponse:
        """Lists the REST APIs the instance serves as tools, without their credentials.

        The
        instance must be `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/apis", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIListResponse,
        )

    def delete(
        self,
        api_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayAPIResponse:
        """Removes an API and returns it as it was.

        An MCP server's `id` answers `404`. The
        instance must be `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not api_id:
            raise ValueError(f"Expected a non-empty value for `api_id` but received {api_id!r}")
        return self._delete(
            path_template("/agent_gateways/{instance_id}/apis/{api_id}", instance_id=instance_id, api_id=api_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayAPIResponse,
        )


class AsyncAPIsResource(AsyncAPIResource):
    """REST APIs on an instance, served to agents as tools."""

    @cached_property
    def with_raw_response(self) -> AsyncAPIsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAPIsResourceWithStreamingResponse(self)

    async def create(
        self,
        instance_id: str,
        *,
        name: str,
        spec_url: str,
        auth: api_create_params.Auth | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayAPIResponse:
        """Adds a REST API by its OpenAPI description.

        Each operation becomes a tool at
        `{gateway_url}/mcp`, named with the API's `name`, a hyphen, and the lowercased
        `operationId`. A description the gateway cannot fetch yields an API with no
        tools. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          name: A name for the API, unique on the instance across MCP servers and APIs,
              regardless of case. Up to 100 letters, digits, `_`, and `.`. The gateway
              prefixes the API's tools with it and a hyphen.

          spec_url: The URL of the API's OpenAPI description: OpenAPI 3.0, OpenAPI 3.1, or Swagger
              2.0.

          auth: How the gateway authenticates to the API. AWS Signature Version 4 is for MCP
              servers only. Replaced whole on an update.

          base_url: Where the gateway sends the API's requests. Without it, the gateway takes the
              description's first `servers` entry.

          forwarded_headers: Headers copied from the agent's request, by name.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          static_headers: Headers sent on every request.

          tools: The operations the API exposes as tools, by tool name. `[]` exposes every
              operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/apis", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "spec_url": spec_url,
                    "auth": auth,
                    "base_url": base_url,
                    "forwarded_headers": forwarded_headers,
                    "open_to_every_key": open_to_every_key,
                    "static_headers": static_headers,
                    "tools": tools,
                },
                api_create_params.APICreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayAPIResponse,
        )

    async def update(
        self,
        api_id: str,
        *,
        instance_id: str,
        auth: api_update_params.Auth | Omit = omit,
        base_url: Optional[str] | Omit = omit,
        forwarded_headers: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        open_to_every_key: bool | Omit = omit,
        spec_url: str | Omit = omit,
        static_headers: Dict[str, str] | Omit = omit,
        tools: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayAPIResponse:
        """Changes an API's settings.

        A field left out stays as it is, `"base_url": null`
        clears the base URL, and `auth` is replaced whole. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          auth: How the gateway authenticates to the API. AWS Signature Version 4 is for MCP
              servers only. Replaced whole on an update.

          base_url: Where the gateway sends the API's requests. Without it, the gateway takes the
              description's first `servers` entry.

          forwarded_headers: Headers copied from the agent's request, by name.

          name: A name for the API, unique on the instance across MCP servers and APIs,
              regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
              API's tools with it and a hyphen.

          open_to_every_key: `true` lets every key on the instance use the server, granted or not.

          spec_url: The URL of the API's OpenAPI description: OpenAPI 3.0, OpenAPI 3.1, or Swagger
              2.0.

          static_headers: Headers sent on every request.

          tools: The operations the API exposes as tools, by tool name. `[]` exposes every
              operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not api_id:
            raise ValueError(f"Expected a non-empty value for `api_id` but received {api_id!r}")
        return await self._patch(
            path_template("/agent_gateways/{instance_id}/apis/{api_id}", instance_id=instance_id, api_id=api_id),
            body=await async_maybe_transform(
                {
                    "auth": auth,
                    "base_url": base_url,
                    "forwarded_headers": forwarded_headers,
                    "name": name,
                    "open_to_every_key": open_to_every_key,
                    "spec_url": spec_url,
                    "static_headers": static_headers,
                    "tools": tools,
                },
                api_update_params.APIUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayAPIResponse,
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
    ) -> APIListResponse:
        """Lists the REST APIs the instance serves as tools, without their credentials.

        The
        instance must be `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/apis", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIListResponse,
        )

    async def delete(
        self,
        api_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayAPIResponse:
        """Removes an API and returns it as it was.

        An MCP server's `id` answers `404`. The
        instance must be `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not api_id:
            raise ValueError(f"Expected a non-empty value for `api_id` but received {api_id!r}")
        return await self._delete(
            path_template("/agent_gateways/{instance_id}/apis/{api_id}", instance_id=instance_id, api_id=api_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayAPIResponse,
        )


class APIsResourceWithRawResponse:
    def __init__(self, apis: APIsResource) -> None:
        self._apis = apis

        self.create = to_raw_response_wrapper(
            apis.create,
        )
        self.update = to_raw_response_wrapper(
            apis.update,
        )
        self.list = to_raw_response_wrapper(
            apis.list,
        )
        self.delete = to_raw_response_wrapper(
            apis.delete,
        )


class AsyncAPIsResourceWithRawResponse:
    def __init__(self, apis: AsyncAPIsResource) -> None:
        self._apis = apis

        self.create = async_to_raw_response_wrapper(
            apis.create,
        )
        self.update = async_to_raw_response_wrapper(
            apis.update,
        )
        self.list = async_to_raw_response_wrapper(
            apis.list,
        )
        self.delete = async_to_raw_response_wrapper(
            apis.delete,
        )


class APIsResourceWithStreamingResponse:
    def __init__(self, apis: APIsResource) -> None:
        self._apis = apis

        self.create = to_streamed_response_wrapper(
            apis.create,
        )
        self.update = to_streamed_response_wrapper(
            apis.update,
        )
        self.list = to_streamed_response_wrapper(
            apis.list,
        )
        self.delete = to_streamed_response_wrapper(
            apis.delete,
        )


class AsyncAPIsResourceWithStreamingResponse:
    def __init__(self, apis: AsyncAPIsResource) -> None:
        self._apis = apis

        self.create = async_to_streamed_response_wrapper(
            apis.create,
        )
        self.update = async_to_streamed_response_wrapper(
            apis.update,
        )
        self.list = async_to_streamed_response_wrapper(
            apis.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            apis.delete,
        )
