# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .labels import (
    LabelsResource,
    AsyncLabelsResource,
    LabelsResourceWithRawResponse,
    AsyncLabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
    AsyncLabelsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncEmailBracketCursorPagination, AsyncEmailBracketCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_inboxes import thread_list_params, thread_retrieve_params
from ....types.email_inboxes.inbound_thread import InboundThread
from ....types.email_inboxes.thread_retrieve_response import ThreadRetrieveResponse

__all__ = ["ThreadsResource", "AsyncThreadsResource"]


class ThreadsResource(SyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def labels(self) -> LabelsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return LabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ThreadsResourceWithStreamingResponse(self)

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
    ) -> ThreadRetrieveResponse:
        """
        Returns a bounded page of inbound and outbound thread messages interleaved in
        chronological order using stable cursor pagination.

        Args:
          page_after: Opaque message cursor returned by the previous thread-detail page.

          page_size: Number of thread messages to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            path_template("/email_inboxes/{inbox_id}/threads/{thread_id}", inbox_id=inbox_id, thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    thread_retrieve_params.ThreadRetrieveParams,
                ),
            ),
            cast_to=ThreadRetrieveResponse,
        )

    def list(
        self,
        inbox_id: str,
        *,
        filter_label: str | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEmailBracketCursorPagination[InboundThread]:
        """
        Lists thread summaries newest first using stable cursor pagination.

        Args:
          filter_label: Returns only threads carrying this label. Thread labels are independent of the
              labels on the thread's messages.

          page_after: Opaque cursor returned by the previous page.

          page_size: Number of results to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._get_api_list(
            path_template("/email_inboxes/{inbox_id}/threads", inbox_id=inbox_id),
            page=SyncEmailBracketCursorPagination[InboundThread],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_label": filter_label,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    thread_list_params.ThreadListParams,
                ),
            ),
            model=InboundThread,
        )


class AsyncThreadsResource(AsyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncLabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncThreadsResourceWithStreamingResponse(self)

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
    ) -> ThreadRetrieveResponse:
        """
        Returns a bounded page of inbound and outbound thread messages interleaved in
        chronological order using stable cursor pagination.

        Args:
          page_after: Opaque message cursor returned by the previous thread-detail page.

          page_size: Number of thread messages to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            path_template("/email_inboxes/{inbox_id}/threads/{thread_id}", inbox_id=inbox_id, thread_id=thread_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    thread_retrieve_params.ThreadRetrieveParams,
                ),
            ),
            cast_to=ThreadRetrieveResponse,
        )

    def list(
        self,
        inbox_id: str,
        *,
        filter_label: str | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InboundThread, AsyncEmailBracketCursorPagination[InboundThread]]:
        """
        Lists thread summaries newest first using stable cursor pagination.

        Args:
          filter_label: Returns only threads carrying this label. Thread labels are independent of the
              labels on the thread's messages.

          page_after: Opaque cursor returned by the previous page.

          page_size: Number of results to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._get_api_list(
            path_template("/email_inboxes/{inbox_id}/threads", inbox_id=inbox_id),
            page=AsyncEmailBracketCursorPagination[InboundThread],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_label": filter_label,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    thread_list_params.ThreadListParams,
                ),
            ),
            model=InboundThread,
        )


class ThreadsResourceWithRawResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.retrieve = to_raw_response_wrapper(
            threads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            threads.list,
        )

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return LabelsResourceWithRawResponse(self._threads.labels)


class AsyncThreadsResourceWithRawResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.retrieve = async_to_raw_response_wrapper(
            threads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            threads.list,
        )

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncLabelsResourceWithRawResponse(self._threads.labels)


class ThreadsResourceWithStreamingResponse:
    def __init__(self, threads: ThreadsResource) -> None:
        self._threads = threads

        self.retrieve = to_streamed_response_wrapper(
            threads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            threads.list,
        )

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return LabelsResourceWithStreamingResponse(self._threads.labels)


class AsyncThreadsResourceWithStreamingResponse:
    def __init__(self, threads: AsyncThreadsResource) -> None:
        self._threads = threads

        self.retrieve = async_to_streamed_response_wrapper(
            threads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            threads.list,
        )

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncLabelsResourceWithStreamingResponse(self._threads.labels)
