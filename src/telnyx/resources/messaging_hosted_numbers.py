# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import messaging_hosted_number_list_params, messaging_hosted_number_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.messaging_hosted_number_delete_response import MessagingHostedNumberDeleteResponse
from ..types.messaging_hosted_number_update_response import MessagingHostedNumberUpdateResponse
from ..types.messaging_hosted_number_retrieve_response import MessagingHostedNumberRetrieveResponse
from ..types.shared.phone_number_with_messaging_settings import PhoneNumberWithMessagingSettings

__all__ = ["MessagingHostedNumbersResource", "AsyncMessagingHostedNumbersResource"]


class MessagingHostedNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingHostedNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingHostedNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingHostedNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingHostedNumbersResourceWithStreamingResponse(self)

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
    ) -> MessagingHostedNumberRetrieveResponse:
        """
        Retrieve a specific messaging hosted number by its ID or phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/messaging_hosted_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        messaging_product: str | Omit = omit,
        messaging_profile_id: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingHostedNumberUpdateResponse:
        """
        Update the messaging settings for a hosted number.

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

          tags: Tags to set on this phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/messaging_hosted_numbers/{id}", id=id),
            body=maybe_transform(
                {
                    "messaging_product": messaging_product,
                    "messaging_profile_id": messaging_profile_id,
                    "tags": tags,
                },
                messaging_hosted_number_update_params.MessagingHostedNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberUpdateResponse,
        )

    def list(
        self,
        *,
        filter_messaging_profile_id: str | Omit = omit,
        filter_phone_number: str | Omit = omit,
        filter_phone_number_contains: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_phone_number: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings]:
        """
        List all hosted numbers associated with the authenticated user.

        Args:
          filter_messaging_profile_id: Filter by messaging profile ID.

          filter_phone_number: Filter by exact phone number.

          filter_phone_number_contains: Filter by phone number substring.

          sort_phone_number: Sort by phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_hosted_numbers",
            page=SyncDefaultFlatPagination[PhoneNumberWithMessagingSettings],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_messaging_profile_id": filter_messaging_profile_id,
                        "filter_phone_number": filter_phone_number,
                        "filter_phone_number_contains": filter_phone_number_contains,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_phone_number": sort_phone_number,
                    },
                    messaging_hosted_number_list_params.MessagingHostedNumberListParams,
                ),
            ),
            model=PhoneNumberWithMessagingSettings,
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
    ) -> MessagingHostedNumberDeleteResponse:
        """
        Delete a messaging hosted number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/messaging_hosted_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberDeleteResponse,
        )


class AsyncMessagingHostedNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingHostedNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingHostedNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingHostedNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingHostedNumbersResourceWithStreamingResponse(self)

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
    ) -> MessagingHostedNumberRetrieveResponse:
        """
        Retrieve a specific messaging hosted number by its ID or phone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/messaging_hosted_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        messaging_product: str | Omit = omit,
        messaging_profile_id: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingHostedNumberUpdateResponse:
        """
        Update the messaging settings for a hosted number.

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

          tags: Tags to set on this phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/messaging_hosted_numbers/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "messaging_product": messaging_product,
                    "messaging_profile_id": messaging_profile_id,
                    "tags": tags,
                },
                messaging_hosted_number_update_params.MessagingHostedNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberUpdateResponse,
        )

    def list(
        self,
        *,
        filter_messaging_profile_id: str | Omit = omit,
        filter_phone_number: str | Omit = omit,
        filter_phone_number_contains: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_phone_number: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PhoneNumberWithMessagingSettings, AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings]]:
        """
        List all hosted numbers associated with the authenticated user.

        Args:
          filter_messaging_profile_id: Filter by messaging profile ID.

          filter_phone_number: Filter by exact phone number.

          filter_phone_number_contains: Filter by phone number substring.

          sort_phone_number: Sort by phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/messaging_hosted_numbers",
            page=AsyncDefaultFlatPagination[PhoneNumberWithMessagingSettings],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_messaging_profile_id": filter_messaging_profile_id,
                        "filter_phone_number": filter_phone_number,
                        "filter_phone_number_contains": filter_phone_number_contains,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_phone_number": sort_phone_number,
                    },
                    messaging_hosted_number_list_params.MessagingHostedNumberListParams,
                ),
            ),
            model=PhoneNumberWithMessagingSettings,
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
    ) -> MessagingHostedNumberDeleteResponse:
        """
        Delete a messaging hosted number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/messaging_hosted_numbers/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberDeleteResponse,
        )


class MessagingHostedNumbersResourceWithRawResponse:
    def __init__(self, messaging_hosted_numbers: MessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.retrieve = to_raw_response_wrapper(
            messaging_hosted_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messaging_hosted_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            messaging_hosted_numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            messaging_hosted_numbers.delete,
        )


class AsyncMessagingHostedNumbersResourceWithRawResponse:
    def __init__(self, messaging_hosted_numbers: AsyncMessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.retrieve = async_to_raw_response_wrapper(
            messaging_hosted_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messaging_hosted_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            messaging_hosted_numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messaging_hosted_numbers.delete,
        )


class MessagingHostedNumbersResourceWithStreamingResponse:
    def __init__(self, messaging_hosted_numbers: MessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.retrieve = to_streamed_response_wrapper(
            messaging_hosted_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messaging_hosted_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            messaging_hosted_numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            messaging_hosted_numbers.delete,
        )


class AsyncMessagingHostedNumbersResourceWithStreamingResponse:
    def __init__(self, messaging_hosted_numbers: AsyncMessagingHostedNumbersResource) -> None:
        self._messaging_hosted_numbers = messaging_hosted_numbers

        self.retrieve = async_to_streamed_response_wrapper(
            messaging_hosted_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messaging_hosted_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messaging_hosted_numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messaging_hosted_numbers.delete,
        )
