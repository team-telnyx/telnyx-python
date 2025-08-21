# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    notification_channel_list_params,
    notification_channel_create_params,
    notification_channel_update_params,
)
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
from ..types.notification_channel_list_response import NotificationChannelListResponse
from ..types.notification_channel_create_response import NotificationChannelCreateResponse
from ..types.notification_channel_delete_response import NotificationChannelDeleteResponse
from ..types.notification_channel_update_response import NotificationChannelUpdateResponse
from ..types.notification_channel_retrieve_response import NotificationChannelRetrieveResponse

__all__ = ["NotificationChannelsResource", "AsyncNotificationChannelsResource"]


class NotificationChannelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NotificationChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NotificationChannelsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        channel_destination: str | NotGiven = NOT_GIVEN,
        channel_type_id: Literal["sms", "voice", "email", "webhook"] | NotGiven = NOT_GIVEN,
        notification_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelCreateResponse:
        """
        Create a notification channel.

        Args:
          channel_destination: The destination associated with the channel type.

          channel_type_id: A Channel Type ID

          notification_profile_id: A UUID reference to the associated Notification Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/notification_channels",
            body=maybe_transform(
                {
                    "channel_destination": channel_destination,
                    "channel_type_id": channel_type_id,
                    "notification_profile_id": notification_profile_id,
                },
                notification_channel_create_params.NotificationChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelCreateResponse,
        )

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
    ) -> NotificationChannelRetrieveResponse:
        """
        Get a notification channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/notification_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        channel_destination: str | NotGiven = NOT_GIVEN,
        channel_type_id: Literal["sms", "voice", "email", "webhook"] | NotGiven = NOT_GIVEN,
        notification_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelUpdateResponse:
        """
        Update a notification channel.

        Args:
          channel_destination: The destination associated with the channel type.

          channel_type_id: A Channel Type ID

          notification_profile_id: A UUID reference to the associated Notification Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/notification_channels/{id}",
            body=maybe_transform(
                {
                    "channel_destination": channel_destination,
                    "channel_type_id": channel_type_id,
                    "notification_profile_id": notification_profile_id,
                },
                notification_channel_update_params.NotificationChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelUpdateResponse,
        )

    def list(
        self,
        *,
        filter: notification_channel_list_params.Filter | NotGiven = NOT_GIVEN,
        page: notification_channel_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelListResponse:
        """
        List notification channels.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[associated_record_type][eq], filter[channel_type_id][eq],
              filter[notification_profile_id][eq], filter[notification_channel][eq],
              filter[notification_event_condition_id][eq], filter[status][eq]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/notification_channels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    notification_channel_list_params.NotificationChannelListParams,
                ),
            ),
            cast_to=NotificationChannelListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelDeleteResponse:
        """
        Delete a notification channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/notification_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelDeleteResponse,
        )


class AsyncNotificationChannelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNotificationChannelsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        channel_destination: str | NotGiven = NOT_GIVEN,
        channel_type_id: Literal["sms", "voice", "email", "webhook"] | NotGiven = NOT_GIVEN,
        notification_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelCreateResponse:
        """
        Create a notification channel.

        Args:
          channel_destination: The destination associated with the channel type.

          channel_type_id: A Channel Type ID

          notification_profile_id: A UUID reference to the associated Notification Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/notification_channels",
            body=await async_maybe_transform(
                {
                    "channel_destination": channel_destination,
                    "channel_type_id": channel_type_id,
                    "notification_profile_id": notification_profile_id,
                },
                notification_channel_create_params.NotificationChannelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelCreateResponse,
        )

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
    ) -> NotificationChannelRetrieveResponse:
        """
        Get a notification channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/notification_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        channel_destination: str | NotGiven = NOT_GIVEN,
        channel_type_id: Literal["sms", "voice", "email", "webhook"] | NotGiven = NOT_GIVEN,
        notification_profile_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelUpdateResponse:
        """
        Update a notification channel.

        Args:
          channel_destination: The destination associated with the channel type.

          channel_type_id: A Channel Type ID

          notification_profile_id: A UUID reference to the associated Notification Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/notification_channels/{id}",
            body=await async_maybe_transform(
                {
                    "channel_destination": channel_destination,
                    "channel_type_id": channel_type_id,
                    "notification_profile_id": notification_profile_id,
                },
                notification_channel_update_params.NotificationChannelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: notification_channel_list_params.Filter | NotGiven = NOT_GIVEN,
        page: notification_channel_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelListResponse:
        """
        List notification channels.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[associated_record_type][eq], filter[channel_type_id][eq],
              filter[notification_profile_id][eq], filter[notification_channel][eq],
              filter[notification_event_condition_id][eq], filter[status][eq]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/notification_channels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    notification_channel_list_params.NotificationChannelListParams,
                ),
            ),
            cast_to=NotificationChannelListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationChannelDeleteResponse:
        """
        Delete a notification channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/notification_channels/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationChannelDeleteResponse,
        )


class NotificationChannelsResourceWithRawResponse:
    def __init__(self, notification_channels: NotificationChannelsResource) -> None:
        self._notification_channels = notification_channels

        self.create = to_raw_response_wrapper(
            notification_channels.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notification_channels.retrieve,
        )
        self.update = to_raw_response_wrapper(
            notification_channels.update,
        )
        self.list = to_raw_response_wrapper(
            notification_channels.list,
        )
        self.delete = to_raw_response_wrapper(
            notification_channels.delete,
        )


class AsyncNotificationChannelsResourceWithRawResponse:
    def __init__(self, notification_channels: AsyncNotificationChannelsResource) -> None:
        self._notification_channels = notification_channels

        self.create = async_to_raw_response_wrapper(
            notification_channels.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notification_channels.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            notification_channels.update,
        )
        self.list = async_to_raw_response_wrapper(
            notification_channels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notification_channels.delete,
        )


class NotificationChannelsResourceWithStreamingResponse:
    def __init__(self, notification_channels: NotificationChannelsResource) -> None:
        self._notification_channels = notification_channels

        self.create = to_streamed_response_wrapper(
            notification_channels.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notification_channels.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            notification_channels.update,
        )
        self.list = to_streamed_response_wrapper(
            notification_channels.list,
        )
        self.delete = to_streamed_response_wrapper(
            notification_channels.delete,
        )


class AsyncNotificationChannelsResourceWithStreamingResponse:
    def __init__(self, notification_channels: AsyncNotificationChannelsResource) -> None:
        self._notification_channels = notification_channels

        self.create = async_to_streamed_response_wrapper(
            notification_channels.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notification_channels.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            notification_channels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            notification_channels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notification_channels.delete,
        )
