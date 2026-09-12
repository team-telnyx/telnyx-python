# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.x402.credit_account import payment_list_params
from ....types.x402.credit_account.x402_transaction_record import X402TransactionRecord
from ....types.x402.credit_account.payment_retrieve_response import PaymentRetrieveResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    """Operations for x402 cryptocurrency payment transactions.

    Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
    """

    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRetrieveResponse:
        """Returns a single x402 payment transaction by ID.

        The transaction must belong to
        the authenticated user; organization sub-users must have read permission on
        transactions. Returns 404 if the transaction does not exist or belongs to
        another user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v2/x402/credit_account/payments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[X402TransactionRecord]:
        """
        Returns a paginated list of the authenticated user's x402 payment transactions,
        newest first. Organization sub-users must have read permission on transactions;
        without it the list is empty.

        Args:
          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/x402/credit_account/payments",
            page=SyncDefaultFlatPagination[X402TransactionRecord],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=X402TransactionRecord,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    """Operations for x402 cryptocurrency payment transactions.

    Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentRetrieveResponse:
        """Returns a single x402 payment transaction by ID.

        The transaction must belong to
        the authenticated user; organization sub-users must have read permission on
        transactions. Returns 404 if the transaction does not exist or belongs to
        another user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v2/x402/credit_account/payments/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[X402TransactionRecord, AsyncDefaultFlatPagination[X402TransactionRecord]]:
        """
        Returns a paginated list of the authenticated user's x402 payment transactions,
        newest first. Organization sub-users must have read permission on transactions;
        without it the list is empty.

        Args:
          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/x402/credit_account/payments",
            page=AsyncDefaultFlatPagination[X402TransactionRecord],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=X402TransactionRecord,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.retrieve = to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            payments.list,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.retrieve = async_to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            payments.list,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payments.list,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
