# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from .....types.legacy.reporting.usage_reports import messaging_list_params, messaging_create_params
from .....types.legacy.reporting.usage_reports.messaging_create_response import MessagingCreateResponse
from .....types.legacy.reporting.usage_reports.messaging_delete_response import MessagingDeleteResponse
from .....types.legacy.reporting.usage_reports.messaging_retrieve_response import MessagingRetrieveResponse
from .....types.legacy.reporting.usage_reports.mdr_usage_report_response_legacy import MdrUsageReportResponseLegacy

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
        aggregation_type: int,
        end_time: Union[str, datetime] | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        profiles: SequenceNotStr[str] | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingCreateResponse:
        """
        Creates a new legacy usage V2 MDR report request with the specified filters

        Args:
          aggregation_type: Aggregation type: No aggregation = 0, By Messaging Profile = 1, By Tags = 2

          managed_accounts: List of managed accounts to include

          profiles: List of messaging profile IDs to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legacy/reporting/usage_reports/messaging",
            body=maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "end_time": end_time,
                    "managed_accounts": managed_accounts,
                    "profiles": profiles,
                    "select_all_managed_accounts": select_all_managed_accounts,
                    "start_time": start_time,
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
        Fetch single MDR usage report by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/legacy/reporting/usage_reports/messaging/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
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
    ) -> SyncPerPagePagination[MdrUsageReportResponseLegacy]:
        """
        Fetch all previous requests for MDR usage reports.

        Args:
          page: Page number

          per_page: Size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/legacy/reporting/usage_reports/messaging",
            page=SyncPerPagePagination[MdrUsageReportResponseLegacy],
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
                    messaging_list_params.MessagingListParams,
                ),
            ),
            model=MdrUsageReportResponseLegacy,
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
        Deletes a specific V2 legacy usage MDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/legacy/reporting/usage_reports/messaging/{id}",
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
        aggregation_type: int,
        end_time: Union[str, datetime] | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        profiles: SequenceNotStr[str] | Omit = omit,
        select_all_managed_accounts: bool | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagingCreateResponse:
        """
        Creates a new legacy usage V2 MDR report request with the specified filters

        Args:
          aggregation_type: Aggregation type: No aggregation = 0, By Messaging Profile = 1, By Tags = 2

          managed_accounts: List of managed accounts to include

          profiles: List of messaging profile IDs to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legacy/reporting/usage_reports/messaging",
            body=await async_maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "end_time": end_time,
                    "managed_accounts": managed_accounts,
                    "profiles": profiles,
                    "select_all_managed_accounts": select_all_managed_accounts,
                    "start_time": start_time,
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
        Fetch single MDR usage report by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/legacy/reporting/usage_reports/messaging/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingRetrieveResponse,
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
    ) -> AsyncPaginator[MdrUsageReportResponseLegacy, AsyncPerPagePagination[MdrUsageReportResponseLegacy]]:
        """
        Fetch all previous requests for MDR usage reports.

        Args:
          page: Page number

          per_page: Size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/legacy/reporting/usage_reports/messaging",
            page=AsyncPerPagePagination[MdrUsageReportResponseLegacy],
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
                    messaging_list_params.MessagingListParams,
                ),
            ),
            model=MdrUsageReportResponseLegacy,
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
        Deletes a specific V2 legacy usage MDR report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/legacy/reporting/usage_reports/messaging/{id}",
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
