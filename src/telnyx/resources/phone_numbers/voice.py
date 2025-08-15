# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.phone_numbers import (
    voice_list_params,
    voice_update_params,
)
from ...types.phone_numbers.cnam_listing_param import CnamListingParam
from ...types.phone_numbers.voice_list_response import VoiceListResponse
from ...types.phone_numbers.call_recording_param import CallRecordingParam
from ...types.phone_numbers.media_features_param import MediaFeaturesParam
from ...types.phone_numbers.call_forwarding_param import CallForwardingParam
from ...types.phone_numbers.voice_update_response import VoiceUpdateResponse
from ...types.phone_numbers.voice_retrieve_response import VoiceRetrieveResponse

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)

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
    ) -> VoiceRetrieveResponse:
        """
        Retrieve a phone number with voice settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/phone_numbers/{id}/voice",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        call_forwarding: CallForwardingParam | NotGiven = NOT_GIVEN,
        call_recording: CallRecordingParam | NotGiven = NOT_GIVEN,
        caller_id_name_enabled: bool | NotGiven = NOT_GIVEN,
        cnam_listing: CnamListingParam | NotGiven = NOT_GIVEN,
        inbound_call_screening: Literal["disabled", "reject_calls", "flag_calls"] | NotGiven = NOT_GIVEN,
        media_features: MediaFeaturesParam | NotGiven = NOT_GIVEN,
        tech_prefix_enabled: bool | NotGiven = NOT_GIVEN,
        translated_number: str | NotGiven = NOT_GIVEN,
        usage_payment_method: Literal["pay-per-minute", "channel"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoiceUpdateResponse:
        """
        Update a phone number with voice settings

        Args:
          call_forwarding: The call forwarding settings for a phone number.

          call_recording: The call recording settings for a phone number.

          caller_id_name_enabled: Controls whether the caller ID name is enabled for this phone number.

          cnam_listing: The CNAM listing settings for a phone number.

          inbound_call_screening: The inbound_call_screening setting is a phone number configuration option
              variable that allows users to configure their settings to block or flag
              fraudulent calls. It can be set to disabled, reject_calls, or flag_calls. This
              feature has an additional per-number monthly cost associated with it.

          media_features: The media features settings for a phone number.

          tech_prefix_enabled: Controls whether a tech prefix is enabled for this phone number.

          translated_number: This field allows you to rewrite the destination number of an inbound call
              before the call is routed to you. The value of this field may be any
              alphanumeric value, and the value will replace the number originally dialed.

          usage_payment_method: Controls whether a number is billed per minute or uses your concurrent channels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/phone_numbers/{id}/voice",
            body=maybe_transform(
                {
                    "call_forwarding": call_forwarding,
                    "call_recording": call_recording,
                    "caller_id_name_enabled": caller_id_name_enabled,
                    "cnam_listing": cnam_listing,
                    "inbound_call_screening": inbound_call_screening,
                    "media_features": media_features,
                    "tech_prefix_enabled": tech_prefix_enabled,
                    "translated_number": translated_number,
                    "usage_payment_method": usage_payment_method,
                },
                voice_update_params.VoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceUpdateResponse,
        )

    def list(
        self,
        *,
        filter: voice_list_params.Filter | NotGiven = NOT_GIVEN,
        page: voice_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoiceListResponse:
        """
        List phone numbers with voice settings

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[connection_name], filter[customer_reference],
              filter[voice.usage_payment_method]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_numbers/voice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    voice_list_params.VoiceListParams,
                ),
            ),
            cast_to=VoiceListResponse,
        )


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)

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
    ) -> VoiceRetrieveResponse:
        """
        Retrieve a phone number with voice settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/phone_numbers/{id}/voice",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        call_forwarding: CallForwardingParam | NotGiven = NOT_GIVEN,
        call_recording: CallRecordingParam | NotGiven = NOT_GIVEN,
        caller_id_name_enabled: bool | NotGiven = NOT_GIVEN,
        cnam_listing: CnamListingParam | NotGiven = NOT_GIVEN,
        inbound_call_screening: Literal["disabled", "reject_calls", "flag_calls"] | NotGiven = NOT_GIVEN,
        media_features: MediaFeaturesParam | NotGiven = NOT_GIVEN,
        tech_prefix_enabled: bool | NotGiven = NOT_GIVEN,
        translated_number: str | NotGiven = NOT_GIVEN,
        usage_payment_method: Literal["pay-per-minute", "channel"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoiceUpdateResponse:
        """
        Update a phone number with voice settings

        Args:
          call_forwarding: The call forwarding settings for a phone number.

          call_recording: The call recording settings for a phone number.

          caller_id_name_enabled: Controls whether the caller ID name is enabled for this phone number.

          cnam_listing: The CNAM listing settings for a phone number.

          inbound_call_screening: The inbound_call_screening setting is a phone number configuration option
              variable that allows users to configure their settings to block or flag
              fraudulent calls. It can be set to disabled, reject_calls, or flag_calls. This
              feature has an additional per-number monthly cost associated with it.

          media_features: The media features settings for a phone number.

          tech_prefix_enabled: Controls whether a tech prefix is enabled for this phone number.

          translated_number: This field allows you to rewrite the destination number of an inbound call
              before the call is routed to you. The value of this field may be any
              alphanumeric value, and the value will replace the number originally dialed.

          usage_payment_method: Controls whether a number is billed per minute or uses your concurrent channels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/phone_numbers/{id}/voice",
            body=await async_maybe_transform(
                {
                    "call_forwarding": call_forwarding,
                    "call_recording": call_recording,
                    "caller_id_name_enabled": caller_id_name_enabled,
                    "cnam_listing": cnam_listing,
                    "inbound_call_screening": inbound_call_screening,
                    "media_features": media_features,
                    "tech_prefix_enabled": tech_prefix_enabled,
                    "translated_number": translated_number,
                    "usage_payment_method": usage_payment_method,
                },
                voice_update_params.VoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: voice_list_params.Filter | NotGiven = NOT_GIVEN,
        page: voice_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoiceListResponse:
        """
        List phone numbers with voice settings

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[connection_name], filter[customer_reference],
              filter[voice.usage_payment_method]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_numbers/voice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    voice_list_params.VoiceListParams,
                ),
            ),
            cast_to=VoiceListResponse,
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.retrieve = to_raw_response_wrapper(
            voice.retrieve,
        )
        self.update = to_raw_response_wrapper(
            voice.update,
        )
        self.list = to_raw_response_wrapper(
            voice.list,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.retrieve = async_to_raw_response_wrapper(
            voice.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            voice.update,
        )
        self.list = async_to_raw_response_wrapper(
            voice.list,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.retrieve = to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            voice.update,
        )
        self.list = to_streamed_response_wrapper(
            voice.list,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.retrieve = async_to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            voice.update,
        )
        self.list = async_to_streamed_response_wrapper(
            voice.list,
        )
