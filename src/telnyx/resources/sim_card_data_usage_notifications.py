# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    sim_card_data_usage_notification_list_params,
    sim_card_data_usage_notification_create_params,
    sim_card_data_usage_notification_update_params,
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
from ..types.sim_card_data_usage_notification_list_response import SimCardDataUsageNotificationListResponse
from ..types.sim_card_data_usage_notification_create_response import SimCardDataUsageNotificationCreateResponse
from ..types.sim_card_data_usage_notification_delete_response import SimCardDataUsageNotificationDeleteResponse
from ..types.sim_card_data_usage_notification_update_response import SimCardDataUsageNotificationUpdateResponse
from ..types.sim_card_data_usage_notification_retrieve_response import SimCardDataUsageNotificationRetrieveResponse

__all__ = ["SimCardDataUsageNotificationsResource", "AsyncSimCardDataUsageNotificationsResource"]


class SimCardDataUsageNotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimCardDataUsageNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SimCardDataUsageNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimCardDataUsageNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SimCardDataUsageNotificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        sim_card_id: str,
        threshold: sim_card_data_usage_notification_create_params.Threshold,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDataUsageNotificationCreateResponse:
        """
        Creates a new SIM card data usage notification.

        Args:
          sim_card_id: The identification UUID of the related SIM card resource.

          threshold: Data usage threshold that will trigger the notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sim_card_data_usage_notifications",
            body=maybe_transform(
                {
                    "sim_card_id": sim_card_id,
                    "threshold": threshold,
                },
                sim_card_data_usage_notification_create_params.SimCardDataUsageNotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationCreateResponse,
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
    ) -> SimCardDataUsageNotificationRetrieveResponse:
        """
        Get a single SIM Card Data Usage Notification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sim_card_data_usage_notifications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        sim_card_id: str | NotGiven = NOT_GIVEN,
        threshold: sim_card_data_usage_notification_update_params.Threshold | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDataUsageNotificationUpdateResponse:
        """
        Updates information for a SIM Card Data Usage Notification.

        Args:
          sim_card_id: The identification UUID of the related SIM card resource.

          threshold: Data usage threshold that will trigger the notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/sim_card_data_usage_notifications/{id}",
            body=maybe_transform(
                {
                    "sim_card_id": sim_card_id,
                    "threshold": threshold,
                },
                sim_card_data_usage_notification_update_params.SimCardDataUsageNotificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationUpdateResponse,
        )

    def list(
        self,
        *,
        filter_sim_card_id: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDataUsageNotificationListResponse:
        """Lists a paginated collection of SIM card data usage notifications.

        It enables
        exploring the collection using specific filters.

        Args:
          filter_sim_card_id: A valid SIM card ID.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sim_card_data_usage_notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_sim_card_id": filter_sim_card_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    sim_card_data_usage_notification_list_params.SimCardDataUsageNotificationListParams,
                ),
            ),
            cast_to=SimCardDataUsageNotificationListResponse,
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
    ) -> SimCardDataUsageNotificationDeleteResponse:
        """
        Delete the SIM Card Data Usage Notification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/sim_card_data_usage_notifications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationDeleteResponse,
        )


class AsyncSimCardDataUsageNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimCardDataUsageNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimCardDataUsageNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        sim_card_id: str,
        threshold: sim_card_data_usage_notification_create_params.Threshold,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDataUsageNotificationCreateResponse:
        """
        Creates a new SIM card data usage notification.

        Args:
          sim_card_id: The identification UUID of the related SIM card resource.

          threshold: Data usage threshold that will trigger the notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sim_card_data_usage_notifications",
            body=await async_maybe_transform(
                {
                    "sim_card_id": sim_card_id,
                    "threshold": threshold,
                },
                sim_card_data_usage_notification_create_params.SimCardDataUsageNotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationCreateResponse,
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
    ) -> SimCardDataUsageNotificationRetrieveResponse:
        """
        Get a single SIM Card Data Usage Notification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sim_card_data_usage_notifications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        sim_card_id: str | NotGiven = NOT_GIVEN,
        threshold: sim_card_data_usage_notification_update_params.Threshold | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDataUsageNotificationUpdateResponse:
        """
        Updates information for a SIM Card Data Usage Notification.

        Args:
          sim_card_id: The identification UUID of the related SIM card resource.

          threshold: Data usage threshold that will trigger the notification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/sim_card_data_usage_notifications/{id}",
            body=await async_maybe_transform(
                {
                    "sim_card_id": sim_card_id,
                    "threshold": threshold,
                },
                sim_card_data_usage_notification_update_params.SimCardDataUsageNotificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationUpdateResponse,
        )

    async def list(
        self,
        *,
        filter_sim_card_id: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardDataUsageNotificationListResponse:
        """Lists a paginated collection of SIM card data usage notifications.

        It enables
        exploring the collection using specific filters.

        Args:
          filter_sim_card_id: A valid SIM card ID.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sim_card_data_usage_notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_sim_card_id": filter_sim_card_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    sim_card_data_usage_notification_list_params.SimCardDataUsageNotificationListParams,
                ),
            ),
            cast_to=SimCardDataUsageNotificationListResponse,
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
    ) -> SimCardDataUsageNotificationDeleteResponse:
        """
        Delete the SIM Card Data Usage Notification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/sim_card_data_usage_notifications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardDataUsageNotificationDeleteResponse,
        )


