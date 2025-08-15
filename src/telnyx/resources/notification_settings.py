# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import notification_setting_list_params, notification_setting_create_params
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
from ..types.notification_setting_list_response import NotificationSettingListResponse
from ..types.notification_setting_create_response import NotificationSettingCreateResponse
from ..types.notification_setting_delete_response import NotificationSettingDeleteResponse
from ..types.notification_setting_retrieve_response import NotificationSettingRetrieveResponse

__all__ = ["NotificationSettingsResource", "AsyncNotificationSettingsResource"]


class NotificationSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NotificationSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NotificationSettingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        notification_channel_id: str | NotGiven = NOT_GIVEN,
        notification_event_condition_id: str | NotGiven = NOT_GIVEN,
        notification_profile_id: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[notification_setting_create_params.Parameter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationSettingCreateResponse:
        """
        Add a notification setting.

        Args:
          notification_channel_id: A UUID reference to the associated Notification Channel.

          notification_event_condition_id: A UUID reference to the associated Notification Event Condition.

          notification_profile_id: A UUID reference to the associated Notification Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/notification_settings",
            body=maybe_transform(
                {
                    "notification_channel_id": notification_channel_id,
                    "notification_event_condition_id": notification_event_condition_id,
                    "notification_profile_id": notification_profile_id,
                    "parameters": parameters,
                },
                notification_setting_create_params.NotificationSettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSettingCreateResponse,
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
    ) -> NotificationSettingRetrieveResponse:
        """
        Get a notification setting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/notification_settings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSettingRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: notification_setting_list_params.Filter | NotGiven = NOT_GIVEN,
        page: notification_setting_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationSettingListResponse:
        """
        List notification settings.

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
            "/notification_settings",
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
                    notification_setting_list_params.NotificationSettingListParams,
                ),
            ),
            cast_to=NotificationSettingListResponse,
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
    ) -> NotificationSettingDeleteResponse:
        """
        Delete a notification setting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/notification_settings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSettingDeleteResponse,
        )


class AsyncNotificationSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNotificationSettingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        notification_channel_id: str | NotGiven = NOT_GIVEN,
        notification_event_condition_id: str | NotGiven = NOT_GIVEN,
        notification_profile_id: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[notification_setting_create_params.Parameter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationSettingCreateResponse:
        """
        Add a notification setting.

        Args:
          notification_channel_id: A UUID reference to the associated Notification Channel.

          notification_event_condition_id: A UUID reference to the associated Notification Event Condition.

          notification_profile_id: A UUID reference to the associated Notification Profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/notification_settings",
            body=await async_maybe_transform(
                {
                    "notification_channel_id": notification_channel_id,
                    "notification_event_condition_id": notification_event_condition_id,
                    "notification_profile_id": notification_profile_id,
                    "parameters": parameters,
                },
                notification_setting_create_params.NotificationSettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSettingCreateResponse,
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
    ) -> NotificationSettingRetrieveResponse:
        """
        Get a notification setting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/notification_settings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSettingRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: notification_setting_list_params.Filter | NotGiven = NOT_GIVEN,
        page: notification_setting_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationSettingListResponse:
        """
        List notification settings.

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
            "/notification_settings",
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
                    notification_setting_list_params.NotificationSettingListParams,
                ),
            ),
            cast_to=NotificationSettingListResponse,
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
    ) -> NotificationSettingDeleteResponse:
        """
        Delete a notification setting.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/notification_settings/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationSettingDeleteResponse,
        )


class NotificationSettingsResourceWithRawResponse:
    def __init__(self, notification_settings: NotificationSettingsResource) -> None:
        self._notification_settings = notification_settings

        self.create = to_raw_response_wrapper(
            notification_settings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notification_settings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            notification_settings.list,
        )
        self.delete = to_raw_response_wrapper(
            notification_settings.delete,
        )


class AsyncNotificationSettingsResourceWithRawResponse:
    def __init__(self, notification_settings: AsyncNotificationSettingsResource) -> None:
        self._notification_settings = notification_settings

        self.create = async_to_raw_response_wrapper(
            notification_settings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notification_settings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            notification_settings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notification_settings.delete,
        )


class NotificationSettingsResourceWithStreamingResponse:
    def __init__(self, notification_settings: NotificationSettingsResource) -> None:
        self._notification_settings = notification_settings

        self.create = to_streamed_response_wrapper(
            notification_settings.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notification_settings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            notification_settings.list,
        )
        self.delete = to_streamed_response_wrapper(
            notification_settings.delete,
        )


class AsyncNotificationSettingsResourceWithStreamingResponse:
    def __init__(self, notification_settings: AsyncNotificationSettingsResource) -> None:
        self._notification_settings = notification_settings

        self.create = async_to_streamed_response_wrapper(
            notification_settings.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notification_settings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            notification_settings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notification_settings.delete,
        )
