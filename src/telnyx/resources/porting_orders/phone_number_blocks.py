# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.porting_orders import phone_number_block_list_params, phone_number_block_create_params
from ...types.porting_orders.phone_number_block_list_response import PhoneNumberBlockListResponse
from ...types.porting_orders.phone_number_block_create_response import PhoneNumberBlockCreateResponse
from ...types.porting_orders.phone_number_block_delete_response import PhoneNumberBlockDeleteResponse

__all__ = ["PhoneNumberBlocksResource", "AsyncPhoneNumberBlocksResource"]


class PhoneNumberBlocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumberBlocksResourceWithStreamingResponse(self)

    def create(
        self,
        porting_order_id: str,
        *,
        activation_ranges: Iterable[phone_number_block_create_params.ActivationRange],
        phone_number_range: phone_number_block_create_params.PhoneNumberRange,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberBlockCreateResponse:
        """
        Creates a new phone number block.

        Args:
          activation_ranges: Specifies the activation ranges for this porting phone number block. The
              activation range must be within the block range and should not overlap with
              other activation ranges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._post(
            f"/porting_orders/{porting_order_id}/phone_number_blocks",
            body=maybe_transform(
                {
                    "activation_ranges": activation_ranges,
                    "phone_number_range": phone_number_range,
                },
                phone_number_block_create_params.PhoneNumberBlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBlockCreateResponse,
        )

    def list(
        self,
        porting_order_id: str,
        *,
        filter: phone_number_block_list_params.Filter | NotGiven = NOT_GIVEN,
        page: phone_number_block_list_params.Page | NotGiven = NOT_GIVEN,
        sort: phone_number_block_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberBlockListResponse:
        """
        Returns a list of all phone number blocks of a porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order_id], filter[support_key], filter[status],
              filter[phone_number], filter[activation_status], filter[portability_status]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._get(
            f"/porting_orders/{porting_order_id}/phone_number_blocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_block_list_params.PhoneNumberBlockListParams,
                ),
            ),
            cast_to=PhoneNumberBlockListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        porting_order_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberBlockDeleteResponse:
        """
        Deletes a phone number block.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/porting_orders/{porting_order_id}/phone_number_blocks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBlockDeleteResponse,
        )


class AsyncPhoneNumberBlocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumberBlocksResourceWithStreamingResponse(self)

    async def create(
        self,
        porting_order_id: str,
        *,
        activation_ranges: Iterable[phone_number_block_create_params.ActivationRange],
        phone_number_range: phone_number_block_create_params.PhoneNumberRange,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberBlockCreateResponse:
        """
        Creates a new phone number block.

        Args:
          activation_ranges: Specifies the activation ranges for this porting phone number block. The
              activation range must be within the block range and should not overlap with
              other activation ranges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return await self._post(
            f"/porting_orders/{porting_order_id}/phone_number_blocks",
            body=await async_maybe_transform(
                {
                    "activation_ranges": activation_ranges,
                    "phone_number_range": phone_number_range,
                },
                phone_number_block_create_params.PhoneNumberBlockCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBlockCreateResponse,
        )

    async def list(
        self,
        porting_order_id: str,
        *,
        filter: phone_number_block_list_params.Filter | NotGiven = NOT_GIVEN,
        page: phone_number_block_list_params.Page | NotGiven = NOT_GIVEN,
        sort: phone_number_block_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberBlockListResponse:
        """
        Returns a list of all phone number blocks of a porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order_id], filter[support_key], filter[status],
              filter[phone_number], filter[activation_status], filter[portability_status]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return await self._get(
            f"/porting_orders/{porting_order_id}/phone_number_blocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_block_list_params.PhoneNumberBlockListParams,
                ),
            ),
            cast_to=PhoneNumberBlockListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        porting_order_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberBlockDeleteResponse:
        """
        Deletes a phone number block.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/porting_orders/{porting_order_id}/phone_number_blocks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBlockDeleteResponse,
        )


class PhoneNumberBlocksResourceWithRawResponse:
    def __init__(self, phone_number_blocks: PhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

        self.create = to_raw_response_wrapper(
            phone_number_blocks.create,
        )
        self.list = to_raw_response_wrapper(
            phone_number_blocks.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_number_blocks.delete,
        )


class AsyncPhoneNumberBlocksResourceWithRawResponse:
    def __init__(self, phone_number_blocks: AsyncPhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

        self.create = async_to_raw_response_wrapper(
            phone_number_blocks.create,
        )
        self.list = async_to_raw_response_wrapper(
            phone_number_blocks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_number_blocks.delete,
        )


class PhoneNumberBlocksResourceWithStreamingResponse:
    def __init__(self, phone_number_blocks: PhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

        self.create = to_streamed_response_wrapper(
            phone_number_blocks.create,
        )
        self.list = to_streamed_response_wrapper(
            phone_number_blocks.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_number_blocks.delete,
        )


class AsyncPhoneNumberBlocksResourceWithStreamingResponse:
    def __init__(self, phone_number_blocks: AsyncPhoneNumberBlocksResource) -> None:
        self._phone_number_blocks = phone_number_blocks

        self.create = async_to_streamed_response_wrapper(
            phone_number_blocks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_number_blocks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_number_blocks.delete,
        )
