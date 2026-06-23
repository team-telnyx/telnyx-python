# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import voice_sdk_call_report_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.voice_sdk_call_report import VoiceSDKCallReport
from ..types.voice_sdk_call_report_retrieve_response import VoiceSDKCallReportRetrieveResponse

__all__ = ["VoiceSDKCallReportsResource", "AsyncVoiceSDKCallReportsResource"]


class VoiceSDKCallReportsResource(SyncAPIResource):
    """
    Retrieve raw Voice SDK call report stats payloads for WebRTC call troubleshooting.
    """

    @cached_property
    def with_raw_response(self) -> VoiceSDKCallReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VoiceSDKCallReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceSDKCallReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VoiceSDKCallReportsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSDKCallReportRetrieveResponse:
        """
        Returns raw call report stats JSON payloads stored for the authenticated user
        and `call_id`. The user is derived from Telnyx authentication, not from request
        parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            path_template("/voice_sdk_call_reports/{call_id}", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceSDKCallReportRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["asc", "desc", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[VoiceSDKCallReport]:
        """
        Returns paginated raw call report stats JSON payloads stored for the
        authenticated user. The user is derived from Telnyx authentication, not from
        request parameters.

        Args:
          sort: Set the order of the results by creation date. `asc` and `created_at` sort
              oldest reports first; `desc` and `-created_at` sort newest reports first. If not
              given, results are sorted by creation date in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/voice_sdk_call_reports",
            page=SyncDefaultFlatPagination[VoiceSDKCallReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    voice_sdk_call_report_list_params.VoiceSDKCallReportListParams,
                ),
            ),
            model=VoiceSDKCallReport,
        )


class AsyncVoiceSDKCallReportsResource(AsyncAPIResource):
    """
    Retrieve raw Voice SDK call report stats payloads for WebRTC call troubleshooting.
    """

    @cached_property
    def with_raw_response(self) -> AsyncVoiceSDKCallReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceSDKCallReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceSDKCallReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVoiceSDKCallReportsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSDKCallReportRetrieveResponse:
        """
        Returns raw call report stats JSON payloads stored for the authenticated user
        and `call_id`. The user is derived from Telnyx authentication, not from request
        parameters.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            path_template("/voice_sdk_call_reports/{call_id}", call_id=call_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceSDKCallReportRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["asc", "desc", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VoiceSDKCallReport, AsyncDefaultFlatPagination[VoiceSDKCallReport]]:
        """
        Returns paginated raw call report stats JSON payloads stored for the
        authenticated user. The user is derived from Telnyx authentication, not from
        request parameters.

        Args:
          sort: Set the order of the results by creation date. `asc` and `created_at` sort
              oldest reports first; `desc` and `-created_at` sort newest reports first. If not
              given, results are sorted by creation date in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/voice_sdk_call_reports",
            page=AsyncDefaultFlatPagination[VoiceSDKCallReport],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    voice_sdk_call_report_list_params.VoiceSDKCallReportListParams,
                ),
            ),
            model=VoiceSDKCallReport,
        )


class VoiceSDKCallReportsResourceWithRawResponse:
    def __init__(self, voice_sdk_call_reports: VoiceSDKCallReportsResource) -> None:
        self._voice_sdk_call_reports = voice_sdk_call_reports

        self.retrieve = to_raw_response_wrapper(
            voice_sdk_call_reports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            voice_sdk_call_reports.list,
        )


class AsyncVoiceSDKCallReportsResourceWithRawResponse:
    def __init__(self, voice_sdk_call_reports: AsyncVoiceSDKCallReportsResource) -> None:
        self._voice_sdk_call_reports = voice_sdk_call_reports

        self.retrieve = async_to_raw_response_wrapper(
            voice_sdk_call_reports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            voice_sdk_call_reports.list,
        )


class VoiceSDKCallReportsResourceWithStreamingResponse:
    def __init__(self, voice_sdk_call_reports: VoiceSDKCallReportsResource) -> None:
        self._voice_sdk_call_reports = voice_sdk_call_reports

        self.retrieve = to_streamed_response_wrapper(
            voice_sdk_call_reports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            voice_sdk_call_reports.list,
        )


class AsyncVoiceSDKCallReportsResourceWithStreamingResponse:
    def __init__(self, voice_sdk_call_reports: AsyncVoiceSDKCallReportsResource) -> None:
        self._voice_sdk_call_reports = voice_sdk_call_reports

        self.retrieve = async_to_streamed_response_wrapper(
            voice_sdk_call_reports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            voice_sdk_call_reports.list,
        )
