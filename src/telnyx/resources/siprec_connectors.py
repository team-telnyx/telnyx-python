# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import siprec_connector_create_params, siprec_connector_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.siprec_connector_create_response import SiprecConnectorCreateResponse
from ..types.siprec_connector_update_response import SiprecConnectorUpdateResponse
from ..types.siprec_connector_retrieve_response import SiprecConnectorRetrieveResponse

__all__ = ["SiprecConnectorsResource", "AsyncSiprecConnectorsResource"]


class SiprecConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SiprecConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SiprecConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiprecConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SiprecConnectorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        host: str,
        name: str,
        port: int,
        app_subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecConnectorCreateResponse:
        """
        Creates a new SIPREC connector configuration.

        Args:
          host: Hostname/IPv4 address of the SIPREC SRS.

          name: Name for the SIPREC connector resource.

          port: Port for the SIPREC SRS.

          app_subdomain: Subdomain to route the call when using Telnyx SRS (optional for non-Telnyx SRS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/siprec_connectors",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "port": port,
                    "app_subdomain": app_subdomain,
                },
                siprec_connector_create_params.SiprecConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecConnectorCreateResponse,
        )

    def retrieve(
        self,
        connector_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecConnectorRetrieveResponse:
        """
        Returns details of a stored SIPREC connector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_name:
            raise ValueError(f"Expected a non-empty value for `connector_name` but received {connector_name!r}")
        return self._get(
            f"/siprec_connectors/{connector_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecConnectorRetrieveResponse,
        )

    def update(
        self,
        connector_name: str,
        *,
        host: str,
        name: str,
        port: int,
        app_subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecConnectorUpdateResponse:
        """
        Updates a stored SIPREC connector configuration.

        Args:
          host: Hostname/IPv4 address of the SIPREC SRS.

          name: Name for the SIPREC connector resource.

          port: Port for the SIPREC SRS.

          app_subdomain: Subdomain to route the call when using Telnyx SRS (optional for non-Telnyx SRS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_name:
            raise ValueError(f"Expected a non-empty value for `connector_name` but received {connector_name!r}")
        return self._put(
            f"/siprec_connectors/{connector_name}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "port": port,
                    "app_subdomain": app_subdomain,
                },
                siprec_connector_update_params.SiprecConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecConnectorUpdateResponse,
        )

    def delete(
        self,
        connector_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored SIPREC connector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_name:
            raise ValueError(f"Expected a non-empty value for `connector_name` but received {connector_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/siprec_connectors/{connector_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSiprecConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSiprecConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSiprecConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiprecConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSiprecConnectorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        host: str,
        name: str,
        port: int,
        app_subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecConnectorCreateResponse:
        """
        Creates a new SIPREC connector configuration.

        Args:
          host: Hostname/IPv4 address of the SIPREC SRS.

          name: Name for the SIPREC connector resource.

          port: Port for the SIPREC SRS.

          app_subdomain: Subdomain to route the call when using Telnyx SRS (optional for non-Telnyx SRS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/siprec_connectors",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "port": port,
                    "app_subdomain": app_subdomain,
                },
                siprec_connector_create_params.SiprecConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecConnectorCreateResponse,
        )

    async def retrieve(
        self,
        connector_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecConnectorRetrieveResponse:
        """
        Returns details of a stored SIPREC connector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_name:
            raise ValueError(f"Expected a non-empty value for `connector_name` but received {connector_name!r}")
        return await self._get(
            f"/siprec_connectors/{connector_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecConnectorRetrieveResponse,
        )

    async def update(
        self,
        connector_name: str,
        *,
        host: str,
        name: str,
        port: int,
        app_subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecConnectorUpdateResponse:
        """
        Updates a stored SIPREC connector configuration.

        Args:
          host: Hostname/IPv4 address of the SIPREC SRS.

          name: Name for the SIPREC connector resource.

          port: Port for the SIPREC SRS.

          app_subdomain: Subdomain to route the call when using Telnyx SRS (optional for non-Telnyx SRS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_name:
            raise ValueError(f"Expected a non-empty value for `connector_name` but received {connector_name!r}")
        return await self._put(
            f"/siprec_connectors/{connector_name}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "port": port,
                    "app_subdomain": app_subdomain,
                },
                siprec_connector_update_params.SiprecConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecConnectorUpdateResponse,
        )

    async def delete(
        self,
        connector_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored SIPREC connector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_name:
            raise ValueError(f"Expected a non-empty value for `connector_name` but received {connector_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/siprec_connectors/{connector_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SiprecConnectorsResourceWithRawResponse:
    def __init__(self, siprec_connectors: SiprecConnectorsResource) -> None:
        self._siprec_connectors = siprec_connectors

        self.create = to_raw_response_wrapper(
            siprec_connectors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            siprec_connectors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            siprec_connectors.update,
        )
        self.delete = to_raw_response_wrapper(
            siprec_connectors.delete,
        )


class AsyncSiprecConnectorsResourceWithRawResponse:
    def __init__(self, siprec_connectors: AsyncSiprecConnectorsResource) -> None:
        self._siprec_connectors = siprec_connectors

        self.create = async_to_raw_response_wrapper(
            siprec_connectors.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            siprec_connectors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            siprec_connectors.update,
        )
        self.delete = async_to_raw_response_wrapper(
            siprec_connectors.delete,
        )


class SiprecConnectorsResourceWithStreamingResponse:
    def __init__(self, siprec_connectors: SiprecConnectorsResource) -> None:
        self._siprec_connectors = siprec_connectors

        self.create = to_streamed_response_wrapper(
            siprec_connectors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            siprec_connectors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            siprec_connectors.update,
        )
        self.delete = to_streamed_response_wrapper(
            siprec_connectors.delete,
        )


class AsyncSiprecConnectorsResourceWithStreamingResponse:
    def __init__(self, siprec_connectors: AsyncSiprecConnectorsResource) -> None:
        self._siprec_connectors = siprec_connectors

        self.create = async_to_streamed_response_wrapper(
            siprec_connectors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            siprec_connectors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            siprec_connectors.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            siprec_connectors.delete,
        )
