# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.brand import external_vetting_order_params, external_vetting_import_params
from ..._base_client import make_request_options
from ...types.brand.external_vetting_import_response import ExternalVettingImportResponse

__all__ = ["ExternalVettingResource", "AsyncExternalVettingResource"]


class ExternalVettingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalVettingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ExternalVettingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalVettingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ExternalVettingResourceWithStreamingResponse(self)

    def list(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get list of valid external vetting record for a given brand

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._get(
            f"/brand/{brand_id}/externalVetting",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def import_(
        self,
        brand_id: str,
        *,
        evp_id: str,
        vetting_id: str,
        vetting_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalVettingImportResponse:
        """
        This operation can be used to import an external vetting record from a
        TCR-approved vetting provider. If the vetting provider confirms validity of the
        record, it will be saved with the brand and will be considered for future
        campaign qualification.

        Args:
          evp_id: External vetting provider ID for the brand.

          vetting_id: Unique ID that identifies a vetting transaction performed by a vetting provider.
              This ID is provided by the vetting provider at time of vetting.

          vetting_token: Required by some providers for vetting record confirmation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._put(
            f"/brand/{brand_id}/externalVetting",
            body=maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_id": vetting_id,
                    "vetting_token": vetting_token,
                },
                external_vetting_import_params.ExternalVettingImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingImportResponse,
        )

    def order(
        self,
        brand_id: str,
        *,
        evp_id: str,
        vetting_class: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Order new external vetting for a brand

        Args:
          evp_id: External vetting provider ID for the brand.

          vetting_class: Identifies the vetting classification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._post(
            f"/brand/{brand_id}/externalVetting",
            body=maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_class": vetting_class,
                },
                external_vetting_order_params.ExternalVettingOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncExternalVettingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalVettingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalVettingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalVettingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncExternalVettingResourceWithStreamingResponse(self)

    async def list(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get list of valid external vetting record for a given brand

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._get(
            f"/brand/{brand_id}/externalVetting",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def import_(
        self,
        brand_id: str,
        *,
        evp_id: str,
        vetting_id: str,
        vetting_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalVettingImportResponse:
        """
        This operation can be used to import an external vetting record from a
        TCR-approved vetting provider. If the vetting provider confirms validity of the
        record, it will be saved with the brand and will be considered for future
        campaign qualification.

        Args:
          evp_id: External vetting provider ID for the brand.

          vetting_id: Unique ID that identifies a vetting transaction performed by a vetting provider.
              This ID is provided by the vetting provider at time of vetting.

          vetting_token: Required by some providers for vetting record confirmation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._put(
            f"/brand/{brand_id}/externalVetting",
            body=await async_maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_id": vetting_id,
                    "vetting_token": vetting_token,
                },
                external_vetting_import_params.ExternalVettingImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingImportResponse,
        )

    async def order(
        self,
        brand_id: str,
        *,
        evp_id: str,
        vetting_class: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Order new external vetting for a brand

        Args:
          evp_id: External vetting provider ID for the brand.

          vetting_class: Identifies the vetting classification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._post(
            f"/brand/{brand_id}/externalVetting",
            body=await async_maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_class": vetting_class,
                },
                external_vetting_order_params.ExternalVettingOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ExternalVettingResourceWithRawResponse:
    def __init__(self, external_vetting: ExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.list = to_raw_response_wrapper(
            external_vetting.list,
        )
        self.import_ = to_raw_response_wrapper(
            external_vetting.import_,
        )
        self.order = to_raw_response_wrapper(
            external_vetting.order,
        )


class AsyncExternalVettingResourceWithRawResponse:
    def __init__(self, external_vetting: AsyncExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.list = async_to_raw_response_wrapper(
            external_vetting.list,
        )
        self.import_ = async_to_raw_response_wrapper(
            external_vetting.import_,
        )
        self.order = async_to_raw_response_wrapper(
            external_vetting.order,
        )


class ExternalVettingResourceWithStreamingResponse:
    def __init__(self, external_vetting: ExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.list = to_streamed_response_wrapper(
            external_vetting.list,
        )
        self.import_ = to_streamed_response_wrapper(
            external_vetting.import_,
        )
        self.order = to_streamed_response_wrapper(
            external_vetting.order,
        )


class AsyncExternalVettingResourceWithStreamingResponse:
    def __init__(self, external_vetting: AsyncExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.list = async_to_streamed_response_wrapper(
            external_vetting.list,
        )
        self.import_ = async_to_streamed_response_wrapper(
            external_vetting.import_,
        )
        self.order = async_to_streamed_response_wrapper(
            external_vetting.order,
        )
