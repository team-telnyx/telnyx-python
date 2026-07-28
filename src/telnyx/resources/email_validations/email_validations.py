# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import email_validation_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.email_validation_create_response import EmailValidationCreateResponse

__all__ = ["EmailValidationsResource", "AsyncEmailValidationsResource"]


class EmailValidationsResource(SyncAPIResource):
    """Validate email addresses synchronously or in asynchronous batches."""

    @cached_property
    def batch(self) -> BatchResource:
        """Validate email addresses synchronously or in asynchronous batches."""
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailValidationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailValidationCreateResponse:
        """
        Validates a single email address and returns deliverability checks.

        Args:
          email: Email address to validate. Any non-empty string is accepted; invalid syntax
              returns valid=false rather than a request error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/email_validations",
            body=maybe_transform({"email": email}, email_validation_create_params.EmailValidationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailValidationCreateResponse,
        )


class AsyncEmailValidationsResource(AsyncAPIResource):
    """Validate email addresses synchronously or in asynchronous batches."""

    @cached_property
    def batch(self) -> AsyncBatchResource:
        """Validate email addresses synchronously or in asynchronous batches."""
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailValidationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailValidationCreateResponse:
        """
        Validates a single email address and returns deliverability checks.

        Args:
          email: Email address to validate. Any non-empty string is accepted; invalid syntax
              returns valid=false rather than a request error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/email_validations",
            body=await async_maybe_transform(
                {"email": email}, email_validation_create_params.EmailValidationCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailValidationCreateResponse,
        )


class EmailValidationsResourceWithRawResponse:
    def __init__(self, email_validations: EmailValidationsResource) -> None:
        self._email_validations = email_validations

        self.create = to_raw_response_wrapper(
            email_validations.create,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        """Validate email addresses synchronously or in asynchronous batches."""
        return BatchResourceWithRawResponse(self._email_validations.batch)


class AsyncEmailValidationsResourceWithRawResponse:
    def __init__(self, email_validations: AsyncEmailValidationsResource) -> None:
        self._email_validations = email_validations

        self.create = async_to_raw_response_wrapper(
            email_validations.create,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        """Validate email addresses synchronously or in asynchronous batches."""
        return AsyncBatchResourceWithRawResponse(self._email_validations.batch)


class EmailValidationsResourceWithStreamingResponse:
    def __init__(self, email_validations: EmailValidationsResource) -> None:
        self._email_validations = email_validations

        self.create = to_streamed_response_wrapper(
            email_validations.create,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        """Validate email addresses synchronously or in asynchronous batches."""
        return BatchResourceWithStreamingResponse(self._email_validations.batch)


class AsyncEmailValidationsResourceWithStreamingResponse:
    def __init__(self, email_validations: AsyncEmailValidationsResource) -> None:
        self._email_validations = email_validations

        self.create = async_to_streamed_response_wrapper(
            email_validations.create,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        """Validate email addresses synchronously or in asynchronous batches."""
        return AsyncBatchResourceWithStreamingResponse(self._email_validations.batch)
