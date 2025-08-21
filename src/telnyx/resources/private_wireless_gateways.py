# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import private_wireless_gateway_list_params, private_wireless_gateway_create_params
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
from ..types.private_wireless_gateway_list_response import PrivateWirelessGatewayListResponse
from ..types.private_wireless_gateway_create_response import PrivateWirelessGatewayCreateResponse
from ..types.private_wireless_gateway_delete_response import PrivateWirelessGatewayDeleteResponse
from ..types.private_wireless_gateway_retrieve_response import PrivateWirelessGatewayRetrieveResponse

__all__ = ["PrivateWirelessGatewaysResource", "AsyncPrivateWirelessGatewaysResource"]


class PrivateWirelessGatewaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrivateWirelessGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PrivateWirelessGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateWirelessGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PrivateWirelessGatewaysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        network_id: str,
        region_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateWirelessGatewayCreateResponse:
        """
        Asynchronously create a Private Wireless Gateway for SIM cards for a previously
        created network. This operation may take several minutes so you can check the
        Private Wireless Gateway status at the section Get a Private Wireless Gateway.

        Args:
          name: The private wireless gateway name.

          network_id: The identification of the related network resource.

          region_code: The code of the region where the private wireless gateway will be assigned. A
              list of available regions can be found at the regions endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/private_wireless_gateways",
            body=maybe_transform(
                {
                    "name": name,
                    "network_id": network_id,
                    "region_code": region_code,
                },
                private_wireless_gateway_create_params.PrivateWirelessGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateWirelessGatewayCreateResponse,
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
    ) -> PrivateWirelessGatewayRetrieveResponse:
        """
        Retrieve information about a Private Wireless Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/private_wireless_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateWirelessGatewayRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_created_at: str | NotGiven = NOT_GIVEN,
        filter_ip_range: str | NotGiven = NOT_GIVEN,
        filter_name: str | NotGiven = NOT_GIVEN,
        filter_region_code: str | NotGiven = NOT_GIVEN,
        filter_updated_at: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateWirelessGatewayListResponse:
        """
        Get all Private Wireless Gateways belonging to the user.

        Args:
          filter_created_at: Private Wireless Gateway resource creation date.

          filter_ip_range: The IP address range of the Private Wireless Gateway.

          filter_name: The name of the Private Wireless Gateway.

          filter_region_code: The name of the region where the Private Wireless Gateway is deployed.

          filter_updated_at: When the Private Wireless Gateway was last updated.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/private_wireless_gateways",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at": filter_created_at,
                        "filter_ip_range": filter_ip_range,
                        "filter_name": filter_name,
                        "filter_region_code": filter_region_code,
                        "filter_updated_at": filter_updated_at,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    private_wireless_gateway_list_params.PrivateWirelessGatewayListParams,
                ),
            ),
            cast_to=PrivateWirelessGatewayListResponse,
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
    ) -> PrivateWirelessGatewayDeleteResponse:
        """
        Deletes the Private Wireless Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/private_wireless_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateWirelessGatewayDeleteResponse,
        )


class AsyncPrivateWirelessGatewaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrivateWirelessGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivateWirelessGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateWirelessGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPrivateWirelessGatewaysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        network_id: str,
        region_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateWirelessGatewayCreateResponse:
        """
        Asynchronously create a Private Wireless Gateway for SIM cards for a previously
        created network. This operation may take several minutes so you can check the
        Private Wireless Gateway status at the section Get a Private Wireless Gateway.

        Args:
          name: The private wireless gateway name.

          network_id: The identification of the related network resource.

          region_code: The code of the region where the private wireless gateway will be assigned. A
              list of available regions can be found at the regions endpoint

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/private_wireless_gateways",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network_id": network_id,
                    "region_code": region_code,
                },
                private_wireless_gateway_create_params.PrivateWirelessGatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateWirelessGatewayCreateResponse,
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
    ) -> PrivateWirelessGatewayRetrieveResponse:
        """
        Retrieve information about a Private Wireless Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/private_wireless_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateWirelessGatewayRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter_created_at: str | NotGiven = NOT_GIVEN,
        filter_ip_range: str | NotGiven = NOT_GIVEN,
        filter_name: str | NotGiven = NOT_GIVEN,
        filter_region_code: str | NotGiven = NOT_GIVEN,
        filter_updated_at: str | NotGiven = NOT_GIVEN,
        page_number: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateWirelessGatewayListResponse:
        """
        Get all Private Wireless Gateways belonging to the user.

        Args:
          filter_created_at: Private Wireless Gateway resource creation date.

          filter_ip_range: The IP address range of the Private Wireless Gateway.

          filter_name: The name of the Private Wireless Gateway.

          filter_region_code: The name of the region where the Private Wireless Gateway is deployed.

          filter_updated_at: When the Private Wireless Gateway was last updated.

          page_number: The page number to load.

          page_size: The size of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/private_wireless_gateways",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_created_at": filter_created_at,
                        "filter_ip_range": filter_ip_range,
                        "filter_name": filter_name,
                        "filter_region_code": filter_region_code,
                        "filter_updated_at": filter_updated_at,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    private_wireless_gateway_list_params.PrivateWirelessGatewayListParams,
                ),
            ),
            cast_to=PrivateWirelessGatewayListResponse,
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
    ) -> PrivateWirelessGatewayDeleteResponse:
        """
        Deletes the Private Wireless Gateway.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/private_wireless_gateways/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrivateWirelessGatewayDeleteResponse,
        )


class PrivateWirelessGatewaysResourceWithRawResponse:
    def __init__(self, private_wireless_gateways: PrivateWirelessGatewaysResource) -> None:
        self._private_wireless_gateways = private_wireless_gateways

        self.create = to_raw_response_wrapper(
            private_wireless_gateways.create,
        )
        self.retrieve = to_raw_response_wrapper(
            private_wireless_gateways.retrieve,
        )
        self.list = to_raw_response_wrapper(
            private_wireless_gateways.list,
        )
        self.delete = to_raw_response_wrapper(
            private_wireless_gateways.delete,
        )


class AsyncPrivateWirelessGatewaysResourceWithRawResponse:
    def __init__(self, private_wireless_gateways: AsyncPrivateWirelessGatewaysResource) -> None:
        self._private_wireless_gateways = private_wireless_gateways

        self.create = async_to_raw_response_wrapper(
            private_wireless_gateways.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            private_wireless_gateways.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            private_wireless_gateways.list,
        )
        self.delete = async_to_raw_response_wrapper(
            private_wireless_gateways.delete,
        )


class PrivateWirelessGatewaysResourceWithStreamingResponse:
    def __init__(self, private_wireless_gateways: PrivateWirelessGatewaysResource) -> None:
        self._private_wireless_gateways = private_wireless_gateways

        self.create = to_streamed_response_wrapper(
            private_wireless_gateways.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            private_wireless_gateways.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            private_wireless_gateways.list,
        )
        self.delete = to_streamed_response_wrapper(
            private_wireless_gateways.delete,
        )


class AsyncPrivateWirelessGatewaysResourceWithStreamingResponse:
    def __init__(self, private_wireless_gateways: AsyncPrivateWirelessGatewaysResource) -> None:
        self._private_wireless_gateways = private_wireless_gateways

        self.create = async_to_streamed_response_wrapper(
            private_wireless_gateways.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            private_wireless_gateways.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            private_wireless_gateways.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            private_wireless_gateways.delete,
        )
