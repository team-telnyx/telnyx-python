# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    customer_service_record_list_params,
    customer_service_record_create_params,
    customer_service_record_verify_phone_number_coverage_params,
)
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
from ..types.customer_service_record_list_response import CustomerServiceRecordListResponse
from ..types.customer_service_record_create_response import CustomerServiceRecordCreateResponse
from ..types.customer_service_record_retrieve_response import CustomerServiceRecordRetrieveResponse
from ..types.customer_service_record_verify_phone_number_coverage_response import (
    CustomerServiceRecordVerifyPhoneNumberCoverageResponse,
)

__all__ = ["CustomerServiceRecordsResource", "AsyncCustomerServiceRecordsResource"]


class CustomerServiceRecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomerServiceRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CustomerServiceRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerServiceRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CustomerServiceRecordsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number: str,
        additional_data: customer_service_record_create_params.AdditionalData | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordCreateResponse:
        """
        Create a new customer service record for the provided phone number.

        Args:
          phone_number: A valid US phone number in E164 format.

          webhook_url: Callback URL to receive webhook notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/customer_service_records",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "additional_data": additional_data,
                    "webhook_url": webhook_url,
                },
                customer_service_record_create_params.CustomerServiceRecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerServiceRecordCreateResponse,
        )

    def retrieve(
        self,
        customer_service_record_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordRetrieveResponse:
        """
        Get a specific customer service record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_service_record_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_service_record_id` but received {customer_service_record_id!r}"
            )
        return self._get(
            f"/customer_service_records/{customer_service_record_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerServiceRecordRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: customer_service_record_list_params.Filter | NotGiven = NOT_GIVEN,
        page: customer_service_record_list_params.Page | NotGiven = NOT_GIVEN,
        sort: customer_service_record_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordListResponse:
        """
        List customer service records.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number][eq], filter[phone_number][in][], filter[status][eq],
              filter[status][in][], filter[created_at][lt], filter[created_at][gt]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/customer_service_records",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    customer_service_record_list_params.CustomerServiceRecordListParams,
                ),
            ),
            cast_to=CustomerServiceRecordListResponse,
        )

    def verify_phone_number_coverage(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordVerifyPhoneNumberCoverageResponse:
        """
        Verify the coverage for a list of phone numbers.

        Args:
          phone_numbers: The phone numbers list to be verified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/customer_service_records/phone_number_coverages",
            body=maybe_transform(
                {"phone_numbers": phone_numbers},
                customer_service_record_verify_phone_number_coverage_params.CustomerServiceRecordVerifyPhoneNumberCoverageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerServiceRecordVerifyPhoneNumberCoverageResponse,
        )


class AsyncCustomerServiceRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomerServiceRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerServiceRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerServiceRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCustomerServiceRecordsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number: str,
        additional_data: customer_service_record_create_params.AdditionalData | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordCreateResponse:
        """
        Create a new customer service record for the provided phone number.

        Args:
          phone_number: A valid US phone number in E164 format.

          webhook_url: Callback URL to receive webhook notifications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/customer_service_records",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "additional_data": additional_data,
                    "webhook_url": webhook_url,
                },
                customer_service_record_create_params.CustomerServiceRecordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerServiceRecordCreateResponse,
        )

    async def retrieve(
        self,
        customer_service_record_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordRetrieveResponse:
        """
        Get a specific customer service record.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_service_record_id:
            raise ValueError(
                f"Expected a non-empty value for `customer_service_record_id` but received {customer_service_record_id!r}"
            )
        return await self._get(
            f"/customer_service_records/{customer_service_record_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerServiceRecordRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: customer_service_record_list_params.Filter | NotGiven = NOT_GIVEN,
        page: customer_service_record_list_params.Page | NotGiven = NOT_GIVEN,
        sort: customer_service_record_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordListResponse:
        """
        List customer service records.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number][eq], filter[phone_number][in][], filter[status][eq],
              filter[status][in][], filter[created_at][lt], filter[created_at][gt]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/customer_service_records",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    customer_service_record_list_params.CustomerServiceRecordListParams,
                ),
            ),
            cast_to=CustomerServiceRecordListResponse,
        )

    async def verify_phone_number_coverage(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerServiceRecordVerifyPhoneNumberCoverageResponse:
        """
        Verify the coverage for a list of phone numbers.

        Args:
          phone_numbers: The phone numbers list to be verified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/customer_service_records/phone_number_coverages",
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers},
                customer_service_record_verify_phone_number_coverage_params.CustomerServiceRecordVerifyPhoneNumberCoverageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerServiceRecordVerifyPhoneNumberCoverageResponse,
        )


class CustomerServiceRecordsResourceWithRawResponse:
    def __init__(self, customer_service_records: CustomerServiceRecordsResource) -> None:
        self._customer_service_records = customer_service_records

        self.create = to_raw_response_wrapper(
            customer_service_records.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customer_service_records.retrieve,
        )
        self.list = to_raw_response_wrapper(
            customer_service_records.list,
        )
        self.verify_phone_number_coverage = to_raw_response_wrapper(
            customer_service_records.verify_phone_number_coverage,
        )


class AsyncCustomerServiceRecordsResourceWithRawResponse:
    def __init__(self, customer_service_records: AsyncCustomerServiceRecordsResource) -> None:
        self._customer_service_records = customer_service_records

        self.create = async_to_raw_response_wrapper(
            customer_service_records.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customer_service_records.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            customer_service_records.list,
        )
        self.verify_phone_number_coverage = async_to_raw_response_wrapper(
            customer_service_records.verify_phone_number_coverage,
        )


class CustomerServiceRecordsResourceWithStreamingResponse:
    def __init__(self, customer_service_records: CustomerServiceRecordsResource) -> None:
        self._customer_service_records = customer_service_records

        self.create = to_streamed_response_wrapper(
            customer_service_records.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customer_service_records.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            customer_service_records.list,
        )
        self.verify_phone_number_coverage = to_streamed_response_wrapper(
            customer_service_records.verify_phone_number_coverage,
        )


class AsyncCustomerServiceRecordsResourceWithStreamingResponse:
    def __init__(self, customer_service_records: AsyncCustomerServiceRecordsResource) -> None:
        self._customer_service_records = customer_service_records

        self.create = async_to_streamed_response_wrapper(
            customer_service_records.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customer_service_records.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            customer_service_records.list,
        )
        self.verify_phone_number_coverage = async_to_streamed_response_wrapper(
            customer_service_records.verify_phone_number_coverage,
        )
