# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import phone_numbers_regulatory_requirement_retrieve_params
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
from ..types.phone_numbers_regulatory_requirement_retrieve_response import (
    PhoneNumbersRegulatoryRequirementRetrieveResponse,
)

__all__ = ["PhoneNumbersRegulatoryRequirementsResource", "AsyncPhoneNumbersRegulatoryRequirementsResource"]


class PhoneNumbersRegulatoryRequirementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumbersRegulatoryRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersRegulatoryRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        filter: phone_numbers_regulatory_requirement_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumbersRegulatoryRequirementRetrieveResponse:
        """
        Retrieve regulatory requirements for a list of phone numbers

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_numbers_regulatory_requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter},
                    phone_numbers_regulatory_requirement_retrieve_params.PhoneNumbersRegulatoryRequirementRetrieveParams,
                ),
            ),
            cast_to=PhoneNumbersRegulatoryRequirementRetrieveResponse,
        )


class AsyncPhoneNumbersRegulatoryRequirementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        filter: phone_numbers_regulatory_requirement_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumbersRegulatoryRequirementRetrieveResponse:
        """
        Retrieve regulatory requirements for a list of phone numbers

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_numbers_regulatory_requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter},
                    phone_numbers_regulatory_requirement_retrieve_params.PhoneNumbersRegulatoryRequirementRetrieveParams,
                ),
            ),
            cast_to=PhoneNumbersRegulatoryRequirementRetrieveResponse,
        )


class PhoneNumbersRegulatoryRequirementsResourceWithRawResponse:
    def __init__(self, phone_numbers_regulatory_requirements: PhoneNumbersRegulatoryRequirementsResource) -> None:
        self._phone_numbers_regulatory_requirements = phone_numbers_regulatory_requirements

        self.retrieve = to_raw_response_wrapper(
            phone_numbers_regulatory_requirements.retrieve,
        )


class AsyncPhoneNumbersRegulatoryRequirementsResourceWithRawResponse:
    def __init__(self, phone_numbers_regulatory_requirements: AsyncPhoneNumbersRegulatoryRequirementsResource) -> None:
        self._phone_numbers_regulatory_requirements = phone_numbers_regulatory_requirements

        self.retrieve = async_to_raw_response_wrapper(
            phone_numbers_regulatory_requirements.retrieve,
        )


class PhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse:
    def __init__(self, phone_numbers_regulatory_requirements: PhoneNumbersRegulatoryRequirementsResource) -> None:
        self._phone_numbers_regulatory_requirements = phone_numbers_regulatory_requirements

        self.retrieve = to_streamed_response_wrapper(
            phone_numbers_regulatory_requirements.retrieve,
        )


class AsyncPhoneNumbersRegulatoryRequirementsResourceWithStreamingResponse:
    def __init__(self, phone_numbers_regulatory_requirements: AsyncPhoneNumbersRegulatoryRequirementsResource) -> None:
        self._phone_numbers_regulatory_requirements = phone_numbers_regulatory_requirements

        self.retrieve = async_to_streamed_response_wrapper(
            phone_numbers_regulatory_requirements.retrieve,
        )
