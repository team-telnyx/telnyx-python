# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import global_ip_assignment_list_params, global_ip_assignment_update_params
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
from ..types.global_ip_assignment import GlobalIPAssignment
from ..types.global_ip_assignment_create_response import GlobalIPAssignmentCreateResponse
from ..types.global_ip_assignment_delete_response import GlobalIPAssignmentDeleteResponse
from ..types.global_ip_assignment_update_response import GlobalIPAssignmentUpdateResponse
from ..types.global_ip_assignment_retrieve_response import GlobalIPAssignmentRetrieveResponse

__all__ = ["GlobalIPAssignmentsResource", "AsyncGlobalIPAssignmentsResource"]


class GlobalIPAssignmentsResource(SyncAPIResource):
    """Global IPs"""

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
        """
        Assigns a Global IP to a WireGuard peer so traffic destined for the IP is
        delivered over that peer's tunnel. Assignment is asynchronous, so the request is
        accepted and completes in the background.
        """
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
        Returns the details of a single Global IP assignment, including the Global IP
        and WireGuard peer it links.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/global_ip_assignments/{id}", id=id),
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
        Updates the specified Global IP assignment with the provided fields and returns
        the updated assignment.

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
            path_template(
                "/global_ip_assignments/{global_ip_assignment_id}", global_ip_assignment_id=global_ip_assignment_id
            ),
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
        Returns a paginated list of your Global IP assignments, the links between Global
        IPs and the WireGuard peers that receive their traffic.

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
        Deletes the specified Global IP assignment, detaching the Global IP from its
        WireGuard peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/global_ip_assignments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentDeleteResponse,
        )


class AsyncGlobalIPAssignmentsResource(AsyncAPIResource):
    """Global IPs"""

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
        """
        Assigns a Global IP to a WireGuard peer so traffic destined for the IP is
        delivered over that peer's tunnel. Assignment is asynchronous, so the request is
        accepted and completes in the background.
        """
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
        Returns the details of a single Global IP assignment, including the Global IP
        and WireGuard peer it links.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/global_ip_assignments/{id}", id=id),
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
        Updates the specified Global IP assignment with the provided fields and returns
        the updated assignment.

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
            path_template(
                "/global_ip_assignments/{global_ip_assignment_id}", global_ip_assignment_id=global_ip_assignment_id
            ),
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
        Returns a paginated list of your Global IP assignments, the links between Global
        IPs and the WireGuard peers that receive their traffic.

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
        Deletes the specified Global IP assignment, detaching the Global IP from its
        WireGuard peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/global_ip_assignments/{id}", id=id),
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
