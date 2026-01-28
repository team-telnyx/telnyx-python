# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.phone_numbers import messaging_list_params, messaging_update_params
from ...types.phone_numbers.messaging_update_response import MessagingUpdateResponse
from ...types.phone_numbers.messaging_retrieve_response import MessagingRetrieveResponse
from ...types.shared.phone_number_with_messaging_settings import PhoneNumberWithMessagingSettings

__all__ = ["MessagingResource", "AsyncMessagingResource"]


class MessagingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingResourceWithStreamingResponse(self)

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
    ) -> MessagingRetrieveResponse:
        """
        Retrieve a phone number with messaging settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/phone_numbers/{id}/messaging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        messaging_product: str | Omit = omit,
        messaging_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingUpdateResponse:
        """
        Update the messaging profile and/or messaging product of a phone number

        Args:
          messaging_product:
              Configure the messaging product for this number:

              - Omit this field or set its value to `null` to keep the current value.
              - Set this field to a quoted product ID to set this phone number to that product

          messaging_profile_id:
              Configure the messaging profile this phone number is assigned to:

              - Omit this field or set its value to `null` to keep the current value.
              - Set this field to `""` to unassign the number from its messaging profile
              - Set this field to a quoted UUID of a messaging profile to assign this number
                to that messaging profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/phone_numbers/{id}/messaging",
            body=maybe_transform(
                {
                    "messaging_product": messaging_product,
                    "messaging_profile_id": messaging_profile_id,
                },
                messaging_update_params.MessagingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingUpdateResponse,
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
    ) -> SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings]:
        """
        List phone numbers with messaging settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/phone_numbers/messaging",
            page=SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings],
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
                    messaging_list_params.MessagingListParams,
                ),
            ),
            model=PhoneNumberWithMessagingSettings,
        )


class AsyncMessagingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingResourceWithStreamingResponse(self)

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
    ) -> MessagingRetrieveResponse:
        """
        Retrieve a phone number with messaging settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/phone_numbers/{id}/messaging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        messaging_product: str | Omit = omit,
        messaging_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingUpdateResponse:
        """
        Update the messaging profile and/or messaging product of a phone number

        Args:
          messaging_product:
              Configure the messaging product for this number:

              - Omit this field or set its value to `null` to keep the current value.
              - Set this field to a quoted product ID to set this phone number to that product

          messaging_profile_id:
              Configure the messaging profile this phone number is assigned to:

              - Omit this field or set its value to `null` to keep the current value.
              - Set this field to `""` to unassign the number from its messaging profile
              - Set this field to a quoted UUID of a messaging profile to assign this number
                to that messaging profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/phone_numbers/{id}/messaging",
            body=await async_maybe_transform(
                {
                    "messaging_product": messaging_product,
                    "messaging_profile_id": messaging_profile_id,
                },
                messaging_update_params.MessagingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingUpdateResponse,
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
    ) -> AsyncPaginator[PhoneNumberWithMessagingSettings, AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings]]:
        """
        List phone numbers with messaging settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/phone_numbers/messaging",
            page=AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings],
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
                    messaging_list_params.MessagingListParams,
                ),
            ),
            model=PhoneNumberWithMessagingSettings,
        )


class MessagingResourceWithRawResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = to_raw_response_wrapper(
            messaging.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messaging.update,
        )
        self.list = to_raw_response_wrapper(
            messaging.list,
        )


class AsyncMessagingResourceWithRawResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = async_to_raw_response_wrapper(
            messaging.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messaging.update,
        )
        self.list = async_to_raw_response_wrapper(
            messaging.list,
        )


class MessagingResourceWithStreamingResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = to_streamed_response_wrapper(
            messaging.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messaging.update,
        )
        self.list = to_streamed_response_wrapper(
            messaging.list,
        )


class AsyncMessagingResourceWithStreamingResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

        self.retrieve = async_to_streamed_response_wrapper(
            messaging.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messaging.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messaging.list,
        )
