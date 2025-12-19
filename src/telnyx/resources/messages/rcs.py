# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.messages import rc_send_params, rc_generate_deeplink_params
from ...types.rcs_agent_message_param import RcsAgentMessageParam
from ...types.messages.rc_send_response import RcSendResponse
from ...types.messages.rc_generate_deeplink_response import RcGenerateDeeplinkResponse

__all__ = ["RcsResource", "AsyncRcsResource"]


class RcsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RcsResourceWithStreamingResponse(self)

    def generate_deeplink(
        self,
        agent_id: str,
        *,
        body: str | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RcGenerateDeeplinkResponse:
        """
        Generate a deeplink URL that can be used to start an RCS conversation with a
        specific agent.

        Args:
          body: Pre-filled message body (URL encoded)

          phone_number: Phone number in E164 format (URL encoded)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/messages/rcs/deeplinks/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "body": body,
                        "phone_number": phone_number,
                    },
                    rc_generate_deeplink_params.RcGenerateDeeplinkParams,
                ),
            ),
            cast_to=RcGenerateDeeplinkResponse,
        )

    def send(
        self,
        *,
        agent_id: str,
        agent_message: RcsAgentMessageParam,
        messaging_profile_id: str,
        to: str,
        mms_fallback: rc_send_params.MmsFallback | Omit = omit,
        sms_fallback: rc_send_params.SMSFallback | Omit = omit,
        type: Literal["RCS"] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RcSendResponse:
        """
        Send an RCS message

        Args:
          agent_id: RCS Agent ID

          messaging_profile_id: A valid messaging profile ID

          to: Phone number in +E.164 format

          type: Message type - must be set to "RCS"

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/rcs",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_message": agent_message,
                    "messaging_profile_id": messaging_profile_id,
                    "to": to,
                    "mms_fallback": mms_fallback,
                    "sms_fallback": sms_fallback,
                    "type": type,
                    "webhook_url": webhook_url,
                },
                rc_send_params.RcSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcSendResponse,
        )


class AsyncRcsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRcsResourceWithStreamingResponse(self)

    async def generate_deeplink(
        self,
        agent_id: str,
        *,
        body: str | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RcGenerateDeeplinkResponse:
        """
        Generate a deeplink URL that can be used to start an RCS conversation with a
        specific agent.

        Args:
          body: Pre-filled message body (URL encoded)

          phone_number: Phone number in E164 format (URL encoded)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/messages/rcs/deeplinks/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "body": body,
                        "phone_number": phone_number,
                    },
                    rc_generate_deeplink_params.RcGenerateDeeplinkParams,
                ),
            ),
            cast_to=RcGenerateDeeplinkResponse,
        )

    async def send(
        self,
        *,
        agent_id: str,
        agent_message: RcsAgentMessageParam,
        messaging_profile_id: str,
        to: str,
        mms_fallback: rc_send_params.MmsFallback | Omit = omit,
        sms_fallback: rc_send_params.SMSFallback | Omit = omit,
        type: Literal["RCS"] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RcSendResponse:
        """
        Send an RCS message

        Args:
          agent_id: RCS Agent ID

          messaging_profile_id: A valid messaging profile ID

          to: Phone number in +E.164 format

          type: Message type - must be set to "RCS"

          webhook_url: The URL where webhooks related to this message will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/rcs",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_message": agent_message,
                    "messaging_profile_id": messaging_profile_id,
                    "to": to,
                    "mms_fallback": mms_fallback,
                    "sms_fallback": sms_fallback,
                    "type": type,
                    "webhook_url": webhook_url,
                },
                rc_send_params.RcSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcSendResponse,
        )


class RcsResourceWithRawResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

        self.generate_deeplink = to_raw_response_wrapper(
            rcs.generate_deeplink,
        )
        self.send = to_raw_response_wrapper(
            rcs.send,
        )


class AsyncRcsResourceWithRawResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

        self.generate_deeplink = async_to_raw_response_wrapper(
            rcs.generate_deeplink,
        )
        self.send = async_to_raw_response_wrapper(
            rcs.send,
        )


class RcsResourceWithStreamingResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

        self.generate_deeplink = to_streamed_response_wrapper(
            rcs.generate_deeplink,
        )
        self.send = to_streamed_response_wrapper(
            rcs.send,
        )


class AsyncRcsResourceWithStreamingResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

        self.generate_deeplink = async_to_streamed_response_wrapper(
            rcs.generate_deeplink,
        )
        self.send = async_to_streamed_response_wrapper(
            rcs.send,
        )
