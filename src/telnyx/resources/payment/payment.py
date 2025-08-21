# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .auto_recharge_prefs import (
    AutoRechargePrefsResource,
    AsyncAutoRechargePrefsResource,
    AutoRechargePrefsResourceWithRawResponse,
    AsyncAutoRechargePrefsResourceWithRawResponse,
    AutoRechargePrefsResourceWithStreamingResponse,
    AsyncAutoRechargePrefsResourceWithStreamingResponse,
)

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


class PaymentResourceWithRawResponse:
    def __init__(self, payment: PaymentResource) -> None:
        self._payment = payment

    @cached_property
    def auto_recharge_prefs(self) -> AutoRechargePrefsResourceWithRawResponse:
        return AutoRechargePrefsResourceWithRawResponse(self._payment.auto_recharge_prefs)


class AsyncPaymentResourceWithRawResponse:
    def __init__(self, payment: AsyncPaymentResource) -> None:
        self._payment = payment

    @cached_property
    def auto_recharge_prefs(self) -> AsyncAutoRechargePrefsResourceWithRawResponse:
        return AsyncAutoRechargePrefsResourceWithRawResponse(self._payment.auto_recharge_prefs)


class PaymentResourceWithStreamingResponse:
    def __init__(self, payment: PaymentResource) -> None:
        self._payment = payment

    @cached_property
    def auto_recharge_prefs(self) -> AutoRechargePrefsResourceWithStreamingResponse:
        return AutoRechargePrefsResourceWithStreamingResponse(self._payment.auto_recharge_prefs)


class AsyncPaymentResourceWithStreamingResponse:
    def __init__(self, payment: AsyncPaymentResource) -> None:
        self._payment = payment

    @cached_property
    def auto_recharge_prefs(self) -> AsyncAutoRechargePrefsResourceWithStreamingResponse:
        return AsyncAutoRechargePrefsResourceWithStreamingResponse(self._payment.auto_recharge_prefs)
