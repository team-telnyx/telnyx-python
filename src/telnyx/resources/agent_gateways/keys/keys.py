# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .tool_permissions import (
    ToolPermissionsResource,
    AsyncToolPermissionsResource,
    ToolPermissionsResourceWithRawResponse,
    AsyncToolPermissionsResourceWithRawResponse,
    ToolPermissionsResourceWithStreamingResponse,
    AsyncToolPermissionsResourceWithStreamingResponse,
)
from ....types.agent_gateways import key_list_params, key_create_params, key_update_params
from ....types.agent_gateways.key_list_response import KeyListResponse
from ....types.agent_gateways.key_create_response import KeyCreateResponse
from ....types.agent_gateways.agent_gateway_key_response import AgentGatewayKeyResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    """Keys on an instance."""

    @cached_property
    def tool_permissions(self) -> ToolPermissionsResource:
        """The MCP servers and tools a key or team may use."""
        return ToolPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def create(
        self,
        instance_id: str,
        *,
        budget_resets_every: Optional[str] | Omit = omit,
        expires_in: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        models: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyCreateResponse:
        """Issues a key on the instance.

        The key's value is in this response only. Every
        field is optional; a key without `models` may use every model the instance
        serves. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          budget_resets_every: How often the spend resets: a number and a unit, `s`, `m`, `h`, or `d`.

          expires_in: How long until the key stops working: a number and a unit, `s`, `m`, `h`, or
              `d`.

          max_budget: The most the key may spend, in USD.

          max_parallel_requests: The most requests the key may have in flight at once.

          models: The models the key may use. Leave it out to allow every model.

          name: A label for people, unique on the instance.

          requests_per_minute: The most requests the key may make per minute.

          team_id: A team on the instance. The key shares the team's model list, budget, and rate
              limits.

          tokens_per_minute: The most tokens the key may use per minute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/keys", instance_id=instance_id),
            body=maybe_transform(
                {
                    "budget_resets_every": budget_resets_every,
                    "expires_in": expires_in,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "models": models,
                    "name": name,
                    "requests_per_minute": requests_per_minute,
                    "team_id": team_id,
                    "tokens_per_minute": tokens_per_minute,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCreateResponse,
        )

    def update(
        self,
        key_id: str,
        *,
        instance_id: str,
        blocked: bool | Omit = omit,
        budget_resets_every: Optional[str] | Omit = omit,
        expires_in: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayKeyResponse:
        """Changes a key's settings without reissuing it.

        A field left out stays as it is,
        and `null` clears it. `models: []` lifts the model restriction. `expires_in`
        counts from now. Setting `blocked` to `true` makes the instance refuse the key
        with `401` while keeping its settings and spend; `false` lets it through again.
        The instance must be `ready`; otherwise the request answers `409`.

        Args:
          blocked: `true` makes the instance refuse the key; `false` lets it through again.

          budget_resets_every: How often the spend resets.

          expires_in: How long from now until the key stops working.

          max_budget: The most the key may spend, in USD.

          max_parallel_requests: The most requests the key may have in flight at once.

          models: The models the key may use. `[]` allows every model.

          name: A label for people.

          requests_per_minute: The most requests the key may make per minute.

          team_id: Move the key to this team, or `null` to leave its team.

          tokens_per_minute: The most tokens the key may use per minute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._patch(
            path_template("/agent_gateways/{instance_id}/keys/{key_id}", instance_id=instance_id, key_id=key_id),
            body=maybe_transform(
                {
                    "blocked": blocked,
                    "budget_resets_every": budget_resets_every,
                    "expires_in": expires_in,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "models": models,
                    "name": name,
                    "requests_per_minute": requests_per_minute,
                    "team_id": team_id,
                    "tokens_per_minute": tokens_per_minute,
                },
                key_update_params.KeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayKeyResponse,
        )

    def list(
        self,
        instance_id: str,
        *,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """Lists the instance's keys, without their values.

        Returns the first 100. The
        instance must be `ready`; otherwise the request answers `409`.

        Args:
          team_id: Only the keys of this team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/keys", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"team_id": team_id}, key_list_params.KeyListParams),
            ),
            cast_to=KeyListResponse,
        )

    def delete(
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
    ) -> AgentGatewayKeyResponse:
        """Revokes a key and returns it as it was, without its value.

        The instance must be
        `ready`; otherwise the request answers `409`.

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
        return self._delete(
            path_template("/agent_gateways/{instance_id}/keys/{key_id}", instance_id=instance_id, key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayKeyResponse,
        )


class AsyncKeysResource(AsyncAPIResource):
    """Keys on an instance."""

    @cached_property
    def tool_permissions(self) -> AsyncToolPermissionsResource:
        """The MCP servers and tools a key or team may use."""
        return AsyncToolPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        instance_id: str,
        *,
        budget_resets_every: Optional[str] | Omit = omit,
        expires_in: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        models: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyCreateResponse:
        """Issues a key on the instance.

        The key's value is in this response only. Every
        field is optional; a key without `models` may use every model the instance
        serves. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          budget_resets_every: How often the spend resets: a number and a unit, `s`, `m`, `h`, or `d`.

          expires_in: How long until the key stops working: a number and a unit, `s`, `m`, `h`, or
              `d`.

          max_budget: The most the key may spend, in USD.

          max_parallel_requests: The most requests the key may have in flight at once.

          models: The models the key may use. Leave it out to allow every model.

          name: A label for people, unique on the instance.

          requests_per_minute: The most requests the key may make per minute.

          team_id: A team on the instance. The key shares the team's model list, budget, and rate
              limits.

          tokens_per_minute: The most tokens the key may use per minute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/keys", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "budget_resets_every": budget_resets_every,
                    "expires_in": expires_in,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "models": models,
                    "name": name,
                    "requests_per_minute": requests_per_minute,
                    "team_id": team_id,
                    "tokens_per_minute": tokens_per_minute,
                },
                key_create_params.KeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyCreateResponse,
        )

    async def update(
        self,
        key_id: str,
        *,
        instance_id: str,
        blocked: bool | Omit = omit,
        budget_resets_every: Optional[str] | Omit = omit,
        expires_in: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        max_parallel_requests: Optional[int] | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        team_id: Optional[str] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayKeyResponse:
        """Changes a key's settings without reissuing it.

        A field left out stays as it is,
        and `null` clears it. `models: []` lifts the model restriction. `expires_in`
        counts from now. Setting `blocked` to `true` makes the instance refuse the key
        with `401` while keeping its settings and spend; `false` lets it through again.
        The instance must be `ready`; otherwise the request answers `409`.

        Args:
          blocked: `true` makes the instance refuse the key; `false` lets it through again.

          budget_resets_every: How often the spend resets.

          expires_in: How long from now until the key stops working.

          max_budget: The most the key may spend, in USD.

          max_parallel_requests: The most requests the key may have in flight at once.

          models: The models the key may use. `[]` allows every model.

          name: A label for people.

          requests_per_minute: The most requests the key may make per minute.

          team_id: Move the key to this team, or `null` to leave its team.

          tokens_per_minute: The most tokens the key may use per minute.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._patch(
            path_template("/agent_gateways/{instance_id}/keys/{key_id}", instance_id=instance_id, key_id=key_id),
            body=await async_maybe_transform(
                {
                    "blocked": blocked,
                    "budget_resets_every": budget_resets_every,
                    "expires_in": expires_in,
                    "max_budget": max_budget,
                    "max_parallel_requests": max_parallel_requests,
                    "models": models,
                    "name": name,
                    "requests_per_minute": requests_per_minute,
                    "team_id": team_id,
                    "tokens_per_minute": tokens_per_minute,
                },
                key_update_params.KeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayKeyResponse,
        )

    async def list(
        self,
        instance_id: str,
        *,
        team_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """Lists the instance's keys, without their values.

        Returns the first 100. The
        instance must be `ready`; otherwise the request answers `409`.

        Args:
          team_id: Only the keys of this team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/keys", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"team_id": team_id}, key_list_params.KeyListParams),
            ),
            cast_to=KeyListResponse,
        )

    async def delete(
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
    ) -> AgentGatewayKeyResponse:
        """Revokes a key and returns it as it was, without its value.

        The instance must be
        `ready`; otherwise the request answers `409`.

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
        return await self._delete(
            path_template("/agent_gateways/{instance_id}/keys/{key_id}", instance_id=instance_id, key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayKeyResponse,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_raw_response_wrapper(
            keys.create,
        )
        self.update = to_raw_response_wrapper(
            keys.update,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.delete = to_raw_response_wrapper(
            keys.delete,
        )

    @cached_property
    def tool_permissions(self) -> ToolPermissionsResourceWithRawResponse:
        """The MCP servers and tools a key or team may use."""
        return ToolPermissionsResourceWithRawResponse(self._keys.tool_permissions)


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_raw_response_wrapper(
            keys.create,
        )
        self.update = async_to_raw_response_wrapper(
            keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )

    @cached_property
    def tool_permissions(self) -> AsyncToolPermissionsResourceWithRawResponse:
        """The MCP servers and tools a key or team may use."""
        return AsyncToolPermissionsResourceWithRawResponse(self._keys.tool_permissions)


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_streamed_response_wrapper(
            keys.create,
        )
        self.update = to_streamed_response_wrapper(
            keys.update,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )

    @cached_property
    def tool_permissions(self) -> ToolPermissionsResourceWithStreamingResponse:
        """The MCP servers and tools a key or team may use."""
        return ToolPermissionsResourceWithStreamingResponse(self._keys.tool_permissions)


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_streamed_response_wrapper(
            keys.create,
        )
        self.update = async_to_streamed_response_wrapper(
            keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )

    @cached_property
    def tool_permissions(self) -> AsyncToolPermissionsResourceWithStreamingResponse:
        """The MCP servers and tools a key or team may use."""
        return AsyncToolPermissionsResourceWithStreamingResponse(self._keys.tool_permissions)
