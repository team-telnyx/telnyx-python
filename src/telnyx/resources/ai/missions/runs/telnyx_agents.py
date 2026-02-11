# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.ai.missions.runs import telnyx_agent_link_params
from .....types.ai.missions.runs.telnyx_agent_link_response import TelnyxAgentLinkResponse
from .....types.ai.missions.runs.telnyx_agent_list_response import TelnyxAgentListResponse

__all__ = ["TelnyxAgentsResource", "AsyncTelnyxAgentsResource"]


class TelnyxAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelnyxAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TelnyxAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelnyxAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TelnyxAgentsResourceWithStreamingResponse(self)

    def list(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelnyxAgentListResponse:
        """
        List all Telnyx agents linked to a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxAgentListResponse,
        )

    def link(
        self,
        run_id: str,
        *,
        mission_id: str,
        telnyx_agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelnyxAgentLinkResponse:
        """
        Link a Telnyx AI agent (voice/messaging) to a run

        Args:
          telnyx_agent_id: The Telnyx AI agent ID to link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents",
            body=maybe_transform({"telnyx_agent_id": telnyx_agent_id}, telnyx_agent_link_params.TelnyxAgentLinkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxAgentLinkResponse,
        )

    def unlink(
        self,
        telnyx_agent_id: str,
        *,
        mission_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unlink a Telnyx agent from a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        if not telnyx_agent_id:
            raise ValueError(f"Expected a non-empty value for `telnyx_agent_id` but received {telnyx_agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents/{telnyx_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTelnyxAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelnyxAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelnyxAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelnyxAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTelnyxAgentsResourceWithStreamingResponse(self)

    async def list(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelnyxAgentListResponse:
        """
        List all Telnyx agents linked to a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxAgentListResponse,
        )

    async def link(
        self,
        run_id: str,
        *,
        mission_id: str,
        telnyx_agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelnyxAgentLinkResponse:
        """
        Link a Telnyx AI agent (voice/messaging) to a run

        Args:
          telnyx_agent_id: The Telnyx AI agent ID to link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents",
            body=await async_maybe_transform(
                {"telnyx_agent_id": telnyx_agent_id}, telnyx_agent_link_params.TelnyxAgentLinkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxAgentLinkResponse,
        )

    async def unlink(
        self,
        telnyx_agent_id: str,
        *,
        mission_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unlink a Telnyx agent from a run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        if not telnyx_agent_id:
            raise ValueError(f"Expected a non-empty value for `telnyx_agent_id` but received {telnyx_agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/missions/{mission_id}/runs/{run_id}/telnyx-agents/{telnyx_agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelnyxAgentsResourceWithRawResponse:
    def __init__(self, telnyx_agents: TelnyxAgentsResource) -> None:
        self._telnyx_agents = telnyx_agents

        self.list = to_raw_response_wrapper(
            telnyx_agents.list,
        )
        self.link = to_raw_response_wrapper(
            telnyx_agents.link,
        )
        self.unlink = to_raw_response_wrapper(
            telnyx_agents.unlink,
        )


class AsyncTelnyxAgentsResourceWithRawResponse:
    def __init__(self, telnyx_agents: AsyncTelnyxAgentsResource) -> None:
        self._telnyx_agents = telnyx_agents

        self.list = async_to_raw_response_wrapper(
            telnyx_agents.list,
        )
        self.link = async_to_raw_response_wrapper(
            telnyx_agents.link,
        )
        self.unlink = async_to_raw_response_wrapper(
            telnyx_agents.unlink,
        )


class TelnyxAgentsResourceWithStreamingResponse:
    def __init__(self, telnyx_agents: TelnyxAgentsResource) -> None:
        self._telnyx_agents = telnyx_agents

        self.list = to_streamed_response_wrapper(
            telnyx_agents.list,
        )
        self.link = to_streamed_response_wrapper(
            telnyx_agents.link,
        )
        self.unlink = to_streamed_response_wrapper(
            telnyx_agents.unlink,
        )


class AsyncTelnyxAgentsResourceWithStreamingResponse:
    def __init__(self, telnyx_agents: AsyncTelnyxAgentsResource) -> None:
        self._telnyx_agents = telnyx_agents

        self.list = async_to_streamed_response_wrapper(
            telnyx_agents.list,
        )
        self.link = async_to_streamed_response_wrapper(
            telnyx_agents.link,
        )
        self.unlink = async_to_streamed_response_wrapper(
            telnyx_agents.unlink,
        )
