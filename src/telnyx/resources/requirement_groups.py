# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import requirement_group_list_params, requirement_group_create_params, requirement_group_update_params
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
from ..types.requirement_group import RequirementGroup
from ..types.requirement_group_list_response import RequirementGroupListResponse

__all__ = ["RequirementGroupsResource", "AsyncRequirementGroupsResource"]


class RequirementGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequirementGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RequirementGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequirementGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RequirementGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action: Literal["ordering", "porting"],
        country_code: str,
        phone_number_type: Literal["local", "toll_free", "mobile", "national", "shared_cost"],
        customer_reference: str | NotGiven = NOT_GIVEN,
        regulatory_requirements: Iterable[requirement_group_create_params.RegulatoryRequirement] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroup:
        """
        Create a new requirement group

        Args:
          country_code: ISO alpha 2 country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/requirement_groups",
            body=maybe_transform(
                {
                    "action": action,
                    "country_code": country_code,
                    "phone_number_type": phone_number_type,
                    "customer_reference": customer_reference,
                    "regulatory_requirements": regulatory_requirements,
                },
                requirement_group_create_params.RequirementGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
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
    ) -> RequirementGroup:
        """
        Get a single requirement group by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/requirement_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )

    def update(
        self,
        id: str,
        *,
        customer_reference: str | NotGiven = NOT_GIVEN,
        regulatory_requirements: Iterable[requirement_group_update_params.RegulatoryRequirement] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroup:
        """
        Update requirement values in requirement group

        Args:
          customer_reference: Reference for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/requirement_groups/{id}",
            body=maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "regulatory_requirements": regulatory_requirements,
                },
                requirement_group_update_params.RequirementGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )

    def list(
        self,
        *,
        filter: requirement_group_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroupListResponse:
        """
        List requirement groups

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[country_code], filter[phone_number_type], filter[action], filter[status],
              filter[customer_reference]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/requirement_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, requirement_group_list_params.RequirementGroupListParams),
            ),
            cast_to=RequirementGroupListResponse,
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
    ) -> RequirementGroup:
        """
        Delete a requirement group by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/requirement_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )

    def submit_for_approval(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroup:
        """
        Submit a Requirement Group for Approval

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/requirement_groups/{id}/submit_for_approval",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )


class AsyncRequirementGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequirementGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequirementGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequirementGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRequirementGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action: Literal["ordering", "porting"],
        country_code: str,
        phone_number_type: Literal["local", "toll_free", "mobile", "national", "shared_cost"],
        customer_reference: str | NotGiven = NOT_GIVEN,
        regulatory_requirements: Iterable[requirement_group_create_params.RegulatoryRequirement] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroup:
        """
        Create a new requirement group

        Args:
          country_code: ISO alpha 2 country code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/requirement_groups",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "country_code": country_code,
                    "phone_number_type": phone_number_type,
                    "customer_reference": customer_reference,
                    "regulatory_requirements": regulatory_requirements,
                },
                requirement_group_create_params.RequirementGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
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
    ) -> RequirementGroup:
        """
        Get a single requirement group by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/requirement_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )

    async def update(
        self,
        id: str,
        *,
        customer_reference: str | NotGiven = NOT_GIVEN,
        regulatory_requirements: Iterable[requirement_group_update_params.RegulatoryRequirement] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroup:
        """
        Update requirement values in requirement group

        Args:
          customer_reference: Reference for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/requirement_groups/{id}",
            body=await async_maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "regulatory_requirements": regulatory_requirements,
                },
                requirement_group_update_params.RequirementGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )

    async def list(
        self,
        *,
        filter: requirement_group_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroupListResponse:
        """
        List requirement groups

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[country_code], filter[phone_number_type], filter[action], filter[status],
              filter[customer_reference]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/requirement_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, requirement_group_list_params.RequirementGroupListParams
                ),
            ),
            cast_to=RequirementGroupListResponse,
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
    ) -> RequirementGroup:
        """
        Delete a requirement group by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/requirement_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )

    async def submit_for_approval(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementGroup:
        """
        Submit a Requirement Group for Approval

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/requirement_groups/{id}/submit_for_approval",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementGroup,
        )


class RequirementGroupsResourceWithRawResponse:
    def __init__(self, requirement_groups: RequirementGroupsResource) -> None:
        self._requirement_groups = requirement_groups

        self.create = to_raw_response_wrapper(
            requirement_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            requirement_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            requirement_groups.update,
        )
        self.list = to_raw_response_wrapper(
            requirement_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            requirement_groups.delete,
        )
        self.submit_for_approval = to_raw_response_wrapper(
            requirement_groups.submit_for_approval,
        )


class AsyncRequirementGroupsResourceWithRawResponse:
    def __init__(self, requirement_groups: AsyncRequirementGroupsResource) -> None:
        self._requirement_groups = requirement_groups

        self.create = async_to_raw_response_wrapper(
            requirement_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            requirement_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            requirement_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            requirement_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            requirement_groups.delete,
        )
        self.submit_for_approval = async_to_raw_response_wrapper(
            requirement_groups.submit_for_approval,
        )


class RequirementGroupsResourceWithStreamingResponse:
    def __init__(self, requirement_groups: RequirementGroupsResource) -> None:
        self._requirement_groups = requirement_groups

        self.create = to_streamed_response_wrapper(
            requirement_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            requirement_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            requirement_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            requirement_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            requirement_groups.delete,
        )
        self.submit_for_approval = to_streamed_response_wrapper(
            requirement_groups.submit_for_approval,
        )


class AsyncRequirementGroupsResourceWithStreamingResponse:
    def __init__(self, requirement_groups: AsyncRequirementGroupsResource) -> None:
        self._requirement_groups = requirement_groups

        self.create = async_to_streamed_response_wrapper(
            requirement_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            requirement_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            requirement_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            requirement_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            requirement_groups.delete,
        )
        self.submit_for_approval = async_to_streamed_response_wrapper(
            requirement_groups.submit_for_approval,
        )
