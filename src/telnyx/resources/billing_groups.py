# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import billing_group_list_params, billing_group_create_params, billing_group_update_params
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
from ..types.billing_group_list_response import BillingGroupListResponse
from ..types.billing_group_create_response import BillingGroupCreateResponse
from ..types.billing_group_delete_response import BillingGroupDeleteResponse
from ..types.billing_group_update_response import BillingGroupUpdateResponse
from ..types.billing_group_retrieve_response import BillingGroupRetrieveResponse

__all__ = ["BillingGroupsResource", "AsyncBillingGroupsResource"]


class BillingGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BillingGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BillingGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGroupCreateResponse:
        """
        Create a billing group

        Args:
          name: A name for the billing group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing_groups",
            body=maybe_transform({"name": name}, billing_group_create_params.BillingGroupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupCreateResponse,
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
    ) -> BillingGroupRetrieveResponse:
        """
        Get a billing group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/billing_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGroupUpdateResponse:
        """
        Update a billing group

        Args:
          name: A name for the billing group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/billing_groups/{id}",
            body=maybe_transform({"name": name}, billing_group_update_params.BillingGroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupUpdateResponse,
        )

    def list(
        self,
        *,
        page: billing_group_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGroupListResponse:
        """
        List all billing groups

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/billing_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, billing_group_list_params.BillingGroupListParams),
            ),
            cast_to=BillingGroupListResponse,
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
    ) -> BillingGroupDeleteResponse:
        """
        Delete a billing group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/billing_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupDeleteResponse,
        )


class AsyncBillingGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBillingGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGroupCreateResponse:
        """
        Create a billing group

        Args:
          name: A name for the billing group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing_groups",
            body=await async_maybe_transform({"name": name}, billing_group_create_params.BillingGroupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupCreateResponse,
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
    ) -> BillingGroupRetrieveResponse:
        """
        Get a billing group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/billing_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGroupUpdateResponse:
        """
        Update a billing group

        Args:
          name: A name for the billing group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/billing_groups/{id}",
            body=await async_maybe_transform({"name": name}, billing_group_update_params.BillingGroupUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupUpdateResponse,
        )

    async def list(
        self,
        *,
        page: billing_group_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGroupListResponse:
        """
        List all billing groups

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/billing_groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, billing_group_list_params.BillingGroupListParams),
            ),
            cast_to=BillingGroupListResponse,
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
    ) -> BillingGroupDeleteResponse:
        """
        Delete a billing group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/billing_groups/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGroupDeleteResponse,
        )


class BillingGroupsResourceWithRawResponse:
    def __init__(self, billing_groups: BillingGroupsResource) -> None:
        self._billing_groups = billing_groups

        self.create = to_raw_response_wrapper(
            billing_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            billing_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            billing_groups.update,
        )
        self.list = to_raw_response_wrapper(
            billing_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            billing_groups.delete,
        )


class AsyncBillingGroupsResourceWithRawResponse:
    def __init__(self, billing_groups: AsyncBillingGroupsResource) -> None:
        self._billing_groups = billing_groups

        self.create = async_to_raw_response_wrapper(
            billing_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            billing_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            billing_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            billing_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            billing_groups.delete,
        )


class BillingGroupsResourceWithStreamingResponse:
    def __init__(self, billing_groups: BillingGroupsResource) -> None:
        self._billing_groups = billing_groups

        self.create = to_streamed_response_wrapper(
            billing_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            billing_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            billing_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            billing_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            billing_groups.delete,
        )


class AsyncBillingGroupsResourceWithStreamingResponse:
    def __init__(self, billing_groups: AsyncBillingGroupsResource) -> None:
        self._billing_groups = billing_groups

        self.create = async_to_streamed_response_wrapper(
            billing_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            billing_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            billing_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            billing_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            billing_groups.delete,
        )
