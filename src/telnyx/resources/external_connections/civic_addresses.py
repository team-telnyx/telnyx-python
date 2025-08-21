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
from ..._base_client import make_request_options
from ...types.external_connections import civic_address_list_params
from ...types.external_connections.civic_address_list_response import CivicAddressListResponse
from ...types.external_connections.civic_address_retrieve_response import CivicAddressRetrieveResponse

__all__ = ["CivicAddressesResource", "AsyncCivicAddressesResource"]


class CivicAddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CivicAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CivicAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CivicAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CivicAddressesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        address_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CivicAddressRetrieveResponse:
        """
        Return the details of an existing Civic Address with its Locations inside the
        'data' attribute of the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return self._get(
            f"/external_connections/{id}/civic_addresses/{address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CivicAddressRetrieveResponse,
        )

    def list(
        self,
        id: str,
        *,
        filter: civic_address_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CivicAddressListResponse:
        """
        Returns the civic addresses and locations from Microsoft Teams.

        Args:
          filter: Filter parameter for civic addresses (deepObject style). Supports filtering by
              country.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/external_connections/{id}/civic_addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, civic_address_list_params.CivicAddressListParams),
            ),
            cast_to=CivicAddressListResponse,
        )


class AsyncCivicAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCivicAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCivicAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCivicAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCivicAddressesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        address_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CivicAddressRetrieveResponse:
        """
        Return the details of an existing Civic Address with its Locations inside the
        'data' attribute of the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not address_id:
            raise ValueError(f"Expected a non-empty value for `address_id` but received {address_id!r}")
        return await self._get(
            f"/external_connections/{id}/civic_addresses/{address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CivicAddressRetrieveResponse,
        )

    async def list(
        self,
        id: str,
        *,
        filter: civic_address_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CivicAddressListResponse:
        """
        Returns the civic addresses and locations from Microsoft Teams.

        Args:
          filter: Filter parameter for civic addresses (deepObject style). Supports filtering by
              country.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/external_connections/{id}/civic_addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"filter": filter}, civic_address_list_params.CivicAddressListParams),
            ),
            cast_to=CivicAddressListResponse,
        )


class CivicAddressesResourceWithRawResponse:
    def __init__(self, civic_addresses: CivicAddressesResource) -> None:
        self._civic_addresses = civic_addresses

        self.retrieve = to_raw_response_wrapper(
            civic_addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            civic_addresses.list,
        )


class AsyncCivicAddressesResourceWithRawResponse:
    def __init__(self, civic_addresses: AsyncCivicAddressesResource) -> None:
        self._civic_addresses = civic_addresses

        self.retrieve = async_to_raw_response_wrapper(
            civic_addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            civic_addresses.list,
        )


class CivicAddressesResourceWithStreamingResponse:
    def __init__(self, civic_addresses: CivicAddressesResource) -> None:
        self._civic_addresses = civic_addresses

        self.retrieve = to_streamed_response_wrapper(
            civic_addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            civic_addresses.list,
        )


class AsyncCivicAddressesResourceWithStreamingResponse:
    def __init__(self, civic_addresses: AsyncCivicAddressesResource) -> None:
        self._civic_addresses = civic_addresses

        self.retrieve = async_to_streamed_response_wrapper(
            civic_addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            civic_addresses.list,
        )
