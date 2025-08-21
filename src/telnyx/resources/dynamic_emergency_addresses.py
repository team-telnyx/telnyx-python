# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import dynamic_emergency_address_list_params, dynamic_emergency_address_create_params
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
from ..types.dynamic_emergency_address_list_response import DynamicEmergencyAddressListResponse
from ..types.dynamic_emergency_address_create_response import DynamicEmergencyAddressCreateResponse
from ..types.dynamic_emergency_address_delete_response import DynamicEmergencyAddressDeleteResponse
from ..types.dynamic_emergency_address_retrieve_response import DynamicEmergencyAddressRetrieveResponse

__all__ = ["DynamicEmergencyAddressesResource", "AsyncDynamicEmergencyAddressesResource"]


class DynamicEmergencyAddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DynamicEmergencyAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DynamicEmergencyAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DynamicEmergencyAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DynamicEmergencyAddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        administrative_area: str,
        country_code: Literal["US", "CA", "PR"],
        house_number: str,
        locality: str,
        postal_code: str,
        street_name: str,
        extended_address: str | NotGiven = NOT_GIVEN,
        house_suffix: str | NotGiven = NOT_GIVEN,
        street_post_directional: str | NotGiven = NOT_GIVEN,
        street_pre_directional: str | NotGiven = NOT_GIVEN,
        street_suffix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressCreateResponse:
        """
        Creates a dynamic emergency address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/dynamic_emergency_addresses",
            body=maybe_transform(
                {
                    "administrative_area": administrative_area,
                    "country_code": country_code,
                    "house_number": house_number,
                    "locality": locality,
                    "postal_code": postal_code,
                    "street_name": street_name,
                    "extended_address": extended_address,
                    "house_suffix": house_suffix,
                    "street_post_directional": street_post_directional,
                    "street_pre_directional": street_pre_directional,
                    "street_suffix": street_suffix,
                },
                dynamic_emergency_address_create_params.DynamicEmergencyAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyAddressCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressRetrieveResponse:
        """
        Returns the dynamic emergency address based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/dynamic_emergency_addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyAddressRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: dynamic_emergency_address_list_params.Filter | NotGiven = NOT_GIVEN,
        page: dynamic_emergency_address_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressListResponse:
        """
        Returns the dynamic emergency addresses according to filters

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[country_code]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/dynamic_emergency_addresses",
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
                    dynamic_emergency_address_list_params.DynamicEmergencyAddressListParams,
                ),
            ),
            cast_to=DynamicEmergencyAddressListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressDeleteResponse:
        """
        Deletes the dynamic emergency address based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/dynamic_emergency_addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyAddressDeleteResponse,
        )


class AsyncDynamicEmergencyAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDynamicEmergencyAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDynamicEmergencyAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDynamicEmergencyAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDynamicEmergencyAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        administrative_area: str,
        country_code: Literal["US", "CA", "PR"],
        house_number: str,
        locality: str,
        postal_code: str,
        street_name: str,
        extended_address: str | NotGiven = NOT_GIVEN,
        house_suffix: str | NotGiven = NOT_GIVEN,
        street_post_directional: str | NotGiven = NOT_GIVEN,
        street_pre_directional: str | NotGiven = NOT_GIVEN,
        street_suffix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressCreateResponse:
        """
        Creates a dynamic emergency address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/dynamic_emergency_addresses",
            body=await async_maybe_transform(
                {
                    "administrative_area": administrative_area,
                    "country_code": country_code,
                    "house_number": house_number,
                    "locality": locality,
                    "postal_code": postal_code,
                    "street_name": street_name,
                    "extended_address": extended_address,
                    "house_suffix": house_suffix,
                    "street_post_directional": street_post_directional,
                    "street_pre_directional": street_pre_directional,
                    "street_suffix": street_suffix,
                },
                dynamic_emergency_address_create_params.DynamicEmergencyAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyAddressCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressRetrieveResponse:
        """
        Returns the dynamic emergency address based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/dynamic_emergency_addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyAddressRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: dynamic_emergency_address_list_params.Filter | NotGiven = NOT_GIVEN,
        page: dynamic_emergency_address_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressListResponse:
        """
        Returns the dynamic emergency addresses according to filters

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[status],
              filter[country_code]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/dynamic_emergency_addresses",
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
                    dynamic_emergency_address_list_params.DynamicEmergencyAddressListParams,
                ),
            ),
            cast_to=DynamicEmergencyAddressListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DynamicEmergencyAddressDeleteResponse:
        """
        Deletes the dynamic emergency address based on the ID provided

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/dynamic_emergency_addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicEmergencyAddressDeleteResponse,
        )


class DynamicEmergencyAddressesResourceWithRawResponse:
    def __init__(self, dynamic_emergency_addresses: DynamicEmergencyAddressesResource) -> None:
        self._dynamic_emergency_addresses = dynamic_emergency_addresses

        self.create = to_raw_response_wrapper(
            dynamic_emergency_addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dynamic_emergency_addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            dynamic_emergency_addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            dynamic_emergency_addresses.delete,
        )


class AsyncDynamicEmergencyAddressesResourceWithRawResponse:
    def __init__(self, dynamic_emergency_addresses: AsyncDynamicEmergencyAddressesResource) -> None:
        self._dynamic_emergency_addresses = dynamic_emergency_addresses

        self.create = async_to_raw_response_wrapper(
            dynamic_emergency_addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dynamic_emergency_addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            dynamic_emergency_addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dynamic_emergency_addresses.delete,
        )


class DynamicEmergencyAddressesResourceWithStreamingResponse:
    def __init__(self, dynamic_emergency_addresses: DynamicEmergencyAddressesResource) -> None:
        self._dynamic_emergency_addresses = dynamic_emergency_addresses

        self.create = to_streamed_response_wrapper(
            dynamic_emergency_addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dynamic_emergency_addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            dynamic_emergency_addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            dynamic_emergency_addresses.delete,
        )


class AsyncDynamicEmergencyAddressesResourceWithStreamingResponse:
    def __init__(self, dynamic_emergency_addresses: AsyncDynamicEmergencyAddressesResource) -> None:
        self._dynamic_emergency_addresses = dynamic_emergency_addresses

        self.create = async_to_streamed_response_wrapper(
            dynamic_emergency_addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dynamic_emergency_addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            dynamic_emergency_addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dynamic_emergency_addresses.delete,
        )
