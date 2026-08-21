# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .drafts import (
    DraftsResource,
    AsyncDraftsResource,
    DraftsResourceWithRawResponse,
    AsyncDraftsResourceWithRawResponse,
    DraftsResourceWithStreamingResponse,
    AsyncDraftsResourceWithStreamingResponse,
)
from ...types import email_inbox_list_params, email_inbox_create_params
from .filters import (
    FiltersResource,
    AsyncFiltersResource,
    FiltersResourceWithRawResponse,
    AsyncFiltersResourceWithRawResponse,
    FiltersResourceWithStreamingResponse,
    AsyncFiltersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncEmailCursorPagination, AsyncEmailCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from .threads.threads import (
    ThreadsResource,
    AsyncThreadsResource,
    ThreadsResourceWithRawResponse,
    AsyncThreadsResourceWithRawResponse,
    ThreadsResourceWithStreamingResponse,
    AsyncThreadsResourceWithStreamingResponse,
)
from .messages.messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...types.email_inbox import EmailInbox
from ...types.email_inbox_response import EmailInboxResponse

__all__ = ["EmailInboxesResource", "AsyncEmailInboxesResource"]


class EmailInboxesResource(SyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def drafts(self) -> DraftsResource:
        """
        Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
        """
        return DraftsResource(self._client)

    @cached_property
    def filters(self) -> FiltersResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return FiltersResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def threads(self) -> ThreadsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return ThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailInboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailInboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailInboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailInboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain_id: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailInboxResponse:
        """Creates an inbox on an inbound-enabled domain.

        When `domain_id` is omitted,
        Telnyx allocates the account's shared inbound subdomain so the inbox is
        immediately usable without customer DNS setup. When `username` is omitted, a
        unique username is generated.

        Args:
          domain_id: Account-owned, inbound-enabled domain UUID. The account's shared inbound
              subdomain is allocated when omitted.

          username: Inbox local part. Trimmed and lowercased before validation; the normalized value
              must be 1-64 characters, start and end with a letter or digit, and contain only
              letters, digits, dots, hyphens, and underscores. Generated when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/email_inboxes",
            body=maybe_transform(
                {
                    "domain_id": domain_id,
                    "username": username,
                },
                email_inbox_create_params.EmailInboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailInboxResponse,
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
    ) -> EmailInboxResponse:
        """Returns an account-scoped, non-deleted inbox.

        Missing and foreign inboxes are
        indistinguishable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_inboxes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailInboxResponse,
        )

    def list(
        self,
        *,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEmailCursorPagination[EmailInbox]:
        """
        Lists the account's non-deleted inboxes newest first using stable cursor
        pagination.

        Args:
          page_cursor: Opaque cursor returned by the previous inbox page.

          page_size: Number of results to return. Defaults to 20; maximum is 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_inboxes",
            page=SyncEmailCursorPagination[EmailInbox],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                    },
                    email_inbox_list_params.EmailInboxListParams,
                ),
            ),
            model=EmailInbox,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-deletes an account-scoped inbox.

        Its address remains reserved and the inbox
        is no longer returned by list or get operations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/email_inboxes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEmailInboxesResource(AsyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def drafts(self) -> AsyncDraftsResource:
        """
        Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
        """
        return AsyncDraftsResource(self._client)

    @cached_property
    def filters(self) -> AsyncFiltersResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncFiltersResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def threads(self) -> AsyncThreadsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncThreadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailInboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailInboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailInboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailInboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain_id: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailInboxResponse:
        """Creates an inbox on an inbound-enabled domain.

        When `domain_id` is omitted,
        Telnyx allocates the account's shared inbound subdomain so the inbox is
        immediately usable without customer DNS setup. When `username` is omitted, a
        unique username is generated.

        Args:
          domain_id: Account-owned, inbound-enabled domain UUID. The account's shared inbound
              subdomain is allocated when omitted.

          username: Inbox local part. Trimmed and lowercased before validation; the normalized value
              must be 1-64 characters, start and end with a letter or digit, and contain only
              letters, digits, dots, hyphens, and underscores. Generated when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/email_inboxes",
            body=await async_maybe_transform(
                {
                    "domain_id": domain_id,
                    "username": username,
                },
                email_inbox_create_params.EmailInboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailInboxResponse,
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
    ) -> EmailInboxResponse:
        """Returns an account-scoped, non-deleted inbox.

        Missing and foreign inboxes are
        indistinguishable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_inboxes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailInboxResponse,
        )

    def list(
        self,
        *,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailInbox, AsyncEmailCursorPagination[EmailInbox]]:
        """
        Lists the account's non-deleted inboxes newest first using stable cursor
        pagination.

        Args:
          page_cursor: Opaque cursor returned by the previous inbox page.

          page_size: Number of results to return. Defaults to 20; maximum is 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_inboxes",
            page=AsyncEmailCursorPagination[EmailInbox],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                    },
                    email_inbox_list_params.EmailInboxListParams,
                ),
            ),
            model=EmailInbox,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-deletes an account-scoped inbox.

        Its address remains reserved and the inbox
        is no longer returned by list or get operations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/email_inboxes/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EmailInboxesResourceWithRawResponse:
    def __init__(self, email_inboxes: EmailInboxesResource) -> None:
        self._email_inboxes = email_inboxes

        self.create = to_raw_response_wrapper(
            email_inboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_inboxes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            email_inboxes.list,
        )
        self.delete = to_raw_response_wrapper(
            email_inboxes.delete,
        )

    @cached_property
    def drafts(self) -> DraftsResourceWithRawResponse:
        """
        Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
        """
        return DraftsResourceWithRawResponse(self._email_inboxes.drafts)

    @cached_property
    def filters(self) -> FiltersResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return FiltersResourceWithRawResponse(self._email_inboxes.filters)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._email_inboxes.messages)

    @cached_property
    def threads(self) -> ThreadsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return ThreadsResourceWithRawResponse(self._email_inboxes.threads)


