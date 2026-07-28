# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import email_thread_list_params, email_thread_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.email_thread_retrieve_response import EmailThreadRetrieveResponse
from ..types.email_inboxes.inbound_thread_list_response import InboundThreadListResponse

__all__ = ["EmailThreadsResource", "AsyncEmailThreadsResource"]


class EmailThreadsResource(SyncAPIResource):
    """
    Account-wide conversation threads across every inbox, for agents operating many inboxes at once.
    """

    @cached_property
    def with_raw_response(self) -> EmailThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailThreadsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        thread_id: str,
        *,
        inbox_id: str,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailThreadRetrieveResponse:
        """
        Returns a thread and a bounded page of its inbound and outbound messages,
        interleaved in chronological order. The `inbox_id` returned by the list endpoint
        is required because a thread ID can occur in multiple inboxes. Only messages
        matching that `(inbox_id, thread_id)` pair are returned. Threads outside the
        account return an opaque 404.

        Args:
          inbox_id: Inbox UUID that, together with `thread_id`, identifies the thread.

          page_after: Opaque message cursor returned by the previous thread-detail page.

          page_size: Number of thread messages to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/email_threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "inbox_id": inbox_id,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    email_thread_retrieve_params.EmailThreadRetrieveParams,
                ),
            ),
            cast_to=EmailThreadRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_inbox_id: SequenceNotStr[str] | Omit = omit,
        filter_label: str | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundThreadListResponse:
        """
        Lists thread summaries for the whole account, newest first, using stable cursor
        pagination. An agent operating many inboxes gets every conversation in one call
        instead of one call per inbox. Each thread carries its own `inbox_id` so a reply
        can be routed back to the right inbox. Use `filter[inbox_id]` (repeatable) to
        narrow the result to specific inboxes. Because a thread ID can be delivered to
        multiple inboxes, each result is identified by its `(inbox_id, id)` pair.

        Args:
          filter_inbox_id: Restrict results to one or more inboxes. Repeat the parameter
              (`filter[inbox_id][]=...&filter[inbox_id][]=...`) or pass a comma-separated
              list. Omit to list every inbox in the account. Inboxes outside the account are
              silently excluded. If the filter is present, it must contain at least one
              non-empty UUID.

          filter_label: Returns only threads carrying this label. Matching is exact and case-sensitive.
              Thread labels are independent of the labels on the thread's messages.

          page_after: Opaque cursor returned by the previous page.

          page_size: Number of results to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/email_threads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_inbox_id": filter_inbox_id,
                        "filter_label": filter_label,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    email_thread_list_params.EmailThreadListParams,
                ),
            ),
            cast_to=InboundThreadListResponse,
        )


class AsyncEmailThreadsResource(AsyncAPIResource):
    """
    Account-wide conversation threads across every inbox, for agents operating many inboxes at once.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEmailThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailThreadsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        thread_id: str,
        *,
        inbox_id: str,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailThreadRetrieveResponse:
        """
        Returns a thread and a bounded page of its inbound and outbound messages,
        interleaved in chronological order. The `inbox_id` returned by the list endpoint
        is required because a thread ID can occur in multiple inboxes. Only messages
        matching that `(inbox_id, thread_id)` pair are returned. Threads outside the
        account return an opaque 404.

        Args:
          inbox_id: Inbox UUID that, together with `thread_id`, identifies the thread.

          page_after: Opaque message cursor returned by the previous thread-detail page.

          page_size: Number of thread messages to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/email_threads/{thread_id}", thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "inbox_id": inbox_id,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    email_thread_retrieve_params.EmailThreadRetrieveParams,
                ),
            ),
            cast_to=EmailThreadRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter_inbox_id: SequenceNotStr[str] | Omit = omit,
        filter_label: str | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundThreadListResponse:
        """
        Lists thread summaries for the whole account, newest first, using stable cursor
        pagination. An agent operating many inboxes gets every conversation in one call
        instead of one call per inbox. Each thread carries its own `inbox_id` so a reply
        can be routed back to the right inbox. Use `filter[inbox_id]` (repeatable) to
        narrow the result to specific inboxes. Because a thread ID can be delivered to
        multiple inboxes, each result is identified by its `(inbox_id, id)` pair.

        Args:
          filter_inbox_id: Restrict results to one or more inboxes. Repeat the parameter
              (`filter[inbox_id][]=...&filter[inbox_id][]=...`) or pass a comma-separated
              list. Omit to list every inbox in the account. Inboxes outside the account are
              silently excluded. If the filter is present, it must contain at least one
              non-empty UUID.

          filter_label: Returns only threads carrying this label. Matching is exact and case-sensitive.
              Thread labels are independent of the labels on the thread's messages.

          page_after: Opaque cursor returned by the previous page.

          page_size: Number of results to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/email_threads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_inbox_id": filter_inbox_id,
                        "filter_label": filter_label,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    email_thread_list_params.EmailThreadListParams,
                ),
            ),
            cast_to=InboundThreadListResponse,
        )


class EmailThreadsResourceWithRawResponse:
    def __init__(self, email_threads: EmailThreadsResource) -> None:
        self._email_threads = email_threads

        self.retrieve = to_raw_response_wrapper(
            email_threads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            email_threads.list,
        )


class AsyncEmailThreadsResourceWithRawResponse:
    def __init__(self, email_threads: AsyncEmailThreadsResource) -> None:
        self._email_threads = email_threads

        self.retrieve = async_to_raw_response_wrapper(
            email_threads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            email_threads.list,
        )


class EmailThreadsResourceWithStreamingResponse:
    def __init__(self, email_threads: EmailThreadsResource) -> None:
        self._email_threads = email_threads

        self.retrieve = to_streamed_response_wrapper(
            email_threads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            email_threads.list,
        )


class AsyncEmailThreadsResourceWithStreamingResponse:
    def __init__(self, email_threads: AsyncEmailThreadsResource) -> None:
        self._email_threads = email_threads

        self.retrieve = async_to_streamed_response_wrapper(
            email_threads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            email_threads.list,
        )
