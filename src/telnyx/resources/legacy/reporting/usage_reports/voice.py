# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncPerPagePagination, AsyncPerPagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.legacy.reporting.usage_reports import voice_list_params, voice_create_params
from .....types.legacy.reporting.usage_reports.voice_create_response import VoiceCreateResponse
from .....types.legacy.reporting.usage_reports.voice_delete_response import VoiceDeleteResponse
from .....types.legacy.reporting.usage_reports.voice_retrieve_response import VoiceRetrieveResponse
from .....types.legacy.reporting.usage_reports.cdr_usage_report_response_legacy import CdrUsageReportResponseLegacy

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        aggregation_type: int | Omit = omit,
        connections: Iterable[int] | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        product_breakdown: int | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCreateResponse:
        """
        Creates a new legacy usage V2 CDR report request with the specified filters

        Args:
          end_time: End time in ISO format

          start_time: Start time in ISO format

          aggregation_type: Aggregation type: All = 0, By Connections = 1, By Tags = 2, By Billing Group = 3

          connections: List of connections to filter by

          managed_accounts: List of managed accounts to include

          product_breakdown: Product breakdown type: No breakdown = 0, DID vs Toll-free = 1, Country = 2, DID
              vs Toll-free per Country = 3

          select_all_managed_accounts: Whether to select all managed accounts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legacy/reporting/usage_reports/voice",
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                    "aggregation_type": aggregation_type,
                    "connections": connections,
                    "managed_accounts": managed_accounts,
                    "product_breakdown": product_breakdown,
                    "select_all_managed_accounts": select_all_managed_accounts,
                },
                voice_create_params.VoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCreateResponse,
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
    ) -> VoiceRetrieveResponse:
        """
        Fetch single cdr usage report by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/legacy/reporting/usage_reports/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPerPagePagination[CdrUsageReportResponseLegacy]:
        """
        Fetch all previous requests for cdr usage reports.

        Args:
          page: Page number

          per_page: Size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/legacy/reporting/usage_reports/voice",
            page=SyncPerPagePagination[CdrUsageReportResponseLegacy],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    voice_list_params.VoiceListParams,
                ),
            ),
            model=CdrUsageReportResponseLegacy,
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
    ) -> VoiceDeleteResponse:
        """
        Deletes a specific V2 legacy usage CDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/legacy/reporting/usage_reports/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDeleteResponse,
        )


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        aggregation_type: int | Omit = omit,
        connections: Iterable[int] | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        product_breakdown: int | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCreateResponse:
        """
        Creates a new legacy usage V2 CDR report request with the specified filters

        Args:
          end_time: End time in ISO format

          start_time: Start time in ISO format

          aggregation_type: Aggregation type: All = 0, By Connections = 1, By Tags = 2, By Billing Group = 3

          connections: List of connections to filter by

          managed_accounts: List of managed accounts to include

          product_breakdown: Product breakdown type: No breakdown = 0, DID vs Toll-free = 1, Country = 2, DID
              vs Toll-free per Country = 3

          select_all_managed_accounts: Whether to select all managed accounts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legacy/reporting/usage_reports/voice",
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                    "aggregation_type": aggregation_type,
                    "connections": connections,
                    "managed_accounts": managed_accounts,
                    "product_breakdown": product_breakdown,
                    "select_all_managed_accounts": select_all_managed_accounts,
                },
                voice_create_params.VoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCreateResponse,
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
    ) -> VoiceRetrieveResponse:
        """
        Fetch single cdr usage report by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/legacy/reporting/usage_reports/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CdrUsageReportResponseLegacy, AsyncPerPagePagination[CdrUsageReportResponseLegacy]]:
        """
        Fetch all previous requests for cdr usage reports.

        Args:
          page: Page number

          per_page: Size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/legacy/reporting/usage_reports/voice",
            page=AsyncPerPagePagination[CdrUsageReportResponseLegacy],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    voice_list_params.VoiceListParams,
                ),
            ),
            model=CdrUsageReportResponseLegacy,
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
    ) -> VoiceDeleteResponse:
        """
        Deletes a specific V2 legacy usage CDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/legacy/reporting/usage_reports/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDeleteResponse,
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.create = to_raw_response_wrapper(
            voice.create,
        )
        self.retrieve = to_raw_response_wrapper(
            voice.retrieve,
        )
        self.list = to_raw_response_wrapper(
            voice.list,
        )
        self.delete = to_raw_response_wrapper(
            voice.delete,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.create = async_to_raw_response_wrapper(
            voice.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            voice.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            voice.list,
        )
        self.delete = async_to_raw_response_wrapper(
            voice.delete,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.create = to_streamed_response_wrapper(
            voice.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            voice.list,
        )
        self.delete = to_streamed_response_wrapper(
            voice.delete,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.create = async_to_streamed_response_wrapper(
            voice.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            voice.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            voice.delete,
        )
