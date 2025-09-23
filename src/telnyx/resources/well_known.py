# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.well_known_retrieve_protected_resource_metadata_response import (
    WellKnownRetrieveProtectedResourceMetadataResponse,
)
from ..types.well_known_retrieve_authorization_server_metadata_response import (
    WellKnownRetrieveAuthorizationServerMetadataResponse,
)

__all__ = ["WellKnownResource", "AsyncWellKnownResource"]


class WellKnownResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WellKnownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WellKnownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WellKnownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WellKnownResourceWithStreamingResponse(self)

    def retrieve_authorization_server_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WellKnownRetrieveAuthorizationServerMetadataResponse:
        """OAuth 2.0 Authorization Server Metadata (RFC 8414)"""
        return self._get(
            "/.well-known/oauth-authorization-server"
            if self._client._base_url_overridden
            else "https://api.telnyx.com/.well-known/oauth-authorization-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WellKnownRetrieveAuthorizationServerMetadataResponse,
        )

    def retrieve_protected_resource_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WellKnownRetrieveProtectedResourceMetadataResponse:
        """OAuth 2.0 Protected Resource Metadata for resource discovery"""
        return self._get(
            "/.well-known/oauth-protected-resource"
            if self._client._base_url_overridden
            else "https://api.telnyx.com/.well-known/oauth-protected-resource",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WellKnownRetrieveProtectedResourceMetadataResponse,
        )


class AsyncWellKnownResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWellKnownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWellKnownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWellKnownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWellKnownResourceWithStreamingResponse(self)

    async def retrieve_authorization_server_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WellKnownRetrieveAuthorizationServerMetadataResponse:
        """OAuth 2.0 Authorization Server Metadata (RFC 8414)"""
        return await self._get(
            "/.well-known/oauth-authorization-server"
            if self._client._base_url_overridden
            else "https://api.telnyx.com/.well-known/oauth-authorization-server",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WellKnownRetrieveAuthorizationServerMetadataResponse,
        )

    async def retrieve_protected_resource_metadata(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WellKnownRetrieveProtectedResourceMetadataResponse:
        """OAuth 2.0 Protected Resource Metadata for resource discovery"""
        return await self._get(
            "/.well-known/oauth-protected-resource"
            if self._client._base_url_overridden
            else "https://api.telnyx.com/.well-known/oauth-protected-resource",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WellKnownRetrieveProtectedResourceMetadataResponse,
        )


class WellKnownResourceWithRawResponse:
    def __init__(self, well_known: WellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = to_raw_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = to_raw_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )


class AsyncWellKnownResourceWithRawResponse:
    def __init__(self, well_known: AsyncWellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = async_to_raw_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = async_to_raw_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )


class WellKnownResourceWithStreamingResponse:
    def __init__(self, well_known: WellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = to_streamed_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = to_streamed_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )


class AsyncWellKnownResourceWithStreamingResponse:
    def __init__(self, well_known: AsyncWellKnownResource) -> None:
        self._well_known = well_known

        self.retrieve_authorization_server_metadata = async_to_streamed_response_wrapper(
            well_known.retrieve_authorization_server_metadata,
        )
        self.retrieve_protected_resource_metadata = async_to_streamed_response_wrapper(
            well_known.retrieve_protected_resource_metadata,
        )
