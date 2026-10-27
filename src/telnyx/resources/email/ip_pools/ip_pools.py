# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .ips import (
    IPsResource,
    AsyncIPsResource,
    IPsResourceWithRawResponse,
    AsyncIPsResourceWithRawResponse,
    IPsResourceWithStreamingResponse,
    AsyncIPsResourceWithStreamingResponse,
)
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
from ....types.email import ip_pool_create_params, ip_pool_delete_params, ip_pool_update_params
from ...._base_client import make_request_options
from ....types.email.ip_pool_list_response import IPPoolListResponse
from ....types.email.ip_pool_show_response import IPPoolShowResponse

__all__ = ["IPPoolsResource", "AsyncIPPoolsResource"]


class IPPoolsResource(SyncAPIResource):
    """Group dedicated IPs into pools for sending."""

    @cached_property
    def ips(self) -> IPsResource:
        """Group dedicated IPs into pools for sending."""
        return IPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IPPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return IPPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return IPPoolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        domain_id: str | Omit = omit,
        is_default: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPPoolShowResponse:
        """Create an account-scoped pool of dedicated IPs.

        Set `is_default` or `domain_id`
        for the pool to carry mail; a pool with neither carries none.

        Args:
          name: Pool name: 1-64 characters of lowercase letters, digits, `.`, `_`, and `-`,
              starting and ending with a letter or digit. Must be unique within the account
              and must not start with `dip_`.

          domain_id: Scope the pool to one of the account's email domains; the pool then carries that
              domain's mail. Scope at most one pool to each domain.

          is_default: Make this the account's default pool, which carries mail for sending domains
              without a domain-scoped pool. An account can have one default pool. Defaults to
              `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/email/ip_pools",
            body=maybe_transform(
                {
                    "name": name,
                    "domain_id": domain_id,
                    "is_default": is_default,
                },
                ip_pool_create_params.IPPoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolShowResponse,
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
    ) -> IPPoolShowResponse:
        """
        Retrieve a single IP pool by its identifier, including its dedicated-IP members
        with billing state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email/ip_pools/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolShowResponse,
        )

    def update(
        self,
        id: str,
        *,
        domain_id: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPPoolShowResponse:
        """
        Rename the pool, set or clear the default flag, or change its domain scope.
        Routing follows the new settings for subsequent mail.

        Args:
          domain_id: Scope the pool to one of the account's email domains, or `null` to remove the
              scope.

          is_default: Set or clear the account default flag. An account can have one default pool.

          name: Pool name: 1-64 characters of lowercase letters, digits, `.`, `_`, and `-`,
              starting and ending with a letter or digit. Must be unique within the account
              and must not start with `dip_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/email/ip_pools/{id}", id=id),
            body=maybe_transform(
                {
                    "domain_id": domain_id,
                    "is_default": is_default,
                    "name": name,
                },
                ip_pool_update_params.IPPoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolShowResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPPoolListResponse:
        """List the account's dedicated-IP pools.

        Member IPs are not included (`ips` is
        empty); retrieve a pool to see its members.
        """
        return self._get(
            "/email/ip_pools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        drain: bool | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the pool.

        Member IPs are kept but leave the pool, so they carry no mail
        until added to another pool. Deleting a pool changes routing for subsequently
        resolved messages. It does not reroute messages already assigned to the deleted
        pool. Deleting a pool that still has IPs requires `force=true` and `drain=true`.

        Args:
          drain: Set together with `force=true` to delete a pool that still has IPs. Acknowledges
              deletion while the pool still has members; this flag does not reroute already
              queued messages.

          force: Set together with `drain=true` to delete a pool that still has IPs. Either flag
              alone has no effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/email/ip_pools/{id}", id=id),
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
                    ip_pool_delete_params.IPPoolDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncIPPoolsResource(AsyncAPIResource):
    """Group dedicated IPs into pools for sending."""

    @cached_property
    def ips(self) -> AsyncIPsResource:
        """Group dedicated IPs into pools for sending."""
        return AsyncIPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIPPoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPPoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPPoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncIPPoolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        domain_id: str | Omit = omit,
        is_default: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPPoolShowResponse:
        """Create an account-scoped pool of dedicated IPs.

        Set `is_default` or `domain_id`
        for the pool to carry mail; a pool with neither carries none.

        Args:
          name: Pool name: 1-64 characters of lowercase letters, digits, `.`, `_`, and `-`,
              starting and ending with a letter or digit. Must be unique within the account
              and must not start with `dip_`.

          domain_id: Scope the pool to one of the account's email domains; the pool then carries that
              domain's mail. Scope at most one pool to each domain.

          is_default: Make this the account's default pool, which carries mail for sending domains
              without a domain-scoped pool. An account can have one default pool. Defaults to
              `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/email/ip_pools",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "domain_id": domain_id,
                    "is_default": is_default,
                },
                ip_pool_create_params.IPPoolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolShowResponse,
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
    ) -> IPPoolShowResponse:
        """
        Retrieve a single IP pool by its identifier, including its dedicated-IP members
        with billing state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email/ip_pools/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolShowResponse,
        )

    async def update(
        self,
        id: str,
        *,
        domain_id: Optional[str] | Omit = omit,
        is_default: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPPoolShowResponse:
        """
        Rename the pool, set or clear the default flag, or change its domain scope.
        Routing follows the new settings for subsequent mail.

        Args:
          domain_id: Scope the pool to one of the account's email domains, or `null` to remove the
              scope.

          is_default: Set or clear the account default flag. An account can have one default pool.

          name: Pool name: 1-64 characters of lowercase letters, digits, `.`, `_`, and `-`,
              starting and ending with a letter or digit. Must be unique within the account
              and must not start with `dip_`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/email/ip_pools/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "domain_id": domain_id,
                    "is_default": is_default,
                    "name": name,
                },
                ip_pool_update_params.IPPoolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolShowResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPPoolListResponse:
        """List the account's dedicated-IP pools.

        Member IPs are not included (`ips` is
        empty); retrieve a pool to see its members.
        """
        return await self._get(
            "/email/ip_pools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPPoolListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        drain: bool | Omit = omit,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the pool.

        Member IPs are kept but leave the pool, so they carry no mail
        until added to another pool. Deleting a pool changes routing for subsequently
        resolved messages. It does not reroute messages already assigned to the deleted
        pool. Deleting a pool that still has IPs requires `force=true` and `drain=true`.

        Args:
          drain: Set together with `force=true` to delete a pool that still has IPs. Acknowledges
              deletion while the pool still has members; this flag does not reroute already
              queued messages.

          force: Set together with `drain=true` to delete a pool that still has IPs. Either flag
              alone has no effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/email/ip_pools/{id}", id=id),
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
                    ip_pool_delete_params.IPPoolDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class IPPoolsResourceWithRawResponse:
    def __init__(self, ip_pools: IPPoolsResource) -> None:
        self._ip_pools = ip_pools

        self.create = to_raw_response_wrapper(
            ip_pools.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ip_pools.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ip_pools.update,
        )
        self.list = to_raw_response_wrapper(
            ip_pools.list,
        )
        self.delete = to_raw_response_wrapper(
            ip_pools.delete,
        )

    @cached_property
    def ips(self) -> IPsResourceWithRawResponse:
        """Group dedicated IPs into pools for sending."""
        return IPsResourceWithRawResponse(self._ip_pools.ips)


class AsyncIPPoolsResourceWithRawResponse:
    def __init__(self, ip_pools: AsyncIPPoolsResource) -> None:
        self._ip_pools = ip_pools

        self.create = async_to_raw_response_wrapper(
            ip_pools.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ip_pools.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ip_pools.update,
        )
        self.list = async_to_raw_response_wrapper(
            ip_pools.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ip_pools.delete,
        )

    @cached_property
    def ips(self) -> AsyncIPsResourceWithRawResponse:
        """Group dedicated IPs into pools for sending."""
        return AsyncIPsResourceWithRawResponse(self._ip_pools.ips)


class IPPoolsResourceWithStreamingResponse:
    def __init__(self, ip_pools: IPPoolsResource) -> None:
        self._ip_pools = ip_pools

        self.create = to_streamed_response_wrapper(
            ip_pools.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ip_pools.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ip_pools.update,
        )
        self.list = to_streamed_response_wrapper(
            ip_pools.list,
        )
        self.delete = to_streamed_response_wrapper(
            ip_pools.delete,
        )

    @cached_property
    def ips(self) -> IPsResourceWithStreamingResponse:
        """Group dedicated IPs into pools for sending."""
        return IPsResourceWithStreamingResponse(self._ip_pools.ips)


class AsyncIPPoolsResourceWithStreamingResponse:
    def __init__(self, ip_pools: AsyncIPPoolsResource) -> None:
        self._ip_pools = ip_pools

        self.create = async_to_streamed_response_wrapper(
            ip_pools.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ip_pools.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ip_pools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ip_pools.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ip_pools.delete,
        )

    @cached_property
    def ips(self) -> AsyncIPsResourceWithStreamingResponse:
        """Group dedicated IPs into pools for sending."""
        return AsyncIPsResourceWithStreamingResponse(self._ip_pools.ips)
