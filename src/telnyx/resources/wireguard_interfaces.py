# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import wireguard_interface_list_params, wireguard_interface_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.wireguard_interface_list_response import WireguardInterfaceListResponse
from ..types.wireguard_interface_create_response import WireguardInterfaceCreateResponse
from ..types.wireguard_interface_delete_response import WireguardInterfaceDeleteResponse
from ..types.wireguard_interface_retrieve_response import WireguardInterfaceRetrieveResponse

__all__ = ["WireguardInterfacesResource", "AsyncWireguardInterfacesResource"]


class WireguardInterfacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireguardInterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WireguardInterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireguardInterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WireguardInterfacesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        region_code: str,
        enable_sip_trunking: bool | Omit = omit,
        name: str | Omit = omit,
        network_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WireguardInterfaceCreateResponse:
        """Create a new WireGuard Interface.

        Current limitation of 10 interfaces per user
        can be created.

        Args:
          region_code: The region the interface should be deployed to.

          enable_sip_trunking: Enable SIP traffic forwarding over VPN interface.

          name: A user specified name for the interface.

          network_id: The id of the network associated with the interface.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wireguard_interfaces",
            body=maybe_transform(
                {
                    "region_code": region_code,
                    "enable_sip_trunking": enable_sip_trunking,
                    "name": name,
                    "network_id": network_id,
                },
                wireguard_interface_create_params.WireguardInterfaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardInterfaceCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WireguardInterfaceRetrieveResponse:
        """
        Retrieve a WireGuard Interfaces.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/wireguard_interfaces/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardInterfaceRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: wireguard_interface_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[WireguardInterfaceListResponse]:
        """
        List all WireGuard Interfaces.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/wireguard_interfaces",
            page=SyncDefaultFlatPagination[WireguardInterfaceListResponse],
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
                    wireguard_interface_list_params.WireguardInterfaceListParams,
                ),
            ),
            model=WireguardInterfaceListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WireguardInterfaceDeleteResponse:
        """
        Delete a WireGuard Interface.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/wireguard_interfaces/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardInterfaceDeleteResponse,
        )


class AsyncWireguardInterfacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireguardInterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireguardInterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireguardInterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWireguardInterfacesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        region_code: str,
        enable_sip_trunking: bool | Omit = omit,
        name: str | Omit = omit,
        network_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WireguardInterfaceCreateResponse:
        """Create a new WireGuard Interface.

        Current limitation of 10 interfaces per user
        can be created.

        Args:
          region_code: The region the interface should be deployed to.

          enable_sip_trunking: Enable SIP traffic forwarding over VPN interface.

          name: A user specified name for the interface.

          network_id: The id of the network associated with the interface.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wireguard_interfaces",
            body=await async_maybe_transform(
                {
                    "region_code": region_code,
                    "enable_sip_trunking": enable_sip_trunking,
                    "name": name,
                    "network_id": network_id,
                },
                wireguard_interface_create_params.WireguardInterfaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardInterfaceCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WireguardInterfaceRetrieveResponse:
        """
        Retrieve a WireGuard Interfaces.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/wireguard_interfaces/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardInterfaceRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: wireguard_interface_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WireguardInterfaceListResponse, AsyncDefaultFlatPagination[WireguardInterfaceListResponse]]:
        """
        List all WireGuard Interfaces.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/wireguard_interfaces",
            page=AsyncDefaultFlatPagination[WireguardInterfaceListResponse],
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
                    wireguard_interface_list_params.WireguardInterfaceListParams,
                ),
            ),
            model=WireguardInterfaceListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WireguardInterfaceDeleteResponse:
        """
        Delete a WireGuard Interface.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/wireguard_interfaces/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardInterfaceDeleteResponse,
        )


class WireguardInterfacesResourceWithRawResponse:
    def __init__(self, wireguard_interfaces: WireguardInterfacesResource) -> None:
        self._wireguard_interfaces = wireguard_interfaces

        self.create = to_raw_response_wrapper(
            wireguard_interfaces.create,
        )
        self.retrieve = to_raw_response_wrapper(
            wireguard_interfaces.retrieve,
        )
        self.list = to_raw_response_wrapper(
            wireguard_interfaces.list,
        )
        self.delete = to_raw_response_wrapper(
            wireguard_interfaces.delete,
        )


class AsyncWireguardInterfacesResourceWithRawResponse:
    def __init__(self, wireguard_interfaces: AsyncWireguardInterfacesResource) -> None:
        self._wireguard_interfaces = wireguard_interfaces

        self.create = async_to_raw_response_wrapper(
            wireguard_interfaces.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            wireguard_interfaces.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            wireguard_interfaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            wireguard_interfaces.delete,
        )


class WireguardInterfacesResourceWithStreamingResponse:
    def __init__(self, wireguard_interfaces: WireguardInterfacesResource) -> None:
        self._wireguard_interfaces = wireguard_interfaces

        self.create = to_streamed_response_wrapper(
            wireguard_interfaces.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            wireguard_interfaces.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            wireguard_interfaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            wireguard_interfaces.delete,
        )


class AsyncWireguardInterfacesResourceWithStreamingResponse:
    def __init__(self, wireguard_interfaces: AsyncWireguardInterfacesResource) -> None:
        self._wireguard_interfaces = wireguard_interfaces

        self.create = async_to_streamed_response_wrapper(
            wireguard_interfaces.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            wireguard_interfaces.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            wireguard_interfaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            wireguard_interfaces.delete,
        )
