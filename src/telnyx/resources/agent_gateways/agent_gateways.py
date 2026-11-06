# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from .apis import (
    APIsResource,
    AsyncAPIsResource,
    APIsResourceWithRawResponse,
    AsyncAPIsResourceWithRawResponse,
    APIsResourceWithStreamingResponse,
    AsyncAPIsResourceWithStreamingResponse,
)
from ...types import agent_gateway_list_params, agent_gateway_create_params, agent_gateway_retrieve_spend_logs_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .keys.keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .guardrails import (
    GuardrailsResource,
    AsyncGuardrailsResource,
    GuardrailsResourceWithRawResponse,
    AsyncGuardrailsResourceWithRawResponse,
    GuardrailsResourceWithStreamingResponse,
    AsyncGuardrailsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .mcp_servers import (
    McpServersResource,
    AsyncMcpServersResource,
    McpServersResourceWithRawResponse,
    AsyncMcpServersResourceWithRawResponse,
    McpServersResourceWithStreamingResponse,
    AsyncMcpServersResourceWithStreamingResponse,
)
from .teams.teams import (
    TeamsResource,
    AsyncTeamsResource,
    TeamsResourceWithRawResponse,
    AsyncTeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
    AsyncTeamsResourceWithStreamingResponse,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from .policy_attachments import (
    PolicyAttachmentsResource,
    AsyncPolicyAttachmentsResource,
    PolicyAttachmentsResourceWithRawResponse,
    AsyncPolicyAttachmentsResourceWithRawResponse,
    PolicyAttachmentsResourceWithStreamingResponse,
    AsyncPolicyAttachmentsResourceWithStreamingResponse,
)
from ...types.agent_gateway import AgentGateway
from ...types.agent_gateway_response import AgentGatewayResponse
from ...types.agent_gateway_retrieve_models_response import AgentGatewayRetrieveModelsResponse
from ...types.agent_gateway_retrieve_spend_logs_response import AgentGatewayRetrieveSpendLogsResponse

__all__ = ["AgentGatewaysResource", "AsyncAgentGatewaysResource"]


class AgentGatewaysResource(SyncAPIResource):
    @cached_property
    def apis(self) -> APIsResource:
        """REST APIs on an instance, served to agents as tools."""
        return APIsResource(self._client)

    @cached_property
    def guardrails(self) -> GuardrailsResource:
        """Checks an instance runs on model and tool requests."""
        return GuardrailsResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        """Keys on an instance."""
        return KeysResource(self._client)

    @cached_property
    def mcp_servers(self) -> McpServersResource:
        """MCP servers on an instance, served to agents at one MCP endpoint."""
        return McpServersResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        """Named sets of guardrails an instance applies to requests."""
        return PoliciesResource(self._client)

    @cached_property
    def policy_attachments(self) -> PolicyAttachmentsResource:
        """Where an instance applies each policy."""
        return PolicyAttachmentsResource(self._client)

    @cached_property
    def teams(self) -> TeamsResource:
        """Teams on an instance: shared model lists, budgets, and rate limits."""
        return TeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AgentGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AgentGatewaysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        wireguard_interface_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayResponse:
        """
        Creates an Agent Gateway instance on one of the account's WireGuard Interfaces.
        The instance starts `pending`, moves to `provisioning`, and then to `ready` or
        `failed`. It joins the WireGuard Interface as a peer named `agw-<instance id>`,
        and its `gateway_url` is set when it is `ready`.

        Args:
          wireguard_interface_id: One of the account's WireGuard Interfaces. The instance joins it as a peer, and
              the interface's other peers reach the instance.

          name: A label for people.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agent_gateways",
            body=maybe_transform(
                {
                    "wireguard_interface_id": wireguard_interface_id,
                    "name": name,
                },
                agent_gateway_create_params.AgentGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayResponse,
        )

    def retrieve(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayResponse:
        """
        Returns one of the account's Agent Gateway instances.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[AgentGateway]:
        """
        Lists the account's Agent Gateway instances, newest first, one page at a time.

        Args:
          page_number: The page to return, counting from 1.

          page_size: Results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agent_gateways",
            page=SyncDefaultFlatPagination[AgentGateway],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    agent_gateway_list_params.AgentGatewayListParams,
                ),
            ),
            model=AgentGateway,
        )

    def delete(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayResponse:
        """Deletes an Agent Gateway instance in any status.

        The response shows it
        `deleting`; repeating the request answers the same until the instance is gone,
        and then `404`. The instance's engine and everything stored on it are removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._delete(
            path_template("/agent_gateways/{instance_id}", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayResponse,
        )

    def retrieve_models(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayRetrieveModelsResponse:
        """Lists the models the instance serves.

        Each has the name a request uses, the
        Telnyx Inference model behind it, and its price per million tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/models", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayRetrieveModelsResponse,
        )

    def retrieve_spend_logs(
        self,
        instance_id: str,
        *,
        end: Union[str, datetime] | Omit = omit,
        key_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayRetrieveSpendLogsResponse:
        """
        Lists the requests the instance served with its keys, newest first, one page at
        a time. The window defaults to the last 24 hours and spans at most 31 days. A
        row appears a few seconds after its request. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          end: The window's end, an RFC 3339 timestamp with an offset. Defaults to now.

          key_id: Only the requests made with this key.

          page_number: The page to return, counting from 1.

          page_size: Results per page.

          start: The window's start, an RFC 3339 timestamp with an offset. Defaults to 24 hours
              before `end`.

          team_id: Only the requests made with this team's keys.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/spend_logs", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "key_id": key_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start": start,
                        "team_id": team_id,
                    },
                    agent_gateway_retrieve_spend_logs_params.AgentGatewayRetrieveSpendLogsParams,
                ),
            ),
            cast_to=AgentGatewayRetrieveSpendLogsResponse,
        )


