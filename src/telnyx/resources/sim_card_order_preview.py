# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import sim_card_order_preview_preview_params
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
from ..types.sim_card_order_preview_preview_response import SimCardOrderPreviewPreviewResponse

__all__ = ["SimCardOrderPreviewResource", "AsyncSimCardOrderPreviewResource"]


class SimCardOrderPreviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimCardOrderPreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SimCardOrderPreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimCardOrderPreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SimCardOrderPreviewResourceWithStreamingResponse(self)

    def preview(
        self,
        *,
        address_id: str,
        quantity: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardOrderPreviewPreviewResponse:
        """
        Preview SIM card order purchases.

        Args:
          address_id: Uniquely identifies the address for the order.

          quantity: The amount of SIM cards that the user would like to purchase in the SIM card
              order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sim_card_order_preview",
            body=maybe_transform(
                {
                    "address_id": address_id,
                    "quantity": quantity,
                },
                sim_card_order_preview_preview_params.SimCardOrderPreviewPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardOrderPreviewPreviewResponse,
        )


class AsyncSimCardOrderPreviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimCardOrderPreviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimCardOrderPreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimCardOrderPreviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSimCardOrderPreviewResourceWithStreamingResponse(self)

    async def preview(
        self,
        *,
        address_id: str,
        quantity: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimCardOrderPreviewPreviewResponse:
        """
        Preview SIM card order purchases.

        Args:
          address_id: Uniquely identifies the address for the order.

          quantity: The amount of SIM cards that the user would like to purchase in the SIM card
              order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sim_card_order_preview",
            body=await async_maybe_transform(
                {
                    "address_id": address_id,
                    "quantity": quantity,
                },
                sim_card_order_preview_preview_params.SimCardOrderPreviewPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimCardOrderPreviewPreviewResponse,
        )


class SimCardOrderPreviewResourceWithRawResponse:
    def __init__(self, sim_card_order_preview: SimCardOrderPreviewResource) -> None:
        self._sim_card_order_preview = sim_card_order_preview

        self.preview = to_raw_response_wrapper(
            sim_card_order_preview.preview,
        )


class AsyncSimCardOrderPreviewResourceWithRawResponse:
    def __init__(self, sim_card_order_preview: AsyncSimCardOrderPreviewResource) -> None:
        self._sim_card_order_preview = sim_card_order_preview

        self.preview = async_to_raw_response_wrapper(
            sim_card_order_preview.preview,
        )


class SimCardOrderPreviewResourceWithStreamingResponse:
    def __init__(self, sim_card_order_preview: SimCardOrderPreviewResource) -> None:
        self._sim_card_order_preview = sim_card_order_preview

        self.preview = to_streamed_response_wrapper(
            sim_card_order_preview.preview,
        )


class AsyncSimCardOrderPreviewResourceWithStreamingResponse:
    def __init__(self, sim_card_order_preview: AsyncSimCardOrderPreviewResource) -> None:
        self._sim_card_order_preview = sim_card_order_preview

        self.preview = async_to_streamed_response_wrapper(
            sim_card_order_preview.preview,
        )
