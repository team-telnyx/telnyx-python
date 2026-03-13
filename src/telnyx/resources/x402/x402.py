# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .credit_account import (
    CreditAccountResource,
    AsyncCreditAccountResource,
    CreditAccountResourceWithRawResponse,
    AsyncCreditAccountResourceWithRawResponse,
    CreditAccountResourceWithStreamingResponse,
    AsyncCreditAccountResourceWithStreamingResponse,
)

__all__ = ["X402Resource", "AsyncX402Resource"]


class X402Resource(SyncAPIResource):
    @cached_property
    def credit_account(self) -> CreditAccountResource:
        """Operations for x402 cryptocurrency payment transactions.

        Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
        """
        return CreditAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> X402ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return X402ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> X402ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return X402ResourceWithStreamingResponse(self)


class AsyncX402Resource(AsyncAPIResource):
    @cached_property
    def credit_account(self) -> AsyncCreditAccountResource:
        """Operations for x402 cryptocurrency payment transactions.

        Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
        """
        return AsyncCreditAccountResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncX402ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncX402ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncX402ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncX402ResourceWithStreamingResponse(self)


class X402ResourceWithRawResponse:
    def __init__(self, x402: X402Resource) -> None:
        self._x402 = x402

    @cached_property
    def credit_account(self) -> CreditAccountResourceWithRawResponse:
        """Operations for x402 cryptocurrency payment transactions.

        Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
        """
        return CreditAccountResourceWithRawResponse(self._x402.credit_account)


class AsyncX402ResourceWithRawResponse:
    def __init__(self, x402: AsyncX402Resource) -> None:
        self._x402 = x402

    @cached_property
    def credit_account(self) -> AsyncCreditAccountResourceWithRawResponse:
        """Operations for x402 cryptocurrency payment transactions.

        Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
        """
        return AsyncCreditAccountResourceWithRawResponse(self._x402.credit_account)


class X402ResourceWithStreamingResponse:
    def __init__(self, x402: X402Resource) -> None:
        self._x402 = x402

    @cached_property
    def credit_account(self) -> CreditAccountResourceWithStreamingResponse:
        """Operations for x402 cryptocurrency payment transactions.

        Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
        """
        return CreditAccountResourceWithStreamingResponse(self._x402.credit_account)


class AsyncX402ResourceWithStreamingResponse:
    def __init__(self, x402: AsyncX402Resource) -> None:
        self._x402 = x402

    @cached_property
    def credit_account(self) -> AsyncCreditAccountResourceWithStreamingResponse:
        """Operations for x402 cryptocurrency payment transactions.

        Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
        """
        return AsyncCreditAccountResourceWithStreamingResponse(self._x402.credit_account)
