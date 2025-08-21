# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import messsage_rcs_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.messsage_rcs_response import MesssageRcsResponse
from ..types.rcs_agent_message_param import RcsAgentMessageParam

__all__ = ["MesssagesResource", "AsyncMesssagesResource"]


class MesssagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MesssagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MesssagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MesssagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MesssagesResourceWithStreamingResponse(self)

    def rcs(
        self,
        *,
        agent_id: str,
        agent_message: RcsAgentMessageParam,
        messaging_profile_id: str,
        to: str,
        mms_fallback: messsage_rcs_params.MmsFallback | NotGiven = NOT_GIVEN,
        sms_fallback: messsage_rcs_params.SMSFallback | NotGiven = NOT_GIVEN,
        type: Literal["RCS"] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MesssageRcsResponse:
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
            "/messsages/rcs",
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
                messsage_rcs_params.MesssageRcsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MesssageRcsResponse,
        )


class AsyncMesssagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMesssagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMesssagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMesssagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMesssagesResourceWithStreamingResponse(self)

    async def rcs(
        self,
        *,
        agent_id: str,
        agent_message: RcsAgentMessageParam,
        messaging_profile_id: str,
        to: str,
        mms_fallback: messsage_rcs_params.MmsFallback | NotGiven = NOT_GIVEN,
        sms_fallback: messsage_rcs_params.SMSFallback | NotGiven = NOT_GIVEN,
        type: Literal["RCS"] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MesssageRcsResponse:
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
            "/messsages/rcs",
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
                messsage_rcs_params.MesssageRcsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MesssageRcsResponse,
        )


class MesssagesResourceWithRawResponse:
    def __init__(self, messsages: MesssagesResource) -> None:
        self._messsages = messsages

        self.rcs = to_raw_response_wrapper(
            messsages.rcs,
        )


class AsyncMesssagesResourceWithRawResponse:
    def __init__(self, messsages: AsyncMesssagesResource) -> None:
        self._messsages = messsages

        self.rcs = async_to_raw_response_wrapper(
            messsages.rcs,
        )


class MesssagesResourceWithStreamingResponse:
    def __init__(self, messsages: MesssagesResource) -> None:
        self._messsages = messsages

        self.rcs = to_streamed_response_wrapper(
            messsages.rcs,
        )


class AsyncMesssagesResourceWithStreamingResponse:
    def __init__(self, messsages: AsyncMesssagesResource) -> None:
        self._messsages = messsages

        self.rcs = async_to_streamed_response_wrapper(
            messsages.rcs,
        )
