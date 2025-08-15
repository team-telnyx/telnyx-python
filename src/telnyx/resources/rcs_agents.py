# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import rcs_agent_list_params, rcs_agent_update_params
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
from ..types.rcs_agent_response import RcsAgentResponse
from ..types.rcs_agent_list_response import RcsAgentListResponse

__all__ = ["RcsAgentsResource", "AsyncRcsAgentsResource"]


class RcsAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RcsAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RcsAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RcsAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RcsAgentsResourceWithStreamingResponse(self)

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
    ) -> RcsAgentResponse:
        """
        Retrieve an RCS agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/rcs_agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcsAgentResponse,
        )

    def update(
        self,
        id: str,
        *,
        profile_id: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcsAgentResponse:
        """
        Modify an RCS agent

        Args:
          profile_id: Messaging profile ID associated with the RCS Agent

          webhook_failover_url: Failover URL to receive RCS events

          webhook_url: URL to receive RCS events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/rcs_agents/{id}",
            body=maybe_transform(
                {
                    "profile_id": profile_id,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                rcs_agent_update_params.RcsAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcsAgentResponse,
        )

    def list(
        self,
        *,
        page: rcs_agent_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcsAgentListResponse:
        """
        List all RCS agents

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rcs_agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, rcs_agent_list_params.RcsAgentListParams),
            ),
            cast_to=RcsAgentListResponse,
        )


class AsyncRcsAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRcsAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRcsAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRcsAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRcsAgentsResourceWithStreamingResponse(self)

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
    ) -> RcsAgentResponse:
        """
        Retrieve an RCS agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/rcs_agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcsAgentResponse,
        )

    async def update(
        self,
        id: str,
        *,
        profile_id: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcsAgentResponse:
        """
        Modify an RCS agent

        Args:
          profile_id: Messaging profile ID associated with the RCS Agent

          webhook_failover_url: Failover URL to receive RCS events

          webhook_url: URL to receive RCS events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/rcs_agents/{id}",
            body=await async_maybe_transform(
                {
                    "profile_id": profile_id,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                rcs_agent_update_params.RcsAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcsAgentResponse,
        )

    async def list(
        self,
        *,
        page: rcs_agent_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcsAgentListResponse:
        """
        List all RCS agents

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rcs_agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, rcs_agent_list_params.RcsAgentListParams),
            ),
            cast_to=RcsAgentListResponse,
        )


class RcsAgentsResourceWithRawResponse:
    def __init__(self, rcs_agents: RcsAgentsResource) -> None:
        self._rcs_agents = rcs_agents

        self.retrieve = to_raw_response_wrapper(
            rcs_agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            rcs_agents.update,
        )
        self.list = to_raw_response_wrapper(
            rcs_agents.list,
        )


class AsyncRcsAgentsResourceWithRawResponse:
    def __init__(self, rcs_agents: AsyncRcsAgentsResource) -> None:
        self._rcs_agents = rcs_agents

        self.retrieve = async_to_raw_response_wrapper(
            rcs_agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            rcs_agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            rcs_agents.list,
        )


class RcsAgentsResourceWithStreamingResponse:
    def __init__(self, rcs_agents: RcsAgentsResource) -> None:
        self._rcs_agents = rcs_agents

        self.retrieve = to_streamed_response_wrapper(
            rcs_agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            rcs_agents.update,
        )
        self.list = to_streamed_response_wrapper(
            rcs_agents.list,
        )


class AsyncRcsAgentsResourceWithStreamingResponse:
    def __init__(self, rcs_agents: AsyncRcsAgentsResource) -> None:
        self._rcs_agents = rcs_agents

        self.retrieve = async_to_streamed_response_wrapper(
            rcs_agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            rcs_agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rcs_agents.list,
        )
