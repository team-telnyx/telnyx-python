# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime

import httpx

from ...types import (
    email_message_list_params,
    email_message_batch_params,
    email_message_create_params,
    email_message_delete_all_params,
    email_message_retrieve_events_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from .recipients import (
    RecipientsResource,
    AsyncRecipientsResource,
    RecipientsResourceWithRawResponse,
    AsyncRecipientsResourceWithRawResponse,
    RecipientsResourceWithStreamingResponse,
    AsyncRecipientsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncEmailCursorPagination, AsyncEmailCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message_event import MessageEvent
from ...types.tracking_settings_param import TrackingSettingsParam
from ...types.attachment_request_param import AttachmentRequestParam
from ...types.email_address_input_param import EmailAddressInputParam
from ...types.email_inboxes.email_message import EmailMessage
from ...types.email_message_batch_response import EmailMessageBatchResponse
from ...types.email_message_retrieve_response import EmailMessageRetrieveResponse
from ...types.email_inboxes.email_message_response import EmailMessageResponse

__all__ = ["EmailMessagesResource", "AsyncEmailMessagesResource"]


class EmailMessagesResource(SyncAPIResource):
    """Send and manage email messages.

    Legacy `/v2/emails` routes are aliases for these endpoints.
    """

    @cached_property
    def recipients(self) -> RecipientsResource:
        """Send and manage email messages.

        Legacy `/v2/emails` routes are aliases for these endpoints.
        """
        return RecipientsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailMessagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: EmailAddressInputParam,
        to: SequenceNotStr[EmailAddressInputParam],
        attachments: Iterable[AttachmentRequestParam] | Omit = omit,
        bcc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        cc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        forward_of_message_id: Optional[str] | Omit = omit,
        from_name: str | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html_body: str | Omit = omit,
        ignore_suppression: bool | Omit = omit,
        in_reply_to_message_id: Optional[str] | Omit = omit,
        inline_css: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        reply_to: EmailAddressInputParam | Omit = omit,
        reply_to_all: Optional[bool] | Omit = omit,
        sandbox_mode: bool | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        send_at: Union[str, datetime] | Omit = omit,
        subject: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        template_id: str | Omit = omit,
        template_variables: Dict[str, object] | Omit = omit,
        text_body: str | Omit = omit,
        tracking_settings: TrackingSettingsParam | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Queues, schedules, or sandbox-sends an email message.

        The legacy `/v2/emails`
        POST route is a backward-compatible alias for this operation.

        `subject` is required unless `template_id` is supplied. When using
        `template_id`, do not also provide `subject`, `html_body`, or `text_body`; the
        template is rendered with `template_variables`.

        Note: template lookup failures (not found, wrong account) return 400, not 404.

        Args:
          forward_of_message_id: Telnyx message UUID of the message this send forwards. Forwarded messages start
              a NEW thread per RFC 5322 — NO `In-Reply-To` or `References` headers are set on
              the outbound MIME. The id is recorded in the message's metadata for EDR
              provenance only.

              The id is validated as a UUID but is NOT looked up against the message store —
              existence is the caller's responsibility (the forward is pure metadata; it does
              not affect delivery). Cannot be combined with `in_reply_to_message_id` (422).

          from_name: Optional display name for string `from`; overrides `from.name` when provided.

          group_id: Optional unsubscribe-group UUID used for group-scoped suppression checks and
              unsubscribe handling.

          headers: Custom email headers. Write-only; not returned in responses.

          html_body: HTML email body. Returned only by `GET /email_messages/{id}`; omitted from
              create and list responses.

          ignore_suppression: When true, allows delivery to recipients whose suppressions explicitly permit an
              override. Hard bounces, spam complaints, and invalid-address suppressions cannot
              be overridden. Requires the `email:override` API scope.

          in_reply_to_message_id: Telnyx message UUID of the message this send replies to. When provided, the API
              sets RFC 5322 `In-Reply-To` and `References` headers on the outbound MIME so the
              recipient's mailbox (Gmail/Outlook) threads it correctly. The parent is looked
              up under the caller's account scope; a UUID belonging to another account yields
              a non-enumerating 404.

              Wire-only (Phase 1): the API sets the headers and does NOT resolve or mutate
              `thread_id` on the server side. Messages sent without this parameter are
              standalone (no threading headers injected).

              Cannot be combined with `forward_of_message_id` (422).

          metadata: Custom metadata. Write-only; not returned in responses.

          reply_to: Reply-to address. If provided as an object with a name, only the email is
              stored; the name is ignored.

          reply_to_all: Indicates a reply-all intent. In Phase 1 (wire-only) this does not change the
              threading headers — recipient selection is customer- controlled (`to`/`cc`), and
              a thread is not defined by its audience. When the referenced message has no
              thread context, reply-all degrades to a plain reply (parent ID only in
              `References`). The resolution engine (separate work) will expand the ancestor
              chain at a later phase with no API change.

              Only meaningful alongside `in_reply_to_message_id`.

          scheduled_at: Future ISO 8601 time to schedule sending. Invalid or past timestamps are
              silently ignored and the email is sent immediately. The legacy alias `send_at`
              is still accepted for backward compatibility; when both are provided,
              `scheduled_at` wins.

          send_at: Deprecated alias for `scheduled_at`.

          subject: Required unless `template_id` is supplied. When using a template, the template's
              subject is rendered; if the template has no subject or renders empty, the
              request returns 400.

          tags: Tags for categorization and reporting. Stored on the message and propagated to
              Email Detail Records. Not returned in API responses.

          template_variables: Variables for Liquid template rendering. Non-object values may cause a 422
              validation error on message creation, but are silently treated as an empty
              object for template rendering.

          text_body: Plain text email body. Returned only by `GET /email_messages/{id}`; omitted from
              create and list responses.

          tracking_settings: Per-send open and click tracking overrides. Omitted properties inherit the
              sender domain's tracking settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/email_messages",
            body=maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "forward_of_message_id": forward_of_message_id,
                    "from_name": from_name,
                    "group_id": group_id,
                    "headers": headers,
                    "html_body": html_body,
                    "ignore_suppression": ignore_suppression,
                    "in_reply_to_message_id": in_reply_to_message_id,
                    "inline_css": inline_css,
                    "metadata": metadata,
                    "reply_to": reply_to,
                    "reply_to_all": reply_to_all,
                    "sandbox_mode": sandbox_mode,
                    "scheduled_at": scheduled_at,
                    "send_at": send_at,
                    "subject": subject,
                    "tags": tags,
                    "template_id": template_id,
                    "template_variables": template_variables,
                    "text_body": text_body,
                    "tracking_settings": tracking_settings,
                },
                email_message_create_params.EmailMessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
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
    ) -> EmailMessageRetrieveResponse:
        """
        The legacy `/v2/emails/{id}` GET route is a backward-compatible alias for this
        operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_messages/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageRetrieveResponse,
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
    ) -> SyncEmailCursorPagination[EmailMessage]:
        """Lists messages sorted newest first by `created_at desc, id desc`.

        No filters
        other than cursor pagination are implemented. The legacy `/v2/emails` GET route
        is a backward-compatible alias for this operation.

        Args:
          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_messages",
            page=SyncEmailCursorPagination[EmailMessage],
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
                    email_message_list_params.EmailMessageListParams,
                ),
            ),
            model=EmailMessage,
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
        """
        Permanently deletes an account-scoped email message, its events, its durable
        recipients, and unshared attachment objects. Returns 404 when the message does
        not exist in the authenticated account. The legacy `/v2/emails/{id}` DELETE
        route is a backward-compatible alias.

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
            path_template("/email_messages/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def batch(
        self,
        *,
        messages: Iterable[email_message_batch_params.Message],
        sandbox_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageBatchResponse:
        """
        Creates up to 50 email messages in a single request.

        Args:
          sandbox_mode: Applies sandbox mode to all messages in the batch. Overrides any per-message
              sandbox_mode in the messages array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/email_messages/batch",
            body=maybe_transform(
                {
                    "messages": messages,
                    "sandbox_mode": sandbox_mode,
                },
                email_message_batch_params.EmailMessageBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageBatchResponse,
        )

    def delete_all(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes every email in the authenticated account sent from or to the
        supplied address, including retained events whose parent message has expired.
        Events and durable recipients are deleted immediately with each message. The
        operation never searches or reports matches in another account. The legacy
        `/v2/emails` DELETE route is a backward-compatible alias.

        Args:
          address: Sender or recipient address to delete. Matching is trimmed and case-insensitive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/email_messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"address": address}, email_message_delete_all_params.EmailMessageDeleteAllParams
                ),
            ),
            cast_to=NoneType,
        )

    def delete_schedule(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Cancels a scheduled email and returns it with status `cancelled`.

        The legacy
        `/v2/emails/{id}/schedule` DELETE route is an alias.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._delete(
            path_template("/email_messages/{email_id}/schedule", email_id=email_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )

    def retrieve_events(
        self,
        email_id: str,
        *,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEmailCursorPagination[MessageEvent]:
        """
        Lists events for a single message sorted oldest first by
        `occurred_at asc, id asc`. The legacy `/v2/emails/{id}/events` GET route is a
        backward-compatible alias.

        Args:
          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get_api_list(
            path_template("/email_messages/{email_id}/events", email_id=email_id),
            page=SyncEmailCursorPagination[MessageEvent],
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
                    email_message_retrieve_events_params.EmailMessageRetrieveEventsParams,
                ),
            ),
            model=MessageEvent,
        )


class AsyncEmailMessagesResource(AsyncAPIResource):
    """Send and manage email messages.

    Legacy `/v2/emails` routes are aliases for these endpoints.
    """

    @cached_property
    def recipients(self) -> AsyncRecipientsResource:
        """Send and manage email messages.

        Legacy `/v2/emails` routes are aliases for these endpoints.
        """
        return AsyncRecipientsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: EmailAddressInputParam,
        to: SequenceNotStr[EmailAddressInputParam],
        attachments: Iterable[AttachmentRequestParam] | Omit = omit,
        bcc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        cc: SequenceNotStr[EmailAddressInputParam] | Omit = omit,
        forward_of_message_id: Optional[str] | Omit = omit,
        from_name: str | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html_body: str | Omit = omit,
        ignore_suppression: bool | Omit = omit,
        in_reply_to_message_id: Optional[str] | Omit = omit,
        inline_css: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        reply_to: EmailAddressInputParam | Omit = omit,
        reply_to_all: Optional[bool] | Omit = omit,
        sandbox_mode: bool | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        send_at: Union[str, datetime] | Omit = omit,
        subject: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        template_id: str | Omit = omit,
        template_variables: Dict[str, object] | Omit = omit,
        text_body: str | Omit = omit,
        tracking_settings: TrackingSettingsParam | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Queues, schedules, or sandbox-sends an email message.

        The legacy `/v2/emails`
        POST route is a backward-compatible alias for this operation.

        `subject` is required unless `template_id` is supplied. When using
        `template_id`, do not also provide `subject`, `html_body`, or `text_body`; the
        template is rendered with `template_variables`.

        Note: template lookup failures (not found, wrong account) return 400, not 404.

        Args:
          forward_of_message_id: Telnyx message UUID of the message this send forwards. Forwarded messages start
              a NEW thread per RFC 5322 — NO `In-Reply-To` or `References` headers are set on
              the outbound MIME. The id is recorded in the message's metadata for EDR
              provenance only.

              The id is validated as a UUID but is NOT looked up against the message store —
              existence is the caller's responsibility (the forward is pure metadata; it does
              not affect delivery). Cannot be combined with `in_reply_to_message_id` (422).

          from_name: Optional display name for string `from`; overrides `from.name` when provided.

          group_id: Optional unsubscribe-group UUID used for group-scoped suppression checks and
              unsubscribe handling.

          headers: Custom email headers. Write-only; not returned in responses.

          html_body: HTML email body. Returned only by `GET /email_messages/{id}`; omitted from
              create and list responses.

          ignore_suppression: When true, allows delivery to recipients whose suppressions explicitly permit an
              override. Hard bounces, spam complaints, and invalid-address suppressions cannot
              be overridden. Requires the `email:override` API scope.

          in_reply_to_message_id: Telnyx message UUID of the message this send replies to. When provided, the API
              sets RFC 5322 `In-Reply-To` and `References` headers on the outbound MIME so the
              recipient's mailbox (Gmail/Outlook) threads it correctly. The parent is looked
              up under the caller's account scope; a UUID belonging to another account yields
              a non-enumerating 404.

              Wire-only (Phase 1): the API sets the headers and does NOT resolve or mutate
              `thread_id` on the server side. Messages sent without this parameter are
              standalone (no threading headers injected).

              Cannot be combined with `forward_of_message_id` (422).

          metadata: Custom metadata. Write-only; not returned in responses.

          reply_to: Reply-to address. If provided as an object with a name, only the email is
              stored; the name is ignored.

          reply_to_all: Indicates a reply-all intent. In Phase 1 (wire-only) this does not change the
              threading headers — recipient selection is customer- controlled (`to`/`cc`), and
              a thread is not defined by its audience. When the referenced message has no
              thread context, reply-all degrades to a plain reply (parent ID only in
              `References`). The resolution engine (separate work) will expand the ancestor
              chain at a later phase with no API change.

              Only meaningful alongside `in_reply_to_message_id`.

          scheduled_at: Future ISO 8601 time to schedule sending. Invalid or past timestamps are
              silently ignored and the email is sent immediately. The legacy alias `send_at`
              is still accepted for backward compatibility; when both are provided,
              `scheduled_at` wins.

          send_at: Deprecated alias for `scheduled_at`.

          subject: Required unless `template_id` is supplied. When using a template, the template's
              subject is rendered; if the template has no subject or renders empty, the
              request returns 400.

          tags: Tags for categorization and reporting. Stored on the message and propagated to
              Email Detail Records. Not returned in API responses.

          template_variables: Variables for Liquid template rendering. Non-object values may cause a 422
              validation error on message creation, but are silently treated as an empty
              object for template rendering.

          text_body: Plain text email body. Returned only by `GET /email_messages/{id}`; omitted from
              create and list responses.

          tracking_settings: Per-send open and click tracking overrides. Omitted properties inherit the
              sender domain's tracking settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/email_messages",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "forward_of_message_id": forward_of_message_id,
                    "from_name": from_name,
                    "group_id": group_id,
                    "headers": headers,
                    "html_body": html_body,
                    "ignore_suppression": ignore_suppression,
                    "in_reply_to_message_id": in_reply_to_message_id,
                    "inline_css": inline_css,
                    "metadata": metadata,
                    "reply_to": reply_to,
                    "reply_to_all": reply_to_all,
                    "sandbox_mode": sandbox_mode,
                    "scheduled_at": scheduled_at,
                    "send_at": send_at,
                    "subject": subject,
                    "tags": tags,
                    "template_id": template_id,
                    "template_variables": template_variables,
                    "text_body": text_body,
                    "tracking_settings": tracking_settings,
                },
                email_message_create_params.EmailMessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
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
    ) -> EmailMessageRetrieveResponse:
        """
        The legacy `/v2/emails/{id}` GET route is a backward-compatible alias for this
        operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_messages/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageRetrieveResponse,
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
    ) -> AsyncPaginator[EmailMessage, AsyncEmailCursorPagination[EmailMessage]]:
        """Lists messages sorted newest first by `created_at desc, id desc`.

        No filters
        other than cursor pagination are implemented. The legacy `/v2/emails` GET route
        is a backward-compatible alias for this operation.

        Args:
          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_messages",
            page=AsyncEmailCursorPagination[EmailMessage],
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
                    email_message_list_params.EmailMessageListParams,
                ),
            ),
            model=EmailMessage,
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
        """
        Permanently deletes an account-scoped email message, its events, its durable
        recipients, and unshared attachment objects. Returns 404 when the message does
        not exist in the authenticated account. The legacy `/v2/emails/{id}` DELETE
        route is a backward-compatible alias.

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
            path_template("/email_messages/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def batch(
        self,
        *,
        messages: Iterable[email_message_batch_params.Message],
        sandbox_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageBatchResponse:
        """
        Creates up to 50 email messages in a single request.

        Args:
          sandbox_mode: Applies sandbox mode to all messages in the batch. Overrides any per-message
              sandbox_mode in the messages array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/email_messages/batch",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "sandbox_mode": sandbox_mode,
                },
                email_message_batch_params.EmailMessageBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageBatchResponse,
        )

    async def delete_all(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes every email in the authenticated account sent from or to the
        supplied address, including retained events whose parent message has expired.
        Events and durable recipients are deleted immediately with each message. The
        operation never searches or reports matches in another account. The legacy
        `/v2/emails` DELETE route is a backward-compatible alias.

        Args:
          address: Sender or recipient address to delete. Matching is trimmed and case-insensitive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/email_messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"address": address}, email_message_delete_all_params.EmailMessageDeleteAllParams
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_schedule(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Cancels a scheduled email and returns it with status `cancelled`.

        The legacy
        `/v2/emails/{id}/schedule` DELETE route is an alias.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._delete(
            path_template("/email_messages/{email_id}/schedule", email_id=email_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )

    def retrieve_events(
        self,
        email_id: str,
        *,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MessageEvent, AsyncEmailCursorPagination[MessageEvent]]:
        """
        Lists events for a single message sorted oldest first by
        `occurred_at asc, id asc`. The legacy `/v2/emails/{id}/events` GET route is a
        backward-compatible alias.

        Args:
          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get_api_list(
            path_template("/email_messages/{email_id}/events", email_id=email_id),
            page=AsyncEmailCursorPagination[MessageEvent],
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
                    email_message_retrieve_events_params.EmailMessageRetrieveEventsParams,
                ),
            ),
            model=MessageEvent,
        )


class EmailMessagesResourceWithRawResponse:
    def __init__(self, email_messages: EmailMessagesResource) -> None:
        self._email_messages = email_messages

        self.create = to_raw_response_wrapper(
            email_messages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            email_messages.list,
        )
        self.delete = to_raw_response_wrapper(
            email_messages.delete,
        )
        self.batch = to_raw_response_wrapper(
            email_messages.batch,
        )
        self.delete_all = to_raw_response_wrapper(
            email_messages.delete_all,
        )
        self.delete_schedule = to_raw_response_wrapper(
            email_messages.delete_schedule,
        )
        self.retrieve_events = to_raw_response_wrapper(
            email_messages.retrieve_events,
        )

    @cached_property
    def recipients(self) -> RecipientsResourceWithRawResponse:
        """Send and manage email messages.

        Legacy `/v2/emails` routes are aliases for these endpoints.
        """
        return RecipientsResourceWithRawResponse(self._email_messages.recipients)


class AsyncEmailMessagesResourceWithRawResponse:
    def __init__(self, email_messages: AsyncEmailMessagesResource) -> None:
        self._email_messages = email_messages

        self.create = async_to_raw_response_wrapper(
            email_messages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            email_messages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_messages.delete,
        )
        self.batch = async_to_raw_response_wrapper(
            email_messages.batch,
        )
        self.delete_all = async_to_raw_response_wrapper(
            email_messages.delete_all,
        )
        self.delete_schedule = async_to_raw_response_wrapper(
            email_messages.delete_schedule,
        )
        self.retrieve_events = async_to_raw_response_wrapper(
            email_messages.retrieve_events,
        )

    @cached_property
    def recipients(self) -> AsyncRecipientsResourceWithRawResponse:
        """Send and manage email messages.

        Legacy `/v2/emails` routes are aliases for these endpoints.
        """
        return AsyncRecipientsResourceWithRawResponse(self._email_messages.recipients)


class EmailMessagesResourceWithStreamingResponse:
    def __init__(self, email_messages: EmailMessagesResource) -> None:
        self._email_messages = email_messages

        self.create = to_streamed_response_wrapper(
            email_messages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            email_messages.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_messages.delete,
        )
        self.batch = to_streamed_response_wrapper(
            email_messages.batch,
        )
        self.delete_all = to_streamed_response_wrapper(
            email_messages.delete_all,
        )
        self.delete_schedule = to_streamed_response_wrapper(
            email_messages.delete_schedule,
        )
        self.retrieve_events = to_streamed_response_wrapper(
            email_messages.retrieve_events,
        )

    @cached_property
    def recipients(self) -> RecipientsResourceWithStreamingResponse:
        """Send and manage email messages.

        Legacy `/v2/emails` routes are aliases for these endpoints.
        """
        return RecipientsResourceWithStreamingResponse(self._email_messages.recipients)


class AsyncEmailMessagesResourceWithStreamingResponse:
    def __init__(self, email_messages: AsyncEmailMessagesResource) -> None:
        self._email_messages = email_messages

        self.create = async_to_streamed_response_wrapper(
            email_messages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            email_messages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_messages.delete,
        )
        self.batch = async_to_streamed_response_wrapper(
            email_messages.batch,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            email_messages.delete_all,
        )
        self.delete_schedule = async_to_streamed_response_wrapper(
            email_messages.delete_schedule,
        )
        self.retrieve_events = async_to_streamed_response_wrapper(
            email_messages.retrieve_events,
        )

    @cached_property
    def recipients(self) -> AsyncRecipientsResourceWithStreamingResponse:
        """Send and manage email messages.

        Legacy `/v2/emails` routes are aliases for these endpoints.
        """
        return AsyncRecipientsResourceWithStreamingResponse(self._email_messages.recipients)
