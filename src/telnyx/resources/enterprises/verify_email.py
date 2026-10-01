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
from ..._base_client import make_request_options
from ...types.enterprises import verify_email_confirm_params
from ...types.enterprises.enterprise_email_verification_status_wrapped import EnterpriseEmailVerificationStatusWrapped

__all__ = ["VerifyEmailResource", "AsyncVerifyEmailResource"]


class VerifyEmailResource(SyncAPIResource):
    """Verify ownership of a DIR's authorizer email.

    A short code is emailed and confirmed; the email must be verified before references can be submitted.
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
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseEmailVerificationStatusWrapped:
        """
        Email a 6-digit code to the enterprise account's contact email to confirm
        ownership of that address.

        A BPO (Business Process Outsourcer) account has no DIR, so it proves ownership
        of its own contact email here rather than through a DIR. A BPO account cannot be
        approved for use until this contact email is verified.

        The code expires in 15 minutes. Requesting a new code invalidates any previous
        one. Resends are rate limited (a short cooldown plus a daily cap). Submit the
        code to `POST /enterprises/{enterprise_id}/verify_email/confirm`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/verify_email", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseEmailVerificationStatusWrapped,
        )

    def confirm(
        self,
        enterprise_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseEmailVerificationStatusWrapped:
        """
        Submit the 6-digit code that was emailed to the enterprise account's contact
        email. On success the contact email is marked verified.

        For security, any failure (wrong, expired, already-used, or too many attempts)
        returns the same generic message.

        Args:
          code: The 6-digit code sent to the enterprise account's contact email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/verify_email/confirm", enterprise_id=enterprise_id),
            body=maybe_transform({"code": code}, verify_email_confirm_params.VerifyEmailConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseEmailVerificationStatusWrapped,
        )


class AsyncVerifyEmailResource(AsyncAPIResource):
    """Verify ownership of a DIR's authorizer email.

    A short code is emailed and confirmed; the email must be verified before references can be submitted.
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
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseEmailVerificationStatusWrapped:
        """
        Email a 6-digit code to the enterprise account's contact email to confirm
        ownership of that address.

        A BPO (Business Process Outsourcer) account has no DIR, so it proves ownership
        of its own contact email here rather than through a DIR. A BPO account cannot be
        approved for use until this contact email is verified.

        The code expires in 15 minutes. Requesting a new code invalidates any previous
        one. Resends are rate limited (a short cooldown plus a daily cap). Submit the
        code to `POST /enterprises/{enterprise_id}/verify_email/confirm`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/verify_email", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseEmailVerificationStatusWrapped,
        )

    async def confirm(
        self,
        enterprise_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseEmailVerificationStatusWrapped:
        """
        Submit the 6-digit code that was emailed to the enterprise account's contact
        email. On success the contact email is marked verified.

        For security, any failure (wrong, expired, already-used, or too many attempts)
        returns the same generic message.

        Args:
          code: The 6-digit code sent to the enterprise account's contact email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/verify_email/confirm", enterprise_id=enterprise_id),
            body=await async_maybe_transform({"code": code}, verify_email_confirm_params.VerifyEmailConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseEmailVerificationStatusWrapped,
        )


class VerifyEmailResourceWithRawResponse:
    def __init__(self, verify_email: VerifyEmailResource) -> None:
        self._verify_email = verify_email

        self.create = to_raw_response_wrapper(
            verify_email.create,
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
        self.confirm = async_to_raw_response_wrapper(
            verify_email.confirm,
        )


class VerifyEmailResourceWithStreamingResponse:
    def __init__(self, verify_email: VerifyEmailResource) -> None:
        self._verify_email = verify_email

        self.create = to_streamed_response_wrapper(
            verify_email.create,
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
        self.confirm = async_to_streamed_response_wrapper(
            verify_email.confirm,
        )
