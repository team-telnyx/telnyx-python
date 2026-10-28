# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.email.dedicated_ip_show_response import DedicatedIPShowResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """
    Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
    """

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def complete_warmup(
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
        Manually complete the warm-up ramp (`warming_up` to `active`), bypassing the
        schedule. Use only for an IP already warmed elsewhere. Completion sets
        `warmup.progress` to `100`, clears `warmup.daily_cap`, and applies the
        ramp-complete allowance to the current UTC day: `warmup.today.cap` becomes
        `100000000`, `warmup.today.granted` keeps the sends already released today, and
        `warmup.today.remaining` becomes `cap` minus `granted`. Once completion applies
        this allowance, an exhausted stage allowance does not block the next eligible
        first-attempt send. The response reports these values. On an `active` IP,
        `warmup.progress` and `warmup.daily_cap` are informational: they can keep
        earlier values after a suspension is lifted and do not limit sending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email/dedicated_ips/{id}/actions/complete_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    def pause_warmup(
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
        """Pause the warm-up ramp at its current stage.

        While paused, the IP releases no
        first-attempt sends from hold and the ramp does not advance. Only a `warming_up`
        IP can be paused; pausing an already paused IP refreshes `paused_at`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email/dedicated_ips/{id}/actions/pause_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    def resume_warmup(
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
        """Resume a paused warm-up ramp from its held stage.

        Only a `warming_up` IP can be
        resumed; resuming a ramp that is not paused returns the IP unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email/dedicated_ips/{id}/actions/resume_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    def start_warmup(
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
        """Start the warm-up ramp (`provisioning` to `warming_up`).

        The ramp never starts
        automatically. Only a `provisioning` IP can be started; a `suspended` IP returns
        `409`. Starting does not check DNS: the IP carries mail only while
        `dns_confirmed_at` is set and the IP is in a pool that routes mail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email/dedicated_ips/{id}/actions/start_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    """
    Purchase and manage dedicated sending IP addresses for your Telnyx email traffic.
    """

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def complete_warmup(
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
        Manually complete the warm-up ramp (`warming_up` to `active`), bypassing the
        schedule. Use only for an IP already warmed elsewhere. Completion sets
        `warmup.progress` to `100`, clears `warmup.daily_cap`, and applies the
        ramp-complete allowance to the current UTC day: `warmup.today.cap` becomes
        `100000000`, `warmup.today.granted` keeps the sends already released today, and
        `warmup.today.remaining` becomes `cap` minus `granted`. Once completion applies
        this allowance, an exhausted stage allowance does not block the next eligible
        first-attempt send. The response reports these values. On an `active` IP,
        `warmup.progress` and `warmup.daily_cap` are informational: they can keep
        earlier values after a suspension is lifted and do not limit sending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email/dedicated_ips/{id}/actions/complete_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    async def pause_warmup(
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
        """Pause the warm-up ramp at its current stage.

        While paused, the IP releases no
        first-attempt sends from hold and the ramp does not advance. Only a `warming_up`
        IP can be paused; pausing an already paused IP refreshes `paused_at`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email/dedicated_ips/{id}/actions/pause_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    async def resume_warmup(
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
        """Resume a paused warm-up ramp from its held stage.

        Only a `warming_up` IP can be
        resumed; resuming a ramp that is not paused returns the IP unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email/dedicated_ips/{id}/actions/resume_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )

    async def start_warmup(
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
        """Start the warm-up ramp (`provisioning` to `warming_up`).

        The ramp never starts
        automatically. Only a `provisioning` IP can be started; a `suspended` IP returns
        `409`. Starting does not check DNS: the IP carries mail only while
        `dns_confirmed_at` is set and the IP is in a pool that routes mail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email/dedicated_ips/{id}/actions/start_warmup", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DedicatedIPShowResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.complete_warmup = to_raw_response_wrapper(
            actions.complete_warmup,
        )
        self.pause_warmup = to_raw_response_wrapper(
            actions.pause_warmup,
        )
        self.resume_warmup = to_raw_response_wrapper(
            actions.resume_warmup,
        )
        self.start_warmup = to_raw_response_wrapper(
            actions.start_warmup,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.complete_warmup = async_to_raw_response_wrapper(
            actions.complete_warmup,
        )
        self.pause_warmup = async_to_raw_response_wrapper(
            actions.pause_warmup,
        )
        self.resume_warmup = async_to_raw_response_wrapper(
            actions.resume_warmup,
        )
        self.start_warmup = async_to_raw_response_wrapper(
            actions.start_warmup,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.complete_warmup = to_streamed_response_wrapper(
            actions.complete_warmup,
        )
        self.pause_warmup = to_streamed_response_wrapper(
            actions.pause_warmup,
        )
        self.resume_warmup = to_streamed_response_wrapper(
            actions.resume_warmup,
        )
        self.start_warmup = to_streamed_response_wrapper(
            actions.start_warmup,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.complete_warmup = async_to_streamed_response_wrapper(
            actions.complete_warmup,
        )
        self.pause_warmup = async_to_streamed_response_wrapper(
            actions.pause_warmup,
        )
        self.resume_warmup = async_to_streamed_response_wrapper(
            actions.resume_warmup,
        )
        self.start_warmup = async_to_streamed_response_wrapper(
            actions.start_warmup,
        )
