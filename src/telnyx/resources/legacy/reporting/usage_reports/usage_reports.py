# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .voice import (
    VoiceResource,
    AsyncVoiceResource,
    VoiceResourceWithRawResponse,
    AsyncVoiceResourceWithRawResponse,
    VoiceResourceWithStreamingResponse,
    AsyncVoiceResourceWithStreamingResponse,
)
from .messaging import (
    MessagingResource,
    AsyncMessagingResource,
    MessagingResourceWithRawResponse,
    AsyncMessagingResourceWithRawResponse,
    MessagingResourceWithStreamingResponse,
    AsyncMessagingResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .number_lookup import (
    NumberLookupResource,
    AsyncNumberLookupResource,
    NumberLookupResourceWithRawResponse,
    AsyncNumberLookupResourceWithRawResponse,
    NumberLookupResourceWithStreamingResponse,
    AsyncNumberLookupResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.legacy.reporting import usage_report_retrieve_speech_to_text_params
from .....types.legacy.reporting.usage_report_retrieve_speech_to_text_response import (
    UsageReportRetrieveSpeechToTextResponse,
)

__all__ = ["UsageReportsResource", "AsyncUsageReportsResource"]


class UsageReportsResource(SyncAPIResource):
    @cached_property
    def messaging(self) -> MessagingResource:
        return MessagingResource(self._client)

    @cached_property
    def number_lookup(self) -> NumberLookupResource:
        return NumberLookupResource(self._client)

    @cached_property
    def voice(self) -> VoiceResource:
        return VoiceResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UsageReportsResourceWithStreamingResponse(self)

    def retrieve_speech_to_text(
        self,
        *,
        end_date: Union[str, datetime] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageReportRetrieveSpeechToTextResponse:
        """Generate and fetch speech to text usage report synchronously.

        This endpoint will
        both generate and fetch the speech to text report over a specified time period.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/legacy/reporting/usage_reports/speech_to_text",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    usage_report_retrieve_speech_to_text_params.UsageReportRetrieveSpeechToTextParams,
                ),
            ),
            cast_to=UsageReportRetrieveSpeechToTextResponse,
        )


class AsyncUsageReportsResource(AsyncAPIResource):
    @cached_property
    def messaging(self) -> AsyncMessagingResource:
        return AsyncMessagingResource(self._client)

    @cached_property
    def number_lookup(self) -> AsyncNumberLookupResource:
        return AsyncNumberLookupResource(self._client)

    @cached_property
    def voice(self) -> AsyncVoiceResource:
        return AsyncVoiceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsageReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUsageReportsResourceWithStreamingResponse(self)

    async def retrieve_speech_to_text(
        self,
        *,
        end_date: Union[str, datetime] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageReportRetrieveSpeechToTextResponse:
        """Generate and fetch speech to text usage report synchronously.

        This endpoint will
        both generate and fetch the speech to text report over a specified time period.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/legacy/reporting/usage_reports/speech_to_text",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    usage_report_retrieve_speech_to_text_params.UsageReportRetrieveSpeechToTextParams,
                ),
            ),
            cast_to=UsageReportRetrieveSpeechToTextResponse,
        )


class UsageReportsResourceWithRawResponse:
    def __init__(self, usage_reports: UsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.retrieve_speech_to_text = to_raw_response_wrapper(
            usage_reports.retrieve_speech_to_text,
        )

    @cached_property
    def messaging(self) -> MessagingResourceWithRawResponse:
        return MessagingResourceWithRawResponse(self._usage_reports.messaging)

    @cached_property
    def number_lookup(self) -> NumberLookupResourceWithRawResponse:
        return NumberLookupResourceWithRawResponse(self._usage_reports.number_lookup)

    @cached_property
    def voice(self) -> VoiceResourceWithRawResponse:
        return VoiceResourceWithRawResponse(self._usage_reports.voice)


class AsyncUsageReportsResourceWithRawResponse:
    def __init__(self, usage_reports: AsyncUsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.retrieve_speech_to_text = async_to_raw_response_wrapper(
            usage_reports.retrieve_speech_to_text,
        )

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithRawResponse:
        return AsyncMessagingResourceWithRawResponse(self._usage_reports.messaging)

    @cached_property
    def number_lookup(self) -> AsyncNumberLookupResourceWithRawResponse:
        return AsyncNumberLookupResourceWithRawResponse(self._usage_reports.number_lookup)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithRawResponse:
        return AsyncVoiceResourceWithRawResponse(self._usage_reports.voice)


class UsageReportsResourceWithStreamingResponse:
    def __init__(self, usage_reports: UsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.retrieve_speech_to_text = to_streamed_response_wrapper(
            usage_reports.retrieve_speech_to_text,
        )

    @cached_property
    def messaging(self) -> MessagingResourceWithStreamingResponse:
        return MessagingResourceWithStreamingResponse(self._usage_reports.messaging)

    @cached_property
    def number_lookup(self) -> NumberLookupResourceWithStreamingResponse:
        return NumberLookupResourceWithStreamingResponse(self._usage_reports.number_lookup)

    @cached_property
    def voice(self) -> VoiceResourceWithStreamingResponse:
        return VoiceResourceWithStreamingResponse(self._usage_reports.voice)


class AsyncUsageReportsResourceWithStreamingResponse:
    def __init__(self, usage_reports: AsyncUsageReportsResource) -> None:
        self._usage_reports = usage_reports

        self.retrieve_speech_to_text = async_to_streamed_response_wrapper(
            usage_reports.retrieve_speech_to_text,
        )

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithStreamingResponse:
        return AsyncMessagingResourceWithStreamingResponse(self._usage_reports.messaging)

    @cached_property
    def number_lookup(self) -> AsyncNumberLookupResourceWithStreamingResponse:
        return AsyncNumberLookupResourceWithStreamingResponse(self._usage_reports.number_lookup)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithStreamingResponse:
        return AsyncVoiceResourceWithStreamingResponse(self._usage_reports.voice)
