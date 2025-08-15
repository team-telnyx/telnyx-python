# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    messaging_hosted_number_order_list_params,
    messaging_hosted_number_order_create_params,
    messaging_hosted_number_order_validate_codes_params,
    messaging_hosted_number_order_check_eligibility_params,
    messaging_hosted_number_order_create_verification_codes_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ...types.messaging_hosted_number_order_list_response import MessagingHostedNumberOrderListResponse
from ...types.messaging_hosted_number_order_create_response import MessagingHostedNumberOrderCreateResponse
from ...types.messaging_hosted_number_order_delete_response import MessagingHostedNumberOrderDeleteResponse
from ...types.messaging_hosted_number_order_retrieve_response import MessagingHostedNumberOrderRetrieveResponse
from ...types.messaging_hosted_number_order_validate_codes_response import (
    MessagingHostedNumberOrderValidateCodesResponse,
)
from ...types.messaging_hosted_number_order_check_eligibility_response import (
    MessagingHostedNumberOrderCheckEligibilityResponse,
)
from ...types.messaging_hosted_number_order_create_verification_codes_response import (
    MessagingHostedNumberOrderCreateVerificationCodesResponse,
)

__all__ = ["MessagingHostedNumberOrdersResource", "AsyncMessagingHostedNumberOrdersResource"]


class MessagingHostedNumberOrdersResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagingHostedNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MessagingHostedNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagingHostedNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MessagingHostedNumberOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        phone_numbers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderCreateResponse:
        """
        Create a messaging hosted number order

        Args:
          messaging_profile_id: Automatically associate the number with this messaging profile ID when the order
              is complete.

          phone_numbers: Phone numbers to be used for hosted messaging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messaging_hosted_number_orders",
            body=maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "phone_numbers": phone_numbers,
                },
                messaging_hosted_number_order_create_params.MessagingHostedNumberOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderCreateResponse,
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
    ) -> MessagingHostedNumberOrderRetrieveResponse:
        """
        Retrieve a messaging hosted number order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/messaging_hosted_number_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderRetrieveResponse,
        )

    def list(
        self,
        *,
        page: messaging_hosted_number_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderListResponse:
        """
        List messaging hosted number orders

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/messaging_hosted_number_orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page}, messaging_hosted_number_order_list_params.MessagingHostedNumberOrderListParams
                ),
            ),
            cast_to=MessagingHostedNumberOrderListResponse,
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
    ) -> MessagingHostedNumberOrderDeleteResponse:
        """
        Delete a messaging hosted number order and all associated phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/messaging_hosted_number_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderDeleteResponse,
        )

    def check_eligibility(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderCheckEligibilityResponse:
        """
        Check eligibility of phone numbers for hosted messaging

        Args:
          phone_numbers: List of phone numbers to check eligibility

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messaging_hosted_number_orders/eligibility_numbers_check",
            body=maybe_transform(
                {"phone_numbers": phone_numbers},
                messaging_hosted_number_order_check_eligibility_params.MessagingHostedNumberOrderCheckEligibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderCheckEligibilityResponse,
        )

    def create_verification_codes(
        self,
        id: str,
        *,
        phone_numbers: List[str],
        verification_method: Literal["sms", "call", "flashcall"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderCreateVerificationCodesResponse:
        """Create verification codes to validate numbers of the hosted order.

        The
        verification codes will be sent to the numbers of the hosted order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/messaging_hosted_number_orders/{id}/verification_codes",
            body=maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "verification_method": verification_method,
                },
                messaging_hosted_number_order_create_verification_codes_params.MessagingHostedNumberOrderCreateVerificationCodesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderCreateVerificationCodesResponse,
        )

    def validate_codes(
        self,
        id: str,
        *,
        verification_codes: Iterable[messaging_hosted_number_order_validate_codes_params.VerificationCode],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderValidateCodesResponse:
        """Validate the verification codes sent to the numbers of the hosted order.

        The
        verification codes must be created in the verification codes endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/messaging_hosted_number_orders/{id}/validation_codes",
            body=maybe_transform(
                {"verification_codes": verification_codes},
                messaging_hosted_number_order_validate_codes_params.MessagingHostedNumberOrderValidateCodesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderValidateCodesResponse,
        )


class AsyncMessagingHostedNumberOrdersResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagingHostedNumberOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagingHostedNumberOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messaging_profile_id: str | NotGiven = NOT_GIVEN,
        phone_numbers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderCreateResponse:
        """
        Create a messaging hosted number order

        Args:
          messaging_profile_id: Automatically associate the number with this messaging profile ID when the order
              is complete.

          phone_numbers: Phone numbers to be used for hosted messaging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messaging_hosted_number_orders",
            body=await async_maybe_transform(
                {
                    "messaging_profile_id": messaging_profile_id,
                    "phone_numbers": phone_numbers,
                },
                messaging_hosted_number_order_create_params.MessagingHostedNumberOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderCreateResponse,
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
    ) -> MessagingHostedNumberOrderRetrieveResponse:
        """
        Retrieve a messaging hosted number order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/messaging_hosted_number_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: messaging_hosted_number_order_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderListResponse:
        """
        List messaging hosted number orders

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/messaging_hosted_number_orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, messaging_hosted_number_order_list_params.MessagingHostedNumberOrderListParams
                ),
            ),
            cast_to=MessagingHostedNumberOrderListResponse,
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
    ) -> MessagingHostedNumberOrderDeleteResponse:
        """
        Delete a messaging hosted number order and all associated phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/messaging_hosted_number_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderDeleteResponse,
        )

    async def check_eligibility(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderCheckEligibilityResponse:
        """
        Check eligibility of phone numbers for hosted messaging

        Args:
          phone_numbers: List of phone numbers to check eligibility

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messaging_hosted_number_orders/eligibility_numbers_check",
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers},
                messaging_hosted_number_order_check_eligibility_params.MessagingHostedNumberOrderCheckEligibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderCheckEligibilityResponse,
        )

    async def create_verification_codes(
        self,
        id: str,
        *,
        phone_numbers: List[str],
        verification_method: Literal["sms", "call", "flashcall"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderCreateVerificationCodesResponse:
        """Create verification codes to validate numbers of the hosted order.

        The
        verification codes will be sent to the numbers of the hosted order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/messaging_hosted_number_orders/{id}/verification_codes",
            body=await async_maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "verification_method": verification_method,
                },
                messaging_hosted_number_order_create_verification_codes_params.MessagingHostedNumberOrderCreateVerificationCodesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderCreateVerificationCodesResponse,
        )

    async def validate_codes(
        self,
        id: str,
        *,
        verification_codes: Iterable[messaging_hosted_number_order_validate_codes_params.VerificationCode],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessagingHostedNumberOrderValidateCodesResponse:
        """Validate the verification codes sent to the numbers of the hosted order.

        The
        verification codes must be created in the verification codes endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/messaging_hosted_number_orders/{id}/validation_codes",
            body=await async_maybe_transform(
                {"verification_codes": verification_codes},
                messaging_hosted_number_order_validate_codes_params.MessagingHostedNumberOrderValidateCodesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagingHostedNumberOrderValidateCodesResponse,
        )


class MessagingHostedNumberOrdersResourceWithRawResponse:
    def __init__(self, messaging_hosted_number_orders: MessagingHostedNumberOrdersResource) -> None:
        self._messaging_hosted_number_orders = messaging_hosted_number_orders

        self.create = to_raw_response_wrapper(
            messaging_hosted_number_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            messaging_hosted_number_orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messaging_hosted_number_orders.list,
        )
        self.delete = to_raw_response_wrapper(
            messaging_hosted_number_orders.delete,
        )
        self.check_eligibility = to_raw_response_wrapper(
            messaging_hosted_number_orders.check_eligibility,
        )
        self.create_verification_codes = to_raw_response_wrapper(
            messaging_hosted_number_orders.create_verification_codes,
        )
        self.validate_codes = to_raw_response_wrapper(
            messaging_hosted_number_orders.validate_codes,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._messaging_hosted_number_orders.actions)


class AsyncMessagingHostedNumberOrdersResourceWithRawResponse:
    def __init__(self, messaging_hosted_number_orders: AsyncMessagingHostedNumberOrdersResource) -> None:
        self._messaging_hosted_number_orders = messaging_hosted_number_orders

        self.create = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.delete,
        )
        self.check_eligibility = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.check_eligibility,
        )
        self.create_verification_codes = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.create_verification_codes,
        )
        self.validate_codes = async_to_raw_response_wrapper(
            messaging_hosted_number_orders.validate_codes,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._messaging_hosted_number_orders.actions)


