# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import SpendLimitPeriod, spend_limit_create_params, spend_limit_delete_params, spend_limit_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.spend_limit_period import SpendLimitPeriod
from ..types.spend_limit_response import SpendLimitResponse
from ..types.spend_limit_list_response import SpendLimitListResponse

__all__ = ["SpendLimitsResource", "AsyncSpendLimitsResource"]


class SpendLimitsResource(SyncAPIResource):
    """Daily and monthly spend limits per product.

    A limit applies to the organization of the authenticated user, or to the user's own account when they belong to no organization; every user of the organization sees and changes the same limits.

    - **Periods.** `daily` covers the current UTC day and `monthly` the current UTC calendar month. The two limits are independent: you can set either, both or neither.
    - **Blocking.** When spend in a period goes above the limit (strictly greater), the product is blocked until the period ends: 00:00 UTC the next day for `daily`, 00:00 UTC on the 1st of the next month for `monthly`. A block appears within about 2 minutes (daily) or 10 minutes (monthly) of the spend being recorded.
    - **Changes apply immediately.** Creating, updating or deleting a limit checks the period's spend in the same request: raising the limit above the spend, or removing it, lifts that period's block, and lowering it below the spend blocks the product at once. The `evaluation` object in the response says what happened.
    - **Supported products.** Today only `inference` supports spend limits. A blocked account gets HTTP 403 with the error title `Inference spend limit reached` (code `10039`) on new billable chat completions, Responses, Anthropic Messages and classification requests; requests already running finish normally. Take the list of products from the list operation.
    - **Limits set by Telnyx.** Telnyx support can also set a limit on your account. It is listed with `origin: operator` and you can update or delete it like your own.
    """

    @cached_property
    def with_raw_response(self) -> SpendLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SpendLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SpendLimitsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        amount: float,
        product: str,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Sets a limit for a product and period that has none.

        Send exactly one of
        `amount` and `unlimited: true`. The period's spend is checked at once: if it is
        already above the new limit, the product is blocked immediately
        (`evaluation.blocked_now`). Returns 409 when a limit already exists for the
        product and period; update it instead.

        Args:
          amount: Limit in USD. `0` blocks at the first cent of spend.

          product: Product to limit, as returned in `product` by the list operation.

          period: `daily` is the current UTC day; `monthly` is the current UTC calendar month.

          reason: Why the limit is set or changed, kept for audit.

          unlimited: Optional; only `false` is allowed together with `amount`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        product: str,
        unlimited: Literal[True],
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Sets a limit for a product and period that has none.

        Send exactly one of
        `amount` and `unlimited: true`. The period's spend is checked at once: if it is
        already above the new limit, the product is blocked immediately
        (`evaluation.blocked_now`). Returns 409 when a limit already exists for the
        product and period; update it instead.

        Args:
          product: Product to limit, as returned in `product` by the list operation.

          unlimited: `true`: explicitly no cap.

          period: `daily` is the current UTC day; `monthly` is the current UTC calendar month.

          reason: Why the limit is set or changed, kept for audit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["amount", "product"], ["product", "unlimited"])
    def create(
        self,
        *,
        amount: float | Omit = omit,
        product: str,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        return self._post(
            "/spend_limits",
            body=maybe_transform(
                {
                    "amount": amount,
                    "product": product,
                    "period": period,
                    "reason": reason,
                    "unlimited": unlimited,
                },
                spend_limit_create_params.SpendLimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendLimitResponse,
        )

    @overload
    def update(
        self,
        product: str,
        *,
        amount: float,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Replaces the value of the existing limit for the product and period.

        Send
        exactly one of `amount` and `unlimited: true`. The period's spend is checked at
        once: raising the limit above the spend lifts the period's block
        (`evaluation.released`), and lowering it below the spend blocks the product
        (`evaluation.blocked_now`). Returns 404 when no limit is set; create it instead.

        Args:
          amount: Limit in USD. `0` blocks at the first cent of spend.

          period: Limit period. Defaults to `daily`; send it explicitly.

          reason: Why the limit is set or changed, kept for audit.

          unlimited: Optional; only `false` is allowed together with `amount`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        product: str,
        *,
        unlimited: Literal[True],
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Replaces the value of the existing limit for the product and period.

        Send
        exactly one of `amount` and `unlimited: true`. The period's spend is checked at
        once: raising the limit above the spend lifts the period's block
        (`evaluation.released`), and lowering it below the spend blocks the product
        (`evaluation.blocked_now`). Returns 404 when no limit is set; create it instead.

        Args:
          unlimited: `true`: explicitly no cap.

          period: Limit period. Defaults to `daily`; send it explicitly.

          reason: Why the limit is set or changed, kept for audit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["amount"], ["unlimited"])
    def update(
        self,
        product: str,
        *,
        amount: float | Omit = omit,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        if not product:
            raise ValueError(f"Expected a non-empty value for `product` but received {product!r}")
        return self._patch(
            path_template("/spend_limits/{product}", product=product),
            body=maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                    "unlimited": unlimited,
                },
                spend_limit_update_params.SpendLimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period": period}, spend_limit_update_params.SpendLimitUpdateParams),
            ),
            cast_to=SpendLimitResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitListResponse:
        """
        Returns one entry per product and period you can set a limit on, with the limit,
        the spend so far in the period and whether the product is blocked. An entry
        without a limit is still listed (`limit: null`). When the spend cannot be read,
        the entry is returned with `spend_usd: null` and `spend_error` set. The list is
        not paginated.
        """
        return self._get(
            "/spend_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendLimitListResponse,
        )

    def delete(
        self,
        product: str,
        *,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Removes the limit for the product and period.

        For `inference`, which has no
        default limit, the product becomes unlimited for the period and the period's
        block is lifted (`evaluation.released`). The response carries `limit: null` and
        the `effective_limit_usd` that applies after the removal. Returns 404 when no
        limit is set.

        Args:
          period: Limit period. Defaults to `daily`; send it explicitly.

          reason: Why the limit is removed, kept for audit. At most 500 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product:
            raise ValueError(f"Expected a non-empty value for `product` but received {product!r}")
        return self._delete(
            path_template("/spend_limits/{product}", product=product),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "period": period,
                        "reason": reason,
                    },
                    spend_limit_delete_params.SpendLimitDeleteParams,
                ),
            ),
            cast_to=SpendLimitResponse,
        )


