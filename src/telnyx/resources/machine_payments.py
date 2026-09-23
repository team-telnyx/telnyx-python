# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import machine_payment_account_credit_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.machine_payment_account_credit_response import MachinePaymentAccountCreditResponse

__all__ = ["MachinePaymentsResource", "AsyncMachinePaymentsResource"]


class MachinePaymentsResource(SyncAPIResource):
    """Machine payment (MPP) account-credit operations.

    Fund your Telnyx account programmatically from a machine or agent using the Machine Payment Protocol, an HTTP-402 flow settled via Stripe or Tempo.
    """

    @cached_property
    def with_raw_response(self) -> MachinePaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MachinePaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MachinePaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MachinePaymentsResourceWithStreamingResponse(self)

    def account_credit(
        self,
        *,
        amount_usd: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachinePaymentAccountCreditResponse:
        """
        Creates an account credit using the Machine Payment Protocol (MPP), an HTTP-402
        payment flow for machines and agents.

        The flow has two steps. First, send an authenticated request with the
        `amount_usd` to credit; the response is `402 Payment Required` with one or more
        payment challenges (for example separate Tempo and Stripe challenges) in the
        `WWW-Authenticate` header. Second, retry the request with an
        `Authorization: Payment ...` credential constructed from the challenge; on
        success the response includes the credited transaction and a `Payment-Receipt`
        header.

        The credited account is never chosen by the request body: the initial request
        credits the account of the authenticated user, and a paid retry credits the
        account bound to the verified payment credential. The amount must be within the
        configured bounds (by default between 5.00 and 500.00 USD).

        Successful paid retries are idempotent — when Rails reaches its
        duplicate-transaction lookup for an already-recorded payment, it returns the
        existing transaction with `created: false` instead of crediting the account
        again. This deduplication applies to successful fulfillment: re-sending the same
        Stripe credential may instead be rejected by the upstream provider as an
        idempotent replay and return `402 Payment Required` rather than the existing
        transaction.

        > **Warning: the payment credential is bound to a specific Telnyx account ID.**
        > A payment is captured before the bound account is validated. If the credential
        > names an account that is missing, suspended, blocked, cancelled, dormant, or
        > ineligible for the tier, the payment is captured but **no account is
        > credited**. If the credential names a different but eligible account, that
        > account is credited — the service does not compare it against the payer's
        > account. There is **no automatic refund**: if the captured payment does not
        > credit the intended account, contact Telnyx support for remediation.

        Args:
          amount_usd: Amount to credit in USD, as a decimal string with up to two fractional digits
              (by default between 5.00 and 500.00). The request body is required on the
              initial challenge request and remains required on a paid retry, where you
              re-send the identical body plus the payment credential — the credential, not the
              body, selects the payment, and the retried body is not re-validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/machine-payments/account-credit",
            body=maybe_transform(
                {"amount_usd": amount_usd}, machine_payment_account_credit_params.MachinePaymentAccountCreditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MachinePaymentAccountCreditResponse,
        )


class AsyncMachinePaymentsResource(AsyncAPIResource):
    """Machine payment (MPP) account-credit operations.

    Fund your Telnyx account programmatically from a machine or agent using the Machine Payment Protocol, an HTTP-402 flow settled via Stripe or Tempo.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMachinePaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMachinePaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMachinePaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMachinePaymentsResourceWithStreamingResponse(self)

    async def account_credit(
        self,
        *,
        amount_usd: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachinePaymentAccountCreditResponse:
        """
        Creates an account credit using the Machine Payment Protocol (MPP), an HTTP-402
        payment flow for machines and agents.

        The flow has two steps. First, send an authenticated request with the
        `amount_usd` to credit; the response is `402 Payment Required` with one or more
        payment challenges (for example separate Tempo and Stripe challenges) in the
        `WWW-Authenticate` header. Second, retry the request with an
        `Authorization: Payment ...` credential constructed from the challenge; on
        success the response includes the credited transaction and a `Payment-Receipt`
        header.

        The credited account is never chosen by the request body: the initial request
        credits the account of the authenticated user, and a paid retry credits the
        account bound to the verified payment credential. The amount must be within the
        configured bounds (by default between 5.00 and 500.00 USD).

        Successful paid retries are idempotent — when Rails reaches its
        duplicate-transaction lookup for an already-recorded payment, it returns the
        existing transaction with `created: false` instead of crediting the account
        again. This deduplication applies to successful fulfillment: re-sending the same
        Stripe credential may instead be rejected by the upstream provider as an
        idempotent replay and return `402 Payment Required` rather than the existing
        transaction.

        > **Warning: the payment credential is bound to a specific Telnyx account ID.**
        > A payment is captured before the bound account is validated. If the credential
        > names an account that is missing, suspended, blocked, cancelled, dormant, or
        > ineligible for the tier, the payment is captured but **no account is
        > credited**. If the credential names a different but eligible account, that
        > account is credited — the service does not compare it against the payer's
        > account. There is **no automatic refund**: if the captured payment does not
        > credit the intended account, contact Telnyx support for remediation.

        Args:
          amount_usd: Amount to credit in USD, as a decimal string with up to two fractional digits
              (by default between 5.00 and 500.00). The request body is required on the
              initial challenge request and remains required on a paid retry, where you
              re-send the identical body plus the payment credential — the credential, not the
              body, selects the payment, and the retried body is not re-validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/machine-payments/account-credit",
            body=await async_maybe_transform(
                {"amount_usd": amount_usd}, machine_payment_account_credit_params.MachinePaymentAccountCreditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MachinePaymentAccountCreditResponse,
        )


class MachinePaymentsResourceWithRawResponse:
    def __init__(self, machine_payments: MachinePaymentsResource) -> None:
        self._machine_payments = machine_payments

        self.account_credit = to_raw_response_wrapper(
            machine_payments.account_credit,
        )


class AsyncMachinePaymentsResourceWithRawResponse:
    def __init__(self, machine_payments: AsyncMachinePaymentsResource) -> None:
        self._machine_payments = machine_payments

        self.account_credit = async_to_raw_response_wrapper(
            machine_payments.account_credit,
        )


class MachinePaymentsResourceWithStreamingResponse:
    def __init__(self, machine_payments: MachinePaymentsResource) -> None:
        self._machine_payments = machine_payments

        self.account_credit = to_streamed_response_wrapper(
            machine_payments.account_credit,
        )


class AsyncMachinePaymentsResourceWithStreamingResponse:
    def __init__(self, machine_payments: AsyncMachinePaymentsResource) -> None:
        self._machine_payments = machine_payments

        self.account_credit = async_to_streamed_response_wrapper(
            machine_payments.account_credit,
        )