class AsyncAgentGatewaysResource(AsyncAPIResource):
    @cached_property
    def apis(self) -> AsyncAPIsResource:
        """REST APIs on an instance, served to agents as tools."""
        return AsyncAPIsResource(self._client)

    @cached_property
    def guardrails(self) -> AsyncGuardrailsResource:
        """Checks an instance runs on model and tool requests."""
        return AsyncGuardrailsResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Keys on an instance."""
        return AsyncKeysResource(self._client)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResource:
        """MCP servers on an instance, served to agents at one MCP endpoint."""
        return AsyncMcpServersResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        """Named sets of guardrails an instance applies to requests."""
        return AsyncPoliciesResource(self._client)

    @cached_property
    def policy_attachments(self) -> AsyncPolicyAttachmentsResource:
        """Where an instance applies each policy."""
        return AsyncPolicyAttachmentsResource(self._client)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        """Teams on an instance: shared model lists, budgets, and rate limits."""
        return AsyncTeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAgentGatewaysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        wireguard_interface_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayResponse:
        """
        Creates an Agent Gateway instance on one of the account's WireGuard Interfaces.
        The instance starts `pending`, moves to `provisioning`, and then to `ready` or
        `failed`. It joins the WireGuard Interface as a peer named `agw-<instance id>`,
        and its `gateway_url` is set when it is `ready`.

        Args:
          wireguard_interface_id: One of the account's WireGuard Interfaces. The instance joins it as a peer, and
              the interface's other peers reach the instance.

          name: A label for people.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agent_gateways",
            body=await async_maybe_transform(
                {
                    "wireguard_interface_id": wireguard_interface_id,
                    "name": name,
                },
                agent_gateway_create_params.AgentGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayResponse,
        )

    async def retrieve(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayResponse:
        """
        Returns one of the account's Agent Gateway instances.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgentGateway, AsyncDefaultFlatPagination[AgentGateway]]:
        """
        Lists the account's Agent Gateway instances, newest first, one page at a time.

        Args:
          page_number: The page to return, counting from 1.

          page_size: Results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/agent_gateways",
            page=AsyncDefaultFlatPagination[AgentGateway],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    agent_gateway_list_params.AgentGatewayListParams,
                ),
            ),
            model=AgentGateway,
        )

    async def delete(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayResponse:
        """Deletes an Agent Gateway instance in any status.

        The response shows it
        `deleting`; repeating the request answers the same until the instance is gone,
        and then `404`. The instance's engine and everything stored on it are removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._delete(
            path_template("/agent_gateways/{instance_id}", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayResponse,
        )

    async def retrieve_models(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayRetrieveModelsResponse:
        """Lists the models the instance serves.

        Each has the name a request uses, the
        Telnyx Inference model behind it, and its price per million tokens.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/models", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayRetrieveModelsResponse,
        )

    async def retrieve_spend_logs(
        self,
        instance_id: str,
        *,
        end: Union[str, datetime] | Omit = omit,
        key_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayRetrieveSpendLogsResponse:
        """
        Lists the requests the instance served with its keys, newest first, one page at
        a time. The window defaults to the last 24 hours and spans at most 31 days. A
        row appears a few seconds after its request. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          end: The window's end, an RFC 3339 timestamp with an offset. Defaults to now.

          key_id: Only the requests made with this key.

          page_number: The page to return, counting from 1.

          page_size: Results per page.

          start: The window's start, an RFC 3339 timestamp with an offset. Defaults to 24 hours
              before `end`.

          team_id: Only the requests made with this team's keys.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/spend_logs", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "key_id": key_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "start": start,
                        "team_id": team_id,
                    },
                    agent_gateway_retrieve_spend_logs_params.AgentGatewayRetrieveSpendLogsParams,
                ),
            ),
            cast_to=AgentGatewayRetrieveSpendLogsResponse,
        )


class AgentGatewaysResourceWithRawResponse:
    def __init__(self, agent_gateways: AgentGatewaysResource) -> None:
        self._agent_gateways = agent_gateways

        self.create = to_raw_response_wrapper(
            agent_gateways.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agent_gateways.retrieve,
        )
        self.list = to_raw_response_wrapper(
            agent_gateways.list,
        )
        self.delete = to_raw_response_wrapper(
            agent_gateways.delete,
        )
        self.retrieve_models = to_raw_response_wrapper(
            agent_gateways.retrieve_models,
        )
        self.retrieve_spend_logs = to_raw_response_wrapper(
            agent_gateways.retrieve_spend_logs,
        )

    @cached_property
    def apis(self) -> APIsResourceWithRawResponse:
        """REST APIs on an instance, served to agents as tools."""
        return APIsResourceWithRawResponse(self._agent_gateways.apis)

    @cached_property
    def guardrails(self) -> GuardrailsResourceWithRawResponse:
        """Checks an instance runs on model and tool requests."""
        return GuardrailsResourceWithRawResponse(self._agent_gateways.guardrails)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        """Keys on an instance."""
        return KeysResourceWithRawResponse(self._agent_gateways.keys)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithRawResponse:
        """MCP servers on an instance, served to agents at one MCP endpoint."""
        return McpServersResourceWithRawResponse(self._agent_gateways.mcp_servers)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        """Named sets of guardrails an instance applies to requests."""
        return PoliciesResourceWithRawResponse(self._agent_gateways.policies)

    @cached_property
    def policy_attachments(self) -> PolicyAttachmentsResourceWithRawResponse:
        """Where an instance applies each policy."""
        return PolicyAttachmentsResourceWithRawResponse(self._agent_gateways.policy_attachments)

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        """Teams on an instance: shared model lists, budgets, and rate limits."""
        return TeamsResourceWithRawResponse(self._agent_gateways.teams)


class AsyncAgentGatewaysResourceWithRawResponse:
    def __init__(self, agent_gateways: AsyncAgentGatewaysResource) -> None:
        self._agent_gateways = agent_gateways

        self.create = async_to_raw_response_wrapper(
            agent_gateways.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agent_gateways.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            agent_gateways.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agent_gateways.delete,
        )
        self.retrieve_models = async_to_raw_response_wrapper(
            agent_gateways.retrieve_models,
        )
        self.retrieve_spend_logs = async_to_raw_response_wrapper(
            agent_gateways.retrieve_spend_logs,
        )

    @cached_property
    def apis(self) -> AsyncAPIsResourceWithRawResponse:
        """REST APIs on an instance, served to agents as tools."""
        return AsyncAPIsResourceWithRawResponse(self._agent_gateways.apis)

    @cached_property
    def guardrails(self) -> AsyncGuardrailsResourceWithRawResponse:
        """Checks an instance runs on model and tool requests."""
        return AsyncGuardrailsResourceWithRawResponse(self._agent_gateways.guardrails)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        """Keys on an instance."""
        return AsyncKeysResourceWithRawResponse(self._agent_gateways.keys)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithRawResponse:
        """MCP servers on an instance, served to agents at one MCP endpoint."""
        return AsyncMcpServersResourceWithRawResponse(self._agent_gateways.mcp_servers)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        """Named sets of guardrails an instance applies to requests."""
        return AsyncPoliciesResourceWithRawResponse(self._agent_gateways.policies)

    @cached_property
    def policy_attachments(self) -> AsyncPolicyAttachmentsResourceWithRawResponse:
        """Where an instance applies each policy."""
        return AsyncPolicyAttachmentsResourceWithRawResponse(self._agent_gateways.policy_attachments)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        """Teams on an instance: shared model lists, budgets, and rate limits."""
        return AsyncTeamsResourceWithRawResponse(self._agent_gateways.teams)


class AgentGatewaysResourceWithStreamingResponse:
    def __init__(self, agent_gateways: AgentGatewaysResource) -> None:
        self._agent_gateways = agent_gateways

        self.create = to_streamed_response_wrapper(
            agent_gateways.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agent_gateways.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            agent_gateways.list,
        )
        self.delete = to_streamed_response_wrapper(
            agent_gateways.delete,
        )
        self.retrieve_models = to_streamed_response_wrapper(
            agent_gateways.retrieve_models,
        )
        self.retrieve_spend_logs = to_streamed_response_wrapper(
            agent_gateways.retrieve_spend_logs,
        )

    @cached_property
    def apis(self) -> APIsResourceWithStreamingResponse:
        """REST APIs on an instance, served to agents as tools."""
        return APIsResourceWithStreamingResponse(self._agent_gateways.apis)

    @cached_property
    def guardrails(self) -> GuardrailsResourceWithStreamingResponse:
        """Checks an instance runs on model and tool requests."""
        return GuardrailsResourceWithStreamingResponse(self._agent_gateways.guardrails)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        """Keys on an instance."""
        return KeysResourceWithStreamingResponse(self._agent_gateways.keys)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithStreamingResponse:
        """MCP servers on an instance, served to agents at one MCP endpoint."""
        return McpServersResourceWithStreamingResponse(self._agent_gateways.mcp_servers)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        """Named sets of guardrails an instance applies to requests."""
        return PoliciesResourceWithStreamingResponse(self._agent_gateways.policies)

    @cached_property
    def policy_attachments(self) -> PolicyAttachmentsResourceWithStreamingResponse:
        """Where an instance applies each policy."""
        return PolicyAttachmentsResourceWithStreamingResponse(self._agent_gateways.policy_attachments)

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        """Teams on an instance: shared model lists, budgets, and rate limits."""
        return TeamsResourceWithStreamingResponse(self._agent_gateways.teams)


class AsyncAgentGatewaysResourceWithStreamingResponse:
    def __init__(self, agent_gateways: AsyncAgentGatewaysResource) -> None:
        self._agent_gateways = agent_gateways

        self.create = async_to_streamed_response_wrapper(
            agent_gateways.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agent_gateways.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            agent_gateways.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent_gateways.delete,
        )
        self.retrieve_models = async_to_streamed_response_wrapper(
            agent_gateways.retrieve_models,
        )
        self.retrieve_spend_logs = async_to_streamed_response_wrapper(
            agent_gateways.retrieve_spend_logs,
        )

    @cached_property
    def apis(self) -> AsyncAPIsResourceWithStreamingResponse:
        """REST APIs on an instance, served to agents as tools."""
        return AsyncAPIsResourceWithStreamingResponse(self._agent_gateways.apis)

    @cached_property
    def guardrails(self) -> AsyncGuardrailsResourceWithStreamingResponse:
        """Checks an instance runs on model and tool requests."""
        return AsyncGuardrailsResourceWithStreamingResponse(self._agent_gateways.guardrails)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        """Keys on an instance."""
        return AsyncKeysResourceWithStreamingResponse(self._agent_gateways.keys)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithStreamingResponse:
        """MCP servers on an instance, served to agents at one MCP endpoint."""
        return AsyncMcpServersResourceWithStreamingResponse(self._agent_gateways.mcp_servers)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """Named sets of guardrails an instance applies to requests."""
        return AsyncPoliciesResourceWithStreamingResponse(self._agent_gateways.policies)

    @cached_property
    def policy_attachments(self) -> AsyncPolicyAttachmentsResourceWithStreamingResponse:
        """Where an instance applies each policy."""
        return AsyncPolicyAttachmentsResourceWithStreamingResponse(self._agent_gateways.policy_attachments)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        """Teams on an instance: shared model lists, budgets, and rate limits."""
        return AsyncTeamsResourceWithStreamingResponse(self._agent_gateways.teams)