class AsyncSpendLimitsResource(AsyncAPIResource):
    """Daily and monthly spend limits per product.

    A limit applies to the organization of the authenticated user, or to the user's own account when they belong to no organization; every user of the organization sees and changes the same limits.

    - **Periods.** `daily` covers the current UTC day and `monthly` the current UTC calendar month. The two limits are independent: you can set either, both or neither.
    - **Blocking.** When spend in a period goes above the limit (strictly greater), the product is blocked until the period ends: 00:00 UTC the next day for `daily`, 00:00 UTC on the 1st of the next month for `monthly`. A block appears within about 2 minutes (daily) or 10 minutes (monthly) of the spend being recorded.
    - **Changes apply immediately.** Creating, updating or deleting a limit checks the period's spend in the same request: raising the limit above the spend, or removing it, lifts that period's block, and lowering it below the spend blocks the product at once. The `evaluation` object in the response says what happened.
    - **Supported products.** Today only `inference` supports spend limits. A blocked account gets HTTP 403 with the error title `Inference spend limit reached` (code `10039`) on new billable chat completions, Responses, Anthropic Messages and classification requests; requests already running finish normally. Take the list of products from the list operation.
    - **Limits set by Telnyx.** Telnyx support can also set a limit on your account. It is listed with `origin: operator` and you can update or delete it like your own.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSpendLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpendLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSpendLimitsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        amount: float,
        product: str,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Sets a limit for a product and period that has none.

        Send exactly one of
        `amount` and `unlimited: true`. The period's spend is checked at once: if it is
        already above the new limit, the product is blocked immediately
        (`evaluation.blocked_now`). Returns 409 when a limit already exists for the
        product and period; update it instead.

        Args:
          amount: Limit in USD. `0` blocks at the first cent of spend.

          product: Product to limit, as returned in `product` by the list operation.

          period: `daily` is the current UTC day; `monthly` is the current UTC calendar month.

          reason: Why the limit is set or changed, kept for audit.

          unlimited: Optional; only `false` is allowed together with `amount`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        product: str,
        unlimited: Literal[True],
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Sets a limit for a product and period that has none.

        Send exactly one of
        `amount` and `unlimited: true`. The period's spend is checked at once: if it is
        already above the new limit, the product is blocked immediately
        (`evaluation.blocked_now`). Returns 409 when a limit already exists for the
        product and period; update it instead.

        Args:
          product: Product to limit, as returned in `product` by the list operation.

          unlimited: `true`: explicitly no cap.

          period: `daily` is the current UTC day; `monthly` is the current UTC calendar month.

          reason: Why the limit is set or changed, kept for audit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["amount", "product"], ["product", "unlimited"])
    async def create(
        self,
        *,
        amount: float | Omit = omit,
        product: str,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        return await self._post(
            "/spend_limits",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "product": product,
                    "period": period,
                    "reason": reason,
                    "unlimited": unlimited,
                },
                spend_limit_create_params.SpendLimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendLimitResponse,
        )

    @overload
    async def update(
        self,
        product: str,
        *,
        amount: float,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Replaces the value of the existing limit for the product and period.

        Send
        exactly one of `amount` and `unlimited: true`. The period's spend is checked at
        once: raising the limit above the spend lifts the period's block
        (`evaluation.released`), and lowering it below the spend blocks the product
        (`evaluation.blocked_now`). Returns 404 when no limit is set; create it instead.

        Args:
          amount: Limit in USD. `0` blocks at the first cent of spend.

          period: Limit period. Defaults to `daily`; send it explicitly.

          reason: Why the limit is set or changed, kept for audit.

          unlimited: Optional; only `false` is allowed together with `amount`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        product: str,
        *,
        unlimited: Literal[True],
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Replaces the value of the existing limit for the product and period.

        Send
        exactly one of `amount` and `unlimited: true`. The period's spend is checked at
        once: raising the limit above the spend lifts the period's block
        (`evaluation.released`), and lowering it below the spend blocks the product
        (`evaluation.blocked_now`). Returns 404 when no limit is set; create it instead.

        Args:
          unlimited: `true`: explicitly no cap.

          period: Limit period. Defaults to `daily`; send it explicitly.

          reason: Why the limit is set or changed, kept for audit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["amount"], ["unlimited"])
    async def update(
        self,
        product: str,
        *,
        amount: float | Omit = omit,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        unlimited: Literal[False] | Literal[True] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        if not product:
            raise ValueError(f"Expected a non-empty value for `product` but received {product!r}")
        return await self._patch(
            path_template("/spend_limits/{product}", product=product),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "reason": reason,
                    "unlimited": unlimited,
                },
                spend_limit_update_params.SpendLimitUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"period": period}, spend_limit_update_params.SpendLimitUpdateParams),
            ),
            cast_to=SpendLimitResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitListResponse:
        """
        Returns one entry per product and period you can set a limit on, with the limit,
        the spend so far in the period and whether the product is blocked. An entry
        without a limit is still listed (`limit: null`). When the spend cannot be read,
        the entry is returned with `spend_usd: null` and `spend_error` set. The list is
        not paginated.
        """
        return await self._get(
            "/spend_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpendLimitListResponse,
        )

    async def delete(
        self,
        product: str,
        *,
        period: SpendLimitPeriod | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendLimitResponse:
        """Removes the limit for the product and period.

        For `inference`, which has no
        default limit, the product becomes unlimited for the period and the period's
        block is lifted (`evaluation.released`). The response carries `limit: null` and
        the `effective_limit_usd` that applies after the removal. Returns 404 when no
        limit is set.

        Args:
          period: Limit period. Defaults to `daily`; send it explicitly.

          reason: Why the limit is removed, kept for audit. At most 500 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product:
            raise ValueError(f"Expected a non-empty value for `product` but received {product!r}")
        return await self._delete(
            path_template("/spend_limits/{product}", product=product),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "period": period,
                        "reason": reason,
                    },
                    spend_limit_delete_params.SpendLimitDeleteParams,
                ),
            ),
            cast_to=SpendLimitResponse,
        )


