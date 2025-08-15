# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import requirement_type_list_params
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
from ..types.requirement_type_list_response import RequirementTypeListResponse
from ..types.requirement_type_retrieve_response import RequirementTypeRetrieveResponse

__all__ = ["RequirementTypesResource", "AsyncRequirementTypesResource"]


class RequirementTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequirementTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RequirementTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequirementTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RequirementTypesResourceWithStreamingResponse(self)

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
    ) -> RequirementTypeRetrieveResponse:
        """
        Retrieve a requirement type by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/requirement_types/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementTypeRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: requirement_type_list_params.Filter | NotGiven = NOT_GIVEN,
        sort: List[Literal["name", "created_at", "updated_at", "-name", "-created_at", "-updated_at"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementTypeListResponse:
        """
        List all requirement types ordered by created_at descending

        Args:
          filter: Consolidated filter parameter for requirement types (deepObject style).
              Originally: filter[name]

          sort: Consolidated sort parameter for requirement types (deepObject style).
              Originally: sort[]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/requirement_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "sort": sort,
                    },
                    requirement_type_list_params.RequirementTypeListParams,
                ),
            ),
            cast_to=RequirementTypeListResponse,
        )


class AsyncRequirementTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequirementTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequirementTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequirementTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRequirementTypesResourceWithStreamingResponse(self)

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
    ) -> RequirementTypeRetrieveResponse:
        """
        Retrieve a requirement type by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/requirement_types/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequirementTypeRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: requirement_type_list_params.Filter | NotGiven = NOT_GIVEN,
        sort: List[Literal["name", "created_at", "updated_at", "-name", "-created_at", "-updated_at"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequirementTypeListResponse:
        """
        List all requirement types ordered by created_at descending

        Args:
          filter: Consolidated filter parameter for requirement types (deepObject style).
              Originally: filter[name]

          sort: Consolidated sort parameter for requirement types (deepObject style).
              Originally: sort[]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/requirement_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "sort": sort,
                    },
                    requirement_type_list_params.RequirementTypeListParams,
                ),
            ),
            cast_to=RequirementTypeListResponse,
        )


class RequirementTypesResourceWithRawResponse:
    def __init__(self, requirement_types: RequirementTypesResource) -> None:
        self._requirement_types = requirement_types

        self.retrieve = to_raw_response_wrapper(
            requirement_types.retrieve,
        )
        self.list = to_raw_response_wrapper(
            requirement_types.list,
        )


class AsyncRequirementTypesResourceWithRawResponse:
    def __init__(self, requirement_types: AsyncRequirementTypesResource) -> None:
        self._requirement_types = requirement_types

        self.retrieve = async_to_raw_response_wrapper(
            requirement_types.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            requirement_types.list,
        )


class RequirementTypesResourceWithStreamingResponse:
    def __init__(self, requirement_types: RequirementTypesResource) -> None:
        self._requirement_types = requirement_types

        self.retrieve = to_streamed_response_wrapper(
            requirement_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            requirement_types.list,
        )


class AsyncRequirementTypesResourceWithStreamingResponse:
    def __init__(self, requirement_types: AsyncRequirementTypesResource) -> None:
        self._requirement_types = requirement_types

        self.retrieve = async_to_streamed_response_wrapper(
            requirement_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            requirement_types.list,
        )
