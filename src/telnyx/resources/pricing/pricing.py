# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PricingResource", "AsyncPricingResource"]


class PricingResource(SyncAPIResource):
    @cached_property
    def products(self) -> ProductsResource:
        """Public pricing operations"""
        return ProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PricingResourceWithStreamingResponse(self)


class AsyncPricingResource(AsyncAPIResource):
    @cached_property
    def products(self) -> AsyncProductsResource:
        """Public pricing operations"""
        return AsyncProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPricingResourceWithStreamingResponse(self)


class PricingResourceWithRawResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        """Public pricing operations"""
        return ProductsResourceWithRawResponse(self._pricing.products)


class AsyncPricingResourceWithRawResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        """Public pricing operations"""
        return AsyncProductsResourceWithRawResponse(self._pricing.products)


class PricingResourceWithStreamingResponse:
    def __init__(self, pricing: PricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        """Public pricing operations"""
        return ProductsResourceWithStreamingResponse(self._pricing.products)


class AsyncPricingResourceWithStreamingResponse:
    def __init__(self, pricing: AsyncPricingResource) -> None:
        self._pricing = pricing

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        """Public pricing operations"""
        return AsyncProductsResourceWithStreamingResponse(self._pricing.products)
