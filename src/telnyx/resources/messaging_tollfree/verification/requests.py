# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.messaging_tollfree.verification import (
    Volume,
    UseCaseCategories,
    TfVerificationStatus,
    request_list_params,
    request_create_params,
    request_update_params,
)
from ....types.messaging_tollfree.verification.volume import Volume
from ....types.messaging_tollfree.verification.url_param import URLParam
from ....types.messaging_tollfree.verification.use_case_categories import UseCaseCategories
from ....types.messaging_tollfree.verification.request_list_response import RequestListResponse
from ....types.messaging_tollfree.verification.tf_phone_number_param import TfPhoneNumberParam
from ....types.messaging_tollfree.verification.tf_verification_status import TfVerificationStatus
from ....types.messaging_tollfree.verification.verification_request_egress import VerificationRequestEgress
from ....types.messaging_tollfree.verification.verification_request_status import VerificationRequestStatus

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        additional_information: str,
        business_addr1: str,
        business_city: str,
        business_contact_email: str,
        business_contact_first_name: str,
        business_contact_last_name: str,
        business_contact_phone: str,
        business_name: str,
        business_state: str,
        business_zip: str,
        corporate_website: str,
        isv_reseller: str,
        message_volume: Volume,
        opt_in_workflow: str,
        opt_in_workflow_image_urls: Iterable[URLParam],
        phone_numbers: Iterable[TfPhoneNumberParam],
        production_message_content: str,
        use_case: UseCaseCategories,
        use_case_summary: str,
        business_addr2: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRequestEgress:
        """
        Submit a new tollfree verification request

        Args:
          additional_information: Any additional information

          business_addr1: Line 1 of the business address

          business_city: The city of the business address; the first letter should be capitalized

          business_contact_email: The email address of the business contact

          business_contact_first_name: First name of the business contact; there are no specific requirements on
              formatting

          business_contact_last_name: Last name of the business contact; there are no specific requirements on
              formatting

          business_contact_phone: The phone number of the business contact in E.164 format

          business_name: Name of the business; there are no specific formatting requirements

          business_state: The full name of the state (not the 2 letter code) of the business address; the
              first letter should be capitalized

          business_zip: The ZIP code of the business address

          corporate_website: A URL, including the scheme, pointing to the corporate website

          isv_reseller: ISV name

          message_volume: Message Volume Enums

          opt_in_workflow: Human-readable description of how end users will opt into receiving messages
              from the given phone numbers

          opt_in_workflow_image_urls: Images showing the opt-in workflow

          phone_numbers: The phone numbers to request the verification of

          production_message_content: An example of a message that will be sent from the given phone numbers

          use_case: Tollfree usecase categories

          use_case_summary: Human-readable summary of the desired use-case

          business_addr2: Line 2 of the business address

          webhook_url: URL that should receive webhooks relating to this verification request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messaging_tollfree/verification/requests",
            body=maybe_transform(
                {
                    "additional_information": additional_information,
                    "business_addr1": business_addr1,
                    "business_city": business_city,
                    "business_contact_email": business_contact_email,
                    "business_contact_first_name": business_contact_first_name,
                    "business_contact_last_name": business_contact_last_name,
                    "business_contact_phone": business_contact_phone,
                    "business_name": business_name,
                    "business_state": business_state,
                    "business_zip": business_zip,
                    "corporate_website": corporate_website,
                    "isv_reseller": isv_reseller,
                    "message_volume": message_volume,
                    "opt_in_workflow": opt_in_workflow,
                    "opt_in_workflow_image_urls": opt_in_workflow_image_urls,
                    "phone_numbers": phone_numbers,
                    "production_message_content": production_message_content,
                    "use_case": use_case,
                    "use_case_summary": use_case_summary,
                    "business_addr2": business_addr2,
                    "webhook_url": webhook_url,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRequestEgress,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRequestStatus:
        """
        Get a single verification request by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/messaging_tollfree/verification/requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRequestStatus,
        )

    def update(
        self,
        id: str,
        *,
        additional_information: str,
        business_addr1: str,
        business_city: str,
        business_contact_email: str,
        business_contact_first_name: str,
        business_contact_last_name: str,
        business_contact_phone: str,
        business_name: str,
        business_state: str,
        business_zip: str,
        corporate_website: str,
        isv_reseller: str,
        message_volume: Volume,
        opt_in_workflow: str,
        opt_in_workflow_image_urls: Iterable[URLParam],
        phone_numbers: Iterable[TfPhoneNumberParam],
        production_message_content: str,
        use_case: UseCaseCategories,
        use_case_summary: str,
        business_addr2: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRequestEgress:
        """Update an existing tollfree verification request.

        This is particularly useful
        when there are pending customer actions to be taken.

        Args:
          additional_information: Any additional information

          business_addr1: Line 1 of the business address

          business_city: The city of the business address; the first letter should be capitalized

          business_contact_email: The email address of the business contact

          business_contact_first_name: First name of the business contact; there are no specific requirements on
              formatting

          business_contact_last_name: Last name of the business contact; there are no specific requirements on
              formatting

          business_contact_phone: The phone number of the business contact in E.164 format

          business_name: Name of the business; there are no specific formatting requirements

          business_state: The full name of the state (not the 2 letter code) of the business address; the
              first letter should be capitalized

          business_zip: The ZIP code of the business address

          corporate_website: A URL, including the scheme, pointing to the corporate website

          isv_reseller: ISV name

          message_volume: Message Volume Enums

          opt_in_workflow: Human-readable description of how end users will opt into receiving messages
              from the given phone numbers

          opt_in_workflow_image_urls: Images showing the opt-in workflow

          phone_numbers: The phone numbers to request the verification of

          production_message_content: An example of a message that will be sent from the given phone numbers

          use_case: Tollfree usecase categories

          use_case_summary: Human-readable summary of the desired use-case

          business_addr2: Line 2 of the business address

          webhook_url: URL that should receive webhooks relating to this verification request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/messaging_tollfree/verification/requests/{id}",
            body=maybe_transform(
                {
                    "additional_information": additional_information,
                    "business_addr1": business_addr1,
                    "business_city": business_city,
                    "business_contact_email": business_contact_email,
                    "business_contact_first_name": business_contact_first_name,
                    "business_contact_last_name": business_contact_last_name,
                    "business_contact_phone": business_contact_phone,
                    "business_name": business_name,
                    "business_state": business_state,
                    "business_zip": business_zip,
                    "corporate_website": corporate_website,
                    "isv_reseller": isv_reseller,
                    "message_volume": message_volume,
                    "opt_in_workflow": opt_in_workflow,
                    "opt_in_workflow_image_urls": opt_in_workflow_image_urls,
                    "phone_numbers": phone_numbers,
                    "production_message_content": production_message_content,
                    "use_case": use_case,
                    "use_case_summary": use_case_summary,
                    "business_addr2": business_addr2,
                    "webhook_url": webhook_url,
                },
                request_update_params.RequestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRequestEgress,
        )

    def list(
        self,
        *,
        page: int,
        page_size: int,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        status: TfVerificationStatus | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestListResponse:
        """
        Get a list of previously-submitted tollfree verification requests

        Args:
          page_size: Request this many records per page

                      This value is automatically clamped if the provided value is too large.

          status: Tollfree verification status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/messaging_tollfree/verification/requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "date_end": date_end,
                        "date_start": date_start,
                        "phone_number": phone_number,
                        "status": status,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            cast_to=RequestListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a verification request

        A request may only be deleted when when the request is in the "rejected" state.

        - `HTTP 200`: request successfully deleted
        - `HTTP 400`: request exists but can't be deleted (i.e. not rejected)
        - `HTTP 404`: request unknown or already deleted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/messaging_tollfree/verification/requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        additional_information: str,
        business_addr1: str,
        business_city: str,
        business_contact_email: str,
        business_contact_first_name: str,
        business_contact_last_name: str,
        business_contact_phone: str,
        business_name: str,
        business_state: str,
        business_zip: str,
        corporate_website: str,
        isv_reseller: str,
        message_volume: Volume,
        opt_in_workflow: str,
        opt_in_workflow_image_urls: Iterable[URLParam],
        phone_numbers: Iterable[TfPhoneNumberParam],
        production_message_content: str,
        use_case: UseCaseCategories,
        use_case_summary: str,
        business_addr2: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRequestEgress:
        """
        Submit a new tollfree verification request

        Args:
          additional_information: Any additional information

          business_addr1: Line 1 of the business address

          business_city: The city of the business address; the first letter should be capitalized

          business_contact_email: The email address of the business contact

          business_contact_first_name: First name of the business contact; there are no specific requirements on
              formatting

          business_contact_last_name: Last name of the business contact; there are no specific requirements on
              formatting

          business_contact_phone: The phone number of the business contact in E.164 format

          business_name: Name of the business; there are no specific formatting requirements

          business_state: The full name of the state (not the 2 letter code) of the business address; the
              first letter should be capitalized

          business_zip: The ZIP code of the business address

          corporate_website: A URL, including the scheme, pointing to the corporate website

          isv_reseller: ISV name

          message_volume: Message Volume Enums

          opt_in_workflow: Human-readable description of how end users will opt into receiving messages
              from the given phone numbers

          opt_in_workflow_image_urls: Images showing the opt-in workflow

          phone_numbers: The phone numbers to request the verification of

          production_message_content: An example of a message that will be sent from the given phone numbers

          use_case: Tollfree usecase categories

          use_case_summary: Human-readable summary of the desired use-case

          business_addr2: Line 2 of the business address

          webhook_url: URL that should receive webhooks relating to this verification request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messaging_tollfree/verification/requests",
            body=await async_maybe_transform(
                {
                    "additional_information": additional_information,
                    "business_addr1": business_addr1,
                    "business_city": business_city,
                    "business_contact_email": business_contact_email,
                    "business_contact_first_name": business_contact_first_name,
                    "business_contact_last_name": business_contact_last_name,
                    "business_contact_phone": business_contact_phone,
                    "business_name": business_name,
                    "business_state": business_state,
                    "business_zip": business_zip,
                    "corporate_website": corporate_website,
                    "isv_reseller": isv_reseller,
                    "message_volume": message_volume,
                    "opt_in_workflow": opt_in_workflow,
                    "opt_in_workflow_image_urls": opt_in_workflow_image_urls,
                    "phone_numbers": phone_numbers,
                    "production_message_content": production_message_content,
                    "use_case": use_case,
                    "use_case_summary": use_case_summary,
                    "business_addr2": business_addr2,
                    "webhook_url": webhook_url,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRequestEgress,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRequestStatus:
        """
        Get a single verification request by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/messaging_tollfree/verification/requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRequestStatus,
        )

    async def update(
        self,
        id: str,
        *,
        additional_information: str,
        business_addr1: str,
        business_city: str,
        business_contact_email: str,
        business_contact_first_name: str,
        business_contact_last_name: str,
        business_contact_phone: str,
        business_name: str,
        business_state: str,
        business_zip: str,
        corporate_website: str,
        isv_reseller: str,
        message_volume: Volume,
        opt_in_workflow: str,
        opt_in_workflow_image_urls: Iterable[URLParam],
        phone_numbers: Iterable[TfPhoneNumberParam],
        production_message_content: str,
        use_case: UseCaseCategories,
        use_case_summary: str,
        business_addr2: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationRequestEgress:
        """Update an existing tollfree verification request.

        This is particularly useful
        when there are pending customer actions to be taken.

        Args:
          additional_information: Any additional information

          business_addr1: Line 1 of the business address

          business_city: The city of the business address; the first letter should be capitalized

          business_contact_email: The email address of the business contact

          business_contact_first_name: First name of the business contact; there are no specific requirements on
              formatting

          business_contact_last_name: Last name of the business contact; there are no specific requirements on
              formatting

          business_contact_phone: The phone number of the business contact in E.164 format

          business_name: Name of the business; there are no specific formatting requirements

          business_state: The full name of the state (not the 2 letter code) of the business address; the
              first letter should be capitalized

          business_zip: The ZIP code of the business address

          corporate_website: A URL, including the scheme, pointing to the corporate website

          isv_reseller: ISV name

          message_volume: Message Volume Enums

          opt_in_workflow: Human-readable description of how end users will opt into receiving messages
              from the given phone numbers

          opt_in_workflow_image_urls: Images showing the opt-in workflow

          phone_numbers: The phone numbers to request the verification of

          production_message_content: An example of a message that will be sent from the given phone numbers

          use_case: Tollfree usecase categories

          use_case_summary: Human-readable summary of the desired use-case

          business_addr2: Line 2 of the business address

          webhook_url: URL that should receive webhooks relating to this verification request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/messaging_tollfree/verification/requests/{id}",
            body=await async_maybe_transform(
                {
                    "additional_information": additional_information,
                    "business_addr1": business_addr1,
                    "business_city": business_city,
                    "business_contact_email": business_contact_email,
                    "business_contact_first_name": business_contact_first_name,
                    "business_contact_last_name": business_contact_last_name,
                    "business_contact_phone": business_contact_phone,
                    "business_name": business_name,
                    "business_state": business_state,
                    "business_zip": business_zip,
                    "corporate_website": corporate_website,
                    "isv_reseller": isv_reseller,
                    "message_volume": message_volume,
                    "opt_in_workflow": opt_in_workflow,
                    "opt_in_workflow_image_urls": opt_in_workflow_image_urls,
                    "phone_numbers": phone_numbers,
                    "production_message_content": production_message_content,
                    "use_case": use_case,
                    "use_case_summary": use_case_summary,
                    "business_addr2": business_addr2,
                    "webhook_url": webhook_url,
                },
                request_update_params.RequestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRequestEgress,
        )

    async def list(
        self,
        *,
        page: int,
        page_size: int,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        status: TfVerificationStatus | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestListResponse:
        """
        Get a list of previously-submitted tollfree verification requests

        Args:
          page_size: Request this many records per page

                      This value is automatically clamped if the provided value is too large.

          status: Tollfree verification status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/messaging_tollfree/verification/requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "date_end": date_end,
                        "date_start": date_start,
                        "phone_number": phone_number,
                        "status": status,
                    },
                    request_list_params.RequestListParams,
                ),
            ),
            cast_to=RequestListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a verification request

        A request may only be deleted when when the request is in the "rejected" state.

        - `HTTP 200`: request successfully deleted
        - `HTTP 400`: request exists but can't be deleted (i.e. not rejected)
        - `HTTP 404`: request unknown or already deleted

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/messaging_tollfree/verification/requests/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_raw_response_wrapper(
            requests.create,
        )
        self.retrieve = to_raw_response_wrapper(
            requests.retrieve,
        )
        self.update = to_raw_response_wrapper(
            requests.update,
        )
        self.list = to_raw_response_wrapper(
            requests.list,
        )
        self.delete = to_raw_response_wrapper(
            requests.delete,
        )


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_raw_response_wrapper(
            requests.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            requests.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            requests.update,
        )
        self.list = async_to_raw_response_wrapper(
            requests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            requests.delete,
        )


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
        self._requests = requests

        self.create = to_streamed_response_wrapper(
            requests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            requests.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            requests.update,
        )
        self.list = to_streamed_response_wrapper(
            requests.list,
        )
        self.delete = to_streamed_response_wrapper(
            requests.delete,
        )


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
        self._requests = requests

        self.create = async_to_streamed_response_wrapper(
            requests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            requests.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            requests.update,
        )
        self.list = async_to_streamed_response_wrapper(
            requests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            requests.delete,
        )
