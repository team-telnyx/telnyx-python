# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from .profile.profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from .calling_settings import (
    CallingSettingsResource,
    AsyncCallingSettingsResource,
    CallingSettingsResourceWithRawResponse,
    AsyncCallingSettingsResourceWithRawResponse,
    CallingSettingsResourceWithStreamingResponse,
    AsyncCallingSettingsResourceWithStreamingResponse,
)
from ....types.whatsapp import (
    phone_number_list_params,
    phone_number_verify_params,
    phone_number_resend_verification_params,
)
from ....types.whatsapp.phone_number_list_response import PhoneNumberListResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def calling_settings(self) -> CallingSettingsResource:
        """Manage Whatsapp phone numbers"""
        return CallingSettingsResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        """Manage Whatsapp phone numbers"""
        return ProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> SyncDefaultFlatPagination[PhoneNumberListResponse]:
        """
        List Whatsapp phone numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/whatsapp/phone_numbers",
            page=SyncDefaultFlatPagination[PhoneNumberListResponse],
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
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=PhoneNumberListResponse,
        )

    def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Whatsapp phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def resend_verification(
        self,
        phone_number: str,
        *,
        verification_method: Literal["sms", "voice"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resend verification code

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/resend_verification", phone_number=phone_number),
            body=maybe_transform(
                {"verification_method": verification_method},
                phone_number_resend_verification_params.PhoneNumberResendVerificationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def verify(
        self,
        phone_number: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Submit verification code for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/verify", phone_number=phone_number),
            body=maybe_transform({"code": code}, phone_number_verify_params.PhoneNumberVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def calling_settings(self) -> AsyncCallingSettingsResource:
        """Manage Whatsapp phone numbers"""
        return AsyncCallingSettingsResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        """Manage Whatsapp phone numbers"""
        return AsyncProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[PhoneNumberListResponse, AsyncDefaultFlatPagination[PhoneNumberListResponse]]:
        """
        List Whatsapp phone numbers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/whatsapp/phone_numbers",
            page=AsyncDefaultFlatPagination[PhoneNumberListResponse],
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
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            model=PhoneNumberListResponse,
        )

    async def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Whatsapp phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def resend_verification(
        self,
        phone_number: str,
        *,
        verification_method: Literal["sms", "voice"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resend verification code

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/resend_verification", phone_number=phone_number),
            body=await async_maybe_transform(
                {"verification_method": verification_method},
                phone_number_resend_verification_params.PhoneNumberResendVerificationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def verify(
        self,
        phone_number: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Submit verification code for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/verify", phone_number=phone_number),
            body=await async_maybe_transform({"code": code}, phone_number_verify_params.PhoneNumberVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_numbers.delete,
        )
        self.resend_verification = to_raw_response_wrapper(
            phone_numbers.resend_verification,
        )
        self.verify = to_raw_response_wrapper(
            phone_numbers.verify,
        )

    @cached_property
    def calling_settings(self) -> CallingSettingsResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return CallingSettingsResourceWithRawResponse(self._phone_numbers.calling_settings)

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return ProfileResourceWithRawResponse(self._phone_numbers.profile)


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_numbers.delete,
        )
        self.resend_verification = async_to_raw_response_wrapper(
            phone_numbers.resend_verification,
        )
        self.verify = async_to_raw_response_wrapper(
            phone_numbers.verify,
        )

    @cached_property
    def calling_settings(self) -> AsyncCallingSettingsResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncCallingSettingsResourceWithRawResponse(self._phone_numbers.calling_settings)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncProfileResourceWithRawResponse(self._phone_numbers.profile)


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_numbers.delete,
        )
        self.resend_verification = to_streamed_response_wrapper(
            phone_numbers.resend_verification,
        )
        self.verify = to_streamed_response_wrapper(
            phone_numbers.verify,
        )

    @cached_property
    def calling_settings(self) -> CallingSettingsResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return CallingSettingsResourceWithStreamingResponse(self._phone_numbers.calling_settings)

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return ProfileResourceWithStreamingResponse(self._phone_numbers.profile)


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_numbers.delete,
        )
        self.resend_verification = async_to_streamed_response_wrapper(
            phone_numbers.resend_verification,
        )
        self.verify = async_to_streamed_response_wrapper(
            phone_numbers.verify,
        )

    @cached_property
    def calling_settings(self) -> AsyncCallingSettingsResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncCallingSettingsResourceWithStreamingResponse(self._phone_numbers.calling_settings)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncProfileResourceWithStreamingResponse(self._phone_numbers.profile)
