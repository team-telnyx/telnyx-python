# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import requirement_list_params, requirement_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.doc_reqs_requirement import DocReqsRequirement
from ..types.requirement_retrieve_response import RequirementRetrieveResponse

__all__ = ["RequirementsResource", "AsyncRequirementsResource"]


class RequirementsResource(SyncAPIResource):
    """Requirements for international numbers and porting orders"""

    @cached_property
    def with_raw_response(self) -> RequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RequirementsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequirementRetrieveResponse:
        """
        Retrieve a document requirement record

        Args:
          version: Filter by requirement version number. When omitted, returns the currently-active
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/requirements/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, requirement_retrieve_params.RequirementRetrieveParams),
            ),
            cast_to=RequirementRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: requirement_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: List[
            Literal[
                "created_at",
                "updated_at",
                "country_code",
                "phone_number_type",
                "-created_at",
                "-updated_at",
                "-country_code",
                "-phone_number_type",
            ]
        ]
        | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[DocReqsRequirement]:
        """
        List all requirements with filtering, sorting, and pagination

        Args:
          filter:
              Consolidated filter parameter for requirements (deepObject style). Originally:
              filter[country_code], filter[phone_number_type], filter[action]

          sort:
              Consolidated sort parameter for requirements (deepObject style). Originally:
              sort[]

          version: Filter by requirement version number. When omitted, returns the currently-active
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/requirements",
            page=SyncDefaultFlatPagination[DocReqsRequirement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                        "version": version,
                    },
                    requirement_list_params.RequirementListParams,
                ),
            ),
            model=DocReqsRequirement,
        )


class AsyncRequirementsResource(AsyncAPIResource):
    """Requirements for international numbers and porting orders"""

    @cached_property
    def with_raw_response(self) -> AsyncRequirementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequirementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequirementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRequirementsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequirementRetrieveResponse:
        """
        Retrieve a document requirement record

        Args:
          version: Filter by requirement version number. When omitted, returns the currently-active
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/requirements/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, requirement_retrieve_params.RequirementRetrieveParams
                ),
            ),
            cast_to=RequirementRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: requirement_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: List[
            Literal[
                "created_at",
                "updated_at",
                "country_code",
                "phone_number_type",
                "-created_at",
                "-updated_at",
                "-country_code",
                "-phone_number_type",
            ]
        ]
        | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DocReqsRequirement, AsyncDefaultFlatPagination[DocReqsRequirement]]:
        """
        List all requirements with filtering, sorting, and pagination

        Args:
          filter:
              Consolidated filter parameter for requirements (deepObject style). Originally:
              filter[country_code], filter[phone_number_type], filter[action]

          sort:
              Consolidated sort parameter for requirements (deepObject style). Originally:
              sort[]

          version: Filter by requirement version number. When omitted, returns the currently-active
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/requirements",
            page=AsyncDefaultFlatPagination[DocReqsRequirement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                        "version": version,
                    },
                    requirement_list_params.RequirementListParams,
                ),
            ),
            model=DocReqsRequirement,
        )


class RequirementsResourceWithRawResponse:
    def __init__(self, requirements: RequirementsResource) -> None:
        self._requirements = requirements

        self.retrieve = to_raw_response_wrapper(
            requirements.retrieve,
        )
        self.list = to_raw_response_wrapper(
            requirements.list,
        )


class AsyncRequirementsResourceWithRawResponse:
    def __init__(self, requirements: AsyncRequirementsResource) -> None:
        self._requirements = requirements

        self.retrieve = async_to_raw_response_wrapper(
            requirements.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            requirements.list,
        )


class RequirementsResourceWithStreamingResponse:
    def __init__(self, requirements: RequirementsResource) -> None:
        self._requirements = requirements

        self.retrieve = to_streamed_response_wrapper(
            requirements.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            requirements.list,
        )


class AsyncRequirementsResourceWithStreamingResponse:
    def __init__(self, requirements: AsyncRequirementsResource) -> None:
        self._requirements = requirements

        self.retrieve = async_to_streamed_response_wrapper(
            requirements.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            requirements.list,
        )
