# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.email_inboxes import draft_list_params, draft_patch_params, draft_create_params, draft_update_params
from ...types.email_address_input_param import EmailAddressInputParam
from ...types.email_inboxes.draft_list_response import DraftListResponse
from ...types.email_inboxes.email_draft_response import EmailDraftResponse
from ...types.email_inboxes.email_message_response import EmailMessageResponse

__all__ = ["DraftsResource", "AsyncDraftsResource"]


class DraftsResource(SyncAPIResource):
    """
    Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
    """

    @cached_property
    def with_raw_response(self) -> DraftsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DraftsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DraftsResourceWithStreamingResponse(self)

    def create(
        self,
        inbox_id: str,
        *,
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
        """Creates an unsent draft in the inbox.

        Every field is optional — a draft is a
        work-in-progress and may be saved incomplete. Send-time requirements (sender,
        subject, at least one recipient) are enforced when the draft is sent, not when
        it is created.

        Drafts are unbillable and emit no Email Detail Records until they are sent.

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
        return self._post(
            path_template("/email_inboxes/{inbox_id}/drafts", inbox_id=inbox_id),
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
                draft_create_params.DraftCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    def retrieve(
        self,
        draft_id: str,
        *,
        inbox_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDraftResponse:
        """Returns a single draft.

        Drafts that have been sent remain retrievable, so the
        exact content that was sent stays auditable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return self._get(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    def update(
        self,
        draft_id: str,
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
        """Updates the supplied fields on a draft.

        `account_id` and `inbox_id` are
        server-owned and ignored if present in the body, so a draft can never be moved
        between accounts or inboxes.

        A draft that is being sent or has already been sent is immutable and returns 422
        — modifying it would race with delivery or rewrite the record of what was
        actually sent.

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
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return self._put(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
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
                draft_update_params.DraftUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    def list(
        self,
        inbox_id: str,
        *,
        filter_status: Literal["draft", "sending", "sent"] | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftListResponse:
        """Lists drafts newest first using stable cursor pagination.

        All access is scoped
        to the authenticated account and the given inbox.

        Args:
          filter_status: Restrict results to drafts in this state.

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
            path_template("/email_inboxes/{inbox_id}/drafts", inbox_id=inbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_status": filter_status,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    draft_list_params.DraftListParams,
                ),
            ),
            cast_to=DraftListResponse,
        )

    def delete(
        self,
        draft_id: str,
        *,
        inbox_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes an unsent draft.

        Drafts that are being sent or have been
        sent cannot be deleted; sent drafts are retained for audit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def patch(
        self,
        draft_id: str,
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
        """
        Identical to `PUT`; both apply a partial update to the supplied fields.

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
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return self._patch(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
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
                draft_patch_params.DraftPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    def send(
        self,
        draft_id: str,
        *,
        inbox_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """
        Sends the draft through the standard send pipeline — the same domain resolution,
        suppression, reputation, daily-quota, persistence and Detail Record behaviour as
        `POST /v2/email_messages`. The response body is the created email message.

        If the draft has no explicit `from_email`, the inbox address is used.

        The draft is marked `sent` only after the send is accepted; a send rejected for
        suppression, quota or reputation leaves the draft editable so it can be fixed
        and retried. A draft that is already `sent` returns 422 rather than sending
        twice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return self._post(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}/send", inbox_id=inbox_id, draft_id=draft_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )


class AsyncDraftsResource(AsyncAPIResource):
    """
    Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDraftsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDraftsResourceWithStreamingResponse(self)

    async def create(
        self,
        inbox_id: str,
        *,
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
        """Creates an unsent draft in the inbox.

        Every field is optional — a draft is a
        work-in-progress and may be saved incomplete. Send-time requirements (sender,
        subject, at least one recipient) are enforced when the draft is sent, not when
        it is created.

        Drafts are unbillable and emit no Email Detail Records until they are sent.

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
        return await self._post(
            path_template("/email_inboxes/{inbox_id}/drafts", inbox_id=inbox_id),
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
                draft_create_params.DraftCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    async def retrieve(
        self,
        draft_id: str,
        *,
        inbox_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDraftResponse:
        """Returns a single draft.

        Drafts that have been sent remain retrievable, so the
        exact content that was sent stays auditable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return await self._get(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    async def update(
        self,
        draft_id: str,
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
        """Updates the supplied fields on a draft.

        `account_id` and `inbox_id` are
        server-owned and ignored if present in the body, so a draft can never be moved
        between accounts or inboxes.

        A draft that is being sent or has already been sent is immutable and returns 422
        — modifying it would race with delivery or rewrite the record of what was
        actually sent.

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
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return await self._put(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
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
                draft_update_params.DraftUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    async def list(
        self,
        inbox_id: str,
        *,
        filter_status: Literal["draft", "sending", "sent"] | Omit = omit,
        page_after: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftListResponse:
        """Lists drafts newest first using stable cursor pagination.

        All access is scoped
        to the authenticated account and the given inbox.

        Args:
          filter_status: Restrict results to drafts in this state.

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
            path_template("/email_inboxes/{inbox_id}/drafts", inbox_id=inbox_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_status": filter_status,
                        "page_after": page_after,
                        "page_size": page_size,
                    },
                    draft_list_params.DraftListParams,
                ),
            ),
            cast_to=DraftListResponse,
        )

    async def delete(
        self,
        draft_id: str,
        *,
        inbox_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes an unsent draft.

        Drafts that are being sent or have been
        sent cannot be deleted; sent drafts are retained for audit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def patch(
        self,
        draft_id: str,
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
        """
        Identical to `PUT`; both apply a partial update to the supplied fields.

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
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return await self._patch(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}", inbox_id=inbox_id, draft_id=draft_id),
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
                draft_patch_params.DraftPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDraftResponse,
        )

    async def send(
        self,
        draft_id: str,
        *,
        inbox_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """
        Sends the draft through the standard send pipeline — the same domain resolution,
        suppression, reputation, daily-quota, persistence and Detail Record behaviour as
        `POST /v2/email_messages`. The response body is the created email message.

        If the draft has no explicit `from_email`, the inbox address is used.

        The draft is marked `sent` only after the send is accepted; a send rejected for
        suppression, quota or reputation leaves the draft editable so it can be fixed
        and retried. A draft that is already `sent` returns 422 rather than sending
        twice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        if not draft_id:
            raise ValueError(f"Expected a non-empty value for `draft_id` but received {draft_id!r}")
        return await self._post(
            path_template("/email_inboxes/{inbox_id}/drafts/{draft_id}/send", inbox_id=inbox_id, draft_id=draft_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )


class DraftsResourceWithRawResponse:
    def __init__(self, drafts: DraftsResource) -> None:
        self._drafts = drafts

        self.create = to_raw_response_wrapper(
            drafts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            drafts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            drafts.update,
        )
        self.list = to_raw_response_wrapper(
            drafts.list,
        )
        self.delete = to_raw_response_wrapper(
            drafts.delete,
        )
        self.patch = to_raw_response_wrapper(
            drafts.patch,
        )
        self.send = to_raw_response_wrapper(
            drafts.send,
        )


class AsyncDraftsResourceWithRawResponse:
    def __init__(self, drafts: AsyncDraftsResource) -> None:
        self._drafts = drafts

        self.create = async_to_raw_response_wrapper(
            drafts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            drafts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            drafts.update,
        )
        self.list = async_to_raw_response_wrapper(
            drafts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            drafts.delete,
        )
        self.patch = async_to_raw_response_wrapper(
            drafts.patch,
        )
        self.send = async_to_raw_response_wrapper(
            drafts.send,
        )


class DraftsResourceWithStreamingResponse:
    def __init__(self, drafts: DraftsResource) -> None:
        self._drafts = drafts

        self.create = to_streamed_response_wrapper(
            drafts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            drafts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            drafts.update,
        )
        self.list = to_streamed_response_wrapper(
            drafts.list,
        )
        self.delete = to_streamed_response_wrapper(
            drafts.delete,
        )
        self.patch = to_streamed_response_wrapper(
            drafts.patch,
        )
        self.send = to_streamed_response_wrapper(
            drafts.send,
        )


class AsyncDraftsResourceWithStreamingResponse:
    def __init__(self, drafts: AsyncDraftsResource) -> None:
        self._drafts = drafts

        self.create = async_to_streamed_response_wrapper(
            drafts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            drafts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            drafts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            drafts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            drafts.delete,
        )
        self.patch = async_to_streamed_response_wrapper(
            drafts.patch,
        )
        self.send = async_to_streamed_response_wrapper(
            drafts.send,
        )
