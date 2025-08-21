# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import portability_check_run_params
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
from ..types.portability_check_run_response import PortabilityCheckRunResponse

__all__ = ["PortabilityChecksResource", "AsyncPortabilityChecksResource"]


class PortabilityChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortabilityChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PortabilityChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortabilityChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PortabilityChecksResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        phone_numbers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortabilityCheckRunResponse:
        """
        Runs a portability check, returning the results immediately.

        Args:
          phone_numbers: The list of +E.164 formatted phone numbers to check for portability

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/portability_checks",
            body=maybe_transform(
                {"phone_numbers": phone_numbers}, portability_check_run_params.PortabilityCheckRunParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortabilityCheckRunResponse,
        )


class AsyncPortabilityChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortabilityChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortabilityChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortabilityChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPortabilityChecksResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        phone_numbers: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortabilityCheckRunResponse:
        """
        Runs a portability check, returning the results immediately.

        Args:
          phone_numbers: The list of +E.164 formatted phone numbers to check for portability

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/portability_checks",
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, portability_check_run_params.PortabilityCheckRunParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortabilityCheckRunResponse,
        )


class PortabilityChecksResourceWithRawResponse:
    def __init__(self, portability_checks: PortabilityChecksResource) -> None:
        self._portability_checks = portability_checks

        self.run = to_raw_response_wrapper(
            portability_checks.run,
        )


class AsyncPortabilityChecksResourceWithRawResponse:
    def __init__(self, portability_checks: AsyncPortabilityChecksResource) -> None:
        self._portability_checks = portability_checks

        self.run = async_to_raw_response_wrapper(
            portability_checks.run,
        )


class PortabilityChecksResourceWithStreamingResponse:
    def __init__(self, portability_checks: PortabilityChecksResource) -> None:
        self._portability_checks = portability_checks

        self.run = to_streamed_response_wrapper(
            portability_checks.run,
        )


class AsyncPortabilityChecksResourceWithStreamingResponse:
    def __init__(self, portability_checks: AsyncPortabilityChecksResource) -> None:
        self._portability_checks = portability_checks

        self.run = async_to_streamed_response_wrapper(
            portability_checks.run,
        )
