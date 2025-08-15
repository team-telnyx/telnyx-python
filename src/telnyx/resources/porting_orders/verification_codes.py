# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.porting_orders import (
    verification_code_list_params,
    verification_code_send_params,
    verification_code_verify_params,
)
from ...types.porting_orders.verification_code_list_response import VerificationCodeListResponse
from ...types.porting_orders.verification_code_verify_response import VerificationCodeVerifyResponse

__all__ = ["VerificationCodesResource", "AsyncVerificationCodesResource"]


class VerificationCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerificationCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VerificationCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VerificationCodesResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        filter: verification_code_list_params.Filter | NotGiven = NOT_GIVEN,
        page: verification_code_list_params.Page | NotGiven = NOT_GIVEN,
        sort: verification_code_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCodeListResponse:
        """
        Returns a list of verification codes for a porting order.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[verified]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting_orders/{id}/verification_codes",
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
                    verification_code_list_params.VerificationCodeListParams,
                ),
            ),
            cast_to=VerificationCodeListResponse,
        )

    def send(
        self,
        id: str,
        *,
        phone_numbers: List[str] | NotGiven = NOT_GIVEN,
        verification_method: Literal["sms", "call"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send the verification code for all porting phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/porting_orders/{id}/verification_codes/send",
            body=maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "verification_method": verification_method,
                },
                verification_code_send_params.VerificationCodeSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def verify(
        self,
        id: str,
        *,
        verification_codes: Iterable[verification_code_verify_params.VerificationCode] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCodeVerifyResponse:
        """
        Verifies the verification code for a list of phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/porting_orders/{id}/verification_codes/verify",
            body=maybe_transform(
                {"verification_codes": verification_codes}, verification_code_verify_params.VerificationCodeVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCodeVerifyResponse,
        )


class AsyncVerificationCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerificationCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVerificationCodesResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        filter: verification_code_list_params.Filter | NotGiven = NOT_GIVEN,
        page: verification_code_list_params.Page | NotGiven = NOT_GIVEN,
        sort: verification_code_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCodeListResponse:
        """
        Returns a list of verification codes for a porting order.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[verified]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting_orders/{id}/verification_codes",
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
                    verification_code_list_params.VerificationCodeListParams,
                ),
            ),
            cast_to=VerificationCodeListResponse,
        )

    async def send(
        self,
        id: str,
        *,
        phone_numbers: List[str] | NotGiven = NOT_GIVEN,
        verification_method: Literal["sms", "call"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Send the verification code for all porting phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/porting_orders/{id}/verification_codes/send",
            body=await async_maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "verification_method": verification_method,
                },
                verification_code_send_params.VerificationCodeSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def verify(
        self,
        id: str,
        *,
        verification_codes: Iterable[verification_code_verify_params.VerificationCode] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCodeVerifyResponse:
        """
        Verifies the verification code for a list of phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/porting_orders/{id}/verification_codes/verify",
            body=await async_maybe_transform(
                {"verification_codes": verification_codes}, verification_code_verify_params.VerificationCodeVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCodeVerifyResponse,
        )


class VerificationCodesResourceWithRawResponse:
    def __init__(self, verification_codes: VerificationCodesResource) -> None:
        self._verification_codes = verification_codes

        self.list = to_raw_response_wrapper(
            verification_codes.list,
        )
        self.send = to_raw_response_wrapper(
            verification_codes.send,
        )
        self.verify = to_raw_response_wrapper(
            verification_codes.verify,
        )


class AsyncVerificationCodesResourceWithRawResponse:
    def __init__(self, verification_codes: AsyncVerificationCodesResource) -> None:
        self._verification_codes = verification_codes

        self.list = async_to_raw_response_wrapper(
            verification_codes.list,
        )
        self.send = async_to_raw_response_wrapper(
            verification_codes.send,
        )
        self.verify = async_to_raw_response_wrapper(
            verification_codes.verify,
        )


class VerificationCodesResourceWithStreamingResponse:
    def __init__(self, verification_codes: VerificationCodesResource) -> None:
        self._verification_codes = verification_codes

        self.list = to_streamed_response_wrapper(
            verification_codes.list,
        )
        self.send = to_streamed_response_wrapper(
            verification_codes.send,
        )
        self.verify = to_streamed_response_wrapper(
            verification_codes.verify,
        )


class AsyncVerificationCodesResourceWithStreamingResponse:
    def __init__(self, verification_codes: AsyncVerificationCodesResource) -> None:
        self._verification_codes = verification_codes

        self.list = async_to_streamed_response_wrapper(
            verification_codes.list,
        )
        self.send = async_to_streamed_response_wrapper(
            verification_codes.send,
        )
        self.verify = async_to_streamed_response_wrapper(
            verification_codes.verify,
        )