class AsyncEmailInboxesResourceWithRawResponse:
    def __init__(self, email_inboxes: AsyncEmailInboxesResource) -> None:
        self._email_inboxes = email_inboxes

        self.create = async_to_raw_response_wrapper(
            email_inboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_inboxes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            email_inboxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_inboxes.delete,
        )

    @cached_property
    def drafts(self) -> AsyncDraftsResourceWithRawResponse:
        """
        Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
        """
        return AsyncDraftsResourceWithRawResponse(self._email_inboxes.drafts)

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncFiltersResourceWithRawResponse(self._email_inboxes.filters)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._email_inboxes.messages)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncThreadsResourceWithRawResponse(self._email_inboxes.threads)


class EmailInboxesResourceWithStreamingResponse:
    def __init__(self, email_inboxes: EmailInboxesResource) -> None:
        self._email_inboxes = email_inboxes

        self.create = to_streamed_response_wrapper(
            email_inboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_inboxes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            email_inboxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_inboxes.delete,
        )

    @cached_property
    def drafts(self) -> DraftsResourceWithStreamingResponse:
        """
        Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
        """
        return DraftsResourceWithStreamingResponse(self._email_inboxes.drafts)

    @cached_property
    def filters(self) -> FiltersResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return FiltersResourceWithStreamingResponse(self._email_inboxes.filters)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._email_inboxes.messages)

    @cached_property
    def threads(self) -> ThreadsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return ThreadsResourceWithStreamingResponse(self._email_inboxes.threads)


class AsyncEmailInboxesResourceWithStreamingResponse:
    def __init__(self, email_inboxes: AsyncEmailInboxesResource) -> None:
        self._email_inboxes = email_inboxes

        self.create = async_to_streamed_response_wrapper(
            email_inboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_inboxes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            email_inboxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_inboxes.delete,
        )

    @cached_property
    def drafts(self) -> AsyncDraftsResourceWithStreamingResponse:
        """
        Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
        """
        return AsyncDraftsResourceWithStreamingResponse(self._email_inboxes.drafts)

    @cached_property
    def filters(self) -> AsyncFiltersResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncFiltersResourceWithStreamingResponse(self._email_inboxes.filters)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._email_inboxes.messages)

    @cached_property
    def threads(self) -> AsyncThreadsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncThreadsResourceWithStreamingResponse(self._email_inboxes.threads)
