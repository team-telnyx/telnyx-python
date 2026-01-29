# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import global_ip_assignment_list_params, global_ip_assignment_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.global_ip_assignment import GlobalIPAssignment
from ..types.global_ip_assignment_create_response import GlobalIPAssignmentCreateResponse
from ..types.global_ip_assignment_delete_response import GlobalIPAssignmentDeleteResponse
from ..types.global_ip_assignment_update_response import GlobalIPAssignmentUpdateResponse
from ..types.global_ip_assignment_retrieve_response import GlobalIPAssignmentRetrieveResponse

__all__ = ["GlobalIPAssignmentsResource", "AsyncGlobalIPAssignmentsResource"]


class GlobalIPAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalIPAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GlobalIPAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalIPAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GlobalIPAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentCreateResponse:
        """Create a Global IP assignment."""
        return self._post(
            "/global_ip_assignments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentRetrieveResponse:
        """
        Retrieve a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/global_ip_assignments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentRetrieveResponse,
        )

    def update(
        self,
        global_ip_assignment_id: str,
        *,
        global_ip_assignment_update_request: global_ip_assignment_update_params.GlobalIPAssignmentUpdateRequest,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentUpdateResponse:
        """
        Update a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not global_ip_assignment_id:
            raise ValueError(
                f"Expected a non-empty value for `global_ip_assignment_id` but received {global_ip_assignment_id!r}"
            )
        return self._patch(
            f"/global_ip_assignments/{global_ip_assignment_id}",
            body=maybe_transform(
                global_ip_assignment_update_request, global_ip_assignment_update_params.GlobalIPAssignmentUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[GlobalIPAssignment]:
        """
        List all Global IP assignments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/global_ip_assignments",
            page=SyncDefaultFlatPagination[GlobalIPAssignment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    global_ip_assignment_list_params.GlobalIPAssignmentListParams,
                ),
            ),
            model=GlobalIPAssignment,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentDeleteResponse:
        """
        Delete a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/global_ip_assignments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentDeleteResponse,
        )


class AsyncGlobalIPAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalIPAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalIPAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalIPAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGlobalIPAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentCreateResponse:
        """Create a Global IP assignment."""
        return await self._post(
            "/global_ip_assignments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentRetrieveResponse:
        """
        Retrieve a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/global_ip_assignments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentRetrieveResponse,
        )

    async def update(
        self,
        global_ip_assignment_id: str,
        *,
        global_ip_assignment_update_request: global_ip_assignment_update_params.GlobalIPAssignmentUpdateRequest,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentUpdateResponse:
        """
        Update a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not global_ip_assignment_id:
            raise ValueError(
                f"Expected a non-empty value for `global_ip_assignment_id` but received {global_ip_assignment_id!r}"
            )
        return await self._patch(
            f"/global_ip_assignments/{global_ip_assignment_id}",
            body=await async_maybe_transform(
                global_ip_assignment_update_request, global_ip_assignment_update_params.GlobalIPAssignmentUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GlobalIPAssignment, AsyncDefaultFlatPagination[GlobalIPAssignment]]:
        """
        List all Global IP assignments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/global_ip_assignments",
            page=AsyncDefaultFlatPagination[GlobalIPAssignment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    global_ip_assignment_list_params.GlobalIPAssignmentListParams,
                ),
            ),
            model=GlobalIPAssignment,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalIPAssignmentDeleteResponse:
        """
        Delete a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/global_ip_assignments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentDeleteResponse,
        )


class GlobalIPAssignmentsResourceWithRawResponse:
    def __init__(self, global_ip_assignments: GlobalIPAssignmentsResource) -> None:
        self._global_ip_assignments = global_ip_assignments

        self.create = to_raw_response_wrapper(
            global_ip_assignments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            global_ip_assignments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            global_ip_assignments.update,
        )
        self.list = to_raw_response_wrapper(
            global_ip_assignments.list,
        )
        self.delete = to_raw_response_wrapper(
            global_ip_assignments.delete,
        )


class AsyncGlobalIPAssignmentsResourceWithRawResponse:
    def __init__(self, global_ip_assignments: AsyncGlobalIPAssignmentsResource) -> None:
        self._global_ip_assignments = global_ip_assignments

        self.create = async_to_raw_response_wrapper(
            global_ip_assignments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            global_ip_assignments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            global_ip_assignments.update,
        )
        self.list = async_to_raw_response_wrapper(
            global_ip_assignments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            global_ip_assignments.delete,
        )


class GlobalIPAssignmentsResourceWithStreamingResponse:
    def __init__(self, global_ip_assignments: GlobalIPAssignmentsResource) -> None:
        self._global_ip_assignments = global_ip_assignments

        self.create = to_streamed_response_wrapper(
            global_ip_assignments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            global_ip_assignments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            global_ip_assignments.update,
        )
        self.list = to_streamed_response_wrapper(
            global_ip_assignments.list,
        )
        self.delete = to_streamed_response_wrapper(
            global_ip_assignments.delete,
        )


class AsyncGlobalIPAssignmentsResourceWithStreamingResponse:
    def __init__(self, global_ip_assignments: AsyncGlobalIPAssignmentsResource) -> None:
        self._global_ip_assignments = global_ip_assignments

        self.create = async_to_streamed_response_wrapper(
            global_ip_assignments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            global_ip_assignments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            global_ip_assignments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            global_ip_assignments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            global_ip_assignments.delete,
        )
