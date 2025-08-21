# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import wireguard_peer_list_params, wireguard_peer_create_params, wireguard_peer_update_params
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
from ..types.wireguard_peer_list_response import WireguardPeerListResponse
from ..types.wireguard_peer_create_response import WireguardPeerCreateResponse
from ..types.wireguard_peer_delete_response import WireguardPeerDeleteResponse
from ..types.wireguard_peer_update_response import WireguardPeerUpdateResponse
from ..types.wireguard_peer_retrieve_response import WireguardPeerRetrieveResponse

__all__ = ["WireguardPeersResource", "AsyncWireguardPeersResource"]


class WireguardPeersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WireguardPeersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WireguardPeersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WireguardPeersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WireguardPeersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        wireguard_interface_id: str,
        public_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireguardPeerCreateResponse:
        """Create a new WireGuard Peer.

        Current limitation of 5 peers per interface can be
        created.

        Args:
          wireguard_interface_id: The id of the wireguard interface associated with the peer.

          public_key: The WireGuard `PublicKey`.<br /><br />If you do not provide a Public Key, a new
              Public and Private key pair will be generated for you.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/wireguard_peers",
            body=maybe_transform(
                {
                    "wireguard_interface_id": wireguard_interface_id,
                    "public_key": public_key,
                },
                wireguard_peer_create_params.WireguardPeerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerCreateResponse,
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
    ) -> WireguardPeerRetrieveResponse:
        """
        Retrieve the WireGuard peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/wireguard_peers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        public_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireguardPeerUpdateResponse:
        """
        Update the WireGuard peer.

        Args:
          public_key: The WireGuard `PublicKey`.<br /><br />If you do not provide a Public Key, a new
              Public and Private key pair will be generated for you.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/wireguard_peers/{id}",
            body=maybe_transform({"public_key": public_key}, wireguard_peer_update_params.WireguardPeerUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerUpdateResponse,
        )

    def list(
        self,
        *,
        filter: wireguard_peer_list_params.Filter | NotGiven = NOT_GIVEN,
        page: wireguard_peer_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireguardPeerListResponse:
        """
        List all WireGuard peers.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[wireguard_interface_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/wireguard_peers",
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
                    wireguard_peer_list_params.WireguardPeerListParams,
                ),
            ),
            cast_to=WireguardPeerListResponse,
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
    ) -> WireguardPeerDeleteResponse:
        """
        Delete the WireGuard peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/wireguard_peers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerDeleteResponse,
        )

    def retrieve_config(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Retrieve Wireguard config template for Peer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            f"/wireguard_peers/{id}/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncWireguardPeersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWireguardPeersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWireguardPeersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWireguardPeersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWireguardPeersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        wireguard_interface_id: str,
        public_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireguardPeerCreateResponse:
        """Create a new WireGuard Peer.

        Current limitation of 5 peers per interface can be
        created.

        Args:
          wireguard_interface_id: The id of the wireguard interface associated with the peer.

          public_key: The WireGuard `PublicKey`.<br /><br />If you do not provide a Public Key, a new
              Public and Private key pair will be generated for you.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/wireguard_peers",
            body=await async_maybe_transform(
                {
                    "wireguard_interface_id": wireguard_interface_id,
                    "public_key": public_key,
                },
                wireguard_peer_create_params.WireguardPeerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerCreateResponse,
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
    ) -> WireguardPeerRetrieveResponse:
        """
        Retrieve the WireGuard peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/wireguard_peers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        public_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireguardPeerUpdateResponse:
        """
        Update the WireGuard peer.

        Args:
          public_key: The WireGuard `PublicKey`.<br /><br />If you do not provide a Public Key, a new
              Public and Private key pair will be generated for you.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/wireguard_peers/{id}",
            body=await async_maybe_transform(
                {"public_key": public_key}, wireguard_peer_update_params.WireguardPeerUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: wireguard_peer_list_params.Filter | NotGiven = NOT_GIVEN,
        page: wireguard_peer_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WireguardPeerListResponse:
        """
        List all WireGuard peers.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[wireguard_interface_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/wireguard_peers",
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
                    wireguard_peer_list_params.WireguardPeerListParams,
                ),
            ),
            cast_to=WireguardPeerListResponse,
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
    ) -> WireguardPeerDeleteResponse:
        """
        Delete the WireGuard peer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/wireguard_peers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WireguardPeerDeleteResponse,
        )

    async def retrieve_config(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Retrieve Wireguard config template for Peer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            f"/wireguard_peers/{id}/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class WireguardPeersResourceWithRawResponse:
    def __init__(self, wireguard_peers: WireguardPeersResource) -> None:
        self._wireguard_peers = wireguard_peers

        self.create = to_raw_response_wrapper(
            wireguard_peers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            wireguard_peers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            wireguard_peers.update,
        )
        self.list = to_raw_response_wrapper(
            wireguard_peers.list,
        )
        self.delete = to_raw_response_wrapper(
            wireguard_peers.delete,
        )
        self.retrieve_config = to_raw_response_wrapper(
            wireguard_peers.retrieve_config,
        )


class AsyncWireguardPeersResourceWithRawResponse:
    def __init__(self, wireguard_peers: AsyncWireguardPeersResource) -> None:
        self._wireguard_peers = wireguard_peers

        self.create = async_to_raw_response_wrapper(
            wireguard_peers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            wireguard_peers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            wireguard_peers.update,
        )
        self.list = async_to_raw_response_wrapper(
            wireguard_peers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            wireguard_peers.delete,
        )
        self.retrieve_config = async_to_raw_response_wrapper(
            wireguard_peers.retrieve_config,
        )


class WireguardPeersResourceWithStreamingResponse:
    def __init__(self, wireguard_peers: WireguardPeersResource) -> None:
        self._wireguard_peers = wireguard_peers

        self.create = to_streamed_response_wrapper(
            wireguard_peers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            wireguard_peers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            wireguard_peers.update,
        )
        self.list = to_streamed_response_wrapper(
            wireguard_peers.list,
        )
        self.delete = to_streamed_response_wrapper(
            wireguard_peers.delete,
        )
        self.retrieve_config = to_streamed_response_wrapper(
            wireguard_peers.retrieve_config,
        )


class AsyncWireguardPeersResourceWithStreamingResponse:
    def __init__(self, wireguard_peers: AsyncWireguardPeersResource) -> None:
        self._wireguard_peers = wireguard_peers

        self.create = async_to_streamed_response_wrapper(
            wireguard_peers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            wireguard_peers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            wireguard_peers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            wireguard_peers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            wireguard_peers.delete,
        )
        self.retrieve_config = async_to_streamed_response_wrapper(
            wireguard_peers.retrieve_config,
        )
