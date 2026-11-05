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
from ....types.agent_gateways import team_create_params, team_update_params
from ....types.agent_gateways.team_list_response import TeamListResponse
from ....types.agent_gateways.agent_gateway_team_response import AgentGatewayTeamResponse

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    """Teams on an instance: shared model lists, budgets, and rate limits."""

    @cached_property
    def tool_permissions(self) -> ToolPermissionsResource:
        """The MCP servers and tools a key or team may use."""
        return ToolPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def create(
        self,
        instance_id: str,
        *,
        name: str,
        budget_resets_every: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        models: Optional[SequenceNotStr[str]] | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayTeamResponse:
        """Creates a team on the instance.

        A team is a model list, a budget, and rate
        limits that its keys share. Names need not be unique; the `id` identifies the
        team. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          name: A label for people.

          budget_resets_every: How often the spend resets: a number and a unit, `s`, `m`, `h`, or `d`.

          max_budget: The most the team's keys may spend together, in USD.

          models: The models the team's keys may use. Leave it out to allow every model.

          requests_per_minute: The most requests the team's keys may make per minute, together.

          tokens_per_minute: The most tokens the team's keys may use per minute, together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/teams", instance_id=instance_id),
            body=maybe_transform(
                {
                    "name": name,
                    "budget_resets_every": budget_resets_every,
                    "max_budget": max_budget,
                    "models": models,
                    "requests_per_minute": requests_per_minute,
                    "tokens_per_minute": tokens_per_minute,
                },
                team_create_params.TeamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayTeamResponse,
        )

    def update(
        self,
        team_id: str,
        *,
        instance_id: str,
        blocked: bool | Omit = omit,
        budget_resets_every: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayTeamResponse:
        """Changes a team's settings.

        A field left out stays as it is, and `null` clears
        it. `models: []` lifts the model restriction. Setting `blocked` to `true` makes
        the instance refuse every key in the team with `401`. The instance must be
        `ready`; otherwise the request answers `409`.

        Args:
          blocked: `true` makes the instance refuse every key in the team; `false` lets them
              through again.

          budget_resets_every: How often the spend resets.

          max_budget: The most the team's keys may spend together, in USD.

          models: The models the team's keys may use. `[]` allows every model.

          name: A label for people.

          requests_per_minute: The most requests the team's keys may make per minute, together.

          tokens_per_minute: The most tokens the team's keys may use per minute, together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._patch(
            path_template("/agent_gateways/{instance_id}/teams/{team_id}", instance_id=instance_id, team_id=team_id),
            body=maybe_transform(
                {
                    "blocked": blocked,
                    "budget_resets_every": budget_resets_every,
                    "max_budget": max_budget,
                    "models": models,
                    "name": name,
                    "requests_per_minute": requests_per_minute,
                    "tokens_per_minute": tokens_per_minute,
                },
                team_update_params.TeamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayTeamResponse,
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
    ) -> TeamListResponse:
        """Lists the instance's teams.

        The instance must be `ready`; otherwise the request
        answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/teams", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamListResponse,
        )

    def delete(
        self,
        team_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayTeamResponse:
        """Deletes a team that has no keys and returns it.

        A team that still has keys
        answers `409`; delete or move its keys first. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._delete(
            path_template("/agent_gateways/{instance_id}/teams/{team_id}", instance_id=instance_id, team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayTeamResponse,
        )


class AsyncTeamsResource(AsyncAPIResource):
    """Teams on an instance: shared model lists, budgets, and rate limits."""

    @cached_property
    def tool_permissions(self) -> AsyncToolPermissionsResource:
        """The MCP servers and tools a key or team may use."""
        return AsyncToolPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    async def create(
        self,
        instance_id: str,
        *,
        name: str,
        budget_resets_every: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        models: Optional[SequenceNotStr[str]] | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayTeamResponse:
        """Creates a team on the instance.

        A team is a model list, a budget, and rate
        limits that its keys share. Names need not be unique; the `id` identifies the
        team. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          name: A label for people.

          budget_resets_every: How often the spend resets: a number and a unit, `s`, `m`, `h`, or `d`.

          max_budget: The most the team's keys may spend together, in USD.

          models: The models the team's keys may use. Leave it out to allow every model.

          requests_per_minute: The most requests the team's keys may make per minute, together.

          tokens_per_minute: The most tokens the team's keys may use per minute, together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/teams", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "budget_resets_every": budget_resets_every,
                    "max_budget": max_budget,
                    "models": models,
                    "requests_per_minute": requests_per_minute,
                    "tokens_per_minute": tokens_per_minute,
                },
                team_create_params.TeamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayTeamResponse,
        )

    async def update(
        self,
        team_id: str,
        *,
        instance_id: str,
        blocked: bool | Omit = omit,
        budget_resets_every: Optional[str] | Omit = omit,
        max_budget: Optional[float] | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        requests_per_minute: Optional[int] | Omit = omit,
        tokens_per_minute: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayTeamResponse:
        """Changes a team's settings.

        A field left out stays as it is, and `null` clears
        it. `models: []` lifts the model restriction. Setting `blocked` to `true` makes
        the instance refuse every key in the team with `401`. The instance must be
        `ready`; otherwise the request answers `409`.

        Args:
          blocked: `true` makes the instance refuse every key in the team; `false` lets them
              through again.

          budget_resets_every: How often the spend resets.

          max_budget: The most the team's keys may spend together, in USD.

          models: The models the team's keys may use. `[]` allows every model.

          name: A label for people.

          requests_per_minute: The most requests the team's keys may make per minute, together.

          tokens_per_minute: The most tokens the team's keys may use per minute, together.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._patch(
            path_template("/agent_gateways/{instance_id}/teams/{team_id}", instance_id=instance_id, team_id=team_id),
            body=await async_maybe_transform(
                {
                    "blocked": blocked,
                    "budget_resets_every": budget_resets_every,
                    "max_budget": max_budget,
                    "models": models,
                    "name": name,
                    "requests_per_minute": requests_per_minute,
                    "tokens_per_minute": tokens_per_minute,
                },
                team_update_params.TeamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayTeamResponse,
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
    ) -> TeamListResponse:
        """Lists the instance's teams.

        The instance must be `ready`; otherwise the request
        answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/teams", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TeamListResponse,
        )

    async def delete(
        self,
        team_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayTeamResponse:
        """Deletes a team that has no keys and returns it.

        A team that still has keys
        answers `409`; delete or move its keys first. The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._delete(
            path_template("/agent_gateways/{instance_id}/teams/{team_id}", instance_id=instance_id, team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayTeamResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.create = to_raw_response_wrapper(
            teams.create,
        )
        self.update = to_raw_response_wrapper(
            teams.update,
        )
        self.list = to_raw_response_wrapper(
            teams.list,
        )
        self.delete = to_raw_response_wrapper(
            teams.delete,
        )

    @cached_property
    def tool_permissions(self) -> ToolPermissionsResourceWithRawResponse:
        """The MCP servers and tools a key or team may use."""
        return ToolPermissionsResourceWithRawResponse(self._teams.tool_permissions)


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.create = async_to_raw_response_wrapper(
            teams.create,
        )
        self.update = async_to_raw_response_wrapper(
            teams.update,
        )
        self.list = async_to_raw_response_wrapper(
            teams.list,
        )
        self.delete = async_to_raw_response_wrapper(
            teams.delete,
        )

    @cached_property
    def tool_permissions(self) -> AsyncToolPermissionsResourceWithRawResponse:
        """The MCP servers and tools a key or team may use."""
        return AsyncToolPermissionsResourceWithRawResponse(self._teams.tool_permissions)


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.create = to_streamed_response_wrapper(
            teams.create,
        )
        self.update = to_streamed_response_wrapper(
            teams.update,
        )
        self.list = to_streamed_response_wrapper(
            teams.list,
        )
        self.delete = to_streamed_response_wrapper(
            teams.delete,
        )

    @cached_property
    def tool_permissions(self) -> ToolPermissionsResourceWithStreamingResponse:
        """The MCP servers and tools a key or team may use."""
        return ToolPermissionsResourceWithStreamingResponse(self._teams.tool_permissions)


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.create = async_to_streamed_response_wrapper(
            teams.create,
        )
        self.update = async_to_streamed_response_wrapper(
            teams.update,
        )
        self.list = async_to_streamed_response_wrapper(
            teams.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            teams.delete,
        )

    @cached_property
    def tool_permissions(self) -> AsyncToolPermissionsResourceWithStreamingResponse:
        """The MCP servers and tools a key or team may use."""
        return AsyncToolPermissionsResourceWithStreamingResponse(self._teams.tool_permissions)
