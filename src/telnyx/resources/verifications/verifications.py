# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    verification_trigger_sms_params,
    verification_trigger_call_params,
    verification_trigger_flashcall_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from .by_phone_number.by_phone_number import (
    ByPhoneNumberResource,
    AsyncByPhoneNumberResource,
    ByPhoneNumberResourceWithRawResponse,
    AsyncByPhoneNumberResourceWithRawResponse,
    ByPhoneNumberResourceWithStreamingResponse,
    AsyncByPhoneNumberResourceWithStreamingResponse,
)
from ...types.create_verification_response import CreateVerificationResponse
from ...types.verification_retrieve_response import VerificationRetrieveResponse

__all__ = ["VerificationsResource", "AsyncVerificationsResource"]


class VerificationsResource(SyncAPIResource):
    @cached_property
    def by_phone_number(self) -> ByPhoneNumberResource:
        return ByPhoneNumberResource(self._client)

    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VerificationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRetrieveResponse:
        """
        Retrieve verification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._get(
            f"/verifications/{verification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
        )

    def trigger_call(
        self,
        *,
        phone_number: str,
        verify_profile_id: str,
        custom_code: Optional[str] | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateVerificationResponse:
        """
        Trigger Call verification

        Args:
          phone_number: +E164 formatted phone number.

          verify_profile_id: The identifier of the associated Verify profile.

          custom_code: Send a self-generated numeric code to the end-user

          timeout_secs: The number of seconds the verification code is valid for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verifications/call",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "verify_profile_id": verify_profile_id,
                    "custom_code": custom_code,
                    "timeout_secs": timeout_secs,
                },
                verification_trigger_call_params.VerificationTriggerCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateVerificationResponse,
        )

    def trigger_flashcall(
        self,
        *,
        phone_number: str,
        verify_profile_id: str,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateVerificationResponse:
        """
        Trigger Flash call verification

        Args:
          phone_number: +E164 formatted phone number.

          verify_profile_id: The identifier of the associated Verify profile.

          timeout_secs: The number of seconds the verification code is valid for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verifications/flashcall",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "verify_profile_id": verify_profile_id,
                    "timeout_secs": timeout_secs,
                },
                verification_trigger_flashcall_params.VerificationTriggerFlashcallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateVerificationResponse,
        )

    def trigger_sms(
        self,
        *,
        phone_number: str,
        verify_profile_id: str,
        custom_code: Optional[str] | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateVerificationResponse:
        """
        Trigger SMS verification

        Args:
          phone_number: +E164 formatted phone number.

          verify_profile_id: The identifier of the associated Verify profile.

          custom_code: Send a self-generated numeric code to the end-user

          timeout_secs: The number of seconds the verification code is valid for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verifications/sms",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "verify_profile_id": verify_profile_id,
                    "custom_code": custom_code,
                    "timeout_secs": timeout_secs,
                },
                verification_trigger_sms_params.VerificationTriggerSMSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateVerificationResponse,
        )


