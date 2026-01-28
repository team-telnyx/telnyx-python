# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...types import number_reservation_list_params, number_reservation_create_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ...types.number_reservation import NumberReservation
from ...types.reserved_phone_number_param import ReservedPhoneNumberParam
from ...types.number_reservation_create_response import NumberReservationCreateResponse
from ...types.number_reservation_retrieve_response import NumberReservationRetrieveResponse

__all__ = ["NumberReservationsResource", "AsyncNumberReservationsResource"]


class NumberReservationsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NumberReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumberReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumberReservationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_reference: str | Omit = omit,
        phone_numbers: Iterable[ReservedPhoneNumberParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberReservationCreateResponse:
        """
        Creates a Phone Number Reservation for multiple numbers.

        Args:
          customer_reference: A customer reference string for customer look ups.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/number_reservations",
            body=maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "phone_numbers": phone_numbers,
                },
                number_reservation_create_params.NumberReservationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberReservationCreateResponse,
        )

    def retrieve(
        self,
        number_reservation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberReservationRetrieveResponse:
        """
        Gets a single phone number reservation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_reservation_id:
            raise ValueError(
                f"Expected a non-empty value for `number_reservation_id` but received {number_reservation_id!r}"
            )
        return self._get(
            f"/number_reservations/{number_reservation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberReservationRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: number_reservation_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[NumberReservation]:
        """
        Gets a paginated list of phone number reservations.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[created_at], filter[phone_numbers.phone_number],
              filter[customer_reference]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/number_reservations",
            page=SyncDefaultFlatPagination[NumberReservation],
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
                    },
                    number_reservation_list_params.NumberReservationListParams,
                ),
            ),
            model=NumberReservation,
        )


class AsyncNumberReservationsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNumberReservationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberReservationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberReservationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumberReservationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_reference: str | Omit = omit,
        phone_numbers: Iterable[ReservedPhoneNumberParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberReservationCreateResponse:
        """
        Creates a Phone Number Reservation for multiple numbers.

        Args:
          customer_reference: A customer reference string for customer look ups.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/number_reservations",
            body=await async_maybe_transform(
                {
                    "customer_reference": customer_reference,
                    "phone_numbers": phone_numbers,
                },
                number_reservation_create_params.NumberReservationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberReservationCreateResponse,
        )

    async def retrieve(
        self,
        number_reservation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberReservationRetrieveResponse:
        """
        Gets a single phone number reservation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number_reservation_id:
            raise ValueError(
                f"Expected a non-empty value for `number_reservation_id` but received {number_reservation_id!r}"
            )
        return await self._get(
            f"/number_reservations/{number_reservation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberReservationRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: number_reservation_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NumberReservation, AsyncDefaultFlatPagination[NumberReservation]]:
        """
        Gets a paginated list of phone number reservations.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[created_at], filter[phone_numbers.phone_number],
              filter[customer_reference]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/number_reservations",
            page=AsyncDefaultFlatPagination[NumberReservation],
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
                    },
                    number_reservation_list_params.NumberReservationListParams,
                ),
            ),
            model=NumberReservation,
        )


class NumberReservationsResourceWithRawResponse:
    def __init__(self, number_reservations: NumberReservationsResource) -> None:
        self._number_reservations = number_reservations

        self.create = to_raw_response_wrapper(
            number_reservations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            number_reservations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            number_reservations.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._number_reservations.actions)


class AsyncNumberReservationsResourceWithRawResponse:
    def __init__(self, number_reservations: AsyncNumberReservationsResource) -> None:
        self._number_reservations = number_reservations

        self.create = async_to_raw_response_wrapper(
            number_reservations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            number_reservations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            number_reservations.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._number_reservations.actions)


class NumberReservationsResourceWithStreamingResponse:
    def __init__(self, number_reservations: NumberReservationsResource) -> None:
        self._number_reservations = number_reservations

        self.create = to_streamed_response_wrapper(
            number_reservations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            number_reservations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            number_reservations.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._number_reservations.actions)


class AsyncNumberReservationsResourceWithStreamingResponse:
    def __init__(self, number_reservations: AsyncNumberReservationsResource) -> None:
        self._number_reservations = number_reservations

        self.create = async_to_streamed_response_wrapper(
            number_reservations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            number_reservations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            number_reservations.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._number_reservations.actions)
