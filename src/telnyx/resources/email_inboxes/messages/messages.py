# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .labels import (
    LabelsResource,
    AsyncLabelsResource,
    LabelsResourceWithRawResponse,
    AsyncLabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
    AsyncLabelsResourceWithStreamingResponse,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.email_inboxes import message_list_params, message_drafts_params, message_update_params
from ....types.email_address_input_param import EmailAddressInputParam
from ....types.email_inboxes.email_draft_response import EmailDraftResponse
from ....types.email_inboxes.message_list_response import MessageListResponse
from ....types.email_inboxes.message_update_response import MessageUpdateResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return ActionsResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return LabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def update(
        self,
        message_id: str,
        *,
        inbox_id: str,
        read_at: Union[Optional[Literal[True]], Union[str, datetime]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """Updates the explicit read state of an account-scoped inbound message.

        Set
        `read_at` to `true` to mark the message read at the server's current time, to an
        ISO 8601 timestamp to use that timestamp, or to `null` to mark the message
        unread. Repeating the same update is idempotent.

        Args:
          read_at: Set to `true` for server time, an ISO 8601 timestamp for an explicit read time,
              or `null` to mark unread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._patch(
            path_template("/email_inboxes/{inbox_id}/messages/{message_id}", inbox_id=inbox_id, message_id=message_id),
            body=maybe_transform({"read_at": read_at}, message_update_params.MessageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    def list(
        self,
        inbox_id: str,
        *,
        filter_from: str | Omit = omit,
        filter_label: str | Omit = omit,
        filter_read: bool | Omit = omit,
        filter_received_after: Union[str, datetime] | Omit = omit,
        filter_received_before: Union[str, datetime] | Omit = omit,
        filter_search: str | Omit = omit,
        filter_subject: str | Omit = omit,
        filter_unread: bool | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """Lists inbound messages newest first.

        All access is scoped to the authenticated
        account. `filter[search]` performs PostgreSQL full-text search over the subject,
        plain-text body, and HTML body. Filters compose with stable cursor pagination.

        Args:
          filter_from: Case-insensitive literal substring of the sender address.

          filter_label: Returns only messages carrying this label. Matching is exact and case-sensitive.
              Reserved `telnyx:` labels can be filtered on even though they cannot be written
              by customers.

          filter_read: Whether the message has a read timestamp.

          filter_received_after: Inclusive ISO 8601 lower bound for the received timestamp.

          filter_received_before: Inclusive ISO 8601 upper bound for the received timestamp.

          filter_search: Full-text query over subject and body, up to 500 characters.

          filter_subject: Case-insensitive literal substring of the subject.

          filter_unread: Whether the message has no read timestamp. Set to `true` to return only unread
              messages.

          page_after: Opaque cursor returned by the previous page.

          page_size: Number of results to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._get(
            path_template("/email_inboxes/{inbox_id}/messages", inbox_id=inbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_from": filter_from,
                        "filter_label": filter_label,
                        "filter_read": filter_read,
                        "filter_received_after": filter_received_after,
                        "filter_received_before": filter_received_before,
                        "filter_search": filter_search,
                        "filter_subject": filter_subject,
                        "filter_unread": filter_unread,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def drafts(
        self,
        message_id: str,
        *,
        inbox_id: str,
        attachments: Iterable[object] | Omit = omit,
        bcc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        cc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        from_email: str | Omit = omit,
        from_name: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        html_body: str | Omit = omit,
        labels: SequenceNotStr[str] | Omit = omit,
        metadata: object | Omit = omit,
        reply_to: str | Omit = omit,
        subject: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        text: str | Omit = omit,
        text_body: str | Omit = omit,
        to: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDraftResponse:
        """Creates an unsent reply draft for an inbound message.

        Unlike the
        `/actions/reply` endpoint, which sends immediately, this stores a draft that can
        be reviewed and edited before sending.

        `reply_to_message_id` and `thread_id` are inherited from the parent message and
        cannot be set by the caller. The recipient, `Re:` subject and
        `In-Reply-To`/`References` headers are pre-filled from the parent using the same
        rules as a live reply, so sending the draft threads identically. Supplying `to`
        or `subject` explicitly overrides the pre-filled value.

        Args:
          html: Alias for `html_body`, matching the send endpoint.

          text: Alias for `text_body`, matching the send endpoint.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/drafts", inbox_id=inbox_id, message_id=message_id
            ),
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_email": from_email,
                    "from_name": from_name,
                    "headers": headers,
                    "html": html,
                    "html_body": html_body,
                    "labels": labels,
                    "metadata": metadata,
                    "reply_to": reply_to,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "text_body": text_body,
                    "to": to,
                },
                message_drafts_params.MessageDraftsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncActionsResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncLabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def update(
        self,
        message_id: str,
        *,
        inbox_id: str,
        read_at: Union[Optional[Literal[True]], Union[str, datetime]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """Updates the explicit read state of an account-scoped inbound message.

        Set
        `read_at` to `true` to mark the message read at the server's current time, to an
        ISO 8601 timestamp to use that timestamp, or to `null` to mark the message
        unread. Repeating the same update is idempotent.

        Args:
          read_at: Set to `true` for server time, an ISO 8601 timestamp for an explicit read time,
              or `null` to mark unread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._patch(
            path_template("/email_inboxes/{inbox_id}/messages/{message_id}", inbox_id=inbox_id, message_id=message_id),
            body=await async_maybe_transform({"read_at": read_at}, message_update_params.MessageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    async def list(
        self,
        inbox_id: str,
        *,
        filter_from: str | Omit = omit,
        filter_label: str | Omit = omit,
        filter_read: bool | Omit = omit,
        filter_received_after: Union[str, datetime] | Omit = omit,
        filter_received_before: Union[str, datetime] | Omit = omit,
        filter_search: str | Omit = omit,
        filter_subject: str | Omit = omit,
        filter_unread: bool | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """Lists inbound messages newest first.

        All access is scoped to the authenticated
        account. `filter[search]` performs PostgreSQL full-text search over the subject,
        plain-text body, and HTML body. Filters compose with stable cursor pagination.

        Args:
          filter_from: Case-insensitive literal substring of the sender address.

          filter_label: Returns only messages carrying this label. Matching is exact and case-sensitive.
              Reserved `telnyx:` labels can be filtered on even though they cannot be written
              by customers.

          filter_read: Whether the message has a read timestamp.

          filter_received_after: Inclusive ISO 8601 lower bound for the received timestamp.

          filter_received_before: Inclusive ISO 8601 upper bound for the received timestamp.

          filter_search: Full-text query over subject and body, up to 500 characters.

          filter_subject: Case-insensitive literal substring of the subject.

          filter_unread: Whether the message has no read timestamp. Set to `true` to return only unread
              messages.

          page_after: Opaque cursor returned by the previous page.

          page_size: Number of results to return. Defaults to 25; maximum is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return await self._get(
            path_template("/email_inboxes/{inbox_id}/messages", inbox_id=inbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_from": filter_from,
                        "filter_label": filter_label,
                        "filter_read": filter_read,
                        "filter_received_after": filter_received_after,
                        "filter_received_before": filter_received_before,
                        "filter_search": filter_search,
                        "filter_subject": filter_subject,
                        "filter_unread": filter_unread,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def drafts(
        self,
        message_id: str,
        *,
        inbox_id: str,
        attachments: Iterable[object] | Omit = omit,
        bcc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        cc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        from_email: str | Omit = omit,
        from_name: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        html_body: str | Omit = omit,
        labels: SequenceNotStr[str] | Omit = omit,
        metadata: object | Omit = omit,
        reply_to: str | Omit = omit,
        subject: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        text: str | Omit = omit,
        text_body: str | Omit = omit,
        to: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDraftResponse:
        """Creates an unsent reply draft for an inbound message.

        Unlike the
        `/actions/reply` endpoint, which sends immediately, this stores a draft that can
        be reviewed and edited before sending.

        `reply_to_message_id` and `thread_id` are inherited from the parent message and
        cannot be set by the caller. The recipient, `Re:` subject and
        `In-Reply-To`/`References` headers are pre-filled from the parent using the same
        rules as a live reply, so sending the draft threads identically. Supplying `to`
        or `subject` explicitly overrides the pre-filled value.

        Args:
          html: Alias for `html_body`, matching the send endpoint.

          text: Alias for `text_body`, matching the send endpoint.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/drafts", inbox_id=inbox_id, message_id=message_id
            ),
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_email": from_email,
                    "from_name": from_name,
                    "headers": headers,
                    "html": html,
                    "html_body": html_body,
                    "labels": labels,
                    "metadata": metadata,
                    "reply_to": reply_to,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "text_body": text_body,
                    "to": to,
                },
                message_drafts_params.MessageDraftsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.drafts = to_raw_response_wrapper(
            messages.drafts,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return ActionsResourceWithRawResponse(self._messages.actions)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return LabelsResourceWithRawResponse(self._messages.labels)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.drafts = async_to_raw_response_wrapper(
            messages.drafts,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncActionsResourceWithRawResponse(self._messages.actions)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncLabelsResourceWithRawResponse(self._messages.labels)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.drafts = to_streamed_response_wrapper(
            messages.drafts,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return ActionsResourceWithStreamingResponse(self._messages.actions)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return LabelsResourceWithStreamingResponse(self._messages.labels)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.drafts = async_to_streamed_response_wrapper(
            messages.drafts,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncActionsResourceWithStreamingResponse(self._messages.actions)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
        """
        return AsyncLabelsResourceWithStreamingResponse(self._messages.labels)