class SpendLimitsResourceWithRawResponse:
    def __init__(self, spend_limits: SpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.create = to_raw_response_wrapper(
            spend_limits.create,
        )
        self.update = to_raw_response_wrapper(
            spend_limits.update,
        )
        self.list = to_raw_response_wrapper(
            spend_limits.list,
        )
        self.delete = to_raw_response_wrapper(
            spend_limits.delete,
        )


class AsyncSpendLimitsResourceWithRawResponse:
    def __init__(self, spend_limits: AsyncSpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.create = async_to_raw_response_wrapper(
            spend_limits.create,
        )
        self.update = async_to_raw_response_wrapper(
            spend_limits.update,
        )
        self.list = async_to_raw_response_wrapper(
            spend_limits.list,
        )
        self.delete = async_to_raw_response_wrapper(
            spend_limits.delete,
        )


class SpendLimitsResourceWithStreamingResponse:
    def __init__(self, spend_limits: SpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.create = to_streamed_response_wrapper(
            spend_limits.create,
        )
        self.update = to_streamed_response_wrapper(
            spend_limits.update,
        )
        self.list = to_streamed_response_wrapper(
            spend_limits.list,
        )
        self.delete = to_streamed_response_wrapper(
            spend_limits.delete,
        )


class AsyncSpendLimitsResourceWithStreamingResponse:
    def __init__(self, spend_limits: AsyncSpendLimitsResource) -> None:
        self._spend_limits = spend_limits

        self.create = async_to_streamed_response_wrapper(
            spend_limits.create,
        )
        self.update = async_to_streamed_response_wrapper(
            spend_limits.update,
        )
        self.list = async_to_streamed_response_wrapper(
            spend_limits.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            spend_limits.delete,
        )
