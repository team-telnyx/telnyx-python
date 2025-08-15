# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import (
    number_order_phone_number_list_params,
    number_order_phone_number_update_requirements_params,
    number_order_phone_number_update_requirement_group_params,
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
from ..types.update_regulatory_requirement_param import UpdateRegulatoryRequirementParam
from ..types.number_order_phone_number_list_response import NumberOrderPhoneNumberListResponse
from ..types.number_order_phone_number_retrieve_response import NumberOrderPhoneNumberRetrieveResponse
from ..types.number_order_phone_number_update_requirements_response import (
    NumberOrderPhoneNumberUpdateRequirementsResponse,
)
from ..types.number_order_phone_number_update_requirement_group_response import (
    NumberOrderPhoneNumberUpdateRequirementGroupResponse,
)

__all__ = ["NumberOrderPhoneNumbersResource", "AsyncNumberOrderPhoneNumbersResource"]


class NumberOrderPhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberOrderPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumberOrderPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberOrderPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumberOrderPhoneNumbersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        number_order_phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberRetrieveResponse:
        """
        Get an existing phone number in number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_phone_number_id:
            raise ValueError(
                f"Expected a non-empty value for `number_order_phone_number_id` but received {number_order_phone_number_id!r}"
            )
        return self._get(
            f"/number_order_phone_numbers/{number_order_phone_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderPhoneNumberRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: number_order_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberListResponse:
        """
        Get a list of phone numbers associated to orders.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[country_code]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/number_order_phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"filter": filter}, number_order_phone_number_list_params.NumberOrderPhoneNumberListParams
                ),
            ),
            cast_to=NumberOrderPhoneNumberListResponse,
        )

    def update_requirement_group(
        self,
        id: str,
        *,
        requirement_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberUpdateRequirementGroupResponse:
        """
        Update requirement group for a phone number order

        Args:
          requirement_group_id: The ID of the requirement group to associate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/number_order_phone_numbers/{id}/requirement_group",
            body=maybe_transform(
                {"requirement_group_id": requirement_group_id},
                number_order_phone_number_update_requirement_group_params.NumberOrderPhoneNumberUpdateRequirementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderPhoneNumberUpdateRequirementGroupResponse,
        )

    def update_requirements(
        self,
        number_order_phone_number_id: str,
        *,
        regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberUpdateRequirementsResponse:
        """
        Updates requirements for a single phone number within a number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_phone_number_id:
            raise ValueError(
                f"Expected a non-empty value for `number_order_phone_number_id` but received {number_order_phone_number_id!r}"
            )
        return self._patch(
            f"/number_order_phone_numbers/{number_order_phone_number_id}",
            body=maybe_transform(
                {"regulatory_requirements": regulatory_requirements},
                number_order_phone_number_update_requirements_params.NumberOrderPhoneNumberUpdateRequirementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderPhoneNumberUpdateRequirementsResponse,
        )


class AsyncNumberOrderPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberOrderPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberOrderPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        number_order_phone_number_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberRetrieveResponse:
        """
        Get an existing phone number in number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_phone_number_id:
            raise ValueError(
                f"Expected a non-empty value for `number_order_phone_number_id` but received {number_order_phone_number_id!r}"
            )
        return await self._get(
            f"/number_order_phone_numbers/{number_order_phone_number_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderPhoneNumberRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: number_order_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberListResponse:
        """
        Get a list of phone numbers associated to orders.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[country_code]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/number_order_phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, number_order_phone_number_list_params.NumberOrderPhoneNumberListParams
                ),
            ),
            cast_to=NumberOrderPhoneNumberListResponse,
        )

    async def update_requirement_group(
        self,
        id: str,
        *,
        requirement_group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberUpdateRequirementGroupResponse:
        """
        Update requirement group for a phone number order

        Args:
          requirement_group_id: The ID of the requirement group to associate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/number_order_phone_numbers/{id}/requirement_group",
            body=await async_maybe_transform(
                {"requirement_group_id": requirement_group_id},
                number_order_phone_number_update_requirement_group_params.NumberOrderPhoneNumberUpdateRequirementGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderPhoneNumberUpdateRequirementGroupResponse,
        )

    async def update_requirements(
        self,
        number_order_phone_number_id: str,
        *,
        regulatory_requirements: Iterable[UpdateRegulatoryRequirementParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NumberOrderPhoneNumberUpdateRequirementsResponse:
        """
        Updates requirements for a single phone number within a number order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_order_phone_number_id:
            raise ValueError(
                f"Expected a non-empty value for `number_order_phone_number_id` but received {number_order_phone_number_id!r}"
            )
        return await self._patch(
            f"/number_order_phone_numbers/{number_order_phone_number_id}",
            body=await async_maybe_transform(
                {"regulatory_requirements": regulatory_requirements},
                number_order_phone_number_update_requirements_params.NumberOrderPhoneNumberUpdateRequirementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberOrderPhoneNumberUpdateRequirementsResponse,
        )


class NumberOrderPhoneNumbersResourceWithRawResponse:
    def __init__(self, number_order_phone_numbers: NumberOrderPhoneNumbersResource) -> None:
        self._number_order_phone_numbers = number_order_phone_numbers

        self.retrieve = to_raw_response_wrapper(
            number_order_phone_numbers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            number_order_phone_numbers.list,
        )
        self.update_requirement_group = to_raw_response_wrapper(
            number_order_phone_numbers.update_requirement_group,
        )
        self.update_requirements = to_raw_response_wrapper(
            number_order_phone_numbers.update_requirements,
        )


class AsyncNumberOrderPhoneNumbersResourceWithRawResponse:
    def __init__(self, number_order_phone_numbers: AsyncNumberOrderPhoneNumbersResource) -> None:
        self._number_order_phone_numbers = number_order_phone_numbers

        self.retrieve = async_to_raw_response_wrapper(
            number_order_phone_numbers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            number_order_phone_numbers.list,
        )
        self.update_requirement_group = async_to_raw_response_wrapper(
            number_order_phone_numbers.update_requirement_group,
        )
        self.update_requirements = async_to_raw_response_wrapper(
            number_order_phone_numbers.update_requirements,
        )


class NumberOrderPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, number_order_phone_numbers: NumberOrderPhoneNumbersResource) -> None:
        self._number_order_phone_numbers = number_order_phone_numbers

        self.retrieve = to_streamed_response_wrapper(
            number_order_phone_numbers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            number_order_phone_numbers.list,
        )
        self.update_requirement_group = to_streamed_response_wrapper(
            number_order_phone_numbers.update_requirement_group,
        )
        self.update_requirements = to_streamed_response_wrapper(
            number_order_phone_numbers.update_requirements,
        )


class AsyncNumberOrderPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, number_order_phone_numbers: AsyncNumberOrderPhoneNumbersResource) -> None:
        self._number_order_phone_numbers = number_order_phone_numbers

        self.retrieve = async_to_streamed_response_wrapper(
            number_order_phone_numbers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            number_order_phone_numbers.list,
        )
        self.update_requirement_group = async_to_streamed_response_wrapper(
            number_order_phone_numbers.update_requirement_group,
        )
        self.update_requirements = async_to_streamed_response_wrapper(
            number_order_phone_numbers.update_requirements,
        )
