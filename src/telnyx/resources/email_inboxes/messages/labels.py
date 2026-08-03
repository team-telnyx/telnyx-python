# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.email_inboxes.messages import label_create_params, label_delete_all_params
from ....types.email_inboxes.messages.label_create_response import LabelCreateResponse
from ....types.email_inboxes.messages.label_delete_all_response import LabelDeleteAllResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def create(
        self,
        message_id: str,
        *,
        inbox_id: str,
        labels: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelCreateResponse:
        """Adds one or more mutable labels to a message.

        Labels carry agent workflow state
        such as `spam`, `needs_review`, or `processed`.

        Labels are **not** the same as the send-time `tags` on outbound messages: `tags`
        are immutable and propagate to Email Detail Records and Mission Control for
        billing attribution, while labels are mailbox state that never reaches the
        reporting contract.

        The operation is an idempotent set union — adding a label the message already
        carries is a no-op and still returns 200. Labels are case-sensitive, and message
        labels are independent of thread labels.

        Args:
          labels: One or more labels. Each label is a freeform, case-sensitive string of at most
              255 characters; a message or thread may carry at most 50 labels. The `telnyx:`
              prefix is a reserved system namespace and is rejected on customer writes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template(
                "/email_inboxes/{inbox_id}/messages/{message_id}/labels", inbox_id=inbox_id, message_id=message_id
            ),
            body=maybe_transform({"labels": labels}, label_create_params.LabelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelCreateResponse,
        )

    def delete_all(
        self,
        message_id: str,
        *,
        inbox_id: str,
        labels: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelDeleteAllResponse:
        """Removes one or more labels from a message.

        Idempotent — removing a label the
        message does not carry is a no-op and still returns 200. Removal is
        case-sensitive.

        Args:
          labels: One or more labels. Each label is a freeform, case-sensitive string of at most
              255 characters; a message or thread may carry at most 50 labels. The `telnyx:`
              prefix is a reserved system namespace and is rejected on customer writes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template(
                "/email_inboxes/{inbox_id}/messages/{message_id}/labels", inbox_id=inbox_id, message_id=message_id
            ),
            body=maybe_transform({"labels": labels}, label_delete_all_params.LabelDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelDeleteAllResponse,
        )


class AsyncLabelsResource(AsyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def create(
        self,
        message_id: str,
        *,
        inbox_id: str,
        labels: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelCreateResponse:
        """Adds one or more mutable labels to a message.

        Labels carry agent workflow state
        such as `spam`, `needs_review`, or `processed`.

        Labels are **not** the same as the send-time `tags` on outbound messages: `tags`
        are immutable and propagate to Email Detail Records and Mission Control for
        billing attribution, while labels are mailbox state that never reaches the
        reporting contract.

        The operation is an idempotent set union — adding a label the message already
        carries is a no-op and still returns 200. Labels are case-sensitive, and message
        labels are independent of thread labels.

        Args:
          labels: One or more labels. Each label is a freeform, case-sensitive string of at most
              255 characters; a message or thread may carry at most 50 labels. The `telnyx:`
              prefix is a reserved system namespace and is rejected on customer writes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template(
                "/email_inboxes/{inbox_id}/messages/{message_id}/labels", inbox_id=inbox_id, message_id=message_id
            ),
            body=await async_maybe_transform({"labels": labels}, label_create_params.LabelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelCreateResponse,
        )

    async def delete_all(
        self,
        message_id: str,
        *,
        inbox_id: str,
        labels: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelDeleteAllResponse:
        """Removes one or more labels from a message.

        Idempotent — removing a label the
        message does not carry is a no-op and still returns 200. Removal is
        case-sensitive.

        Args:
          labels: One or more labels. Each label is a freeform, case-sensitive string of at most
              255 characters; a message or thread may carry at most 50 labels. The `telnyx:`
              prefix is a reserved system namespace and is rejected on customer writes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template(
                "/email_inboxes/{inbox_id}/messages/{message_id}/labels", inbox_id=inbox_id, message_id=message_id
            ),
            body=await async_maybe_transform({"labels": labels}, label_delete_all_params.LabelDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelDeleteAllResponse,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_raw_response_wrapper(
            labels.create,
        )
        self.delete_all = to_raw_response_wrapper(
            labels.delete_all,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_raw_response_wrapper(
            labels.create,
        )
        self.delete_all = async_to_raw_response_wrapper(
            labels.delete_all,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_streamed_response_wrapper(
            labels.create,
        )
        self.delete_all = to_streamed_response_wrapper(
            labels.delete_all,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_streamed_response_wrapper(
            labels.create,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            labels.delete_all,
        )
