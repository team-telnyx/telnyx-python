# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .rcs import (
    RcsResource,
    AsyncRcsResource,
    RcsResourceWithRawResponse,
    AsyncRcsResourceWithRawResponse,
    RcsResourceWithStreamingResponse,
    AsyncRcsResourceWithStreamingResponse,
)
from ...types import (
    message_send_params,
    message_schedule_params,
    message_send_group_mms_params,
    message_send_long_code_params,
    message_send_short_code_params,
    message_send_number_pool_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.message_send_response import MessageSendResponse
from ...types.message_retrieve_response import MessageRetrieveResponse
from ...types.message_schedule_response import MessageScheduleResponse
from ...types.message_send_group_mms_response import MessageSendGroupMmsResponse
from ...types.message_send_long_code_response import MessageSendLongCodeResponse
from ...types.message_send_short_code_response import MessageSendShortCodeResponse
from ...types.message_cancel_scheduled_response import MessageCancelScheduledResponse
from ...types.message_send_number_pool_response import MessageSendNumberPoolResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def rcs(self) -> RcsResource:
        return RcsResource(self._client)

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

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageRetrieveResponse:
        """
        Note: This API endpoint can only retrieve messages that are no older than 10
        days since their creation. If you require messages older than this, please
        generate an
        [MDR report.](https://developers.telnyx.com/api/v1/mission-control/add-mdr-request)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def cancel_scheduled(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCancelScheduledResponse:
        """Cancel a scheduled message that has not yet been sent.

        Only messages with
        `status=scheduled` and `send_at` more than a minute from now can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCancelScheduledResponse,
        )

    def schedule(
        self,
        *,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageScheduleResponse:
        """
        Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or
        Number Pool.

        This endpoint allows you to schedule a message with any messaging resource.
        Current messaging resources include: long-code, short-code, number-pool, and
        alphanumeric-sender-id.

        Args:
          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          from_: Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
              code).

              **Required if sending with a phone number, short code, or alphanumeric sender
              ID.**

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          messaging_profile_id: Unique identifier for a messaging profile.

              **Required if sending via number pool or with an alphanumeric sender ID.**

          send_at: ISO 8601 formatted date indicating when to send the message - accurate up till a
              minute.

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/schedule",
            body=maybe_transform(
                {
                    "to": to,
                    "auto_detect": auto_detect,
                    "from_": from_,
                    "media_urls": media_urls,
                    "messaging_profile_id": messaging_profile_id,
                    "send_at": send_at,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_schedule_params.MessageScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageScheduleResponse,
        )

    def send(
        self,
        *,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendResponse:
        """
        Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number
        Pool.

        This endpoint allows you to send a message with any messaging resource. Current
        messaging resources include: long-code, short-code, number-pool, and
        alphanumeric-sender-id.

        Args:
          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          from_: Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
              code).

              **Required if sending with a phone number, short code, or alphanumeric sender
              ID.**

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          messaging_profile_id: Unique identifier for a messaging profile.

              **Required if sending via number pool or with an alphanumeric sender ID.**

          send_at: ISO 8601 formatted date indicating when to send the message - accurate up till a
              minute.

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages",
            body=maybe_transform(
                {
                    "to": to,
                    "auto_detect": auto_detect,
                    "from_": from_,
                    "media_urls": media_urls,
                    "messaging_profile_id": messaging_profile_id,
                    "send_at": send_at,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )

    def send_group_mms(
        self,
        *,
        from_: str,
        to: List[str],
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendGroupMmsResponse:
        """
        Send a group MMS message

        Args:
          from_: Phone number, in +E.164 format, used to send the message.

          to: A list of destinations. No more than 8 destinations are allowed.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/group_mms",
            body=maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_group_mms_params.MessageSendGroupMmsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendGroupMmsResponse,
        )

    def send_long_code(
        self,
        *,
        from_: str,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendLongCodeResponse:
        """
        Send a long code message

        Args:
          from_: Phone number, in +E.164 format, used to send the message.

          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/long_code",
            body=maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "auto_detect": auto_detect,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_long_code_params.MessageSendLongCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendLongCodeResponse,
        )

    def send_number_pool(
        self,
        *,
        messaging_profile_id: str,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendNumberPoolResponse:
        """
        Send a message using number pool

        Args:
          messaging_profile_id: Unique identifier for a messaging profile.

          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/number_pool",
            body=maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "to": to,
                    "auto_detect": auto_detect,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_number_pool_params.MessageSendNumberPoolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendNumberPoolResponse,
        )

    def send_short_code(
        self,
        *,
        from_: str,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendShortCodeResponse:
        """
        Send a short code message

        Args:
          from_: Phone number, in +E.164 format, used to send the message.

          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/short_code",
            body=maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "auto_detect": auto_detect,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_short_code_params.MessageSendShortCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendShortCodeResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def rcs(self) -> AsyncRcsResource:
        return AsyncRcsResource(self._client)

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

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageRetrieveResponse:
        """
        Note: This API endpoint can only retrieve messages that are no older than 10
        days since their creation. If you require messages older than this, please
        generate an
        [MDR report.](https://developers.telnyx.com/api/v1/mission-control/add-mdr-request)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def cancel_scheduled(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCancelScheduledResponse:
        """Cancel a scheduled message that has not yet been sent.

        Only messages with
        `status=scheduled` and `send_at` more than a minute from now can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCancelScheduledResponse,
        )

    async def schedule(
        self,
        *,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageScheduleResponse:
        """
        Schedule a message with a Phone Number, Alphanumeric Sender ID, Short Code or
        Number Pool.

        This endpoint allows you to schedule a message with any messaging resource.
        Current messaging resources include: long-code, short-code, number-pool, and
        alphanumeric-sender-id.

        Args:
          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          from_: Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
              code).

              **Required if sending with a phone number, short code, or alphanumeric sender
              ID.**

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          messaging_profile_id: Unique identifier for a messaging profile.

              **Required if sending via number pool or with an alphanumeric sender ID.**

          send_at: ISO 8601 formatted date indicating when to send the message - accurate up till a
              minute.

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/schedule",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "auto_detect": auto_detect,
                    "from_": from_,
                    "media_urls": media_urls,
                    "messaging_profile_id": messaging_profile_id,
                    "send_at": send_at,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_schedule_params.MessageScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageScheduleResponse,
        )

    async def send(
        self,
        *,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        send_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendResponse:
        """
        Send a message with a Phone Number, Alphanumeric Sender ID, Short Code or Number
        Pool.

        This endpoint allows you to send a message with any messaging resource. Current
        messaging resources include: long-code, short-code, number-pool, and
        alphanumeric-sender-id.

        Args:
          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          from_: Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
              code).

              **Required if sending with a phone number, short code, or alphanumeric sender
              ID.**

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          messaging_profile_id: Unique identifier for a messaging profile.

              **Required if sending via number pool or with an alphanumeric sender ID.**

          send_at: ISO 8601 formatted date indicating when to send the message - accurate up till a
              minute.

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages",
            body=await async_maybe_transform(
                {
                    "to": to,
                    "auto_detect": auto_detect,
                    "from_": from_,
                    "media_urls": media_urls,
                    "messaging_profile_id": messaging_profile_id,
                    "send_at": send_at,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )

    async def send_group_mms(
        self,
        *,
        from_: str,
        to: List[str],
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendGroupMmsResponse:
        """
        Send a group MMS message

        Args:
          from_: Phone number, in +E.164 format, used to send the message.

          to: A list of destinations. No more than 8 destinations are allowed.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/group_mms",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_group_mms_params.MessageSendGroupMmsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendGroupMmsResponse,
        )

    async def send_long_code(
        self,
        *,
        from_: str,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendLongCodeResponse:
        """
        Send a long code message

        Args:
          from_: Phone number, in +E.164 format, used to send the message.

          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/long_code",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "auto_detect": auto_detect,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_long_code_params.MessageSendLongCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendLongCodeResponse,
        )

    async def send_number_pool(
        self,
        *,
        messaging_profile_id: str,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendNumberPoolResponse:
        """
        Send a message using number pool

        Args:
          messaging_profile_id: Unique identifier for a messaging profile.

          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/number_pool",
            body=await async_maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "to": to,
                    "auto_detect": auto_detect,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_number_pool_params.MessageSendNumberPoolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendNumberPoolResponse,
        )

    async def send_short_code(
        self,
        *,
        from_: str,
        to: str,
        auto_detect: bool | NotGiven = NOT_GIVEN,
        media_urls: List[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["SMS", "MMS"] | NotGiven = NOT_GIVEN,
        use_profile_webhooks: bool | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageSendShortCodeResponse:
        """
        Send a short code message

        Args:
          from_: Phone number, in +E.164 format, used to send the message.

          to: Receiving address (+E.164 formatted phone number or short code).

          auto_detect: Automatically detect if an SMS message is unusually long and exceeds a
              recommended limit of message parts.

          media_urls: A list of media URLs. The total media size must be less than 1 MB.

              **Required for MMS**

          subject: Subject of multimedia message

          text: Message body (i.e., content) as a non-empty string.

              **Required for SMS**

          type: The protocol for sending the message, either SMS or MMS.

          use_profile_webhooks: If the profile this number is associated with has webhooks, use them for
              delivery notifications. If webhooks are also specified on the message itself,
              they will be attempted first, then those on the profile.

          webhook_failover_url: The failover URL where webhooks related to this message will be sent if sending
              to the primary URL fails.

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/short_code",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "to": to,
                    "auto_detect": auto_detect,
                    "media_urls": media_urls,
                    "subject": subject,
                    "text": text,
                    "type": type,
                    "use_profile_webhooks": use_profile_webhooks,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                message_send_short_code_params.MessageSendShortCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendShortCodeResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.cancel_scheduled = to_raw_response_wrapper(
            messages.cancel_scheduled,
        )
        self.schedule = to_raw_response_wrapper(
            messages.schedule,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )
        self.send_group_mms = to_raw_response_wrapper(
            messages.send_group_mms,
        )
        self.send_long_code = to_raw_response_wrapper(
            messages.send_long_code,
        )
        self.send_number_pool = to_raw_response_wrapper(
            messages.send_number_pool,
        )
        self.send_short_code = to_raw_response_wrapper(
            messages.send_short_code,
        )

    @cached_property
    def rcs(self) -> RcsResourceWithRawResponse:
        return RcsResourceWithRawResponse(self._messages.rcs)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.cancel_scheduled = async_to_raw_response_wrapper(
            messages.cancel_scheduled,
        )
        self.schedule = async_to_raw_response_wrapper(
            messages.schedule,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )
        self.send_group_mms = async_to_raw_response_wrapper(
            messages.send_group_mms,
        )
        self.send_long_code = async_to_raw_response_wrapper(
            messages.send_long_code,
        )
        self.send_number_pool = async_to_raw_response_wrapper(
            messages.send_number_pool,
        )
        self.send_short_code = async_to_raw_response_wrapper(
            messages.send_short_code,
        )

    @cached_property
    def rcs(self) -> AsyncRcsResourceWithRawResponse:
        return AsyncRcsResourceWithRawResponse(self._messages.rcs)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.cancel_scheduled = to_streamed_response_wrapper(
            messages.cancel_scheduled,
        )
        self.schedule = to_streamed_response_wrapper(
            messages.schedule,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )
        self.send_group_mms = to_streamed_response_wrapper(
            messages.send_group_mms,
        )
        self.send_long_code = to_streamed_response_wrapper(
            messages.send_long_code,
        )
        self.send_number_pool = to_streamed_response_wrapper(
            messages.send_number_pool,
        )
        self.send_short_code = to_streamed_response_wrapper(
            messages.send_short_code,
        )

    @cached_property
    def rcs(self) -> RcsResourceWithStreamingResponse:
        return RcsResourceWithStreamingResponse(self._messages.rcs)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.cancel_scheduled = async_to_streamed_response_wrapper(
            messages.cancel_scheduled,
        )
        self.schedule = async_to_streamed_response_wrapper(
            messages.schedule,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
        self.send_group_mms = async_to_streamed_response_wrapper(
            messages.send_group_mms,
        )
        self.send_long_code = async_to_streamed_response_wrapper(
            messages.send_long_code,
        )
        self.send_number_pool = async_to_streamed_response_wrapper(
            messages.send_number_pool,
        )
        self.send_short_code = async_to_streamed_response_wrapper(
            messages.send_short_code,
        )

    @cached_property
    def rcs(self) -> AsyncRcsResourceWithStreamingResponse:
        return AsyncRcsResourceWithStreamingResponse(self._messages.rcs)
