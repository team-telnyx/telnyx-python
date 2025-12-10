# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.number_10dlc.brand import (
    external_vetting_external_vetting_params,
    external_vetting_update_external_vetting_params,
)
from ....types.number_10dlc.brand.external_vetting_external_vetting_response import (
    ExternalVettingExternalVettingResponse,
)
from ....types.number_10dlc.brand.external_vetting_update_external_vetting_response import (
    ExternalVettingUpdateExternalVettingResponse,
)
from ....types.number_10dlc.brand.external_vetting_retrieve_external_vetting_response import (
    ExternalVettingRetrieveExternalVettingResponse,
)

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

    def external_vetting(
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVettingExternalVettingResponse:
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
            f"/10dlc/brand/{brand_id}/externalVetting",
            body=maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_class": vetting_class,
                },
                external_vetting_external_vetting_params.ExternalVettingExternalVettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingExternalVettingResponse,
        )

    def retrieve_external_vetting(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVettingRetrieveExternalVettingResponse:
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
            f"/10dlc/brand/{brand_id}/externalVetting",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingRetrieveExternalVettingResponse,
        )

    def update_external_vetting(
        self,
        brand_id: str,
        *,
        evp_id: str,
        vetting_id: str,
        vetting_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVettingUpdateExternalVettingResponse:
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
            f"/10dlc/brand/{brand_id}/externalVetting",
            body=maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_id": vetting_id,
                    "vetting_token": vetting_token,
                },
                external_vetting_update_external_vetting_params.ExternalVettingUpdateExternalVettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingUpdateExternalVettingResponse,
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

    async def external_vetting(
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVettingExternalVettingResponse:
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
            f"/10dlc/brand/{brand_id}/externalVetting",
            body=await async_maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_class": vetting_class,
                },
                external_vetting_external_vetting_params.ExternalVettingExternalVettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingExternalVettingResponse,
        )

    async def retrieve_external_vetting(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVettingRetrieveExternalVettingResponse:
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
            f"/10dlc/brand/{brand_id}/externalVetting",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingRetrieveExternalVettingResponse,
        )

    async def update_external_vetting(
        self,
        brand_id: str,
        *,
        evp_id: str,
        vetting_id: str,
        vetting_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExternalVettingUpdateExternalVettingResponse:
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
            f"/10dlc/brand/{brand_id}/externalVetting",
            body=await async_maybe_transform(
                {
                    "evp_id": evp_id,
                    "vetting_id": vetting_id,
                    "vetting_token": vetting_token,
                },
                external_vetting_update_external_vetting_params.ExternalVettingUpdateExternalVettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalVettingUpdateExternalVettingResponse,
        )


class ExternalVettingResourceWithRawResponse:
    def __init__(self, external_vetting: ExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.external_vetting = to_raw_response_wrapper(
            external_vetting.external_vetting,
        )
        self.retrieve_external_vetting = to_raw_response_wrapper(
            external_vetting.retrieve_external_vetting,
        )
        self.update_external_vetting = to_raw_response_wrapper(
            external_vetting.update_external_vetting,
        )


class AsyncExternalVettingResourceWithRawResponse:
    def __init__(self, external_vetting: AsyncExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.external_vetting = async_to_raw_response_wrapper(
            external_vetting.external_vetting,
        )
        self.retrieve_external_vetting = async_to_raw_response_wrapper(
            external_vetting.retrieve_external_vetting,
        )
        self.update_external_vetting = async_to_raw_response_wrapper(
            external_vetting.update_external_vetting,
        )


class ExternalVettingResourceWithStreamingResponse:
    def __init__(self, external_vetting: ExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.external_vetting = to_streamed_response_wrapper(
            external_vetting.external_vetting,
        )
        self.retrieve_external_vetting = to_streamed_response_wrapper(
            external_vetting.retrieve_external_vetting,
        )
        self.update_external_vetting = to_streamed_response_wrapper(
            external_vetting.update_external_vetting,
        )


class AsyncExternalVettingResourceWithStreamingResponse:
    def __init__(self, external_vetting: AsyncExternalVettingResource) -> None:
        self._external_vetting = external_vetting

        self.external_vetting = async_to_streamed_response_wrapper(
            external_vetting.external_vetting,
        )
        self.retrieve_external_vetting = async_to_streamed_response_wrapper(
            external_vetting.retrieve_external_vetting,
        )
        self.update_external_vetting = async_to_streamed_response_wrapper(
            external_vetting.update_external_vetting,
        )
