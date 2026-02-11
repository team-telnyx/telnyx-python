# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.ai.missions.runs import event_log_params, event_list_params
from .....types.ai.missions.runs.event_log_response import EventLogResponse
from .....types.ai.missions.runs.event_list_response import EventListResponse
from .....types.ai.missions.runs.event_get_event_details_response import EventGetEventDetailsResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        run_id: str,
        *,
        mission_id: str,
        agent_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        step_id: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EventListResponse]:
        """
        List events for a run (paginated)

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            f"/ai/missions/{mission_id}/runs/{run_id}/events",
            page=SyncDefaultFlatPagination[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "step_id": step_id,
                        "type": type,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )

    def get_event_details(
        self,
        event_id: str,
        *,
        mission_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetEventDetailsResponse:
        """
        Get details of a specific event

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
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventGetEventDetailsResponse,
        )

    def log(
        self,
        run_id: str,
        *,
        mission_id: str,
        summary: str,
        type: Literal[
            "status_change",
            "step_started",
            "step_completed",
            "step_failed",
            "tool_call",
            "tool_result",
            "message",
            "error",
            "custom",
        ],
        agent_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        payload: Dict[str, object] | Omit = omit,
        step_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventLogResponse:
        """
        Log an event for a run

        Args:
          idempotency_key: Prevents duplicate events on retry

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
            f"/ai/missions/{mission_id}/runs/{run_id}/events",
            body=maybe_transform(
                {
                    "summary": summary,
                    "type": type,
                    "agent_id": agent_id,
                    "idempotency_key": idempotency_key,
                    "payload": payload,
                    "step_id": step_id,
                },
                event_log_params.EventLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventLogResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    def list(
        self,
        run_id: str,
        *,
        mission_id: str,
        agent_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        step_id: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EventListResponse, AsyncDefaultFlatPagination[EventListResponse]]:
        """
        List events for a run (paginated)

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            f"/ai/missions/{mission_id}/runs/{run_id}/events",
            page=AsyncDefaultFlatPagination[EventListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "step_id": step_id,
                        "type": type,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventListResponse,
        )

    async def get_event_details(
        self,
        event_id: str,
        *,
        mission_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetEventDetailsResponse:
        """
        Get details of a specific event

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
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventGetEventDetailsResponse,
        )

    async def log(
        self,
        run_id: str,
        *,
        mission_id: str,
        summary: str,
        type: Literal[
            "status_change",
            "step_started",
            "step_completed",
            "step_failed",
            "tool_call",
            "tool_result",
            "message",
            "error",
            "custom",
        ],
        agent_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        payload: Dict[str, object] | Omit = omit,
        step_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventLogResponse:
        """
        Log an event for a run

        Args:
          idempotency_key: Prevents duplicate events on retry

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
            f"/ai/missions/{mission_id}/runs/{run_id}/events",
            body=await async_maybe_transform(
                {
                    "summary": summary,
                    "type": type,
                    "agent_id": agent_id,
                    "idempotency_key": idempotency_key,
                    "payload": payload,
                    "step_id": step_id,
                },
                event_log_params.EventLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventLogResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.get_event_details = to_raw_response_wrapper(
            events.get_event_details,
        )
        self.log = to_raw_response_wrapper(
            events.log,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.get_event_details = async_to_raw_response_wrapper(
            events.get_event_details,
        )
        self.log = async_to_raw_response_wrapper(
            events.log,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.get_event_details = to_streamed_response_wrapper(
            events.get_event_details,
        )
        self.log = to_streamed_response_wrapper(
            events.log,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.get_event_details = async_to_streamed_response_wrapper(
            events.get_event_details,
        )
        self.log = async_to_streamed_response_wrapper(
            events.log,
        )
