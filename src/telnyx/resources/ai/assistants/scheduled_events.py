# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, cast
from datetime import datetime

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.assistants import ConversationChannelType, scheduled_event_list_params, scheduled_event_create_params
from ....types.ai.assistants.scheduled_event_response import ScheduledEventResponse
from ....types.ai.assistants.conversation_channel_type import ConversationChannelType
from ....types.ai.assistants.scheduled_event_list_response import ScheduledEventListResponse

__all__ = ["ScheduledEventsResource", "AsyncScheduledEventsResource"]


class ScheduledEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ScheduledEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduledEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ScheduledEventsResourceWithStreamingResponse(self)

    def create(
        self,
        assistant_id: str,
        *,
        scheduled_at_fixed_datetime: Union[str, datetime],
        telnyx_agent_target: str,
        telnyx_conversation_channel: ConversationChannelType,
        telnyx_end_user_target: str,
        conversation_metadata: Dict[str, Union[str, int, bool]] | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledEventResponse:
        """
        Create a scheduled event for an assistant

        Args:
          scheduled_at_fixed_datetime: The datetime at which the event should be scheduled. Formatted as ISO 8601.

          telnyx_agent_target: The phone number, SIP URI, to schedule the call or text from.

          telnyx_end_user_target: The phone number, SIP URI, to schedule the call or text to.

          conversation_metadata: Metadata associated with the conversation. Telnyx provides several pieces of
              metadata, but customers can also add their own.

          text: Required for sms scheduled events. The text to be sent to the end user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return cast(
            ScheduledEventResponse,
            self._post(
                f"/ai/assistants/{assistant_id}/scheduled_events",
                body=maybe_transform(
                    {
                        "scheduled_at_fixed_datetime": scheduled_at_fixed_datetime,
                        "telnyx_agent_target": telnyx_agent_target,
                        "telnyx_conversation_channel": telnyx_conversation_channel,
                        "telnyx_end_user_target": telnyx_end_user_target,
                        "conversation_metadata": conversation_metadata,
                        "text": text,
                    },
                    scheduled_event_create_params.ScheduledEventCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ScheduledEventResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        event_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledEventResponse:
        """
        Retrieve a scheduled event by event ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return cast(
            ScheduledEventResponse,
            self._get(
                f"/ai/assistants/{assistant_id}/scheduled_events/{event_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ScheduledEventResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        assistant_id: str,
        *,
        conversation_channel: ConversationChannelType | NotGiven = NOT_GIVEN,
        from_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: scheduled_event_list_params.Page | NotGiven = NOT_GIVEN,
        to_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledEventListResponse:
        """
        Get scheduled events for an assistant with pagination and filtering

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/ai/assistants/{assistant_id}/scheduled_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conversation_channel": conversation_channel,
                        "from_date": from_date,
                        "page": page,
                        "to_date": to_date,
                    },
                    scheduled_event_list_params.ScheduledEventListParams,
                ),
            ),
            cast_to=ScheduledEventListResponse,
        )

    def delete(
        self,
        event_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """If the event is pending, this will cancel the event.

        Otherwise, this will simply
        remove the record of the event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            f"/ai/assistants/{assistant_id}/scheduled_events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncScheduledEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduledEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduledEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncScheduledEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        assistant_id: str,
        *,
        scheduled_at_fixed_datetime: Union[str, datetime],
        telnyx_agent_target: str,
        telnyx_conversation_channel: ConversationChannelType,
        telnyx_end_user_target: str,
        conversation_metadata: Dict[str, Union[str, int, bool]] | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledEventResponse:
        """
        Create a scheduled event for an assistant

        Args:
          scheduled_at_fixed_datetime: The datetime at which the event should be scheduled. Formatted as ISO 8601.

          telnyx_agent_target: The phone number, SIP URI, to schedule the call or text from.

          telnyx_end_user_target: The phone number, SIP URI, to schedule the call or text to.

          conversation_metadata: Metadata associated with the conversation. Telnyx provides several pieces of
              metadata, but customers can also add their own.

          text: Required for sms scheduled events. The text to be sent to the end user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return cast(
            ScheduledEventResponse,
            await self._post(
                f"/ai/assistants/{assistant_id}/scheduled_events",
                body=await async_maybe_transform(
                    {
                        "scheduled_at_fixed_datetime": scheduled_at_fixed_datetime,
                        "telnyx_agent_target": telnyx_agent_target,
                        "telnyx_conversation_channel": telnyx_conversation_channel,
                        "telnyx_end_user_target": telnyx_end_user_target,
                        "conversation_metadata": conversation_metadata,
                        "text": text,
                    },
                    scheduled_event_create_params.ScheduledEventCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ScheduledEventResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        event_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledEventResponse:
        """
        Retrieve a scheduled event by event ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return cast(
            ScheduledEventResponse,
            await self._get(
                f"/ai/assistants/{assistant_id}/scheduled_events/{event_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ScheduledEventResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        assistant_id: str,
        *,
        conversation_channel: ConversationChannelType | NotGiven = NOT_GIVEN,
        from_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: scheduled_event_list_params.Page | NotGiven = NOT_GIVEN,
        to_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledEventListResponse:
        """
        Get scheduled events for an assistant with pagination and filtering

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/ai/assistants/{assistant_id}/scheduled_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conversation_channel": conversation_channel,
                        "from_date": from_date,
                        "page": page,
                        "to_date": to_date,
                    },
                    scheduled_event_list_params.ScheduledEventListParams,
                ),
            ),
            cast_to=ScheduledEventListResponse,
        )

    async def delete(
        self,
        event_id: str,
        *,
        assistant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """If the event is pending, this will cancel the event.

        Otherwise, this will simply
        remove the record of the event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            f"/ai/assistants/{assistant_id}/scheduled_events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ScheduledEventsResourceWithRawResponse:
    def __init__(self, scheduled_events: ScheduledEventsResource) -> None:
        self._scheduled_events = scheduled_events

        self.create = to_raw_response_wrapper(
            scheduled_events.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scheduled_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            scheduled_events.list,
        )
        self.delete = to_raw_response_wrapper(
            scheduled_events.delete,
        )


class AsyncScheduledEventsResourceWithRawResponse:
    def __init__(self, scheduled_events: AsyncScheduledEventsResource) -> None:
        self._scheduled_events = scheduled_events

        self.create = async_to_raw_response_wrapper(
            scheduled_events.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scheduled_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            scheduled_events.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scheduled_events.delete,
        )


class ScheduledEventsResourceWithStreamingResponse:
    def __init__(self, scheduled_events: ScheduledEventsResource) -> None:
        self._scheduled_events = scheduled_events

        self.create = to_streamed_response_wrapper(
            scheduled_events.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scheduled_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            scheduled_events.list,
        )
        self.delete = to_streamed_response_wrapper(
            scheduled_events.delete,
        )


class AsyncScheduledEventsResourceWithStreamingResponse:
    def __init__(self, scheduled_events: AsyncScheduledEventsResource) -> None:
        self._scheduled_events = scheduled_events

        self.create = async_to_streamed_response_wrapper(
            scheduled_events.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scheduled_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            scheduled_events.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scheduled_events.delete,
        )
