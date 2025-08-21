# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    virtual_cross_connect_list_params,
    virtual_cross_connect_create_params,
    virtual_cross_connect_update_params,
)
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
from ..types.virtual_cross_connect_list_response import VirtualCrossConnectListResponse
from ..types.virtual_cross_connect_create_response import VirtualCrossConnectCreateResponse
from ..types.virtual_cross_connect_delete_response import VirtualCrossConnectDeleteResponse
from ..types.virtual_cross_connect_update_response import VirtualCrossConnectUpdateResponse
from ..types.virtual_cross_connect_retrieve_response import VirtualCrossConnectRetrieveResponse

__all__ = ["VirtualCrossConnectsResource", "AsyncVirtualCrossConnectsResource"]


class VirtualCrossConnectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualCrossConnectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VirtualCrossConnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualCrossConnectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VirtualCrossConnectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bgp_asn: float,
        cloud_provider: Literal["aws", "azure", "gce"],
        cloud_provider_region: str,
        network_id: str,
        primary_cloud_account_id: str,
        region_code: str,
        bandwidth_mbps: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        primary_bgp_key: str | NotGiven = NOT_GIVEN,
        primary_cloud_ip: str | NotGiven = NOT_GIVEN,
        primary_telnyx_ip: str | NotGiven = NOT_GIVEN,
        secondary_bgp_key: str | NotGiven = NOT_GIVEN,
        secondary_cloud_account_id: str | NotGiven = NOT_GIVEN,
        secondary_cloud_ip: str | NotGiven = NOT_GIVEN,
        secondary_telnyx_ip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectCreateResponse:
        """
        Create a new Virtual Cross Connect.<br /><br />For AWS and GCE, you have the
        option of creating the primary connection first and the secondary connection
        later. You also have the option of disabling the primary and/or secondary
        connections at any time and later re-enabling them. With Azure, you do not have
        this option. Azure requires both the primary and secondary connections to be
        created at the same time and they can not be independantly disabled.

        Args:
          bgp_asn: The Border Gateway Protocol (BGP) Autonomous System Number (ASN). If null, value
              will be assigned by Telnyx.

          cloud_provider: The Virtual Private Cloud with which you would like to establish a cross
              connect.

          cloud_provider_region: The region where your Virtual Private Cloud hosts are located.<br /><br />The
              available regions can be found using the /virtual_cross_connect_regions
              endpoint.

          network_id: The id of the network associated with the interface.

          primary_cloud_account_id: The identifier for your Virtual Private Cloud. The number will be different
              based upon your Cloud provider.

          region_code: The region the interface should be deployed to.

          bandwidth_mbps: The desired throughput in Megabits per Second (Mbps) for your Virtual Cross
              Connect.<br /><br />The available bandwidths can be found using the
              /virtual_cross_connect_regions endpoint.

          name: A user specified name for the interface.

          primary_bgp_key: The authentication key for BGP peer configuration.

          primary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          primary_telnyx_ip: The IP address assigned to the Telnyx side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          secondary_bgp_key: The authentication key for BGP peer configuration.

          secondary_cloud_account_id: The identifier for your Virtual Private Cloud. The number will be different
              based upon your Cloud provider.<br /><br />This attribute is only necessary for
              GCE.

          secondary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          secondary_telnyx_ip: The IP address assigned to the Telnyx side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/virtual_cross_connects",
            body=maybe_transform(
                {
                    "bgp_asn": bgp_asn,
                    "cloud_provider": cloud_provider,
                    "cloud_provider_region": cloud_provider_region,
                    "network_id": network_id,
                    "primary_cloud_account_id": primary_cloud_account_id,
                    "region_code": region_code,
                    "bandwidth_mbps": bandwidth_mbps,
                    "name": name,
                    "primary_bgp_key": primary_bgp_key,
                    "primary_cloud_ip": primary_cloud_ip,
                    "primary_telnyx_ip": primary_telnyx_ip,
                    "secondary_bgp_key": secondary_bgp_key,
                    "secondary_cloud_account_id": secondary_cloud_account_id,
                    "secondary_cloud_ip": secondary_cloud_ip,
                    "secondary_telnyx_ip": secondary_telnyx_ip,
                },
                virtual_cross_connect_create_params.VirtualCrossConnectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectCreateResponse,
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
    ) -> VirtualCrossConnectRetrieveResponse:
        """
        Retrieve a Virtual Cross Connect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/virtual_cross_connects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        primary_cloud_ip: str | NotGiven = NOT_GIVEN,
        primary_enabled: bool | NotGiven = NOT_GIVEN,
        primary_routing_announcement: bool | NotGiven = NOT_GIVEN,
        secondary_cloud_ip: str | NotGiven = NOT_GIVEN,
        secondary_enabled: bool | NotGiven = NOT_GIVEN,
        secondary_routing_announcement: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectUpdateResponse:
        """
        Update the Virtual Cross Connect.<br /><br />Cloud IPs can only be patched
        during the `created` state, as GCE will only inform you of your generated IP
        once the pending connection requested has been accepted. Once the Virtual Cross
        Connect has moved to `provisioning`, the IPs can no longer be
        patched.<br /><br />Once the Virtual Cross Connect has moved to `provisioned`
        and you are ready to enable routing, you can toggle the routing announcements to
        `true`.

        Args:
          primary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value can not be patched once the VXC has bene provisioned.

          primary_enabled: Indicates whether the primary circuit is enabled. Setting this to `false` will
              disable the circuit.

          primary_routing_announcement: Whether the primary BGP route is being announced.

          secondary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value can not be patched once the VXC has bene provisioned.

          secondary_enabled: Indicates whether the secondary circuit is enabled. Setting this to `false` will
              disable the circuit.

          secondary_routing_announcement: Whether the secondary BGP route is being announced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/virtual_cross_connects/{id}",
            body=maybe_transform(
                {
                    "primary_cloud_ip": primary_cloud_ip,
                    "primary_enabled": primary_enabled,
                    "primary_routing_announcement": primary_routing_announcement,
                    "secondary_cloud_ip": secondary_cloud_ip,
                    "secondary_enabled": secondary_enabled,
                    "secondary_routing_announcement": secondary_routing_announcement,
                },
                virtual_cross_connect_update_params.VirtualCrossConnectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectUpdateResponse,
        )

    def list(
        self,
        *,
        filter: virtual_cross_connect_list_params.Filter | NotGiven = NOT_GIVEN,
        page: virtual_cross_connect_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectListResponse:
        """
        List all Virtual Cross Connects.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/virtual_cross_connects",
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
                    virtual_cross_connect_list_params.VirtualCrossConnectListParams,
                ),
            ),
            cast_to=VirtualCrossConnectListResponse,
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
    ) -> VirtualCrossConnectDeleteResponse:
        """
        Delete a Virtual Cross Connect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/virtual_cross_connects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectDeleteResponse,
        )


class AsyncVirtualCrossConnectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualCrossConnectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVirtualCrossConnectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualCrossConnectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVirtualCrossConnectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bgp_asn: float,
        cloud_provider: Literal["aws", "azure", "gce"],
        cloud_provider_region: str,
        network_id: str,
        primary_cloud_account_id: str,
        region_code: str,
        bandwidth_mbps: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        primary_bgp_key: str | NotGiven = NOT_GIVEN,
        primary_cloud_ip: str | NotGiven = NOT_GIVEN,
        primary_telnyx_ip: str | NotGiven = NOT_GIVEN,
        secondary_bgp_key: str | NotGiven = NOT_GIVEN,
        secondary_cloud_account_id: str | NotGiven = NOT_GIVEN,
        secondary_cloud_ip: str | NotGiven = NOT_GIVEN,
        secondary_telnyx_ip: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectCreateResponse:
        """
        Create a new Virtual Cross Connect.<br /><br />For AWS and GCE, you have the
        option of creating the primary connection first and the secondary connection
        later. You also have the option of disabling the primary and/or secondary
        connections at any time and later re-enabling them. With Azure, you do not have
        this option. Azure requires both the primary and secondary connections to be
        created at the same time and they can not be independantly disabled.

        Args:
          bgp_asn: The Border Gateway Protocol (BGP) Autonomous System Number (ASN). If null, value
              will be assigned by Telnyx.

          cloud_provider: The Virtual Private Cloud with which you would like to establish a cross
              connect.

          cloud_provider_region: The region where your Virtual Private Cloud hosts are located.<br /><br />The
              available regions can be found using the /virtual_cross_connect_regions
              endpoint.

          network_id: The id of the network associated with the interface.

          primary_cloud_account_id: The identifier for your Virtual Private Cloud. The number will be different
              based upon your Cloud provider.

          region_code: The region the interface should be deployed to.

          bandwidth_mbps: The desired throughput in Megabits per Second (Mbps) for your Virtual Cross
              Connect.<br /><br />The available bandwidths can be found using the
              /virtual_cross_connect_regions endpoint.

          name: A user specified name for the interface.

          primary_bgp_key: The authentication key for BGP peer configuration.

          primary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          primary_telnyx_ip: The IP address assigned to the Telnyx side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          secondary_bgp_key: The authentication key for BGP peer configuration.

          secondary_cloud_account_id: The identifier for your Virtual Private Cloud. The number will be different
              based upon your Cloud provider.<br /><br />This attribute is only necessary for
              GCE.

          secondary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          secondary_telnyx_ip: The IP address assigned to the Telnyx side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value should be null for GCE as Google will only inform you
              of your assigned IP once the connection has been accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/virtual_cross_connects",
            body=await async_maybe_transform(
                {
                    "bgp_asn": bgp_asn,
                    "cloud_provider": cloud_provider,
                    "cloud_provider_region": cloud_provider_region,
                    "network_id": network_id,
                    "primary_cloud_account_id": primary_cloud_account_id,
                    "region_code": region_code,
                    "bandwidth_mbps": bandwidth_mbps,
                    "name": name,
                    "primary_bgp_key": primary_bgp_key,
                    "primary_cloud_ip": primary_cloud_ip,
                    "primary_telnyx_ip": primary_telnyx_ip,
                    "secondary_bgp_key": secondary_bgp_key,
                    "secondary_cloud_account_id": secondary_cloud_account_id,
                    "secondary_cloud_ip": secondary_cloud_ip,
                    "secondary_telnyx_ip": secondary_telnyx_ip,
                },
                virtual_cross_connect_create_params.VirtualCrossConnectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectCreateResponse,
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
    ) -> VirtualCrossConnectRetrieveResponse:
        """
        Retrieve a Virtual Cross Connect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/virtual_cross_connects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        primary_cloud_ip: str | NotGiven = NOT_GIVEN,
        primary_enabled: bool | NotGiven = NOT_GIVEN,
        primary_routing_announcement: bool | NotGiven = NOT_GIVEN,
        secondary_cloud_ip: str | NotGiven = NOT_GIVEN,
        secondary_enabled: bool | NotGiven = NOT_GIVEN,
        secondary_routing_announcement: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectUpdateResponse:
        """
        Update the Virtual Cross Connect.<br /><br />Cloud IPs can only be patched
        during the `created` state, as GCE will only inform you of your generated IP
        once the pending connection requested has been accepted. Once the Virtual Cross
        Connect has moved to `provisioning`, the IPs can no longer be
        patched.<br /><br />Once the Virtual Cross Connect has moved to `provisioned`
        and you are ready to enable routing, you can toggle the routing announcements to
        `true`.

        Args:
          primary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value can not be patched once the VXC has bene provisioned.

          primary_enabled: Indicates whether the primary circuit is enabled. Setting this to `false` will
              disable the circuit.

          primary_routing_announcement: Whether the primary BGP route is being announced.

          secondary_cloud_ip: The IP address assigned for your side of the Virtual Cross
              Connect.<br /><br />If none is provided, one will be generated for
              you.<br /><br />This value can not be patched once the VXC has bene provisioned.

          secondary_enabled: Indicates whether the secondary circuit is enabled. Setting this to `false` will
              disable the circuit.

          secondary_routing_announcement: Whether the secondary BGP route is being announced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/virtual_cross_connects/{id}",
            body=await async_maybe_transform(
                {
                    "primary_cloud_ip": primary_cloud_ip,
                    "primary_enabled": primary_enabled,
                    "primary_routing_announcement": primary_routing_announcement,
                    "secondary_cloud_ip": secondary_cloud_ip,
                    "secondary_enabled": secondary_enabled,
                    "secondary_routing_announcement": secondary_routing_announcement,
                },
                virtual_cross_connect_update_params.VirtualCrossConnectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: virtual_cross_connect_list_params.Filter | NotGiven = NOT_GIVEN,
        page: virtual_cross_connect_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VirtualCrossConnectListResponse:
        """
        List all Virtual Cross Connects.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[network_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/virtual_cross_connects",
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
                    virtual_cross_connect_list_params.VirtualCrossConnectListParams,
                ),
            ),
            cast_to=VirtualCrossConnectListResponse,
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
    ) -> VirtualCrossConnectDeleteResponse:
        """
        Delete a Virtual Cross Connect.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/virtual_cross_connects/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VirtualCrossConnectDeleteResponse,
        )


