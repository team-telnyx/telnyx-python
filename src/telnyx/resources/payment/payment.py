# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import payment_create_stored_payment_transaction_params
from ..._types import Body, Query, Headers, NotGiven, not_given
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
from .auto_recharge_prefs import (
    AutoRechargePrefsResource,
    AsyncAutoRechargePrefsResource,
    AutoRechargePrefsResourceWithRawResponse,
    AsyncAutoRechargePrefsResourceWithRawResponse,
    AutoRechargePrefsResourceWithStreamingResponse,
    AsyncAutoRechargePrefsResourceWithStreamingResponse,
)
from ...types.payment_create_stored_payment_transaction_response import PaymentCreateStoredPaymentTransactionResponse

__all__ = ["PaymentResource", "AsyncPaymentResource"]


class PaymentResource(SyncAPIResource):
    @cached_property
    def auto_recharge_prefs(self) -> AutoRechargePrefsResource:
        return AutoRechargePrefsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PaymentResourceWithStreamingResponse(self)

    def create_stored_payment_transaction(
        self,
        *,
        amount: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateStoredPaymentTransactionResponse:
        """
        Create a stored payment transaction

        Args:
          amount: Amount in dollars and cents, e.g. "120.00"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/payment/stored_payment_transactions",
            body=maybe_transform(
                {"amount": amount},
                payment_create_stored_payment_transaction_params.PaymentCreateStoredPaymentTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateStoredPaymentTransactionResponse,
        )


class AsyncPaymentResource(AsyncAPIResource):
    @cached_property
    def auto_recharge_prefs(self) -> AsyncAutoRechargePrefsResource:
        return AsyncAutoRechargePrefsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPaymentResourceWithStreamingResponse(self)

    async def create_stored_payment_transaction(
        self,
        *,
        amount: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentCreateStoredPaymentTransactionResponse:
        """
        Create a stored payment transaction

        Args:
          amount: Amount in dollars and cents, e.g. "120.00"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/payment/stored_payment_transactions",
            body=await async_maybe_transform(
                {"amount": amount},
                payment_create_stored_payment_transaction_params.PaymentCreateStoredPaymentTransactionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateStoredPaymentTransactionResponse,
        )


class PaymentResourceWithRawResponse:
    def __init__(self, payment: PaymentResource) -> None:
        self._payment = payment

        self.create_stored_payment_transaction = to_raw_response_wrapper(
            payment.create_stored_payment_transaction,
        )

    @cached_property
    def auto_recharge_prefs(self) -> AutoRechargePrefsResourceWithRawResponse:
        return AutoRechargePrefsResourceWithRawResponse(self._payment.auto_recharge_prefs)


class AsyncPaymentResourceWithRawResponse:
    def __init__(self, payment: AsyncPaymentResource) -> None:
        self._payment = payment

        self.create_stored_payment_transaction = async_to_raw_response_wrapper(
            payment.create_stored_payment_transaction,
        )

    @cached_property
    def auto_recharge_prefs(self) -> AsyncAutoRechargePrefsResourceWithRawResponse:
        return AsyncAutoRechargePrefsResourceWithRawResponse(self._payment.auto_recharge_prefs)


class PaymentResourceWithStreamingResponse:
    def __init__(self, payment: PaymentResource) -> None:
        self._payment = payment

        self.create_stored_payment_transaction = to_streamed_response_wrapper(
            payment.create_stored_payment_transaction,
        )

    @cached_property
    def auto_recharge_prefs(self) -> AutoRechargePrefsResourceWithStreamingResponse:
        return AutoRechargePrefsResourceWithStreamingResponse(self._payment.auto_recharge_prefs)


class AsyncPaymentResourceWithStreamingResponse:
    def __init__(self, payment: AsyncPaymentResource) -> None:
        self._payment = payment

        self.create_stored_payment_transaction = async_to_streamed_response_wrapper(
            payment.create_stored_payment_transaction,
        )

    @cached_property
    def auto_recharge_prefs(self) -> AsyncAutoRechargePrefsResourceWithStreamingResponse:
        return AsyncAutoRechargePrefsResourceWithStreamingResponse(self._payment.auto_recharge_prefs)
