# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    notification_profile_list_params,
    notification_profile_create_params,
    notification_profile_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.notification_profile import NotificationProfile
from ..types.notification_profile_create_response import NotificationProfileCreateResponse
from ..types.notification_profile_delete_response import NotificationProfileDeleteResponse
from ..types.notification_profile_update_response import NotificationProfileUpdateResponse
from ..types.notification_profile_retrieve_response import NotificationProfileRetrieveResponse

__all__ = ["NotificationProfilesResource", "AsyncNotificationProfilesResource"]


class NotificationProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NotificationProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NotificationProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileCreateResponse:
        """
        Create a notification profile.

        Args:
          name: A human readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/notification_profiles",
            body=maybe_transform({"name": name}, notification_profile_create_params.NotificationProfileCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileRetrieveResponse:
        """
        Get a notification profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/notification_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileRetrieveResponse,
        )

    def update(
        self,
        notification_profile_id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileUpdateResponse:
        """
        Update a notification profile.

        Args:
          name: A human readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `notification_profile_id` but received {notification_profile_id!r}"
            )
        return self._patch(
            f"/notification_profiles/{notification_profile_id}",
            body=maybe_transform({"name": name}, notification_profile_update_params.NotificationProfileUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileUpdateResponse,
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
    ) -> SyncDefaultFlatPagination[NotificationProfile]:
        """
        Returns a list of your notifications profiles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notification_profiles",
            page=SyncDefaultFlatPagination[NotificationProfile],
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
                    notification_profile_list_params.NotificationProfileListParams,
                ),
            ),
            model=NotificationProfile,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileDeleteResponse:
        """
        Delete a notification profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/notification_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileDeleteResponse,
        )


class AsyncNotificationProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNotificationProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileCreateResponse:
        """
        Create a notification profile.

        Args:
          name: A human readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/notification_profiles",
            body=await async_maybe_transform(
                {"name": name}, notification_profile_create_params.NotificationProfileCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileRetrieveResponse:
        """
        Get a notification profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/notification_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileRetrieveResponse,
        )

    async def update(
        self,
        notification_profile_id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileUpdateResponse:
        """
        Update a notification profile.

        Args:
          name: A human readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_profile_id:
            raise ValueError(
                f"Expected a non-empty value for `notification_profile_id` but received {notification_profile_id!r}"
            )
        return await self._patch(
            f"/notification_profiles/{notification_profile_id}",
            body=await async_maybe_transform(
                {"name": name}, notification_profile_update_params.NotificationProfileUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileUpdateResponse,
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
    ) -> AsyncPaginator[NotificationProfile, AsyncDefaultFlatPagination[NotificationProfile]]:
        """
        Returns a list of your notifications profiles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/notification_profiles",
            page=AsyncDefaultFlatPagination[NotificationProfile],
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
                    notification_profile_list_params.NotificationProfileListParams,
                ),
            ),
            model=NotificationProfile,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationProfileDeleteResponse:
        """
        Delete a notification profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/notification_profiles/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationProfileDeleteResponse,
        )


class NotificationProfilesResourceWithRawResponse:
    def __init__(self, notification_profiles: NotificationProfilesResource) -> None:
        self._notification_profiles = notification_profiles

        self.create = to_raw_response_wrapper(
            notification_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notification_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            notification_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            notification_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            notification_profiles.delete,
        )


class AsyncNotificationProfilesResourceWithRawResponse:
    def __init__(self, notification_profiles: AsyncNotificationProfilesResource) -> None:
        self._notification_profiles = notification_profiles

        self.create = async_to_raw_response_wrapper(
            notification_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notification_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            notification_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            notification_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            notification_profiles.delete,
        )


class NotificationProfilesResourceWithStreamingResponse:
    def __init__(self, notification_profiles: NotificationProfilesResource) -> None:
        self._notification_profiles = notification_profiles

        self.create = to_streamed_response_wrapper(
            notification_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notification_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            notification_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            notification_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            notification_profiles.delete,
        )


class AsyncNotificationProfilesResourceWithStreamingResponse:
    def __init__(self, notification_profiles: AsyncNotificationProfilesResource) -> None:
        self._notification_profiles = notification_profiles

        self.create = async_to_streamed_response_wrapper(
            notification_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notification_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            notification_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            notification_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            notification_profiles.delete,
        )
