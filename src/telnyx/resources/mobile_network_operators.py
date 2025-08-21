# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import mobile_network_operator_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.mobile_network_operator_list_response import MobileNetworkOperatorListResponse

__all__ = ["MobileNetworkOperatorsResource", "AsyncMobileNetworkOperatorsResource"]


class MobileNetworkOperatorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MobileNetworkOperatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MobileNetworkOperatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MobileNetworkOperatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MobileNetworkOperatorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: mobile_network_operator_list_params.Filter | NotGiven = NOT_GIVEN,
        page: mobile_network_operator_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MobileNetworkOperatorListResponse:
        """
        Telnyx has a set of GSM mobile operators partners that are available through our
        mobile network roaming. This resource is entirely managed by Telnyx and may
        change over time. That means that this resource won't allow any write operations
        for it. Still, it's available so it can be used as a support resource that can
        be related to other resources or become a configuration option.

        Args:
          filter: Consolidated filter parameter for mobile network operators (deepObject style).
              Originally: filter[name][starts_with], filter[name][contains],
              filter[name][ends_with], filter[country_code], filter[mcc], filter[mnc],
              filter[tadig], filter[network_preferences_enabled]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/mobile_network_operators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    mobile_network_operator_list_params.MobileNetworkOperatorListParams,
                ),
            ),
            cast_to=MobileNetworkOperatorListResponse,
        )


class AsyncMobileNetworkOperatorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMobileNetworkOperatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMobileNetworkOperatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMobileNetworkOperatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMobileNetworkOperatorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: mobile_network_operator_list_params.Filter | NotGiven = NOT_GIVEN,
        page: mobile_network_operator_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MobileNetworkOperatorListResponse:
        """
        Telnyx has a set of GSM mobile operators partners that are available through our
        mobile network roaming. This resource is entirely managed by Telnyx and may
        change over time. That means that this resource won't allow any write operations
        for it. Still, it's available so it can be used as a support resource that can
        be related to other resources or become a configuration option.

        Args:
          filter: Consolidated filter parameter for mobile network operators (deepObject style).
              Originally: filter[name][starts_with], filter[name][contains],
              filter[name][ends_with], filter[country_code], filter[mcc], filter[mnc],
              filter[tadig], filter[network_preferences_enabled]

          page: Consolidated pagination parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/mobile_network_operators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    mobile_network_operator_list_params.MobileNetworkOperatorListParams,
                ),
            ),
            cast_to=MobileNetworkOperatorListResponse,
        )


class MobileNetworkOperatorsResourceWithRawResponse:
    def __init__(self, mobile_network_operators: MobileNetworkOperatorsResource) -> None:
        self._mobile_network_operators = mobile_network_operators

        self.list = to_raw_response_wrapper(
            mobile_network_operators.list,
        )


class AsyncMobileNetworkOperatorsResourceWithRawResponse:
    def __init__(self, mobile_network_operators: AsyncMobileNetworkOperatorsResource) -> None:
        self._mobile_network_operators = mobile_network_operators

        self.list = async_to_raw_response_wrapper(
            mobile_network_operators.list,
        )


class MobileNetworkOperatorsResourceWithStreamingResponse:
    def __init__(self, mobile_network_operators: MobileNetworkOperatorsResource) -> None:
        self._mobile_network_operators = mobile_network_operators

        self.list = to_streamed_response_wrapper(
            mobile_network_operators.list,
        )


class AsyncMobileNetworkOperatorsResourceWithStreamingResponse:
    def __init__(self, mobile_network_operators: AsyncMobileNetworkOperatorsResource) -> None:
        self._mobile_network_operators = mobile_network_operators

        self.list = async_to_streamed_response_wrapper(
            mobile_network_operators.list,
        )
