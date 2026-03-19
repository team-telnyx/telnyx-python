# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.x402 import credit_account_settle_payment_params, credit_account_create_payment_quote_params
from ..._base_client import make_request_options
from ...types.x402.credit_account_settle_payment_response import CreditAccountSettlePaymentResponse
from ...types.x402.credit_account_create_payment_quote_response import CreditAccountCreatePaymentQuoteResponse

__all__ = ["CreditAccountResource", "AsyncCreditAccountResource"]


class CreditAccountResource(SyncAPIResource):
    """Operations for x402 cryptocurrency payment transactions.

    Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
    """

    @cached_property
    def with_raw_response(self) -> CreditAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CreditAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CreditAccountResourceWithStreamingResponse(self)

    def create_payment_quote(
        self,
        *,
        amount_usd: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditAccountCreatePaymentQuoteResponse:
        """Creates a payment quote for the specified USD amount.

        Returns payment details
        including the x402 payment requirements, network, and expiration time. The quote
        must be settled before it expires.

        Args:
          amount_usd: Amount in USD to fund (minimum 5.00, maximum 10000.00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/x402/credit_account/quote",
            body=maybe_transform(
                {"amount_usd": amount_usd},
                credit_account_create_payment_quote_params.CreditAccountCreatePaymentQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditAccountCreatePaymentQuoteResponse,
        )

    def settle_payment(
        self,
        *,
        id: str,
        body_payment_signature: str | Omit = omit,
        header_payment_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditAccountSettlePaymentResponse:
        """
        Settles an x402 payment using the quote ID and a signed payment authorization.
        The payment signature can be provided via the `PAYMENT-SIGNATURE` header or the
        `payment_signature` body parameter. Settlement is idempotent — submitting the
        same quote ID multiple times returns the existing transaction.

        Args:
          id: The quote ID to settle.

          body_payment_signature: Base64-encoded signed payment authorization (x402 PaymentPayload). Can
              alternatively be provided via the PAYMENT-SIGNATURE header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"PAYMENT-SIGNATURE": header_payment_signature}), **(extra_headers or {})}
        return self._post(
            "/v2/x402/credit_account",
            body=maybe_transform(
                {
                    "id": id,
                    "body_payment_signature": body_payment_signature,
                },
                credit_account_settle_payment_params.CreditAccountSettlePaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditAccountSettlePaymentResponse,
        )


class AsyncCreditAccountResource(AsyncAPIResource):
    """Operations for x402 cryptocurrency payment transactions.

    Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCreditAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCreditAccountResourceWithStreamingResponse(self)

    async def create_payment_quote(
        self,
        *,
        amount_usd: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditAccountCreatePaymentQuoteResponse:
        """Creates a payment quote for the specified USD amount.

        Returns payment details
        including the x402 payment requirements, network, and expiration time. The quote
        must be settled before it expires.

        Args:
          amount_usd: Amount in USD to fund (minimum 5.00, maximum 10000.00).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/x402/credit_account/quote",
            body=await async_maybe_transform(
                {"amount_usd": amount_usd},
                credit_account_create_payment_quote_params.CreditAccountCreatePaymentQuoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditAccountCreatePaymentQuoteResponse,
        )

    async def settle_payment(
        self,
        *,
        id: str,
        body_payment_signature: str | Omit = omit,
        header_payment_signature: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditAccountSettlePaymentResponse:
        """
        Settles an x402 payment using the quote ID and a signed payment authorization.
        The payment signature can be provided via the `PAYMENT-SIGNATURE` header or the
        `payment_signature` body parameter. Settlement is idempotent — submitting the
        same quote ID multiple times returns the existing transaction.

        Args:
          id: The quote ID to settle.

          body_payment_signature: Base64-encoded signed payment authorization (x402 PaymentPayload). Can
              alternatively be provided via the PAYMENT-SIGNATURE header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"PAYMENT-SIGNATURE": header_payment_signature}), **(extra_headers or {})}
        return await self._post(
            "/v2/x402/credit_account",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "body_payment_signature": body_payment_signature,
                },
                credit_account_settle_payment_params.CreditAccountSettlePaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditAccountSettlePaymentResponse,
        )


class CreditAccountResourceWithRawResponse:
    def __init__(self, credit_account: CreditAccountResource) -> None:
        self._credit_account = credit_account

        self.create_payment_quote = to_raw_response_wrapper(
            credit_account.create_payment_quote,
        )
        self.settle_payment = to_raw_response_wrapper(
            credit_account.settle_payment,
        )


class AsyncCreditAccountResourceWithRawResponse:
    def __init__(self, credit_account: AsyncCreditAccountResource) -> None:
        self._credit_account = credit_account

        self.create_payment_quote = async_to_raw_response_wrapper(
            credit_account.create_payment_quote,
        )
        self.settle_payment = async_to_raw_response_wrapper(
            credit_account.settle_payment,
        )


class CreditAccountResourceWithStreamingResponse:
    def __init__(self, credit_account: CreditAccountResource) -> None:
        self._credit_account = credit_account

        self.create_payment_quote = to_streamed_response_wrapper(
            credit_account.create_payment_quote,
        )
        self.settle_payment = to_streamed_response_wrapper(
            credit_account.settle_payment,
        )


class AsyncCreditAccountResourceWithStreamingResponse:
    def __init__(self, credit_account: AsyncCreditAccountResource) -> None:
        self._credit_account = credit_account

        self.create_payment_quote = async_to_streamed_response_wrapper(
            credit_account.create_payment_quote,
        )
        self.settle_payment = async_to_streamed_response_wrapper(
            credit_account.settle_payment,
        )