class MessagingHostedNumberOrdersResourceWithStreamingResponse:
    def __init__(self, messaging_hosted_number_orders: MessagingHostedNumberOrdersResource) -> None:
        self._messaging_hosted_number_orders = messaging_hosted_number_orders

        self.create = to_streamed_response_wrapper(
            messaging_hosted_number_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            messaging_hosted_number_orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messaging_hosted_number_orders.list,
        )
        self.delete = to_streamed_response_wrapper(
            messaging_hosted_number_orders.delete,
        )
        self.check_eligibility = to_streamed_response_wrapper(
            messaging_hosted_number_orders.check_eligibility,
        )
        self.create_verification_codes = to_streamed_response_wrapper(
            messaging_hosted_number_orders.create_verification_codes,
        )
        self.validate_codes = to_streamed_response_wrapper(
            messaging_hosted_number_orders.validate_codes,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._messaging_hosted_number_orders.actions)


class AsyncMessagingHostedNumberOrdersResourceWithStreamingResponse:
    def __init__(self, messaging_hosted_number_orders: AsyncMessagingHostedNumberOrdersResource) -> None:
        self._messaging_hosted_number_orders = messaging_hosted_number_orders

        self.create = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.delete,
        )
        self.check_eligibility = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.check_eligibility,
        )
        self.create_verification_codes = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.create_verification_codes,
        )
        self.validate_codes = async_to_streamed_response_wrapper(
            messaging_hosted_number_orders.validate_codes,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._messaging_hosted_number_orders.actions)
