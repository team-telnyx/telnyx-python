# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.bundle_pricing import billing_bundle_list_params
from ...types.bundle_pricing.billing_bundle_summary import BillingBundleSummary
from ...types.bundle_pricing.billing_bundle_retrieve_response import BillingBundleRetrieveResponse

__all__ = ["BillingBundlesResource", "AsyncBillingBundlesResource"]


class BillingBundlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingBundlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BillingBundlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingBundlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BillingBundlesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingBundleRetrieveResponse:
        """
        Get a single bundle by ID.

        Args:
          bundle_id: Billing bundle's ID, this is used to identify the billing bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bundle_id:
            raise ValueError(f"Expected a non-empty value for `bundle_id` but received {bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get(
            f"/bundle_pricing/billing_bundles/{bundle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingBundleRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: billing_bundle_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[BillingBundleSummary]:
        """
        Get all allowed bundles.

        Args:
          filter: Consolidated filter parameter (deepObject style). Supports filtering by
              country_iso and resource. Examples: filter[country_iso]=US or
              filter[resource]=+15617819942

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get_api_list(
            "/bundle_pricing/billing_bundles",
            page=SyncDefaultFlatPagination[BillingBundleSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    billing_bundle_list_params.BillingBundleListParams,
                ),
            ),
            model=BillingBundleSummary,
        )


class AsyncBillingBundlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingBundlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingBundlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingBundlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBillingBundlesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingBundleRetrieveResponse:
        """
        Get a single bundle by ID.

        Args:
          bundle_id: Billing bundle's ID, this is used to identify the billing bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bundle_id:
            raise ValueError(f"Expected a non-empty value for `bundle_id` but received {bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._get(
            f"/bundle_pricing/billing_bundles/{bundle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingBundleRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: billing_bundle_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BillingBundleSummary, AsyncDefaultFlatPagination[BillingBundleSummary]]:
        """
        Get all allowed bundles.

        Args:
          filter: Consolidated filter parameter (deepObject style). Supports filtering by
              country_iso and resource. Examples: filter[country_iso]=US or
              filter[resource]=+15617819942

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get_api_list(
            "/bundle_pricing/billing_bundles",
            page=AsyncDefaultFlatPagination[BillingBundleSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    billing_bundle_list_params.BillingBundleListParams,
                ),
            ),
            model=BillingBundleSummary,
        )


class BillingBundlesResourceWithRawResponse:
    def __init__(self, billing_bundles: BillingBundlesResource) -> None:
        self._billing_bundles = billing_bundles

        self.retrieve = to_raw_response_wrapper(
            billing_bundles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            billing_bundles.list,
        )


class AsyncBillingBundlesResourceWithRawResponse:
    def __init__(self, billing_bundles: AsyncBillingBundlesResource) -> None:
        self._billing_bundles = billing_bundles

        self.retrieve = async_to_raw_response_wrapper(
            billing_bundles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            billing_bundles.list,
        )


class BillingBundlesResourceWithStreamingResponse:
    def __init__(self, billing_bundles: BillingBundlesResource) -> None:
        self._billing_bundles = billing_bundles

        self.retrieve = to_streamed_response_wrapper(
            billing_bundles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            billing_bundles.list,
        )


class AsyncBillingBundlesResourceWithStreamingResponse:
    def __init__(self, billing_bundles: AsyncBillingBundlesResource) -> None:
        self._billing_bundles = billing_bundles

        self.retrieve = async_to_streamed_response_wrapper(
            billing_bundles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            billing_bundles.list,
        )
