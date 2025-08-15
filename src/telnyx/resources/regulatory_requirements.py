# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import regulatory_requirement_retrieve_params
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
from ..types.regulatory_requirement_retrieve_response import RegulatoryRequirementRetrieveResponse

__all__ = ["RegulatoryRequirementsResource", "AsyncRegulatoryRequirementsResource"]


class RegulatoryRequirementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegulatoryRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RegulatoryRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegulatoryRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RegulatoryRequirementsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        filter: regulatory_requirement_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegulatoryRequirementRetrieveResponse:
        """
        Retrieve regulatory requirements

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[requirement_group_id], filter[country_code],
              filter[phone_number_type], filter[action]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/regulatory_requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter}, regulatory_requirement_retrieve_params.RegulatoryRequirementRetrieveParams
                ),
            ),
            cast_to=RegulatoryRequirementRetrieveResponse,
        )


class AsyncRegulatoryRequirementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegulatoryRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegulatoryRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegulatoryRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRegulatoryRequirementsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        filter: regulatory_requirement_retrieve_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegulatoryRequirementRetrieveResponse:
        """
        Retrieve regulatory requirements

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[requirement_group_id], filter[country_code],
              filter[phone_number_type], filter[action]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/regulatory_requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, regulatory_requirement_retrieve_params.RegulatoryRequirementRetrieveParams
                ),
            ),
            cast_to=RegulatoryRequirementRetrieveResponse,
        )


class RegulatoryRequirementsResourceWithRawResponse:
    def __init__(self, regulatory_requirements: RegulatoryRequirementsResource) -> None:
        self._regulatory_requirements = regulatory_requirements

        self.retrieve = to_raw_response_wrapper(
            regulatory_requirements.retrieve,
        )


class AsyncRegulatoryRequirementsResourceWithRawResponse:
    def __init__(self, regulatory_requirements: AsyncRegulatoryRequirementsResource) -> None:
        self._regulatory_requirements = regulatory_requirements

        self.retrieve = async_to_raw_response_wrapper(
            regulatory_requirements.retrieve,
        )


class RegulatoryRequirementsResourceWithStreamingResponse:
    def __init__(self, regulatory_requirements: RegulatoryRequirementsResource) -> None:
        self._regulatory_requirements = regulatory_requirements

        self.retrieve = to_streamed_response_wrapper(
            regulatory_requirements.retrieve,
        )


class AsyncRegulatoryRequirementsResourceWithStreamingResponse:
    def __init__(self, regulatory_requirements: AsyncRegulatoryRequirementsResource) -> None:
        self._regulatory_requirements = regulatory_requirements

        self.retrieve = async_to_streamed_response_wrapper(
            regulatory_requirements.retrieve,
        )
