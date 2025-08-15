# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    global_ip_assignment_list_params,
    global_ip_assignment_create_params,
    global_ip_assignment_update_params,
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
from ..types.global_ip_assignment_list_response import GlobalIPAssignmentListResponse
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
        global_ip_id: str | NotGiven = NOT_GIVEN,
        is_in_maintenance: bool | NotGiven = NOT_GIVEN,
        wireguard_peer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentCreateResponse:
        """
        Create a Global IP assignment.

        Args:
          global_ip_id: Global IP ID.

          is_in_maintenance: Enable/disable BGP announcement.

          wireguard_peer_id: Wireguard peer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/global_ip_assignments",
            body=maybe_transform(
                {
                    "global_ip_id": global_ip_id,
                    "is_in_maintenance": is_in_maintenance,
                    "wireguard_peer_id": wireguard_peer_id,
                },
                global_ip_assignment_create_params.GlobalIPAssignmentCreateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        id: str,
        *,
        body: global_ip_assignment_update_params.Body,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentUpdateResponse:
        """
        Update a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/global_ip_assignments/{id}",
            body=maybe_transform(body, global_ip_assignment_update_params.GlobalIPAssignmentUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentUpdateResponse,
        )

    def list(
        self,
        *,
        page: global_ip_assignment_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentListResponse:
        """
        List all Global IP assignments.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/global_ip_assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, global_ip_assignment_list_params.GlobalIPAssignmentListParams),
            ),
            cast_to=GlobalIPAssignmentListResponse,
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
        global_ip_id: str | NotGiven = NOT_GIVEN,
        is_in_maintenance: bool | NotGiven = NOT_GIVEN,
        wireguard_peer_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentCreateResponse:
        """
        Create a Global IP assignment.

        Args:
          global_ip_id: Global IP ID.

          is_in_maintenance: Enable/disable BGP announcement.

          wireguard_peer_id: Wireguard peer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/global_ip_assignments",
            body=await async_maybe_transform(
                {
                    "global_ip_id": global_ip_id,
                    "is_in_maintenance": is_in_maintenance,
                    "wireguard_peer_id": wireguard_peer_id,
                },
                global_ip_assignment_create_params.GlobalIPAssignmentCreateParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        id: str,
        *,
        body: global_ip_assignment_update_params.Body,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentUpdateResponse:
        """
        Update a Global IP assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/global_ip_assignments/{id}",
            body=await async_maybe_transform(body, global_ip_assignment_update_params.GlobalIPAssignmentUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalIPAssignmentUpdateResponse,
        )

    async def list(
        self,
        *,
        page: global_ip_assignment_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalIPAssignmentListResponse:
        """
        List all Global IP assignments.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/global_ip_assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, global_ip_assignment_list_params.GlobalIPAssignmentListParams
                ),
            ),
            cast_to=GlobalIPAssignmentListResponse,
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
