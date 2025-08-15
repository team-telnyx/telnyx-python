# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .user_bundles import (
    UserBundlesResource,
    AsyncUserBundlesResource,
    UserBundlesResourceWithRawResponse,
    AsyncUserBundlesResourceWithRawResponse,
    UserBundlesResourceWithStreamingResponse,
    AsyncUserBundlesResourceWithStreamingResponse,
)
from .billing_bundles import (
    BillingBundlesResource,
    AsyncBillingBundlesResource,
    BillingBundlesResourceWithRawResponse,
    AsyncBillingBundlesResourceWithRawResponse,
    BillingBundlesResourceWithStreamingResponse,
    AsyncBillingBundlesResourceWithStreamingResponse,
)

__all__ = ["BundlePricingResource", "AsyncBundlePricingResource"]


class BundlePricingResource(SyncAPIResource):
    @cached_property
    def billing_bundles(self) -> BillingBundlesResource:
        return BillingBundlesResource(self._client)

    @cached_property
    def user_bundles(self) -> UserBundlesResource:
        return UserBundlesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BundlePricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BundlePricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BundlePricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BundlePricingResourceWithStreamingResponse(self)


class AsyncBundlePricingResource(AsyncAPIResource):
    @cached_property
    def billing_bundles(self) -> AsyncBillingBundlesResource:
        return AsyncBillingBundlesResource(self._client)

    @cached_property
    def user_bundles(self) -> AsyncUserBundlesResource:
        return AsyncUserBundlesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBundlePricingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBundlePricingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBundlePricingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBundlePricingResourceWithStreamingResponse(self)


class BundlePricingResourceWithRawResponse:
    def __init__(self, bundle_pricing: BundlePricingResource) -> None:
        self._bundle_pricing = bundle_pricing

    @cached_property
    def billing_bundles(self) -> BillingBundlesResourceWithRawResponse:
        return BillingBundlesResourceWithRawResponse(self._bundle_pricing.billing_bundles)

    @cached_property
    def user_bundles(self) -> UserBundlesResourceWithRawResponse:
        return UserBundlesResourceWithRawResponse(self._bundle_pricing.user_bundles)


class AsyncBundlePricingResourceWithRawResponse:
    def __init__(self, bundle_pricing: AsyncBundlePricingResource) -> None:
        self._bundle_pricing = bundle_pricing

    @cached_property
    def billing_bundles(self) -> AsyncBillingBundlesResourceWithRawResponse:
        return AsyncBillingBundlesResourceWithRawResponse(self._bundle_pricing.billing_bundles)

    @cached_property
    def user_bundles(self) -> AsyncUserBundlesResourceWithRawResponse:
        return AsyncUserBundlesResourceWithRawResponse(self._bundle_pricing.user_bundles)


class BundlePricingResourceWithStreamingResponse:
    def __init__(self, bundle_pricing: BundlePricingResource) -> None:
        self._bundle_pricing = bundle_pricing

    @cached_property
    def billing_bundles(self) -> BillingBundlesResourceWithStreamingResponse:
        return BillingBundlesResourceWithStreamingResponse(self._bundle_pricing.billing_bundles)

    @cached_property
    def user_bundles(self) -> UserBundlesResourceWithStreamingResponse:
        return UserBundlesResourceWithStreamingResponse(self._bundle_pricing.user_bundles)


class AsyncBundlePricingResourceWithStreamingResponse:
    def __init__(self, bundle_pricing: AsyncBundlePricingResource) -> None:
        self._bundle_pricing = bundle_pricing

    @cached_property
    def billing_bundles(self) -> AsyncBillingBundlesResourceWithStreamingResponse:
        return AsyncBillingBundlesResourceWithStreamingResponse(self._bundle_pricing.billing_bundles)

    @cached_property
    def user_bundles(self) -> AsyncUserBundlesResourceWithStreamingResponse:
        return AsyncUserBundlesResourceWithStreamingResponse(self._bundle_pricing.user_bundles)
