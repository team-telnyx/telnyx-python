# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.legacy.reporting.usage_reports import number_lookup_create_params
from .....types.legacy.reporting.usage_reports.number_lookup_list_response import NumberLookupListResponse
from .....types.legacy.reporting.usage_reports.number_lookup_create_response import NumberLookupCreateResponse
from .....types.legacy.reporting.usage_reports.number_lookup_retrieve_response import NumberLookupRetrieveResponse

__all__ = ["NumberLookupResource", "AsyncNumberLookupResource"]


class NumberLookupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumberLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumberLookupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aggregation_type: Literal["ALL", "BY_ORGANIZATION_MEMBER"] | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberLookupCreateResponse:
        """
        Submit a new telco data usage report

        Args:
          aggregation_type: Type of aggregation for the report

          end_date: End date for the usage report

          managed_accounts: List of managed accounts to include in the report

          start_date: Start date for the usage report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legacy/reporting/usage_reports/number_lookup",
            body=maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "end_date": end_date,
                    "managed_accounts": managed_accounts,
                    "start_date": start_date,
                },
                number_lookup_create_params.NumberLookupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberLookupCreateResponse,
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
    ) -> NumberLookupRetrieveResponse:
        """
        Retrieve a specific telco data usage report by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/legacy/reporting/usage_reports/number_lookup/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberLookupRetrieveResponse,
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
    ) -> NumberLookupListResponse:
        """Retrieve a paginated list of telco data usage reports"""
        return self._get(
            "/legacy/reporting/usage_reports/number_lookup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberLookupListResponse,
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
    ) -> None:
        """
        Delete a specific telco data usage report by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/legacy/reporting/usage_reports/number_lookup/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNumberLookupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumberLookupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aggregation_type: Literal["ALL", "BY_ORGANIZATION_MEMBER"] | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        managed_accounts: SequenceNotStr[str] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberLookupCreateResponse:
        """
        Submit a new telco data usage report

        Args:
          aggregation_type: Type of aggregation for the report

          end_date: End date for the usage report

          managed_accounts: List of managed accounts to include in the report

          start_date: Start date for the usage report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legacy/reporting/usage_reports/number_lookup",
            body=await async_maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "end_date": end_date,
                    "managed_accounts": managed_accounts,
                    "start_date": start_date,
                },
                number_lookup_create_params.NumberLookupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberLookupCreateResponse,
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
    ) -> NumberLookupRetrieveResponse:
        """
        Retrieve a specific telco data usage report by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/legacy/reporting/usage_reports/number_lookup/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberLookupRetrieveResponse,
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
    ) -> NumberLookupListResponse:
        """Retrieve a paginated list of telco data usage reports"""
        return await self._get(
            "/legacy/reporting/usage_reports/number_lookup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberLookupListResponse,
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
    ) -> None:
        """
        Delete a specific telco data usage report by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/legacy/reporting/usage_reports/number_lookup/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NumberLookupResourceWithRawResponse:
    def __init__(self, number_lookup: NumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.create = to_raw_response_wrapper(
            number_lookup.create,
        )
        self.retrieve = to_raw_response_wrapper(
            number_lookup.retrieve,
        )
        self.list = to_raw_response_wrapper(
            number_lookup.list,
        )
        self.delete = to_raw_response_wrapper(
            number_lookup.delete,
        )


class AsyncNumberLookupResourceWithRawResponse:
    def __init__(self, number_lookup: AsyncNumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.create = async_to_raw_response_wrapper(
            number_lookup.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            number_lookup.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            number_lookup.list,
        )
        self.delete = async_to_raw_response_wrapper(
            number_lookup.delete,
        )


class NumberLookupResourceWithStreamingResponse:
    def __init__(self, number_lookup: NumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.create = to_streamed_response_wrapper(
            number_lookup.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            number_lookup.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            number_lookup.list,
        )
        self.delete = to_streamed_response_wrapper(
            number_lookup.delete,
        )


class AsyncNumberLookupResourceWithStreamingResponse:
    def __init__(self, number_lookup: AsyncNumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.create = async_to_streamed_response_wrapper(
            number_lookup.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            number_lookup.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            number_lookup.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            number_lookup.delete,
        )
