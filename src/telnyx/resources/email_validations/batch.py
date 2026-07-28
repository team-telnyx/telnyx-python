# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.email_validations import batch_create_params
from ...types.email_validations.batch_create_response import BatchCreateResponse
from ...types.email_validations.batch_retrieve_response import BatchRetrieveResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    """Validate email addresses synchronously or in asynchronous batches."""

    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        emails: SequenceNotStr[str],
        webhook_url: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCreateResponse:
        """
        Creates an asynchronous batch validation job for up to 1,000 email addresses.

        Args:
          webhook_url: URL for batch completion webhook. Empty string is treated as omitted.
              SSRF-protected; private/reserved IPs and internal hostnames are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/email_validations/batch",
            body=maybe_transform(
                {
                    "emails": emails,
                    "webhook_url": webhook_url,
                },
                batch_create_params.BatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCreateResponse,
        )

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
    ) -> BatchRetrieveResponse:
        """
        Retrieves the current status and, once completed, validation results for a batch
        job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_validations/batch/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchRetrieveResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    """Validate email addresses synchronously or in asynchronous batches."""

    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        emails: SequenceNotStr[str],
        webhook_url: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCreateResponse:
        """
        Creates an asynchronous batch validation job for up to 1,000 email addresses.

        Args:
          webhook_url: URL for batch completion webhook. Empty string is treated as omitted.
              SSRF-protected; private/reserved IPs and internal hostnames are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/email_validations/batch",
            body=await async_maybe_transform(
                {
                    "emails": emails,
                    "webhook_url": webhook_url,
                },
                batch_create_params.BatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCreateResponse,
        )

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
    ) -> BatchRetrieveResponse:
        """
        Retrieves the current status and, once completed, validation results for a batch
        job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_validations/batch/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchRetrieveResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.retrieve = to_raw_response_wrapper(
            batch.retrieve,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            batch.retrieve,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            batch.retrieve,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            batch.retrieve,
        )
