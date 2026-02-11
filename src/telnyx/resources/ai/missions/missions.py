# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .runs.runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.ai import (
    mission_list_params,
    mission_create_params,
    mission_list_events_params,
    mission_update_mission_params,
)
from .mcp_servers import (
    McpServersResource,
    AsyncMcpServersResource,
    McpServersResourceWithRawResponse,
    AsyncMcpServersResourceWithRawResponse,
    McpServersResourceWithStreamingResponse,
    AsyncMcpServersResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from .knowledge_bases import (
    KnowledgeBasesResource,
    AsyncKnowledgeBasesResource,
    KnowledgeBasesResourceWithRawResponse,
    AsyncKnowledgeBasesResourceWithRawResponse,
    KnowledgeBasesResourceWithStreamingResponse,
    AsyncKnowledgeBasesResourceWithStreamingResponse,
)
from ....types.ai.mission_list_response import MissionListResponse
from ....types.ai.mission_create_response import MissionCreateResponse
from ....types.ai.mission_retrieve_response import MissionRetrieveResponse
from ....types.ai.mission_list_events_response import MissionListEventsResponse
from ....types.ai.mission_update_mission_response import MissionUpdateMissionResponse

__all__ = ["MissionsResource", "AsyncMissionsResource"]


class MissionsResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResource:
        return KnowledgeBasesResource(self._client)

    @cached_property
    def mcp_servers(self) -> McpServersResource:
        return McpServersResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MissionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        execution_mode: Literal["external", "managed"] | Omit = omit,
        instructions: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MissionCreateResponse:
        """
        Create a new mission definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/missions",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "execution_mode": execution_mode,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                },
                mission_create_params.MissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionCreateResponse,
        )

    def retrieve(
        self,
        mission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MissionRetrieveResponse:
        """
        Get a mission by ID (includes tools, knowledge_bases, mcp_servers)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return self._get(
            f"/ai/missions/{mission_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionRetrieveResponse,
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
    ) -> SyncDefaultFlatPagination[MissionListResponse]:
        """
        List all missions for the organization

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/missions",
            page=SyncDefaultFlatPagination[MissionListResponse],
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
                    mission_list_params.MissionListParams,
                ),
            ),
            model=MissionListResponse,
        )

    def clone_mission(
        self,
        mission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Clone an existing mission

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return self._post(
            f"/ai/missions/{mission_id}/clone",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete_mission(
        self,
        mission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a mission

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/missions/{mission_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_events(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[MissionListEventsResponse]:
        """
        List recent events across all missions

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/missions/events",
            page=SyncDefaultFlatPagination[MissionListEventsResponse],
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
                    },
                    mission_list_events_params.MissionListEventsParams,
                ),
            ),
            model=MissionListEventsResponse,
        )

    def update_mission(
        self,
        mission_id: str,
        *,
        description: str | Omit = omit,
        execution_mode: Literal["external", "managed"] | Omit = omit,
        instructions: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        model: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MissionUpdateMissionResponse:
        """
        Update a mission definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return self._put(
            f"/ai/missions/{mission_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "execution_mode": execution_mode,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                },
                mission_update_mission_params.MissionUpdateMissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionUpdateMissionResponse,
        )


class AsyncMissionsResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResource:
        return AsyncKnowledgeBasesResource(self._client)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResource:
        return AsyncMcpServersResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMissionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | Omit = omit,
        execution_mode: Literal["external", "managed"] | Omit = omit,
        instructions: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MissionCreateResponse:
        """
        Create a new mission definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/missions",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "execution_mode": execution_mode,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                },
                mission_create_params.MissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionCreateResponse,
        )

    async def retrieve(
        self,
        mission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MissionRetrieveResponse:
        """
        Get a mission by ID (includes tools, knowledge_bases, mcp_servers)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return await self._get(
            f"/ai/missions/{mission_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionRetrieveResponse,
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
    ) -> AsyncPaginator[MissionListResponse, AsyncDefaultFlatPagination[MissionListResponse]]:
        """
        List all missions for the organization

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/missions",
            page=AsyncDefaultFlatPagination[MissionListResponse],
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
                    mission_list_params.MissionListParams,
                ),
            ),
            model=MissionListResponse,
        )

    async def clone_mission(
        self,
        mission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Clone an existing mission

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return await self._post(
            f"/ai/missions/{mission_id}/clone",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete_mission(
        self,
        mission_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a mission

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/missions/{mission_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_events(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MissionListEventsResponse, AsyncDefaultFlatPagination[MissionListEventsResponse]]:
        """
        List recent events across all missions

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/missions/events",
            page=AsyncDefaultFlatPagination[MissionListEventsResponse],
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
                    },
                    mission_list_events_params.MissionListEventsParams,
                ),
            ),
            model=MissionListEventsResponse,
        )

    async def update_mission(
        self,
        mission_id: str,
        *,
        description: str | Omit = omit,
        execution_mode: Literal["external", "managed"] | Omit = omit,
        instructions: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        model: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MissionUpdateMissionResponse:
        """
        Update a mission definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return await self._put(
            f"/ai/missions/{mission_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "execution_mode": execution_mode,
                    "instructions": instructions,
                    "metadata": metadata,
                    "model": model,
                    "name": name,
                },
                mission_update_mission_params.MissionUpdateMissionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MissionUpdateMissionResponse,
        )


class MissionsResourceWithRawResponse:
    def __init__(self, missions: MissionsResource) -> None:
        self._missions = missions

        self.create = to_raw_response_wrapper(
            missions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            missions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            missions.list,
        )
        self.clone_mission = to_raw_response_wrapper(
            missions.clone_mission,
        )
        self.delete_mission = to_raw_response_wrapper(
            missions.delete_mission,
        )
        self.list_events = to_raw_response_wrapper(
            missions.list_events,
        )
        self.update_mission = to_raw_response_wrapper(
            missions.update_mission,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._missions.runs)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithRawResponse:
        return KnowledgeBasesResourceWithRawResponse(self._missions.knowledge_bases)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithRawResponse:
        return McpServersResourceWithRawResponse(self._missions.mcp_servers)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._missions.tools)


class AsyncMissionsResourceWithRawResponse:
    def __init__(self, missions: AsyncMissionsResource) -> None:
        self._missions = missions

        self.create = async_to_raw_response_wrapper(
            missions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            missions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            missions.list,
        )
        self.clone_mission = async_to_raw_response_wrapper(
            missions.clone_mission,
        )
        self.delete_mission = async_to_raw_response_wrapper(
            missions.delete_mission,
        )
        self.list_events = async_to_raw_response_wrapper(
            missions.list_events,
        )
        self.update_mission = async_to_raw_response_wrapper(
            missions.update_mission,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._missions.runs)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        return AsyncKnowledgeBasesResourceWithRawResponse(self._missions.knowledge_bases)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithRawResponse:
        return AsyncMcpServersResourceWithRawResponse(self._missions.mcp_servers)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._missions.tools)


class MissionsResourceWithStreamingResponse:
    def __init__(self, missions: MissionsResource) -> None:
        self._missions = missions

        self.create = to_streamed_response_wrapper(
            missions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            missions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            missions.list,
        )
        self.clone_mission = to_streamed_response_wrapper(
            missions.clone_mission,
        )
        self.delete_mission = to_streamed_response_wrapper(
            missions.delete_mission,
        )
        self.list_events = to_streamed_response_wrapper(
            missions.list_events,
        )
        self.update_mission = to_streamed_response_wrapper(
            missions.update_mission,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._missions.runs)

    @cached_property
    def knowledge_bases(self) -> KnowledgeBasesResourceWithStreamingResponse:
        return KnowledgeBasesResourceWithStreamingResponse(self._missions.knowledge_bases)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithStreamingResponse:
        return McpServersResourceWithStreamingResponse(self._missions.mcp_servers)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._missions.tools)


class AsyncMissionsResourceWithStreamingResponse:
    def __init__(self, missions: AsyncMissionsResource) -> None:
        self._missions = missions

        self.create = async_to_streamed_response_wrapper(
            missions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            missions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            missions.list,
        )
        self.clone_mission = async_to_streamed_response_wrapper(
            missions.clone_mission,
        )
        self.delete_mission = async_to_streamed_response_wrapper(
            missions.delete_mission,
        )
        self.list_events = async_to_streamed_response_wrapper(
            missions.list_events,
        )
        self.update_mission = async_to_streamed_response_wrapper(
            missions.update_mission,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._missions.runs)

    @cached_property
    def knowledge_bases(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self._missions.knowledge_bases)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithStreamingResponse:
        return AsyncMcpServersResourceWithStreamingResponse(self._missions.mcp_servers)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._missions.tools)
