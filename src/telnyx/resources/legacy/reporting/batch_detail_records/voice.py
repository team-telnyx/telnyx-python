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
from ....._base_client import make_request_options
from .....types.legacy.reporting.filter_param import FilterParam
from .....types.legacy.reporting.batch_detail_records import voice_create_params
from .....types.legacy.reporting.batch_detail_records.voice_list_response import VoiceListResponse
from .....types.legacy.reporting.batch_detail_records.voice_create_response import VoiceCreateResponse
from .....types.legacy.reporting.batch_detail_records.voice_delete_response import VoiceDeleteResponse
from .....types.legacy.reporting.batch_detail_records.voice_retrieve_response import VoiceRetrieveResponse
from .....types.legacy.reporting.batch_detail_records.voice_retrieve_fields_response import VoiceRetrieveFieldsResponse

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
        call_types: Iterable[int] | Omit = omit,
        connections: Iterable[int] | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        filters: Iterable[FilterParam] | Omit = omit,
        include_all_metadata: bool | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        record_types: Iterable[int] | Omit = omit,
        report_name: str | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        source: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCreateResponse:
        """
        Creates a new CDR report request with the specified filters

        Args:
          end_time: End time in ISO format

          start_time: Start time in ISO format

          call_types: List of call types to filter by (Inbound = 1, Outbound = 2)

          connections: List of connections to filter by

          fields: Set of fields to include in the report

          filters: List of filters to apply

          include_all_metadata: Whether to include all metadata

          managed_accounts: List of managed accounts to include

          record_types: List of record types to filter by (Complete = 1, Incomplete = 2, Errors = 3)

          report_name: Name of the report

          select_all_managed_accounts: Whether to select all managed accounts

          source: Source of the report. Valid values: calls (default), call-control, fax-api,
              webrtc

          timezone: Timezone for the report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legacy/reporting/batch_detail_records/voice",
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                    "call_types": call_types,
                    "connections": connections,
                    "fields": fields,
                    "filters": filters,
                    "include_all_metadata": include_all_metadata,
                    "managed_accounts": managed_accounts,
                    "record_types": record_types,
                    "report_name": report_name,
                    "select_all_managed_accounts": select_all_managed_accounts,
                    "source": source,
                    "timezone": timezone,
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
        Retrieves a specific CDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/legacy/reporting/batch_detail_records/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceListResponse:
        """Retrieves all CDR report requests for the authenticated user"""
        return self._get(
            "/legacy/reporting/batch_detail_records/voice",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceListResponse,
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
        Deletes a specific CDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/legacy/reporting/batch_detail_records/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDeleteResponse,
        )

    def retrieve_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceRetrieveFieldsResponse:
        """Retrieves all available fields that can be used in CDR reports"""
        return self._get(
            "/legacy/reporting/batch_detail_records/voice/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveFieldsResponse,
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
        call_types: Iterable[int] | Omit = omit,
        connections: Iterable[int] | Omit = omit,
        fields: SequenceNotStr[str] | Omit = omit,
        filters: Iterable[FilterParam] | Omit = omit,
        include_all_metadata: bool | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        record_types: Iterable[int] | Omit = omit,
        report_name: str | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        source: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCreateResponse:
        """
        Creates a new CDR report request with the specified filters

        Args:
          end_time: End time in ISO format

          start_time: Start time in ISO format

          call_types: List of call types to filter by (Inbound = 1, Outbound = 2)

          connections: List of connections to filter by

          fields: Set of fields to include in the report

          filters: List of filters to apply

          include_all_metadata: Whether to include all metadata

          managed_accounts: List of managed accounts to include

          record_types: List of record types to filter by (Complete = 1, Incomplete = 2, Errors = 3)

          report_name: Name of the report

          select_all_managed_accounts: Whether to select all managed accounts

          source: Source of the report. Valid values: calls (default), call-control, fax-api,
              webrtc

          timezone: Timezone for the report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legacy/reporting/batch_detail_records/voice",
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                    "call_types": call_types,
                    "connections": connections,
                    "fields": fields,
                    "filters": filters,
                    "include_all_metadata": include_all_metadata,
                    "managed_accounts": managed_accounts,
                    "record_types": record_types,
                    "report_name": report_name,
                    "select_all_managed_accounts": select_all_managed_accounts,
                    "source": source,
                    "timezone": timezone,
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
        Retrieves a specific CDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/legacy/reporting/batch_detail_records/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceListResponse:
        """Retrieves all CDR report requests for the authenticated user"""
        return await self._get(
            "/legacy/reporting/batch_detail_records/voice",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceListResponse,
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
        Deletes a specific CDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/legacy/reporting/batch_detail_records/voice/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDeleteResponse,
        )

    async def retrieve_fields(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceRetrieveFieldsResponse:
        """Retrieves all available fields that can be used in CDR reports"""
        return await self._get(
            "/legacy/reporting/batch_detail_records/voice/fields",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceRetrieveFieldsResponse,
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
        self.retrieve_fields = to_raw_response_wrapper(
            voice.retrieve_fields,
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
        self.retrieve_fields = async_to_raw_response_wrapper(
            voice.retrieve_fields,
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
        self.retrieve_fields = to_streamed_response_wrapper(
            voice.retrieve_fields,
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
        self.retrieve_fields = async_to_streamed_response_wrapper(
            voice.retrieve_fields,
        )
