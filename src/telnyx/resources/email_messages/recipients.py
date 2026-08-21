# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.email_messages import recipient_list_params
from ...types.email_messages.email_recipient import EmailRecipient
from ...types.email_messages.recipient_retrieve_response import RecipientRetrieveResponse

__all__ = ["RecipientsResource", "AsyncRecipientsResource"]


class RecipientsResource(SyncAPIResource):
    """Send and manage email messages.

    Legacy `/v2/emails` routes are aliases for these endpoints.
    """

    @cached_property
    def with_raw_response(self) -> RecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RecipientsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        recipient_id: str,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecipientRetrieveResponse:
        """
        Returns the current delivery state of a single recipient, including status,
        billable flag, SMTP detail, and lifecycle timestamps. BCC recipient addresses
        are redacted (returned as null).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        if not recipient_id:
            raise ValueError(f"Expected a non-empty value for `recipient_id` but received {recipient_id!r}")
        return self._get(
            path_template(
                "/email_messages/{email_id}/recipients/{recipient_id}", email_id=email_id, recipient_id=recipient_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecipientRetrieveResponse,
        )

    def list(
        self,
        email_id: str,
        *,
        kind: Literal["to", "cc", "bcc"] | Omit = omit,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal[
            "queued", "sending", "sent", "deferred", "delivered", "bounced", "failed", "gw_reject", "cancelled"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEmailCursorPagination[EmailRecipient]:
        """
        Lists per-recipient delivery states for a single message with cursor pagination.
        Each recipient has an independent status, billable flag, and lifecycle
        timestamps. BCC recipient addresses are redacted (returned as null) to protect
        BCC privacy. Default page size is 25, maximum is 100.

        Args:
          kind: Filter recipients by address kind.

          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          status: Filter recipients by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get_api_list(
            path_template("/email_messages/{email_id}/recipients", email_id=email_id),
            page=SyncEmailCursorPagination[EmailRecipient],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "kind": kind,
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "status": status,
                    },
                    recipient_list_params.RecipientListParams,
                ),
            ),
            model=EmailRecipient,
        )


class AsyncRecipientsResource(AsyncAPIResource):
    """Send and manage email messages.

    Legacy `/v2/emails` routes are aliases for these endpoints.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRecipientsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        recipient_id: str,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecipientRetrieveResponse:
        """
        Returns the current delivery state of a single recipient, including status,
        billable flag, SMTP detail, and lifecycle timestamps. BCC recipient addresses
        are redacted (returned as null).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        if not recipient_id:
            raise ValueError(f"Expected a non-empty value for `recipient_id` but received {recipient_id!r}")
        return await self._get(
            path_template(
                "/email_messages/{email_id}/recipients/{recipient_id}", email_id=email_id, recipient_id=recipient_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecipientRetrieveResponse,
        )

    def list(
        self,
        email_id: str,
        *,
        kind: Literal["to", "cc", "bcc"] | Omit = omit,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        status: Literal[
            "queued", "sending", "sent", "deferred", "delivered", "bounced", "failed", "gw_reject", "cancelled"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailRecipient, AsyncEmailCursorPagination[EmailRecipient]]:
        """
        Lists per-recipient delivery states for a single message with cursor pagination.
        Each recipient has an independent status, billable flag, and lifecycle
        timestamps. BCC recipient addresses are redacted (returned as null) to protect
        BCC privacy. Default page size is 25, maximum is 100.

        Args:
          kind: Filter recipients by address kind.

          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          status: Filter recipients by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get_api_list(
            path_template("/email_messages/{email_id}/recipients", email_id=email_id),
            page=AsyncEmailCursorPagination[EmailRecipient],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "kind": kind,
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "status": status,
                    },
                    recipient_list_params.RecipientListParams,
                ),
            ),
            model=EmailRecipient,
        )


class RecipientsResourceWithRawResponse:
    def __init__(self, recipients: RecipientsResource) -> None:
        self._recipients = recipients

        self.retrieve = to_raw_response_wrapper(
            recipients.retrieve,
        )
        self.list = to_raw_response_wrapper(
            recipients.list,
        )


class AsyncRecipientsResourceWithRawResponse:
    def __init__(self, recipients: AsyncRecipientsResource) -> None:
        self._recipients = recipients

        self.retrieve = async_to_raw_response_wrapper(
            recipients.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            recipients.list,
        )


class RecipientsResourceWithStreamingResponse:
    def __init__(self, recipients: RecipientsResource) -> None:
        self._recipients = recipients

        self.retrieve = to_streamed_response_wrapper(
            recipients.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            recipients.list,
        )


class AsyncRecipientsResourceWithStreamingResponse:
    def __init__(self, recipients: AsyncRecipientsResource) -> None:
        self._recipients = recipients

        self.retrieve = async_to_streamed_response_wrapper(
            recipients.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            recipients.list,
        )