class SimCardDataUsageNotificationsResourceWithRawResponse:
    def __init__(self, sim_card_data_usage_notifications: SimCardDataUsageNotificationsResource) -> None:
        self._sim_card_data_usage_notifications = sim_card_data_usage_notifications

        self.create = to_raw_response_wrapper(
            sim_card_data_usage_notifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sim_card_data_usage_notifications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sim_card_data_usage_notifications.update,
        )
        self.list = to_raw_response_wrapper(
            sim_card_data_usage_notifications.list,
        )
        self.delete = to_raw_response_wrapper(
            sim_card_data_usage_notifications.delete,
        )


class AsyncSimCardDataUsageNotificationsResourceWithRawResponse:
    def __init__(self, sim_card_data_usage_notifications: AsyncSimCardDataUsageNotificationsResource) -> None:
        self._sim_card_data_usage_notifications = sim_card_data_usage_notifications

        self.create = async_to_raw_response_wrapper(
            sim_card_data_usage_notifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sim_card_data_usage_notifications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sim_card_data_usage_notifications.update,
        )
        self.list = async_to_raw_response_wrapper(
            sim_card_data_usage_notifications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sim_card_data_usage_notifications.delete,
        )


class SimCardDataUsageNotificationsResourceWithStreamingResponse:
    def __init__(self, sim_card_data_usage_notifications: SimCardDataUsageNotificationsResource) -> None:
        self._sim_card_data_usage_notifications = sim_card_data_usage_notifications

        self.create = to_streamed_response_wrapper(
            sim_card_data_usage_notifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sim_card_data_usage_notifications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sim_card_data_usage_notifications.update,
        )
        self.list = to_streamed_response_wrapper(
            sim_card_data_usage_notifications.list,
        )
        self.delete = to_streamed_response_wrapper(
            sim_card_data_usage_notifications.delete,
        )


class AsyncSimCardDataUsageNotificationsResourceWithStreamingResponse:
    def __init__(self, sim_card_data_usage_notifications: AsyncSimCardDataUsageNotificationsResource) -> None:
        self._sim_card_data_usage_notifications = sim_card_data_usage_notifications

        self.create = async_to_streamed_response_wrapper(
            sim_card_data_usage_notifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sim_card_data_usage_notifications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sim_card_data_usage_notifications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sim_card_data_usage_notifications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sim_card_data_usage_notifications.delete,
        )