class AsyncVerificationsResource(AsyncAPIResource):
    @cached_property
    def by_phone_number(self) -> AsyncByPhoneNumberResource:
        return AsyncByPhoneNumberResource(self._client)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVerificationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRetrieveResponse:
        """
        Retrieve verification

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._get(
            f"/verifications/{verification_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
        )

    async def trigger_call(
        self,
        *,
        phone_number: str,
        verify_profile_id: str,
        custom_code: Optional[str] | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateVerificationResponse:
        """
        Trigger Call verification

        Args:
          phone_number: +E164 formatted phone number.

          verify_profile_id: The identifier of the associated Verify profile.

          custom_code: Send a self-generated numeric code to the end-user

          timeout_secs: The number of seconds the verification code is valid for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verifications/call",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "verify_profile_id": verify_profile_id,
                    "custom_code": custom_code,
                    "timeout_secs": timeout_secs,
                },
                verification_trigger_call_params.VerificationTriggerCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateVerificationResponse,
        )

    async def trigger_flashcall(
        self,
        *,
        phone_number: str,
        verify_profile_id: str,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateVerificationResponse:
        """
        Trigger Flash call verification

        Args:
          phone_number: +E164 formatted phone number.

          verify_profile_id: The identifier of the associated Verify profile.

          timeout_secs: The number of seconds the verification code is valid for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verifications/flashcall",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "verify_profile_id": verify_profile_id,
                    "timeout_secs": timeout_secs,
                },
                verification_trigger_flashcall_params.VerificationTriggerFlashcallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateVerificationResponse,
        )

    async def trigger_sms(
        self,
        *,
        phone_number: str,
        verify_profile_id: str,
        custom_code: Optional[str] | NotGiven = NOT_GIVEN,
        timeout_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateVerificationResponse:
        """
        Trigger SMS verification

        Args:
          phone_number: +E164 formatted phone number.

          verify_profile_id: The identifier of the associated Verify profile.

          custom_code: Send a self-generated numeric code to the end-user

          timeout_secs: The number of seconds the verification code is valid for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verifications/sms",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "verify_profile_id": verify_profile_id,
                    "custom_code": custom_code,
                    "timeout_secs": timeout_secs,
                },
                verification_trigger_sms_params.VerificationTriggerSMSParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateVerificationResponse,
        )


class VerificationsResourceWithRawResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.retrieve = to_raw_response_wrapper(
            verifications.retrieve,
        )
        self.trigger_call = to_raw_response_wrapper(
            verifications.trigger_call,
        )
        self.trigger_flashcall = to_raw_response_wrapper(
            verifications.trigger_flashcall,
        )
        self.trigger_sms = to_raw_response_wrapper(
            verifications.trigger_sms,
        )

    @cached_property
    def by_phone_number(self) -> ByPhoneNumberResourceWithRawResponse:
        return ByPhoneNumberResourceWithRawResponse(self._verifications.by_phone_number)

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._verifications.actions)


class AsyncVerificationsResourceWithRawResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.retrieve = async_to_raw_response_wrapper(
            verifications.retrieve,
        )
        self.trigger_call = async_to_raw_response_wrapper(
            verifications.trigger_call,
        )
        self.trigger_flashcall = async_to_raw_response_wrapper(
            verifications.trigger_flashcall,
        )
        self.trigger_sms = async_to_raw_response_wrapper(
            verifications.trigger_sms,
        )

    @cached_property
    def by_phone_number(self) -> AsyncByPhoneNumberResourceWithRawResponse:
        return AsyncByPhoneNumberResourceWithRawResponse(self._verifications.by_phone_number)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._verifications.actions)


class VerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.retrieve = to_streamed_response_wrapper(
            verifications.retrieve,
        )
        self.trigger_call = to_streamed_response_wrapper(
            verifications.trigger_call,
        )
        self.trigger_flashcall = to_streamed_response_wrapper(
            verifications.trigger_flashcall,
        )
        self.trigger_sms = to_streamed_response_wrapper(
            verifications.trigger_sms,
        )

    @cached_property
    def by_phone_number(self) -> ByPhoneNumberResourceWithStreamingResponse:
        return ByPhoneNumberResourceWithStreamingResponse(self._verifications.by_phone_number)

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._verifications.actions)


class AsyncVerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.retrieve = async_to_streamed_response_wrapper(
            verifications.retrieve,
        )
        self.trigger_call = async_to_streamed_response_wrapper(
            verifications.trigger_call,
        )
        self.trigger_flashcall = async_to_streamed_response_wrapper(
            verifications.trigger_flashcall,
        )
        self.trigger_sms = async_to_streamed_response_wrapper(
            verifications.trigger_sms,
        )

    @cached_property
    def by_phone_number(self) -> AsyncByPhoneNumberResourceWithStreamingResponse:
        return AsyncByPhoneNumberResourceWithStreamingResponse(self._verifications.by_phone_number)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._verifications.actions)
