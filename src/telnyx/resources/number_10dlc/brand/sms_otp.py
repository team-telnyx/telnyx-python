# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.number_10dlc.brand import sms_otp_verify_params, sms_otp_trigger_params, sms_otp_get_status_params
from ....types.number_10dlc.brand.sms_otp_trigger_response import SMSOtpTriggerResponse
from ....types.number_10dlc.brand.sms_otp_get_status_response import SMSOtpGetStatusResponse

__all__ = ["SMSOtpResource", "AsyncSMSOtpResource"]


class SMSOtpResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SMSOtpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SMSOtpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SMSOtpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SMSOtpResourceWithStreamingResponse(self)

    def get_status(
        self,
        reference_id: str,
        *,
        brand_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SMSOtpGetStatusResponse:
        """
        Query the status of an SMS OTP (One-Time Password) for Sole Proprietor brand
        verification.

        This endpoint allows you to check the delivery and verification status of an OTP
        sent during the Sole Proprietor brand verification process. You can query by
        either:

        - `referenceId` - The reference ID returned when the OTP was initially triggered
        - `brandId` - Query parameter for portal users to look up OTP status by Brand ID

        The response includes delivery status, verification dates, and detailed delivery
        information.

        Args:
          brand_id: Filter by Brand ID for easier lookup in portal applications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reference_id:
            raise ValueError(f"Expected a non-empty value for `reference_id` but received {reference_id!r}")
        return self._get(
            f"/10dlc/brand/smsOtp/{reference_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"brand_id": brand_id}, sms_otp_get_status_params.SMSOtpGetStatusParams),
            ),
            cast_to=SMSOtpGetStatusResponse,
        )

    def trigger(
        self,
        brand_id: str,
        *,
        pin_sms: str,
        success_sms: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SMSOtpTriggerResponse:
        """
        Trigger or re-trigger an SMS OTP (One-Time Password) for Sole Proprietor brand
        verification.

        **Important Notes:**

        - Only allowed for Sole Proprietor (`SOLE_PROPRIETOR`) brands
        - Triggers generation of a one-time password sent to the `mobilePhone` number in
          the brand's profile
        - Campaigns cannot be created until OTP verification is complete
        - US/CA numbers only for real OTPs; mock brands can use non-US/CA numbers for
          testing
        - Returns a `referenceId` that can be used to check OTP status via the GET
          `/10dlc/brand/smsOtp/{referenceId}` endpoint

        **Use Cases:**

        - Initial OTP trigger after Sole Proprietor brand creation
        - Re-triggering OTP if the user didn't receive or needs a new code

        Args:
          pin_sms: SMS message template to send the OTP. Must include `@OTP_PIN@` placeholder which
              will be replaced with the actual PIN

          success_sms: SMS message to send upon successful OTP verification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._post(
            f"/10dlc/brand/{brand_id}/smsOtp",
            body=maybe_transform(
                {
                    "pin_sms": pin_sms,
                    "success_sms": success_sms,
                },
                sms_otp_trigger_params.SMSOtpTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SMSOtpTriggerResponse,
        )

    def verify(
        self,
        brand_id: str,
        *,
        otp_pin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Verify the SMS OTP (One-Time Password) for Sole Proprietor brand verification.

        **Verification Flow:**

        1. User receives OTP via SMS after triggering
        2. User submits the OTP pin through this endpoint
        3. Upon successful verification:
           - A `BRAND_OTP_VERIFIED` webhook event is sent to the CSP
           - The brand's `identityStatus` changes to `VERIFIED`
           - Campaigns can now be created for this brand

        **Error Handling:**

        Provides proper error responses for:

        - Invalid OTP pins
        - Expired OTPs
        - OTP verification failures

        Args:
          otp_pin: The OTP PIN received via SMS

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/10dlc/brand/{brand_id}/smsOtp",
            body=maybe_transform({"otp_pin": otp_pin}, sms_otp_verify_params.SMSOtpVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSMSOtpResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSMSOtpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSMSOtpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSMSOtpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSMSOtpResourceWithStreamingResponse(self)

    async def get_status(
        self,
        reference_id: str,
        *,
        brand_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SMSOtpGetStatusResponse:
        """
        Query the status of an SMS OTP (One-Time Password) for Sole Proprietor brand
        verification.

        This endpoint allows you to check the delivery and verification status of an OTP
        sent during the Sole Proprietor brand verification process. You can query by
        either:

        - `referenceId` - The reference ID returned when the OTP was initially triggered
        - `brandId` - Query parameter for portal users to look up OTP status by Brand ID

        The response includes delivery status, verification dates, and detailed delivery
        information.

        Args:
          brand_id: Filter by Brand ID for easier lookup in portal applications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not reference_id:
            raise ValueError(f"Expected a non-empty value for `reference_id` but received {reference_id!r}")
        return await self._get(
            f"/10dlc/brand/smsOtp/{reference_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"brand_id": brand_id}, sms_otp_get_status_params.SMSOtpGetStatusParams
                ),
            ),
            cast_to=SMSOtpGetStatusResponse,
        )

    async def trigger(
        self,
        brand_id: str,
        *,
        pin_sms: str,
        success_sms: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SMSOtpTriggerResponse:
        """
        Trigger or re-trigger an SMS OTP (One-Time Password) for Sole Proprietor brand
        verification.

        **Important Notes:**

        - Only allowed for Sole Proprietor (`SOLE_PROPRIETOR`) brands
        - Triggers generation of a one-time password sent to the `mobilePhone` number in
          the brand's profile
        - Campaigns cannot be created until OTP verification is complete
        - US/CA numbers only for real OTPs; mock brands can use non-US/CA numbers for
          testing
        - Returns a `referenceId` that can be used to check OTP status via the GET
          `/10dlc/brand/smsOtp/{referenceId}` endpoint

        **Use Cases:**

        - Initial OTP trigger after Sole Proprietor brand creation
        - Re-triggering OTP if the user didn't receive or needs a new code

        Args:
          pin_sms: SMS message template to send the OTP. Must include `@OTP_PIN@` placeholder which
              will be replaced with the actual PIN

          success_sms: SMS message to send upon successful OTP verification

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._post(
            f"/10dlc/brand/{brand_id}/smsOtp",
            body=await async_maybe_transform(
                {
                    "pin_sms": pin_sms,
                    "success_sms": success_sms,
                },
                sms_otp_trigger_params.SMSOtpTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SMSOtpTriggerResponse,
        )

    async def verify(
        self,
        brand_id: str,
        *,
        otp_pin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Verify the SMS OTP (One-Time Password) for Sole Proprietor brand verification.

        **Verification Flow:**

        1. User receives OTP via SMS after triggering
        2. User submits the OTP pin through this endpoint
        3. Upon successful verification:
           - A `BRAND_OTP_VERIFIED` webhook event is sent to the CSP
           - The brand's `identityStatus` changes to `VERIFIED`
           - Campaigns can now be created for this brand

        **Error Handling:**

        Provides proper error responses for:

        - Invalid OTP pins
        - Expired OTPs
        - OTP verification failures

        Args:
          otp_pin: The OTP PIN received via SMS

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/10dlc/brand/{brand_id}/smsOtp",
            body=await async_maybe_transform({"otp_pin": otp_pin}, sms_otp_verify_params.SMSOtpVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SMSOtpResourceWithRawResponse:
    def __init__(self, sms_otp: SMSOtpResource) -> None:
        self._sms_otp = sms_otp

        self.get_status = to_raw_response_wrapper(
            sms_otp.get_status,
        )
        self.trigger = to_raw_response_wrapper(
            sms_otp.trigger,
        )
        self.verify = to_raw_response_wrapper(
            sms_otp.verify,
        )


class AsyncSMSOtpResourceWithRawResponse:
    def __init__(self, sms_otp: AsyncSMSOtpResource) -> None:
        self._sms_otp = sms_otp

        self.get_status = async_to_raw_response_wrapper(
            sms_otp.get_status,
        )
        self.trigger = async_to_raw_response_wrapper(
            sms_otp.trigger,
        )
        self.verify = async_to_raw_response_wrapper(
            sms_otp.verify,
        )


class SMSOtpResourceWithStreamingResponse:
    def __init__(self, sms_otp: SMSOtpResource) -> None:
        self._sms_otp = sms_otp

        self.get_status = to_streamed_response_wrapper(
            sms_otp.get_status,
        )
        self.trigger = to_streamed_response_wrapper(
            sms_otp.trigger,
        )
        self.verify = to_streamed_response_wrapper(
            sms_otp.verify,
        )


class AsyncSMSOtpResourceWithStreamingResponse:
    def __init__(self, sms_otp: AsyncSMSOtpResource) -> None:
        self._sms_otp = sms_otp

        self.get_status = async_to_streamed_response_wrapper(
            sms_otp.get_status,
        )
        self.trigger = async_to_streamed_response_wrapper(
            sms_otp.trigger,
        )
        self.verify = async_to_streamed_response_wrapper(
            sms_otp.verify,
        )