class VirtualCrossConnectsResourceWithRawResponse:
    def __init__(self, virtual_cross_connects: VirtualCrossConnectsResource) -> None:
        self._virtual_cross_connects = virtual_cross_connects

        self.create = to_raw_response_wrapper(
            virtual_cross_connects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            virtual_cross_connects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            virtual_cross_connects.update,
        )
        self.list = to_raw_response_wrapper(
            virtual_cross_connects.list,
        )
        self.delete = to_raw_response_wrapper(
            virtual_cross_connects.delete,
        )


class AsyncVirtualCrossConnectsResourceWithRawResponse:
    def __init__(self, virtual_cross_connects: AsyncVirtualCrossConnectsResource) -> None:
        self._virtual_cross_connects = virtual_cross_connects

        self.create = async_to_raw_response_wrapper(
            virtual_cross_connects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            virtual_cross_connects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            virtual_cross_connects.update,
        )
        self.list = async_to_raw_response_wrapper(
            virtual_cross_connects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            virtual_cross_connects.delete,
        )


class VirtualCrossConnectsResourceWithStreamingResponse:
    def __init__(self, virtual_cross_connects: VirtualCrossConnectsResource) -> None:
        self._virtual_cross_connects = virtual_cross_connects

        self.create = to_streamed_response_wrapper(
            virtual_cross_connects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            virtual_cross_connects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            virtual_cross_connects.update,
        )
        self.list = to_streamed_response_wrapper(
            virtual_cross_connects.list,
        )
        self.delete = to_streamed_response_wrapper(
            virtual_cross_connects.delete,
        )


class AsyncVirtualCrossConnectsResourceWithStreamingResponse:
    def __init__(self, virtual_cross_connects: AsyncVirtualCrossConnectsResource) -> None:
        self._virtual_cross_connects = virtual_cross_connects

        self.create = async_to_streamed_response_wrapper(
            virtual_cross_connects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            virtual_cross_connects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            virtual_cross_connects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            virtual_cross_connects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            virtual_cross_connects.delete,
        )
