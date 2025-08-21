# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.porting_orders import associated_phone_number_list_params, associated_phone_number_create_params
from ...types.porting_orders.associated_phone_number_list_response import AssociatedPhoneNumberListResponse
from ...types.porting_orders.associated_phone_number_create_response import AssociatedPhoneNumberCreateResponse
from ...types.porting_orders.associated_phone_number_delete_response import AssociatedPhoneNumberDeleteResponse

__all__ = ["AssociatedPhoneNumbersResource", "AsyncAssociatedPhoneNumbersResource"]


class AssociatedPhoneNumbersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssociatedPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AssociatedPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociatedPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AssociatedPhoneNumbersResourceWithStreamingResponse(self)

    def create(
        self,
        porting_order_id: str,
        *,
        action: Literal["keep", "disconnect"],
        phone_number_range: associated_phone_number_create_params.PhoneNumberRange,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssociatedPhoneNumberCreateResponse:
        """Creates a new associated phone number for a porting order.

        This is used for
        partial porting in GB to specify which phone numbers should be kept or
        disconnected.

        Args:
          action: Specifies the action to take with this phone number during partial porting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return self._post(
            f"/porting_orders/{porting_order_id}/associated_phone_numbers",
            body=maybe_transform(
                {
                    "action": action,
                    "phone_number_range": phone_number_range,
                },
                associated_phone_number_create_params.AssociatedPhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociatedPhoneNumberCreateResponse,
        )

    def list(
        self,
        porting_order_id: str,
        *,
        filter: associated_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        page: associated_phone_number_list_params.Page | NotGiven = NOT_GIVEN,
        sort: associated_phone_number_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssociatedPhoneNumberListResponse:
        """Returns a list of all associated phone numbers for a porting order.

        Associated
        phone numbers are used for partial porting in GB to specify which phone numbers
        should be kept or disconnected.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[action]

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
            f"/porting_orders/{porting_order_id}/associated_phone_numbers",
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
                    associated_phone_number_list_params.AssociatedPhoneNumberListParams,
                ),
            ),
            cast_to=AssociatedPhoneNumberListResponse,
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
    ) -> AssociatedPhoneNumberDeleteResponse:
        """
        Deletes an associated phone number from a porting order.

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
            f"/porting_orders/{porting_order_id}/associated_phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociatedPhoneNumberDeleteResponse,
        )


class AsyncAssociatedPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssociatedPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssociatedPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociatedPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAssociatedPhoneNumbersResourceWithStreamingResponse(self)

    async def create(
        self,
        porting_order_id: str,
        *,
        action: Literal["keep", "disconnect"],
        phone_number_range: associated_phone_number_create_params.PhoneNumberRange,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssociatedPhoneNumberCreateResponse:
        """Creates a new associated phone number for a porting order.

        This is used for
        partial porting in GB to specify which phone numbers should be kept or
        disconnected.

        Args:
          action: Specifies the action to take with this phone number during partial porting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not porting_order_id:
            raise ValueError(f"Expected a non-empty value for `porting_order_id` but received {porting_order_id!r}")
        return await self._post(
            f"/porting_orders/{porting_order_id}/associated_phone_numbers",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "phone_number_range": phone_number_range,
                },
                associated_phone_number_create_params.AssociatedPhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociatedPhoneNumberCreateResponse,
        )

    async def list(
        self,
        porting_order_id: str,
        *,
        filter: associated_phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        page: associated_phone_number_list_params.Page | NotGiven = NOT_GIVEN,
        sort: associated_phone_number_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssociatedPhoneNumberListResponse:
        """Returns a list of all associated phone numbers for a porting order.

        Associated
        phone numbers are used for partial porting in GB to specify which phone numbers
        should be kept or disconnected.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[phone_number], filter[action]

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
            f"/porting_orders/{porting_order_id}/associated_phone_numbers",
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
                    associated_phone_number_list_params.AssociatedPhoneNumberListParams,
                ),
            ),
            cast_to=AssociatedPhoneNumberListResponse,
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
    ) -> AssociatedPhoneNumberDeleteResponse:
        """
        Deletes an associated phone number from a porting order.

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
            f"/porting_orders/{porting_order_id}/associated_phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssociatedPhoneNumberDeleteResponse,
        )


class AssociatedPhoneNumbersResourceWithRawResponse:
    def __init__(self, associated_phone_numbers: AssociatedPhoneNumbersResource) -> None:
        self._associated_phone_numbers = associated_phone_numbers

        self.create = to_raw_response_wrapper(
            associated_phone_numbers.create,
        )
        self.list = to_raw_response_wrapper(
            associated_phone_numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            associated_phone_numbers.delete,
        )


class AsyncAssociatedPhoneNumbersResourceWithRawResponse:
    def __init__(self, associated_phone_numbers: AsyncAssociatedPhoneNumbersResource) -> None:
        self._associated_phone_numbers = associated_phone_numbers

        self.create = async_to_raw_response_wrapper(
            associated_phone_numbers.create,
        )
        self.list = async_to_raw_response_wrapper(
            associated_phone_numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            associated_phone_numbers.delete,
        )


class AssociatedPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, associated_phone_numbers: AssociatedPhoneNumbersResource) -> None:
        self._associated_phone_numbers = associated_phone_numbers

        self.create = to_streamed_response_wrapper(
            associated_phone_numbers.create,
        )
        self.list = to_streamed_response_wrapper(
            associated_phone_numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            associated_phone_numbers.delete,
        )


class AsyncAssociatedPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, associated_phone_numbers: AsyncAssociatedPhoneNumbersResource) -> None:
        self._associated_phone_numbers = associated_phone_numbers

        self.create = async_to_streamed_response_wrapper(
            associated_phone_numbers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            associated_phone_numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            associated_phone_numbers.delete,
        )
