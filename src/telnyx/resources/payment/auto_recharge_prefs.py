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
from ...types.payment import auto_recharge_pref_update_params
from ...types.payment.auto_recharge_pref_list_response import AutoRechargePrefListResponse
from ...types.payment.auto_recharge_pref_update_response import AutoRechargePrefUpdateResponse

__all__ = ["AutoRechargePrefsResource", "AsyncAutoRechargePrefsResource"]


class AutoRechargePrefsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoRechargePrefsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AutoRechargePrefsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoRechargePrefsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AutoRechargePrefsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        invoice_enabled: bool | NotGiven = NOT_GIVEN,
        preference: Literal["credit_paypal", "ach"] | NotGiven = NOT_GIVEN,
        recharge_amount: str | NotGiven = NOT_GIVEN,
        threshold_amount: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRechargePrefUpdateResponse:
        """
        Update payment auto recharge preferences.

        Args:
          enabled: Whether auto recharge is enabled.

          preference: The payment preference for auto recharge.

          recharge_amount: The amount to recharge the account, the actual recharge amount will be the
              amount necessary to reach the threshold amount plus the recharge amount.

          threshold_amount: The threshold amount at which the account will be recharged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/payment/auto_recharge_prefs",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "invoice_enabled": invoice_enabled,
                    "preference": preference,
                    "recharge_amount": recharge_amount,
                    "threshold_amount": threshold_amount,
                },
                auto_recharge_pref_update_params.AutoRechargePrefUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRechargePrefUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRechargePrefListResponse:
        """Returns the payment auto recharge preferences."""
        return self._get(
            "/payment/auto_recharge_prefs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRechargePrefListResponse,
        )


class AsyncAutoRechargePrefsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoRechargePrefsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoRechargePrefsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoRechargePrefsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAutoRechargePrefsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        invoice_enabled: bool | NotGiven = NOT_GIVEN,
        preference: Literal["credit_paypal", "ach"] | NotGiven = NOT_GIVEN,
        recharge_amount: str | NotGiven = NOT_GIVEN,
        threshold_amount: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRechargePrefUpdateResponse:
        """
        Update payment auto recharge preferences.

        Args:
          enabled: Whether auto recharge is enabled.

          preference: The payment preference for auto recharge.

          recharge_amount: The amount to recharge the account, the actual recharge amount will be the
              amount necessary to reach the threshold amount plus the recharge amount.

          threshold_amount: The threshold amount at which the account will be recharged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/payment/auto_recharge_prefs",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "invoice_enabled": invoice_enabled,
                    "preference": preference,
                    "recharge_amount": recharge_amount,
                    "threshold_amount": threshold_amount,
                },
                auto_recharge_pref_update_params.AutoRechargePrefUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRechargePrefUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRechargePrefListResponse:
        """Returns the payment auto recharge preferences."""
        return await self._get(
            "/payment/auto_recharge_prefs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRechargePrefListResponse,
        )


class AutoRechargePrefsResourceWithRawResponse:
    def __init__(self, auto_recharge_prefs: AutoRechargePrefsResource) -> None:
        self._auto_recharge_prefs = auto_recharge_prefs

        self.update = to_raw_response_wrapper(
            auto_recharge_prefs.update,
        )
        self.list = to_raw_response_wrapper(
            auto_recharge_prefs.list,
        )


class AsyncAutoRechargePrefsResourceWithRawResponse:
    def __init__(self, auto_recharge_prefs: AsyncAutoRechargePrefsResource) -> None:
        self._auto_recharge_prefs = auto_recharge_prefs

        self.update = async_to_raw_response_wrapper(
            auto_recharge_prefs.update,
        )
        self.list = async_to_raw_response_wrapper(
            auto_recharge_prefs.list,
        )


class AutoRechargePrefsResourceWithStreamingResponse:
    def __init__(self, auto_recharge_prefs: AutoRechargePrefsResource) -> None:
        self._auto_recharge_prefs = auto_recharge_prefs

        self.update = to_streamed_response_wrapper(
            auto_recharge_prefs.update,
        )
        self.list = to_streamed_response_wrapper(
            auto_recharge_prefs.list,
        )


class AsyncAutoRechargePrefsResourceWithStreamingResponse:
    def __init__(self, auto_recharge_prefs: AsyncAutoRechargePrefsResource) -> None:
        self._auto_recharge_prefs = auto_recharge_prefs

        self.update = async_to_streamed_response_wrapper(
            auto_recharge_prefs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            auto_recharge_prefs.list,
        )
