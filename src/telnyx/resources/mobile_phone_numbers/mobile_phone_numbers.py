# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import mobile_phone_number_list_params, mobile_phone_number_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .messaging import (
    MessagingResource,
    AsyncMessagingResource,
    MessagingResourceWithRawResponse,
    AsyncMessagingResourceWithRawResponse,
    MessagingResourceWithStreamingResponse,
    AsyncMessagingResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.mobile_phone_number import MobilePhoneNumber
from ...types.mobile_phone_number_update_response import MobilePhoneNumberUpdateResponse
from ...types.mobile_phone_number_retrieve_response import MobilePhoneNumberRetrieveResponse

__all__ = ["MobilePhoneNumbersResource", "AsyncMobilePhoneNumbersResource"]


class MobilePhoneNumbersResource(SyncAPIResource):
    @cached_property
    def messaging(self) -> MessagingResource:
        return MessagingResource(self._client)

    @cached_property
    def with_raw_response(self) -> MobilePhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MobilePhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MobilePhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MobilePhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> MobilePhoneNumberRetrieveResponse:
        """
        Retrieve a Mobile Phone Number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/mobile_phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobilePhoneNumberRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        call_forwarding: mobile_phone_number_update_params.CallForwarding | Omit = omit,
        call_recording: mobile_phone_number_update_params.CallRecording | Omit = omit,
        caller_id_name_enabled: bool | Omit = omit,
        cnam_listing: mobile_phone_number_update_params.CnamListing | Omit = omit,
        connection_id: Optional[str] | Omit = omit,
        customer_reference: Optional[str] | Omit = omit,
        inbound: mobile_phone_number_update_params.Inbound | Omit = omit,
        inbound_call_screening: Literal["disabled", "reject_calls", "flag_calls"] | Omit = omit,
        noise_suppression: bool | Omit = omit,
        outbound: mobile_phone_number_update_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobilePhoneNumberUpdateResponse:
        """
        Update a Mobile Phone Number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/mobile_phone_numbers/{id}",
            body=maybe_transform(
                {
                    "call_forwarding": call_forwarding,
                    "call_recording": call_recording,
                    "caller_id_name_enabled": caller_id_name_enabled,
                    "cnam_listing": cnam_listing,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "inbound": inbound,
                    "inbound_call_screening": inbound_call_screening,
                    "noise_suppression": noise_suppression,
                    "outbound": outbound,
                    "tags": tags,
                },
                mobile_phone_number_update_params.MobilePhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobilePhoneNumberUpdateResponse,
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
    ) -> SyncDefaultFlatPagination[MobilePhoneNumber]:
        """
        List Mobile Phone Numbers

        Args:
          page_number: The page number to load

          page_size: The size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/mobile_phone_numbers",
            page=SyncDefaultFlatPagination[MobilePhoneNumber],
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
                    mobile_phone_number_list_params.MobilePhoneNumberListParams,
                ),
            ),
            model=MobilePhoneNumber,
        )


class AsyncMobilePhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def messaging(self) -> AsyncMessagingResource:
        return AsyncMessagingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMobilePhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMobilePhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMobilePhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMobilePhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> MobilePhoneNumberRetrieveResponse:
        """
        Retrieve a Mobile Phone Number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/mobile_phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobilePhoneNumberRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        call_forwarding: mobile_phone_number_update_params.CallForwarding | Omit = omit,
        call_recording: mobile_phone_number_update_params.CallRecording | Omit = omit,
        caller_id_name_enabled: bool | Omit = omit,
        cnam_listing: mobile_phone_number_update_params.CnamListing | Omit = omit,
        connection_id: Optional[str] | Omit = omit,
        customer_reference: Optional[str] | Omit = omit,
        inbound: mobile_phone_number_update_params.Inbound | Omit = omit,
        inbound_call_screening: Literal["disabled", "reject_calls", "flag_calls"] | Omit = omit,
        noise_suppression: bool | Omit = omit,
        outbound: mobile_phone_number_update_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobilePhoneNumberUpdateResponse:
        """
        Update a Mobile Phone Number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/mobile_phone_numbers/{id}",
            body=await async_maybe_transform(
                {
                    "call_forwarding": call_forwarding,
                    "call_recording": call_recording,
                    "caller_id_name_enabled": caller_id_name_enabled,
                    "cnam_listing": cnam_listing,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "inbound": inbound,
                    "inbound_call_screening": inbound_call_screening,
                    "noise_suppression": noise_suppression,
                    "outbound": outbound,
                    "tags": tags,
                },
                mobile_phone_number_update_params.MobilePhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobilePhoneNumberUpdateResponse,
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
    ) -> AsyncPaginator[MobilePhoneNumber, AsyncDefaultFlatPagination[MobilePhoneNumber]]:
        """
        List Mobile Phone Numbers

        Args:
          page_number: The page number to load

          page_size: The size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/mobile_phone_numbers",
            page=AsyncDefaultFlatPagination[MobilePhoneNumber],
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
                    mobile_phone_number_list_params.MobilePhoneNumberListParams,
                ),
            ),
            model=MobilePhoneNumber,
        )


class MobilePhoneNumbersResourceWithRawResponse:
    def __init__(self, mobile_phone_numbers: MobilePhoneNumbersResource) -> None:
        self._mobile_phone_numbers = mobile_phone_numbers

        self.retrieve = to_raw_response_wrapper(
            mobile_phone_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mobile_phone_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            mobile_phone_numbers.list,
        )

    @cached_property
    def messaging(self) -> MessagingResourceWithRawResponse:
        return MessagingResourceWithRawResponse(self._mobile_phone_numbers.messaging)


class AsyncMobilePhoneNumbersResourceWithRawResponse:
    def __init__(self, mobile_phone_numbers: AsyncMobilePhoneNumbersResource) -> None:
        self._mobile_phone_numbers = mobile_phone_numbers

        self.retrieve = async_to_raw_response_wrapper(
            mobile_phone_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mobile_phone_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            mobile_phone_numbers.list,
        )

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithRawResponse:
        return AsyncMessagingResourceWithRawResponse(self._mobile_phone_numbers.messaging)


class MobilePhoneNumbersResourceWithStreamingResponse:
    def __init__(self, mobile_phone_numbers: MobilePhoneNumbersResource) -> None:
        self._mobile_phone_numbers = mobile_phone_numbers

        self.retrieve = to_streamed_response_wrapper(
            mobile_phone_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mobile_phone_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            mobile_phone_numbers.list,
        )

    @cached_property
    def messaging(self) -> MessagingResourceWithStreamingResponse:
        return MessagingResourceWithStreamingResponse(self._mobile_phone_numbers.messaging)


class AsyncMobilePhoneNumbersResourceWithStreamingResponse:
    def __init__(self, mobile_phone_numbers: AsyncMobilePhoneNumbersResource) -> None:
        self._mobile_phone_numbers = mobile_phone_numbers

        self.retrieve = async_to_streamed_response_wrapper(
            mobile_phone_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mobile_phone_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mobile_phone_numbers.list,
        )

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithStreamingResponse:
        return AsyncMessagingResourceWithStreamingResponse(self._mobile_phone_numbers.messaging)
