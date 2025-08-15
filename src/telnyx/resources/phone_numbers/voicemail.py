# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.phone_numbers import voicemail_create_params, voicemail_update_params
from ...types.phone_numbers.voicemail_create_response import VoicemailCreateResponse
from ...types.phone_numbers.voicemail_update_response import VoicemailUpdateResponse
from ...types.phone_numbers.voicemail_retrieve_response import VoicemailRetrieveResponse

__all__ = ["VoicemailResource", "AsyncVoicemailResource"]


class VoicemailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoicemailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VoicemailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoicemailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VoicemailResourceWithStreamingResponse(self)

    def create(
        self,
        phone_number_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoicemailCreateResponse:
        """
        Create voicemail settings for a phone number

        Args:
          enabled: Whether voicemail is enabled.

          pin: The pin used for voicemail

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._post(
            f"/phone_numbers/{phone_number_id}/voicemail",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "pin": pin,
                },
                voicemail_create_params.VoicemailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicemailCreateResponse,
        )

    def retrieve(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoicemailRetrieveResponse:
        """
        Returns the voicemail settings for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._get(
            f"/phone_numbers/{phone_number_id}/voicemail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicemailRetrieveResponse,
        )

    def update(
        self,
        phone_number_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoicemailUpdateResponse:
        """
        Update voicemail settings for a phone number

        Args:
          enabled: Whether voicemail is enabled.

          pin: The pin used for voicemail

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return self._patch(
            f"/phone_numbers/{phone_number_id}/voicemail",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "pin": pin,
                },
                voicemail_update_params.VoicemailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicemailUpdateResponse,
        )


class AsyncVoicemailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoicemailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoicemailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoicemailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVoicemailResourceWithStreamingResponse(self)

    async def create(
        self,
        phone_number_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoicemailCreateResponse:
        """
        Create voicemail settings for a phone number

        Args:
          enabled: Whether voicemail is enabled.

          pin: The pin used for voicemail

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._post(
            f"/phone_numbers/{phone_number_id}/voicemail",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "pin": pin,
                },
                voicemail_create_params.VoicemailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicemailCreateResponse,
        )

    async def retrieve(
        self,
        phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoicemailRetrieveResponse:
        """
        Returns the voicemail settings for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._get(
            f"/phone_numbers/{phone_number_id}/voicemail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicemailRetrieveResponse,
        )

    async def update(
        self,
        phone_number_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VoicemailUpdateResponse:
        """
        Update voicemail settings for a phone number

        Args:
          enabled: Whether voicemail is enabled.

          pin: The pin used for voicemail

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number_id:
            raise ValueError(f"Expected a non-empty value for `phone_number_id` but received {phone_number_id!r}")
        return await self._patch(
            f"/phone_numbers/{phone_number_id}/voicemail",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "pin": pin,
                },
                voicemail_update_params.VoicemailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoicemailUpdateResponse,
        )


class VoicemailResourceWithRawResponse:
    def __init__(self, voicemail: VoicemailResource) -> None:
        self._voicemail = voicemail

        self.create = to_raw_response_wrapper(
            voicemail.create,
        )
        self.retrieve = to_raw_response_wrapper(
            voicemail.retrieve,
        )
        self.update = to_raw_response_wrapper(
            voicemail.update,
        )


class AsyncVoicemailResourceWithRawResponse:
    def __init__(self, voicemail: AsyncVoicemailResource) -> None:
        self._voicemail = voicemail

        self.create = async_to_raw_response_wrapper(
            voicemail.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            voicemail.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            voicemail.update,
        )


class VoicemailResourceWithStreamingResponse:
    def __init__(self, voicemail: VoicemailResource) -> None:
        self._voicemail = voicemail

        self.create = to_streamed_response_wrapper(
            voicemail.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            voicemail.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            voicemail.update,
        )


class AsyncVoicemailResourceWithStreamingResponse:
    def __init__(self, voicemail: AsyncVoicemailResource) -> None:
        self._voicemail = voicemail

        self.create = async_to_streamed_response_wrapper(
            voicemail.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            voicemail.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            voicemail.update,
        )
