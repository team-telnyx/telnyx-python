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
from .....types.legacy.reporting.batch_detail_records import messaging_create_params
from .....types.legacy.reporting.batch_detail_records.messaging_list_response import MessagingListResponse
from .....types.legacy.reporting.batch_detail_records.messaging_create_response import MessagingCreateResponse
from .....types.legacy.reporting.batch_detail_records.messaging_delete_response import MessagingDeleteResponse
from .....types.legacy.reporting.batch_detail_records.messaging_retrieve_response import MessagingRetrieveResponse

__all__ = ["MessagingResource", "AsyncMessagingResource"]


class MessagingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        connections: Iterable[int] | Omit = omit,
        directions: Iterable[int] | Omit = omit,
        filters: Iterable[FilterParam] | Omit = omit,
        include_message_body: bool | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        profiles: SequenceNotStr[str] | Omit = omit,
        record_types: Iterable[int] | Omit = omit,
        report_name: str | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingCreateResponse:
        """
        Creates a new MDR detailed report request with the specified filters

        Args:
          end_time: End time in ISO format. Note: If end time includes the last 4 hours, some MDRs
              might not appear in this report, due to wait time for downstream message
              delivery confirmation

          start_time: Start time in ISO format

          connections: List of connections to filter by

          directions: List of directions to filter by (Inbound = 1, Outbound = 2)

          filters: List of filters to apply

          include_message_body: Whether to include message body in the report

          managed_accounts: List of managed accounts to include

          profiles: List of messaging profile IDs to filter by

          record_types: List of record types to filter by (Complete = 1, Incomplete = 2, Errors = 3)

          report_name: Name of the report

          select_all_managed_accounts: Whether to select all managed accounts

          timezone: Timezone for the report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legacy/reporting/batch_detail_records/messaging",
            body=maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                    "connections": connections,
                    "directions": directions,
                    "filters": filters,
                    "include_message_body": include_message_body,
                    "managed_accounts": managed_accounts,
                    "profiles": profiles,
                    "record_types": record_types,
                    "report_name": report_name,
                    "select_all_managed_accounts": select_all_managed_accounts,
                    "timezone": timezone,
                },
                messaging_create_params.MessagingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingCreateResponse,
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
    ) -> MessagingRetrieveResponse:
        """
        Retrieves a specific MDR detailed report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/legacy/reporting/batch_detail_records/messaging/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
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
    ) -> MessagingListResponse:
        """Retrieves all MDR detailed report requests for the authenticated user"""
        return self._get(
            "/legacy/reporting/batch_detail_records/messaging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingListResponse,
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
    ) -> MessagingDeleteResponse:
        """
        Deletes a specific MDR detailed report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/legacy/reporting/batch_detail_records/messaging/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingDeleteResponse,
        )


class AsyncMessagingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        connections: Iterable[int] | Omit = omit,
        directions: Iterable[int] | Omit = omit,
        filters: Iterable[FilterParam] | Omit = omit,
        include_message_body: bool | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        profiles: SequenceNotStr[str] | Omit = omit,
        record_types: Iterable[int] | Omit = omit,
        report_name: str | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingCreateResponse:
        """
        Creates a new MDR detailed report request with the specified filters

        Args:
          end_time: End time in ISO format. Note: If end time includes the last 4 hours, some MDRs
              might not appear in this report, due to wait time for downstream message
              delivery confirmation

          start_time: Start time in ISO format

          connections: List of connections to filter by

          directions: List of directions to filter by (Inbound = 1, Outbound = 2)

          filters: List of filters to apply

          include_message_body: Whether to include message body in the report

          managed_accounts: List of managed accounts to include

          profiles: List of messaging profile IDs to filter by

          record_types: List of record types to filter by (Complete = 1, Incomplete = 2, Errors = 3)

          report_name: Name of the report

          select_all_managed_accounts: Whether to select all managed accounts

          timezone: Timezone for the report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legacy/reporting/batch_detail_records/messaging",
            body=await async_maybe_transform(
                {
                    "end_time": end_time,
                    "start_time": start_time,
                    "connections": connections,
                    "directions": directions,
                    "filters": filters,
                    "include_message_body": include_message_body,
                    "managed_accounts": managed_accounts,
                    "profiles": profiles,
                    "record_types": record_types,
                    "report_name": report_name,
                    "select_all_managed_accounts": select_all_managed_accounts,
                    "timezone": timezone,
                },
                messaging_create_params.MessagingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingCreateResponse,
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
    ) -> MessagingRetrieveResponse:
        """
        Retrieves a specific MDR detailed report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/legacy/reporting/batch_detail_records/messaging/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
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
    ) -> MessagingListResponse:
        """Retrieves all MDR detailed report requests for the authenticated user"""
        return await self._get(
            "/legacy/reporting/batch_detail_records/messaging",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingListResponse,
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
    ) -> MessagingDeleteResponse:
        """
        Deletes a specific MDR detailed report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/legacy/reporting/batch_detail_records/messaging/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingDeleteResponse,
        )


class MessagingResourceWithRawResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

        self.create = to_raw_response_wrapper(
            messaging.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messaging.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messaging.list,
        )
        self.delete = to_raw_response_wrapper(
            messaging.delete,
        )


class AsyncMessagingResourceWithRawResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

        self.create = async_to_raw_response_wrapper(
            messaging.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messaging.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messaging.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messaging.delete,
        )


class MessagingResourceWithStreamingResponse:
    def __init__(self, messaging: MessagingResource) -> None:
        self._messaging = messaging

        self.create = to_streamed_response_wrapper(
            messaging.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messaging.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messaging.list,
        )
        self.delete = to_streamed_response_wrapper(
            messaging.delete,
        )


class AsyncMessagingResourceWithStreamingResponse:
    def __init__(self, messaging: AsyncMessagingResource) -> None:
        self._messaging = messaging

        self.create = async_to_streamed_response_wrapper(
            messaging.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messaging.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messaging.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messaging.delete,
        )
