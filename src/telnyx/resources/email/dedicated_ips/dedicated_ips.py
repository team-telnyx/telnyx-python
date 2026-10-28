# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.email import (
    dedicated_ip_list_params,
    dedicated_ip_create_params,
    dedicated_ip_delete_params,
    dedicated_ip_update_params,
)
from ...._base_client import make_request_options
from ....types.email.dedicated_ip_list_response import DedicatedIPListResponse
from ....types.email.dedicated_ip_show_response import DedicatedIPShowResponse

__all__ = ["DedicatedIPsResource", "AsyncDedicatedIPsResource"]


class DedicatedIPsResource(SyncAPIResource):
    """
    Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
    """

    @cached_property
    def actions(self) -> ActionsResource:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DedicatedIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DedicatedIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DedicatedIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DedicatedIPsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        idempotency_key: str,
        ip_version: Literal["ipv4"] | Omit = omit,
        region: Literal["ewr-nj1"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPShowResponse:
        """Purchase a dedicated sending IP.

        Requires a verified, enterprise, or legacy
        account, and an `Idempotency-Key` header: a request without the header returns
        `400` (code `10015`) and allocates nothing. Telnyx allocates the next available
        IP from stock. The optional `region` and `ip_version` fields each restrict which
        stock IP is allocated; they never change the allocated IP's metadata. An omitted
        field applies no restriction for that field, and omitting the body applies
        neither restriction. An unsupported selector value returns `422`; a supported
        value that matches no available IP returns `429` and records the request on the
        waitlist. Billing: $14/month/IP, charged as a monthly recurring charge (MRC)
        from purchase. The IP is returned in `provisioning` status with a Telnyx-managed
        PTR hostname and carries no mail until you call `start_warmup` and add it to a
        pool that routes mail.

        Args:
          ip_version: Allocate an IP of this address family. Supported value: `ipv4`. Any other value,
              including `ipv6` or `null`, returns `422`.

          region: Allocate an IP in this region. Supported value: `ewr-nj1`. Any other value,
              including an empty string or `null`, returns `422`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/email/dedicated_ips",
            body=maybe_transform(
                {
                    "ip_version": ip_version,
                    "region": region,
                },
                dedicated_ip_create_params.DedicatedIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
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
    ) -> DedicatedIPShowResponse:
        """
        Retrieve a single dedicated IP by its identifier, including warm-up state,
        billing state, and the DNS/PTR provisioning checklist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email/dedicated_ips/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    def update(
        self,
        id: str,
        *,
        drain: bool | Omit = omit,
        force: bool | Omit = omit,
        pool_id: str | Omit = omit,
        warmup: dedicated_ip_update_params.Warmup | Omit = omit,
        warmup_paused: bool | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPShowResponse:
        """Move the IP to another pool, or pause/resume its warm-up ramp.

        One change
        applies per request. `pool_id` takes precedence over warm-up changes. Otherwise,
        use `warmup_paused` or `warmup.paused`; a Boolean `warmup_paused` takes
        precedence. Moving the last IP out of a pool requires `force: true` and
        `drain: true`. The PTR hostname is managed by Telnyx: a request that includes
        `ptr_hostname` returns `422` unless `pool_id` or a warm-up field is present, in
        which case `ptr_hostname` is ignored.

        Args:
          drain: Set together with `force: true` to move the last IP out of its current pool.
              Acknowledges that mail routed to the emptied pool is held. Used only with
              `pool_id`.

          force: Set together with `drain: true` to move the last IP out of its current pool.
              Used only with `pool_id`.

          pool_id: Move the IP to this pool, replacing its current membership. Use the IP's current
              pool to change only its weight. To take an IP out of a pool, use
              `DELETE /email/ip_pools/{id}/ips/{ip_id}`.

          warmup: Alias for `warmup_paused`.

          warmup_paused: Pause (`true`) or resume (`false`) the warm-up ramp; equivalent to the
              `pause_warmup` and `resume_warmup` actions. A Boolean value takes precedence
              over `warmup.paused`. When a pause field is present and `pool_id` is absent,
              supplying neither pause field as a Boolean invokes resume.

          weight: Routing weight in the target pool. Used only with `pool_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/email/dedicated_ips/{id}", id=id),
            body=maybe_transform(
                {
                    "drain": drain,
                    "force": force,
                    "pool_id": pool_id,
                    "warmup": warmup,
                    "warmup_paused": warmup_paused,
                    "weight": weight,
                },
                dedicated_ip_update_params.DedicatedIPUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    def list(
        self,
        *,
        filter_pool_id: str | Omit = omit,
        filter_region: str | Omit = omit,
        filter_status: Literal["provisioning", "warming_up", "active", "suspended", "released"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPListResponse:
        """List the dedicated sending IPs owned by the account, newest first.

        Narrow the
        list with `filter[status]`, `filter[pool_id]`, and `filter[region]`; supplied
        filters combine, so an IP must match every one. An empty value, or a nested or
        array value such as `filter[status][]=active`, applies no filter, and other
        `filter[...]` keys are ignored. A value that no IP can match (an unknown status,
        a `pool_id` that is not a UUID, or a value containing a NUL byte) returns an
        empty list, not an error.

        Args:
          filter_pool_id: Return only IPs in this pool (exact match on `pool_id`). A value that is not a
              UUID returns an empty list. An empty value applies no filter.

          filter_region: Return only IPs in this region (exact, case-sensitive match on `region`). An
              empty value applies no filter.

          filter_status: Return only IPs in this lifecycle status (exact match). Any other value returns
              an empty list. An empty value applies no filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/email/dedicated_ips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_pool_id": filter_pool_id,
                        "filter_region": filter_region,
                        "filter_status": filter_status,
                    },
                    dedicated_ip_list_params.DedicatedIPListParams,
                ),
            ),
            cast_to=DedicatedIPListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        query_drain: bool | Omit = omit,
        query_force: bool | Omit = omit,
        query_reason: str | Omit = omit,
        body_drain: bool | Omit = omit,
        body_force: bool | Omit = omit,
        body_reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPShowResponse:
        """Release the dedicated IP to Telnyx.

        The IP stops carrying mail immediately,
        leaves its pool, and moves to `released`. Telnyx sets `quarantine_until` to 30
        days after release. Release requests that the MRC stop asynchronously. Check
        `billing`: `stopping` means the stop is pending, `stopped` means it completed,
        and `stop_failed` means the charge remains. If the charge was never created or
        its creation has not completed, `billing` keeps showing the creation status
        (`not_started`, `pending`, `in_progress`, or `failed`). Any status except
        `released` can be released. Releasing the last IP in a pool requires
        `force=true` and `drain=true`.

        Args:
          query_drain: Set together with `force=true` to release the last IP in a pool. Acknowledges
              that mail routed to the emptied pool is held until the pool has a sendable IP
              again. Also accepted in the JSON body.

          query_force: Set together with `drain=true` to release the last IP in a pool. Either flag
              alone has no effect. Also accepted in the JSON body.

          query_reason: Free-text reason recorded with the release. Also accepted in the JSON body.

          body_drain: Set together with `force: true` to release the last IP in a pool. Acknowledges
              that mail routed to the emptied pool is held until the pool has a sendable IP
              again.

          body_force: Set together with `drain: true` to release the last IP in a pool. Either flag
              alone has no effect.

          body_reason: Free-text reason recorded with the release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/email/dedicated_ips/{id}", id=id),
            body=maybe_transform(
                {
                    "body_drain": body_drain,
                    "body_force": body_force,
                    "body_reason": body_reason,
                },
                dedicated_ip_delete_params.DedicatedIPDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query_drain": query_drain,
                        "query_force": query_force,
                        "query_reason": query_reason,
                    },
                    dedicated_ip_delete_params.DedicatedIPDeleteParams,
                ),
            ),
            cast_to=DedicatedIPShowResponse,
        )


class AsyncDedicatedIPsResource(AsyncAPIResource):
    """
    Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
    """

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDedicatedIPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDedicatedIPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDedicatedIPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDedicatedIPsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        idempotency_key: str,
        ip_version: Literal["ipv4"] | Omit = omit,
        region: Literal["ewr-nj1"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPShowResponse:
        """Purchase a dedicated sending IP.

        Requires a verified, enterprise, or legacy
        account, and an `Idempotency-Key` header: a request without the header returns
        `400` (code `10015`) and allocates nothing. Telnyx allocates the next available
        IP from stock. The optional `region` and `ip_version` fields each restrict which
        stock IP is allocated; they never change the allocated IP's metadata. An omitted
        field applies no restriction for that field, and omitting the body applies
        neither restriction. An unsupported selector value returns `422`; a supported
        value that matches no available IP returns `429` and records the request on the
        waitlist. Billing: $14/month/IP, charged as a monthly recurring charge (MRC)
        from purchase. The IP is returned in `provisioning` status with a Telnyx-managed
        PTR hostname and carries no mail until you call `start_warmup` and add it to a
        pool that routes mail.

        Args:
          ip_version: Allocate an IP of this address family. Supported value: `ipv4`. Any other value,
              including `ipv6` or `null`, returns `422`.

          region: Allocate an IP in this region. Supported value: `ewr-nj1`. Any other value,
              including an empty string or `null`, returns `422`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/email/dedicated_ips",
            body=await async_maybe_transform(
                {
                    "ip_version": ip_version,
                    "region": region,
                },
                dedicated_ip_create_params.DedicatedIPCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
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
    ) -> DedicatedIPShowResponse:
        """
        Retrieve a single dedicated IP by its identifier, including warm-up state,
        billing state, and the DNS/PTR provisioning checklist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email/dedicated_ips/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    async def update(
        self,
        id: str,
        *,
        drain: bool | Omit = omit,
        force: bool | Omit = omit,
        pool_id: str | Omit = omit,
        warmup: dedicated_ip_update_params.Warmup | Omit = omit,
        warmup_paused: bool | Omit = omit,
        weight: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPShowResponse:
        """Move the IP to another pool, or pause/resume its warm-up ramp.

        One change
        applies per request. `pool_id` takes precedence over warm-up changes. Otherwise,
        use `warmup_paused` or `warmup.paused`; a Boolean `warmup_paused` takes
        precedence. Moving the last IP out of a pool requires `force: true` and
        `drain: true`. The PTR hostname is managed by Telnyx: a request that includes
        `ptr_hostname` returns `422` unless `pool_id` or a warm-up field is present, in
        which case `ptr_hostname` is ignored.

        Args:
          drain: Set together with `force: true` to move the last IP out of its current pool.
              Acknowledges that mail routed to the emptied pool is held. Used only with
              `pool_id`.

          force: Set together with `drain: true` to move the last IP out of its current pool.
              Used only with `pool_id`.

          pool_id: Move the IP to this pool, replacing its current membership. Use the IP's current
              pool to change only its weight. To take an IP out of a pool, use
              `DELETE /email/ip_pools/{id}/ips/{ip_id}`.

          warmup: Alias for `warmup_paused`.

          warmup_paused: Pause (`true`) or resume (`false`) the warm-up ramp; equivalent to the
              `pause_warmup` and `resume_warmup` actions. A Boolean value takes precedence
              over `warmup.paused`. When a pause field is present and `pool_id` is absent,
              supplying neither pause field as a Boolean invokes resume.

          weight: Routing weight in the target pool. Used only with `pool_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/email/dedicated_ips/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "drain": drain,
                    "force": force,
                    "pool_id": pool_id,
                    "warmup": warmup,
                    "warmup_paused": warmup_paused,
                    "weight": weight,
                },
                dedicated_ip_update_params.DedicatedIPUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    async def list(
        self,
        *,
        filter_pool_id: str | Omit = omit,
        filter_region: str | Omit = omit,
        filter_status: Literal["provisioning", "warming_up", "active", "suspended", "released"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPListResponse:
        """List the dedicated sending IPs owned by the account, newest first.

        Narrow the
        list with `filter[status]`, `filter[pool_id]`, and `filter[region]`; supplied
        filters combine, so an IP must match every one. An empty value, or a nested or
        array value such as `filter[status][]=active`, applies no filter, and other
        `filter[...]` keys are ignored. A value that no IP can match (an unknown status,
        a `pool_id` that is not a UUID, or a value containing a NUL byte) returns an
        empty list, not an error.

        Args:
          filter_pool_id: Return only IPs in this pool (exact match on `pool_id`). A value that is not a
              UUID returns an empty list. An empty value applies no filter.

          filter_region: Return only IPs in this region (exact, case-sensitive match on `region`). An
              empty value applies no filter.

          filter_status: Return only IPs in this lifecycle status (exact match). Any other value returns
              an empty list. An empty value applies no filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/email/dedicated_ips",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_pool_id": filter_pool_id,
                        "filter_region": filter_region,
                        "filter_status": filter_status,
                    },
                    dedicated_ip_list_params.DedicatedIPListParams,
                ),
            ),
            cast_to=DedicatedIPListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        query_drain: bool | Omit = omit,
        query_force: bool | Omit = omit,
        query_reason: str | Omit = omit,
        body_drain: bool | Omit = omit,
        body_force: bool | Omit = omit,
        body_reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DedicatedIPShowResponse:
        """Release the dedicated IP to Telnyx.

        The IP stops carrying mail immediately,
        leaves its pool, and moves to `released`. Telnyx sets `quarantine_until` to 30
        days after release. Release requests that the MRC stop asynchronously. Check
        `billing`: `stopping` means the stop is pending, `stopped` means it completed,
        and `stop_failed` means the charge remains. If the charge was never created or
        its creation has not completed, `billing` keeps showing the creation status
        (`not_started`, `pending`, `in_progress`, or `failed`). Any status except
        `released` can be released. Releasing the last IP in a pool requires
        `force=true` and `drain=true`.

        Args:
          query_drain: Set together with `force=true` to release the last IP in a pool. Acknowledges
              that mail routed to the emptied pool is held until the pool has a sendable IP
              again. Also accepted in the JSON body.

          query_force: Set together with `drain=true` to release the last IP in a pool. Either flag
              alone has no effect. Also accepted in the JSON body.

          query_reason: Free-text reason recorded with the release. Also accepted in the JSON body.

          body_drain: Set together with `force: true` to release the last IP in a pool. Acknowledges
              that mail routed to the emptied pool is held until the pool has a sendable IP
              again.

          body_force: Set together with `drain: true` to release the last IP in a pool. Either flag
              alone has no effect.

          body_reason: Free-text reason recorded with the release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/email/dedicated_ips/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "body_drain": body_drain,
                    "body_force": body_force,
                    "body_reason": body_reason,
                },
                dedicated_ip_delete_params.DedicatedIPDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query_drain": query_drain,
                        "query_force": query_force,
                        "query_reason": query_reason,
                    },
                    dedicated_ip_delete_params.DedicatedIPDeleteParams,
                ),
            ),
            cast_to=DedicatedIPShowResponse,
        )


class DedicatedIPsResourceWithRawResponse:
    def __init__(self, dedicated_ips: DedicatedIPsResource) -> None:
        self._dedicated_ips = dedicated_ips

        self.create = to_raw_response_wrapper(
            dedicated_ips.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dedicated_ips.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dedicated_ips.update,
        )
        self.list = to_raw_response_wrapper(
            dedicated_ips.list,
        )
        self.delete = to_raw_response_wrapper(
            dedicated_ips.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return ActionsResourceWithRawResponse(self._dedicated_ips.actions)


class AsyncDedicatedIPsResourceWithRawResponse:
    def __init__(self, dedicated_ips: AsyncDedicatedIPsResource) -> None:
        self._dedicated_ips = dedicated_ips

        self.create = async_to_raw_response_wrapper(
            dedicated_ips.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dedicated_ips.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dedicated_ips.update,
        )
        self.list = async_to_raw_response_wrapper(
            dedicated_ips.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dedicated_ips.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return AsyncActionsResourceWithRawResponse(self._dedicated_ips.actions)


class DedicatedIPsResourceWithStreamingResponse:
    def __init__(self, dedicated_ips: DedicatedIPsResource) -> None:
        self._dedicated_ips = dedicated_ips

        self.create = to_streamed_response_wrapper(
            dedicated_ips.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dedicated_ips.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dedicated_ips.update,
        )
        self.list = to_streamed_response_wrapper(
            dedicated_ips.list,
        )
        self.delete = to_streamed_response_wrapper(
            dedicated_ips.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return ActionsResourceWithStreamingResponse(self._dedicated_ips.actions)


class AsyncDedicatedIPsResourceWithStreamingResponse:
    def __init__(self, dedicated_ips: AsyncDedicatedIPsResource) -> None:
        self._dedicated_ips = dedicated_ips

        self.create = async_to_streamed_response_wrapper(
            dedicated_ips.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dedicated_ips.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dedicated_ips.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dedicated_ips.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dedicated_ips.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
        """
        return AsyncActionsResourceWithStreamingResponse(self._dedicated_ips.actions)
