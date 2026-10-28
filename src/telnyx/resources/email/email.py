# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .ip_pools.ip_pools import (
    IPPoolsResource,
    AsyncIPPoolsResource,
    IPPoolsResourceWithRawResponse,
    AsyncIPPoolsResourceWithRawResponse,
    IPPoolsResourceWithStreamingResponse,
    AsyncIPPoolsResourceWithStreamingResponse,
)
from .dedicated_ips.dedicated_ips import (
    DedicatedIPsResource,
    AsyncDedicatedIPsResource,
    DedicatedIPsResourceWithRawResponse,
    AsyncDedicatedIPsResourceWithRawResponse,
    DedicatedIPsResourceWithStreamingResponse,
    AsyncDedicatedIPsResourceWithStreamingResponse,
)

__all__ = ["EmailResource", "AsyncEmailResource"]


class EmailResource(SyncAPIResource):
    @cached_property
    def dedicated_ips(self) -> DedicatedIPsResource:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return DedicatedIPsResource(self._client)

    @cached_property
    def ip_pools(self) -> IPPoolsResource:
        """Group dedicated IPs into pools for sending."""
        return IPPoolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailResourceWithStreamingResponse(self)


class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def dedicated_ips(self) -> AsyncDedicatedIPsResource:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return AsyncDedicatedIPsResource(self._client)

    @cached_property
    def ip_pools(self) -> AsyncIPPoolsResource:
        """Group dedicated IPs into pools for sending."""
        return AsyncIPPoolsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailResourceWithStreamingResponse(self)


class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def dedicated_ips(self) -> DedicatedIPsResourceWithRawResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return DedicatedIPsResourceWithRawResponse(self._email.dedicated_ips)

    @cached_property
    def ip_pools(self) -> IPPoolsResourceWithRawResponse:
        """Group dedicated IPs into pools for sending."""
        return IPPoolsResourceWithRawResponse(self._email.ip_pools)


class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def dedicated_ips(self) -> AsyncDedicatedIPsResourceWithRawResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return AsyncDedicatedIPsResourceWithRawResponse(self._email.dedicated_ips)

    @cached_property
    def ip_pools(self) -> AsyncIPPoolsResourceWithRawResponse:
        """Group dedicated IPs into pools for sending."""
        return AsyncIPPoolsResourceWithRawResponse(self._email.ip_pools)


class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def dedicated_ips(self) -> DedicatedIPsResourceWithStreamingResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return DedicatedIPsResourceWithStreamingResponse(self._email.dedicated_ips)

    @cached_property
    def ip_pools(self) -> IPPoolsResourceWithStreamingResponse:
        """Group dedicated IPs into pools for sending."""
        return IPPoolsResourceWithStreamingResponse(self._email.ip_pools)


class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def dedicated_ips(self) -> AsyncDedicatedIPsResourceWithStreamingResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return AsyncDedicatedIPsResourceWithStreamingResponse(self._email.dedicated_ips)

    @cached_property
    def ip_pools(self) -> AsyncIPPoolsResourceWithStreamingResponse:
        """Group dedicated IPs into pools for sending."""
        return AsyncIPPoolsResourceWithStreamingResponse(self._email.ip_pools)
