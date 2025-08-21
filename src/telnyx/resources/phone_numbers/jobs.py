# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.phone_numbers import (
    job_list_params,
    job_delete_batch_params,
    job_update_batch_params,
    job_update_emergency_settings_batch_params,
)
from ...types.phone_numbers.job_list_response import JobListResponse
from ...types.phone_numbers.job_retrieve_response import JobRetrieveResponse
from ...types.phone_numbers.job_delete_batch_response import JobDeleteBatchResponse
from ...types.phone_numbers.job_update_batch_response import JobUpdateBatchResponse
from ...types.phone_numbers.update_voice_settings_param import UpdateVoiceSettingsParam
from ...types.phone_numbers.job_update_emergency_settings_batch_response import JobUpdateEmergencySettingsBatchResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobRetrieveResponse:
        """
        Retrieve a phone numbers job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/phone_numbers/jobs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: job_list_params.Filter | NotGiven = NOT_GIVEN,
        page: job_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
        """
        Lists the phone numbers jobs

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_numbers/jobs",
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
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    def delete_batch(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobDeleteBatchResponse:
        """Creates a new background job to delete a batch of numbers.

        At most one thousand
        numbers can be updated per API call.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_numbers/jobs/delete_phone_numbers",
            body=maybe_transform({"phone_numbers": phone_numbers}, job_delete_batch_params.JobDeleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobDeleteBatchResponse,
        )

    def update_batch(
        self,
        *,
        phone_numbers: List[str],
        filter: job_update_batch_params.Filter | NotGiven = NOT_GIVEN,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        external_pin: str | NotGiven = NOT_GIVEN,
        hd_voice_enabled: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        voice: UpdateVoiceSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateBatchResponse:
        """Creates a new background job to update a batch of numbers.

        At most one thousand
        numbers can be updated per API call. At least one of the updateable fields must
        be submitted. IMPORTANT: You must either specify filters (using the filter
        parameters) or specific phone numbers (using the phone_numbers parameter in the
        request body). If you specify filters, ALL phone numbers that match the given
        filters (up to 1000 at a time) will be updated. If you want to update only
        specific numbers, you must use the phone_numbers parameter in the request body.
        When using the phone_numbers parameter, ensure you follow the correct format as
        shown in the example (either phone number IDs or phone numbers in E164 format).

        Args:
          phone_numbers: Array of phone number ids and/or phone numbers in E164 format to update. This
              parameter is required if no filter parameters are provided. If you want to
              update specific numbers rather than all numbers matching a filter, you must use
              this parameter. Each item must be either a valid phone number ID or a phone
              number in E164 format (e.g., '+13127367254').

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[has_bundle], filter[tag], filter[connection_id], filter[phone_number],
              filter[status], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference]

          billing_group_id: Identifies the billing group associated with the phone number.

          connection_id: Identifies the connection associated with the phone number.

          customer_reference: A customer reference string for customer look ups.

          external_pin: If someone attempts to port your phone number away from Telnyx and your phone
              number has an external PIN set, we will attempt to verify that you provided the
              correct external PIN to the winning carrier. Note that not all carriers
              cooperate with this security mechanism.

          hd_voice_enabled: Indicates whether to enable or disable HD Voice on each phone number. HD Voice
              is a paid feature and may not be available for all phone numbers, more details
              about it can be found in the Telnyx support documentation.

          tags: A list of user-assigned tags to help organize phone numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_numbers/jobs/update_phone_numbers",
            body=maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "external_pin": external_pin,
                    "hd_voice_enabled": hd_voice_enabled,
                    "tags": tags,
                    "voice": voice,
                },
                job_update_batch_params.JobUpdateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, job_update_batch_params.JobUpdateBatchParams),
            ),
            cast_to=JobUpdateBatchResponse,
        )

    def update_emergency_settings_batch(
        self,
        *,
        emergency_enabled: bool,
        phone_numbers: List[str],
        emergency_address_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateEmergencySettingsBatchResponse:
        """
        Creates a background job to update the emergency settings of a collection of
        phone numbers. At most one thousand numbers can be updated per API call.

        Args:
          emergency_enabled: Indicates whether to enable or disable emergency services on the numbers.

          emergency_address_id: Identifies the address to be used with emergency services. Required if
              emergency_enabled is true, must be null or omitted if emergency_enabled is
              false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_numbers/jobs/update_emergency_settings",
            body=maybe_transform(
                {
                    "emergency_enabled": emergency_enabled,
                    "phone_numbers": phone_numbers,
                    "emergency_address_id": emergency_address_id,
                },
                job_update_emergency_settings_batch_params.JobUpdateEmergencySettingsBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobUpdateEmergencySettingsBatchResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobRetrieveResponse:
        """
        Retrieve a phone numbers job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/phone_numbers/jobs/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: job_list_params.Filter | NotGiven = NOT_GIVEN,
        page: job_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
        """
        Lists the phone numbers jobs

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_numbers/jobs",
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
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    async def delete_batch(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobDeleteBatchResponse:
        """Creates a new background job to delete a batch of numbers.

        At most one thousand
        numbers can be updated per API call.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_numbers/jobs/delete_phone_numbers",
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, job_delete_batch_params.JobDeleteBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobDeleteBatchResponse,
        )

    async def update_batch(
        self,
        *,
        phone_numbers: List[str],
        filter: job_update_batch_params.Filter | NotGiven = NOT_GIVEN,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        external_pin: str | NotGiven = NOT_GIVEN,
        hd_voice_enabled: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        voice: UpdateVoiceSettingsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateBatchResponse:
        """Creates a new background job to update a batch of numbers.

        At most one thousand
        numbers can be updated per API call. At least one of the updateable fields must
        be submitted. IMPORTANT: You must either specify filters (using the filter
        parameters) or specific phone numbers (using the phone_numbers parameter in the
        request body). If you specify filters, ALL phone numbers that match the given
        filters (up to 1000 at a time) will be updated. If you want to update only
        specific numbers, you must use the phone_numbers parameter in the request body.
        When using the phone_numbers parameter, ensure you follow the correct format as
        shown in the example (either phone number IDs or phone numbers in E164 format).

        Args:
          phone_numbers: Array of phone number ids and/or phone numbers in E164 format to update. This
              parameter is required if no filter parameters are provided. If you want to
              update specific numbers rather than all numbers matching a filter, you must use
              this parameter. Each item must be either a valid phone number ID or a phone
              number in E164 format (e.g., '+13127367254').

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[has_bundle], filter[tag], filter[connection_id], filter[phone_number],
              filter[status], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference]

          billing_group_id: Identifies the billing group associated with the phone number.

          connection_id: Identifies the connection associated with the phone number.

          customer_reference: A customer reference string for customer look ups.

          external_pin: If someone attempts to port your phone number away from Telnyx and your phone
              number has an external PIN set, we will attempt to verify that you provided the
              correct external PIN to the winning carrier. Note that not all carriers
              cooperate with this security mechanism.

          hd_voice_enabled: Indicates whether to enable or disable HD Voice on each phone number. HD Voice
              is a paid feature and may not be available for all phone numbers, more details
              about it can be found in the Telnyx support documentation.

          tags: A list of user-assigned tags to help organize phone numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_numbers/jobs/update_phone_numbers",
            body=await async_maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "external_pin": external_pin,
                    "hd_voice_enabled": hd_voice_enabled,
                    "tags": tags,
                    "voice": voice,
                },
                job_update_batch_params.JobUpdateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"filter": filter}, job_update_batch_params.JobUpdateBatchParams),
            ),
            cast_to=JobUpdateBatchResponse,
        )

    async def update_emergency_settings_batch(
        self,
        *,
        emergency_enabled: bool,
        phone_numbers: List[str],
        emergency_address_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobUpdateEmergencySettingsBatchResponse:
        """
        Creates a background job to update the emergency settings of a collection of
        phone numbers. At most one thousand numbers can be updated per API call.

        Args:
          emergency_enabled: Indicates whether to enable or disable emergency services on the numbers.

          emergency_address_id: Identifies the address to be used with emergency services. Required if
              emergency_enabled is true, must be null or omitted if emergency_enabled is
              false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_numbers/jobs/update_emergency_settings",
            body=await async_maybe_transform(
                {
                    "emergency_enabled": emergency_enabled,
                    "phone_numbers": phone_numbers,
                    "emergency_address_id": emergency_address_id,
                },
                job_update_emergency_settings_batch_params.JobUpdateEmergencySettingsBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobUpdateEmergencySettingsBatchResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.delete_batch = to_raw_response_wrapper(
            jobs.delete_batch,
        )
        self.update_batch = to_raw_response_wrapper(
            jobs.update_batch,
        )
        self.update_emergency_settings_batch = to_raw_response_wrapper(
            jobs.update_emergency_settings_batch,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.delete_batch = async_to_raw_response_wrapper(
            jobs.delete_batch,
        )
        self.update_batch = async_to_raw_response_wrapper(
            jobs.update_batch,
        )
        self.update_emergency_settings_batch = async_to_raw_response_wrapper(
            jobs.update_emergency_settings_batch,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete_batch = to_streamed_response_wrapper(
            jobs.delete_batch,
        )
        self.update_batch = to_streamed_response_wrapper(
            jobs.update_batch,
        )
        self.update_emergency_settings_batch = to_streamed_response_wrapper(
            jobs.update_emergency_settings_batch,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete_batch = async_to_streamed_response_wrapper(
            jobs.delete_batch,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            jobs.update_batch,
        )
        self.update_emergency_settings_batch = async_to_streamed_response_wrapper(
            jobs.update_emergency_settings_batch,
        )
