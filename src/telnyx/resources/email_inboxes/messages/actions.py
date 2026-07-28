# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import make_request_options
from ....types.email_inboxes.messages import (
    action_reply_params,
    action_forward_params,
    action_reply_all_params,
)
from ....types.email_inboxes.email_message_response import EmailMessageResponse
from ....types.email_inboxes.messages.inbox_action_recipient_input_param import InboxActionRecipientInputParam

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def forward(
        self,
        message_id: str,
        *,
        inbox_id: str,
        to: action_forward_params.To,
        bcc: InboxActionRecipientInputParam | Omit = omit,
        cc: InboxActionRecipientInputParam | Omit = omit,
        html: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """
        Sends from the inbox address through the standard email send pipeline to
        caller-supplied To, Cc, and Bcc recipients. `to` must contain at least one
        recipient. Optional `text` and `html` are prepended to a forwarded-message block
        containing the original metadata and available body content. The subject is
        prefixed with `Fwd:` unless it already has that prefix.

        Threading headers are derived from the original message: `In-Reply-To` is set to
        its RFC Message-ID, and `References` contains the original References values
        plus that Message-ID, de-duplicated and limited to the most recent 20 values.

        Args:
          to: One recipient or a non-empty recipient array. Each recipient may be an email
              string or an object with `email` and optional `name`.

          bcc: One recipient or a recipient array. Each recipient may be an email string or an
              object with `email` and optional `name`.

          cc: One recipient or a recipient array. Each recipient may be an email string or an
              object with `email` and optional `name`.

          html: Optional HTML note prepended to the generated forwarded-message block. Blank
              values are treated as omitted.

          text: Optional plain-text note prepended to the generated forwarded-message block.
              Blank values are treated as omitted.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/actions/forward",
                inbox_id=inbox_id,
                message_id=message_id,
            ),
            body=maybe_transform(
                {
                    "to": to,
                    "bcc": bcc,
                    "cc": cc,
                    "html": html,
                    "text": text,
                },
                action_forward_params.ActionForwardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )

    def reply(
        self,
        message_id: str,
        *,
        inbox_id: str,
        html: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Sends from the inbox address through the standard email send pipeline.

        The
        recipient is the original `Reply-To`, falling back to `From`; original Cc
        recipients are not included. The subject is prefixed with `Re:` unless it
        already has that prefix.

        Threading headers are derived from the original message: `In-Reply-To` is set to
        its RFC Message-ID, and `References` contains the original References values
        plus that Message-ID, de-duplicated and limited to the most recent 20 values.

        Args:
          html: HTML reply body.

          text: Plain-text reply body.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/actions/reply",
                inbox_id=inbox_id,
                message_id=message_id,
            ),
            body=maybe_transform(
                {
                    "html": html,
                    "text": text,
                },
                action_reply_params.ActionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )

    def reply_all(
        self,
        message_id: str,
        *,
        inbox_id: str,
        html: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Sends from the inbox address through the standard email send pipeline.

        The To
        list starts with the original `Reply-To` (or `From`) and includes original To
        recipients; the Cc list includes original Cc recipients. The inbox address is
        excluded, and recipients are de-duplicated case-insensitively across To and Cc.
        Bcc is always empty. The subject is prefixed with `Re:` unless it already has
        that prefix.

        Threading headers are derived from the original message: `In-Reply-To` is set to
        its RFC Message-ID, and `References` contains the original References values
        plus that Message-ID, de-duplicated and limited to the most recent 20 values.

        Args:
          html: HTML reply body.

          text: Plain-text reply body.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/actions/reply_all",
                inbox_id=inbox_id,
                message_id=message_id,
            ),
            body=maybe_transform(
                {
                    "html": html,
                    "text": text,
                },
                action_reply_all_params.ActionReplyAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def forward(
        self,
        message_id: str,
        *,
        inbox_id: str,
        to: action_forward_params.To,
        bcc: InboxActionRecipientInputParam | Omit = omit,
        cc: InboxActionRecipientInputParam | Omit = omit,
        html: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """
        Sends from the inbox address through the standard email send pipeline to
        caller-supplied To, Cc, and Bcc recipients. `to` must contain at least one
        recipient. Optional `text` and `html` are prepended to a forwarded-message block
        containing the original metadata and available body content. The subject is
        prefixed with `Fwd:` unless it already has that prefix.

        Threading headers are derived from the original message: `In-Reply-To` is set to
        its RFC Message-ID, and `References` contains the original References values
        plus that Message-ID, de-duplicated and limited to the most recent 20 values.

        Args:
          to: One recipient or a non-empty recipient array. Each recipient may be an email
              string or an object with `email` and optional `name`.

          bcc: One recipient or a recipient array. Each recipient may be an email string or an
              object with `email` and optional `name`.

          cc: One recipient or a recipient array. Each recipient may be an email string or an
              object with `email` and optional `name`.

          html: Optional HTML note prepended to the generated forwarded-message block. Blank
              values are treated as omitted.

          text: Optional plain-text note prepended to the generated forwarded-message block.
              Blank values are treated as omitted.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/actions/forward",
                inbox_id=inbox_id,
                message_id=message_id,
            ),
            body=await async_maybe_transform(
                {
                    "to": to,
                    "bcc": bcc,
                    "cc": cc,
                    "html": html,
                    "text": text,
                },
                action_forward_params.ActionForwardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )

    async def reply(
        self,
        message_id: str,
        *,
        inbox_id: str,
        html: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Sends from the inbox address through the standard email send pipeline.

        The
        recipient is the original `Reply-To`, falling back to `From`; original Cc
        recipients are not included. The subject is prefixed with `Re:` unless it
        already has that prefix.

        Threading headers are derived from the original message: `In-Reply-To` is set to
        its RFC Message-ID, and `References` contains the original References values
        plus that Message-ID, de-duplicated and limited to the most recent 20 values.

        Args:
          html: HTML reply body.

          text: Plain-text reply body.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/actions/reply",
                inbox_id=inbox_id,
                message_id=message_id,
            ),
            body=await async_maybe_transform(
                {
                    "html": html,
                    "text": text,
                },
                action_reply_params.ActionReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )

    async def reply_all(
        self,
        message_id: str,
        *,
        inbox_id: str,
        html: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailMessageResponse:
        """Sends from the inbox address through the standard email send pipeline.

        The To
        list starts with the original `Reply-To` (or `From`) and includes original To
        recipients; the Cc list includes original Cc recipients. The inbox address is
        excluded, and recipients are de-duplicated case-insensitively across To and Cc.
        Bcc is always empty. The subject is prefixed with `Re:` unless it already has
        that prefix.

        Threading headers are derived from the original message: `In-Reply-To` is set to
        its RFC Message-ID, and `References` contains the original References values
        plus that Message-ID, de-duplicated and limited to the most recent 20 values.

        Args:
          html: HTML reply body.

          text: Plain-text reply body.

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
                "/email_inboxes/{inbox_id}/messages/{message_id}/actions/reply_all",
                inbox_id=inbox_id,
                message_id=message_id,
            ),
            body=await async_maybe_transform(
                {
                    "html": html,
                    "text": text,
                },
                action_reply_all_params.ActionReplyAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailMessageResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.forward = to_raw_response_wrapper(
            actions.forward,
        )
        self.reply = to_raw_response_wrapper(
            actions.reply,
        )
        self.reply_all = to_raw_response_wrapper(
            actions.reply_all,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.forward = async_to_raw_response_wrapper(
            actions.forward,
        )
        self.reply = async_to_raw_response_wrapper(
            actions.reply,
        )
        self.reply_all = async_to_raw_response_wrapper(
            actions.reply_all,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.forward = to_streamed_response_wrapper(
            actions.forward,
        )
        self.reply = to_streamed_response_wrapper(
            actions.reply,
        )
        self.reply_all = to_streamed_response_wrapper(
            actions.reply_all,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.forward = async_to_streamed_response_wrapper(
            actions.forward,
        )
        self.reply = async_to_streamed_response_wrapper(
            actions.reply,
        )
        self.reply_all = async_to_streamed_response_wrapper(
            actions.reply_all,
        )
