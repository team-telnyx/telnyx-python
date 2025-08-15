# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ...types.actions import purchase_create_params
from ...types.actions.purchase_create_response import PurchaseCreateResponse

__all__ = ["PurchaseResource", "AsyncPurchaseResource"]


class PurchaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurchaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PurchaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PurchaseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        product: str | NotGiven = NOT_GIVEN,
        sim_card_group_id: str | NotGiven = NOT_GIVEN,
        status: Literal["enabled", "disabled", "standby"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        whitelabel_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseCreateResponse:
        """
        Purchases and registers the specified amount of eSIMs to the current user's
        account.<br/><br/> If <code>sim_card_group_id</code> is provided, the eSIMs will
        be associated with that group. Otherwise, the default group for the current user
        will be used.<br/><br/>

        Args:
          amount: The amount of eSIMs to be purchased.

          product: Type of product to be purchased, specify "whitelabel" to use a custom SPN

          sim_card_group_id: The group SIMCardGroup identification. This attribute can be <code>null</code>
              when it's present in an associated resource.

          status: Status on which the SIM cards will be set after being successfully registered.

          tags: Searchable tags associated with the SIM cards

          whitelabel_name: Service Provider Name (SPN) for the Whitelabel eSIM product. It will be
              displayed as the mobile service name by operating systems of smartphones. This
              parameter must only contain letters, numbers and whitespaces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/actions/purchase/esims",
            body=maybe_transform(
                {
                    "amount": amount,
                    "product": product,
                    "sim_card_group_id": sim_card_group_id,
                    "status": status,
                    "tags": tags,
                    "whitelabel_name": whitelabel_name,
                },
                purchase_create_params.PurchaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreateResponse,
        )


class AsyncPurchaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurchaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPurchaseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        product: str | NotGiven = NOT_GIVEN,
        sim_card_group_id: str | NotGiven = NOT_GIVEN,
        status: Literal["enabled", "disabled", "standby"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        whitelabel_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseCreateResponse:
        """
        Purchases and registers the specified amount of eSIMs to the current user's
        account.<br/><br/> If <code>sim_card_group_id</code> is provided, the eSIMs will
        be associated with that group. Otherwise, the default group for the current user
        will be used.<br/><br/>

        Args:
          amount: The amount of eSIMs to be purchased.

          product: Type of product to be purchased, specify "whitelabel" to use a custom SPN

          sim_card_group_id: The group SIMCardGroup identification. This attribute can be <code>null</code>
              when it's present in an associated resource.

          status: Status on which the SIM cards will be set after being successfully registered.

          tags: Searchable tags associated with the SIM cards

          whitelabel_name: Service Provider Name (SPN) for the Whitelabel eSIM product. It will be
              displayed as the mobile service name by operating systems of smartphones. This
              parameter must only contain letters, numbers and whitespaces.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/actions/purchase/esims",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "product": product,
                    "sim_card_group_id": sim_card_group_id,
                    "status": status,
                    "tags": tags,
                    "whitelabel_name": whitelabel_name,
                },
                purchase_create_params.PurchaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseCreateResponse,
        )


class PurchaseResourceWithRawResponse:
    def __init__(self, purchase: PurchaseResource) -> None:
        self._purchase = purchase

        self.create = to_raw_response_wrapper(
            purchase.create,
        )


class AsyncPurchaseResourceWithRawResponse:
    def __init__(self, purchase: AsyncPurchaseResource) -> None:
        self._purchase = purchase

        self.create = async_to_raw_response_wrapper(
            purchase.create,
        )


class PurchaseResourceWithStreamingResponse:
    def __init__(self, purchase: PurchaseResource) -> None:
        self._purchase = purchase

        self.create = to_streamed_response_wrapper(
            purchase.create,
        )


class AsyncPurchaseResourceWithStreamingResponse:
    def __init__(self, purchase: AsyncPurchaseResource) -> None:
        self._purchase = purchase

        self.create = async_to_streamed_response_wrapper(
            purchase.create,
        )
