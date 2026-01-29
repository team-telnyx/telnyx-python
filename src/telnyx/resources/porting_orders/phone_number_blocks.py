# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.porting_orders import phone_number_block_list_params, phone_number_block_create_params
from ...types.porting_orders.porting_phone_number_block import PortingPhoneNumberBlock
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        filter: phone_number_block_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: phone_number_block_list_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[PortingPhoneNumberBlock]:
        """
        Returns a list of all phone number blocks of a porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order_id], filter[support_key], filter[status],
              filter[phone_number], filter[activation_status], filter[portability_status]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._get_api_list(
            f"/porting_orders/{porting_order_id}/phone_number_blocks",
            page=SyncDefaultFlatPagination[PortingPhoneNumberBlock],
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
                    },
                    phone_number_block_list_params.PhoneNumberBlockListParams,
                ),
            ),
            model=PortingPhoneNumberBlock,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list(
        self,
        porting_order_id: str,
        *,
        filter: phone_number_block_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: phone_number_block_list_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PortingPhoneNumberBlock, AsyncDefaultFlatPagination[PortingPhoneNumberBlock]]:
        """
        Returns a list of all phone number blocks of a porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order_id], filter[support_key], filter[status],
              filter[phone_number], filter[activation_status], filter[portability_status]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._get_api_list(
            f"/porting_orders/{porting_order_id}/phone_number_blocks",
            page=AsyncDefaultFlatPagination[PortingPhoneNumberBlock],
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
                    },
                    phone_number_block_list_params.PhoneNumberBlockListParams,
                ),
            ),
            model=PortingPhoneNumberBlock,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
