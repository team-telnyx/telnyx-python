# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.terms_of_service.branded_calling_agree_response import BrandedCallingAgreeResponse

__all__ = ["BrandedCallingResource", "AsyncBrandedCallingResource"]


class BrandedCallingResource(SyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def with_raw_response(self) -> BrandedCallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BrandedCallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandedCallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BrandedCallingResourceWithStreamingResponse(self)

    def agree(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandedCallingAgreeResponse:
        """
        Records the authenticated user's agreement to the current Branded Calling ToS.
        No body required. Idempotent - re-calling after agreement is a no-op and returns
        the existing agreement.

        This is a prerequisite for activating Branded Calling on any enterprise
        (`POST /enterprises/{id}/branded_calling`); without an agreement, activation
        returns `403`.
        """
        return self._post(
            "/terms_of_service/branded_calling/agree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandedCallingAgreeResponse,
        )


class AsyncBrandedCallingResource(AsyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBrandedCallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandedCallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandedCallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBrandedCallingResourceWithStreamingResponse(self)

    async def agree(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandedCallingAgreeResponse:
        """
        Records the authenticated user's agreement to the current Branded Calling ToS.
        No body required. Idempotent - re-calling after agreement is a no-op and returns
        the existing agreement.

        This is a prerequisite for activating Branded Calling on any enterprise
        (`POST /enterprises/{id}/branded_calling`); without an agreement, activation
        returns `403`.
        """
        return await self._post(
            "/terms_of_service/branded_calling/agree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandedCallingAgreeResponse,
        )


class BrandedCallingResourceWithRawResponse:
    def __init__(self, branded_calling: BrandedCallingResource) -> None:
        self._branded_calling = branded_calling

        self.agree = to_raw_response_wrapper(
            branded_calling.agree,
        )


class AsyncBrandedCallingResourceWithRawResponse:
    def __init__(self, branded_calling: AsyncBrandedCallingResource) -> None:
        self._branded_calling = branded_calling

        self.agree = async_to_raw_response_wrapper(
            branded_calling.agree,
        )


class BrandedCallingResourceWithStreamingResponse:
    def __init__(self, branded_calling: BrandedCallingResource) -> None:
        self._branded_calling = branded_calling

        self.agree = to_streamed_response_wrapper(
            branded_calling.agree,
        )


class AsyncBrandedCallingResourceWithStreamingResponse:
    def __init__(self, branded_calling: AsyncBrandedCallingResource) -> None:
        self._branded_calling = branded_calling

        self.agree = async_to_streamed_response_wrapper(
            branded_calling.agree,
        )
