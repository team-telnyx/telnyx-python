# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.email.ip_pools import ip_create_params, ip_delete_params
from ....types.email.ip_pools.ip_create_response import IPCreateResponse

__all__ = ["IPsResource", "AsyncIPsResource"]


class IPsResource(SyncAPIResource):
    """Group dedicated IPs into pools for sending."""

    @cached_property
    def with_raw_response(self) -> IPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return IPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return IPsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        dedicated_ip_id: str,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPCreateResponse:
        """Add a dedicated IP to the pool with an optional routing weight.

        An IP can belong
        to one pool; to move an IP that is already in a pool, use
        `PATCH /email/dedicated_ips/{id}` with `pool_id`.

        Args:
          dedicated_ip_id: The dedicated IP to add. It must belong to the account, must not be released,
              and must not already be in a pool.

          weight: Relative routing weight for this IP in the pool. Positive integer; defaults
              to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email/ip_pools/{id}/ips", id=id),
            body=maybe_transform(
                {
                    "dedicated_ip_id": dedicated_ip_id,
                    "weight": weight,
                },
                ip_create_params.IPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPCreateResponse,
        )

    def delete(
        self,
        ip_id: str,
        *,
        id: str,
        drain: bool | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove the dedicated IP from the pool.

        The IP is kept but carries no mail until
        added to a pool again. Removing the last IP requires `force=true` and
        `drain=true`.

        Args:
          drain: Set together with `force=true` to remove the last IP in the pool. Acknowledges
              that mail routed to the emptied pool is held until the pool has a sendable IP
              again.

          force: Set together with `drain=true` to remove the last IP in the pool. Either flag
              alone has no effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ip_id:
            raise ValueError(f"Expected a non-empty value for `ip_id` but received {ip_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/email/ip_pools/{id}/ips/{ip_id}", id=id, ip_id=ip_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "drain": drain,
                        "force": force,
                    },
                    ip_delete_params.IPDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncIPsResource(AsyncAPIResource):
    """Group dedicated IPs into pools for sending."""

    @cached_property
    def with_raw_response(self) -> AsyncIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncIPsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        dedicated_ip_id: str,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPCreateResponse:
        """Add a dedicated IP to the pool with an optional routing weight.

        An IP can belong
        to one pool; to move an IP that is already in a pool, use
        `PATCH /email/dedicated_ips/{id}` with `pool_id`.

        Args:
          dedicated_ip_id: The dedicated IP to add. It must belong to the account, must not be released,
              and must not already be in a pool.

          weight: Relative routing weight for this IP in the pool. Positive integer; defaults
              to 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email/ip_pools/{id}/ips", id=id),
            body=await async_maybe_transform(
                {
                    "dedicated_ip_id": dedicated_ip_id,
                    "weight": weight,
                },
                ip_create_params.IPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPCreateResponse,
        )

    async def delete(
        self,
        ip_id: str,
        *,
        id: str,
        drain: bool | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Remove the dedicated IP from the pool.

        The IP is kept but carries no mail until
        added to a pool again. Removing the last IP requires `force=true` and
        `drain=true`.

        Args:
          drain: Set together with `force=true` to remove the last IP in the pool. Acknowledges
              that mail routed to the emptied pool is held until the pool has a sendable IP
              again.

          force: Set together with `drain=true` to remove the last IP in the pool. Either flag
              alone has no effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ip_id:
            raise ValueError(f"Expected a non-empty value for `ip_id` but received {ip_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/email/ip_pools/{id}/ips/{ip_id}", id=id, ip_id=ip_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "drain": drain,
                        "force": force,
                    },
                    ip_delete_params.IPDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class IPsResourceWithRawResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.create = to_raw_response_wrapper(
            ips.create,
        )
        self.delete = to_raw_response_wrapper(
            ips.delete,
        )


class AsyncIPsResourceWithRawResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.create = async_to_raw_response_wrapper(
            ips.create,
        )
        self.delete = async_to_raw_response_wrapper(
            ips.delete,
        )


class IPsResourceWithStreamingResponse:
    def __init__(self, ips: IPsResource) -> None:
        self._ips = ips

        self.create = to_streamed_response_wrapper(
            ips.create,
        )
        self.delete = to_streamed_response_wrapper(
            ips.delete,
        )


class AsyncIPsResourceWithStreamingResponse:
    def __init__(self, ips: AsyncIPsResource) -> None:
        self._ips = ips

        self.create = async_to_streamed_response_wrapper(
            ips.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            ips.delete,
        )
