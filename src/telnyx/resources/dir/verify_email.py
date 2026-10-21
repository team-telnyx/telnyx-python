# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.dir import verify_email_confirm_params
from ..._base_client import make_request_options
from ...types.dir.email_verification_status_wrapped import EmailVerificationStatusWrapped

__all__ = ["VerifyEmailResource", "AsyncVerifyEmailResource"]


class VerifyEmailResource(SyncAPIResource):
    """Verify ownership of a DIR's authorizer email.

    A short code is emailed and confirmed.
    """

    @cached_property
    def with_raw_response(self) -> VerifyEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VerifyEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifyEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VerifyEmailResourceWithStreamingResponse(self)

    def create(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailVerificationStatusWrapped:
        """
        Email a 6-digit code to the DIR's authorizer email to confirm ownership of that
        address. The code goes to the authorizer, not to the caller. If the authorizer
        is someone else (for example a client's executive), that person has to share the
        code with whoever is completing setup.

        How long the code lasts: 15 minutes by default. 8 hours when the DIR has a call
        center (BPO) linked through `bpo_authorizations` whose authorization is pending
        review or approved (a rejected authorization does not count). Link the call
        center before you send the code: a code sent before the link keeps the 15-minute
        window, and a code sent after the link lasts 8 hours. The email states the
        window, and `expires_at` in the response always shows the exact expiry.

        To resend, call this endpoint again. Each send issues a fresh code and
        invalidates the previous one. Sends are limited to one every 60 seconds and 10
        per DIR per UTC day. A throttled send returns `429` with `retry_after_secs` and
        `sends_remaining_today` in the error `meta`.

        Submit the code to `POST /dir/{dir_id}/verify_email/confirm`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._post(
            path_template("/dir/{dir_id}/verify_email", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerificationStatusWrapped,
        )

    def list(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailVerificationStatusWrapped:
        """
        Whether the DIR's current authorizer email has been verified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get(
            path_template("/dir/{dir_id}/verify_email", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerificationStatusWrapped,
        )

    def confirm(
        self,
        dir_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailVerificationStatusWrapped:
        """Submit the 6-digit code that was emailed to the DIR's authorizer email.

        On
        success the authorizer email is marked verified.

        For security, any failure (wrong, expired, already-used, or too many attempts)
        returns the same generic message.

        Args:
          code: The 6-digit code sent to the authorizer email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._post(
            path_template("/dir/{dir_id}/verify_email/confirm", dir_id=dir_id),
            body=maybe_transform({"code": code}, verify_email_confirm_params.VerifyEmailConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerificationStatusWrapped,
        )


class AsyncVerifyEmailResource(AsyncAPIResource):
    """Verify ownership of a DIR's authorizer email.

    A short code is emailed and confirmed.
    """

    @cached_property
    def with_raw_response(self) -> AsyncVerifyEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifyEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifyEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVerifyEmailResourceWithStreamingResponse(self)

    async def create(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailVerificationStatusWrapped:
        """
        Email a 6-digit code to the DIR's authorizer email to confirm ownership of that
        address. The code goes to the authorizer, not to the caller. If the authorizer
        is someone else (for example a client's executive), that person has to share the
        code with whoever is completing setup.

        How long the code lasts: 15 minutes by default. 8 hours when the DIR has a call
        center (BPO) linked through `bpo_authorizations` whose authorization is pending
        review or approved (a rejected authorization does not count). Link the call
        center before you send the code: a code sent before the link keeps the 15-minute
        window, and a code sent after the link lasts 8 hours. The email states the
        window, and `expires_at` in the response always shows the exact expiry.

        To resend, call this endpoint again. Each send issues a fresh code and
        invalidates the previous one. Sends are limited to one every 60 seconds and 10
        per DIR per UTC day. A throttled send returns `429` with `retry_after_secs` and
        `sends_remaining_today` in the error `meta`.

        Submit the code to `POST /dir/{dir_id}/verify_email/confirm`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._post(
            path_template("/dir/{dir_id}/verify_email", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerificationStatusWrapped,
        )

    async def list(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailVerificationStatusWrapped:
        """
        Whether the DIR's current authorizer email has been verified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._get(
            path_template("/dir/{dir_id}/verify_email", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerificationStatusWrapped,
        )

    async def confirm(
        self,
        dir_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailVerificationStatusWrapped:
        """Submit the 6-digit code that was emailed to the DIR's authorizer email.

        On
        success the authorizer email is marked verified.

        For security, any failure (wrong, expired, already-used, or too many attempts)
        returns the same generic message.

        Args:
          code: The 6-digit code sent to the authorizer email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._post(
            path_template("/dir/{dir_id}/verify_email/confirm", dir_id=dir_id),
            body=await async_maybe_transform({"code": code}, verify_email_confirm_params.VerifyEmailConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailVerificationStatusWrapped,
        )


class VerifyEmailResourceWithRawResponse:
    def __init__(self, verify_email: VerifyEmailResource) -> None:
        self._verify_email = verify_email

        self.create = to_raw_response_wrapper(
            verify_email.create,
        )
        self.list = to_raw_response_wrapper(
            verify_email.list,
        )
        self.confirm = to_raw_response_wrapper(
            verify_email.confirm,
        )


class AsyncVerifyEmailResourceWithRawResponse:
    def __init__(self, verify_email: AsyncVerifyEmailResource) -> None:
        self._verify_email = verify_email

        self.create = async_to_raw_response_wrapper(
            verify_email.create,
        )
        self.list = async_to_raw_response_wrapper(
            verify_email.list,
        )
        self.confirm = async_to_raw_response_wrapper(
            verify_email.confirm,
        )


class VerifyEmailResourceWithStreamingResponse:
    def __init__(self, verify_email: VerifyEmailResource) -> None:
        self._verify_email = verify_email

        self.create = to_streamed_response_wrapper(
            verify_email.create,
        )
        self.list = to_streamed_response_wrapper(
            verify_email.list,
        )
        self.confirm = to_streamed_response_wrapper(
            verify_email.confirm,
        )


class AsyncVerifyEmailResourceWithStreamingResponse:
    def __init__(self, verify_email: AsyncVerifyEmailResource) -> None:
        self._verify_email = verify_email

        self.create = async_to_streamed_response_wrapper(
            verify_email.create,
        )
        self.list = async_to_streamed_response_wrapper(
            verify_email.list,
        )
        self.confirm = async_to_streamed_response_wrapper(
            verify_email.confirm,
        )
