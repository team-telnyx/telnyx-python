# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.external_connections import release_list_params
from ...types.external_connections.release_list_response import ReleaseListResponse
from ...types.external_connections.release_retrieve_response import ReleaseRetrieveResponse

__all__ = ["ReleasesResource", "AsyncReleasesResource"]


class ReleasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ReleasesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        release_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseRetrieveResponse:
        """
        Return the details of a Release request and its phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not release_id:
            raise ValueError(f"Expected a non-empty value for `release_id` but received {release_id!r}")
        return self._get(
            f"/external_connections/{id}/releases/{release_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseRetrieveResponse,
        )

    def list(
        self,
        id: str,
        *,
        filter: release_list_params.Filter | NotGiven = NOT_GIVEN,
        page: release_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseListResponse:
        """Returns a list of your Releases for the given external connection.

        These are
        automatically created when you change the `connection_id` of a phone number that
        is currently on Microsoft Teams.

        Args:
          filter: Filter parameter for releases (deepObject style). Supports filtering by status,
              civic_address_id, location_id, and phone_number with eq/contains operations.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/external_connections/{id}/releases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    release_list_params.ReleaseListParams,
                ),
            ),
            cast_to=ReleaseListResponse,
        )


class AsyncReleasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncReleasesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        release_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseRetrieveResponse:
        """
        Return the details of a Release request and its phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not release_id:
            raise ValueError(f"Expected a non-empty value for `release_id` but received {release_id!r}")
        return await self._get(
            f"/external_connections/{id}/releases/{release_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseRetrieveResponse,
        )

    async def list(
        self,
        id: str,
        *,
        filter: release_list_params.Filter | NotGiven = NOT_GIVEN,
        page: release_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseListResponse:
        """Returns a list of your Releases for the given external connection.

        These are
        automatically created when you change the `connection_id` of a phone number that
        is currently on Microsoft Teams.

        Args:
          filter: Filter parameter for releases (deepObject style). Supports filtering by status,
              civic_address_id, location_id, and phone_number with eq/contains operations.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/external_connections/{id}/releases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    release_list_params.ReleaseListParams,
                ),
            ),
            cast_to=ReleaseListResponse,
        )


class ReleasesResourceWithRawResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.retrieve = to_raw_response_wrapper(
            releases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            releases.list,
        )


class AsyncReleasesResourceWithRawResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.retrieve = async_to_raw_response_wrapper(
            releases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            releases.list,
        )


class ReleasesResourceWithStreamingResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.retrieve = to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            releases.list,
        )


class AsyncReleasesResourceWithStreamingResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.retrieve = async_to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            releases.list,
        )
