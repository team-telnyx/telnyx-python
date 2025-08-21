# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.texml.accounts.calls import siprec_siprec_sid_json_params
from .....types.texml.accounts.calls.siprec_siprec_sid_json_response import SiprecSiprecSidJsonResponse

__all__ = ["SiprecResource", "AsyncSiprecResource"]


class SiprecResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SiprecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SiprecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SiprecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SiprecResourceWithStreamingResponse(self)

    def siprec_sid_json(
        self,
        siprec_sid: str,
        *,
        account_sid: str,
        call_sid: str,
        status: Literal["stopped"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecSiprecSidJsonResponse:
        """
        Updates siprec session identified by siprec_sid.

        Args:
          status: The new status of the resource. Specifying `stopped` will end the siprec
              session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        if not siprec_sid:
            raise ValueError(f"Expected a non-empty value for `siprec_sid` but received {siprec_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{siprec_sid}.json",
            body=maybe_transform({"status": status}, siprec_siprec_sid_json_params.SiprecSiprecSidJsonParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecSiprecSidJsonResponse,
        )


class AsyncSiprecResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSiprecResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSiprecResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSiprecResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSiprecResourceWithStreamingResponse(self)

    async def siprec_sid_json(
        self,
        siprec_sid: str,
        *,
        account_sid: str,
        call_sid: str,
        status: Literal["stopped"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SiprecSiprecSidJsonResponse:
        """
        Updates siprec session identified by siprec_sid.

        Args:
          status: The new status of the resource. Specifying `stopped` will end the siprec
              session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not call_sid:
            raise ValueError(f"Expected a non-empty value for `call_sid` but received {call_sid!r}")
        if not siprec_sid:
            raise ValueError(f"Expected a non-empty value for `siprec_sid` but received {siprec_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{siprec_sid}.json",
            body=await async_maybe_transform(
                {"status": status}, siprec_siprec_sid_json_params.SiprecSiprecSidJsonParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SiprecSiprecSidJsonResponse,
        )


class SiprecResourceWithRawResponse:
    def __init__(self, siprec: SiprecResource) -> None:
        self._siprec = siprec

        self.siprec_sid_json = to_raw_response_wrapper(
            siprec.siprec_sid_json,
        )


class AsyncSiprecResourceWithRawResponse:
    def __init__(self, siprec: AsyncSiprecResource) -> None:
        self._siprec = siprec

        self.siprec_sid_json = async_to_raw_response_wrapper(
            siprec.siprec_sid_json,
        )


class SiprecResourceWithStreamingResponse:
    def __init__(self, siprec: SiprecResource) -> None:
        self._siprec = siprec

        self.siprec_sid_json = to_streamed_response_wrapper(
            siprec.siprec_sid_json,
        )


class AsyncSiprecResourceWithStreamingResponse:
    def __init__(self, siprec: AsyncSiprecResource) -> None:
        self._siprec = siprec

        self.siprec_sid_json = async_to_streamed_response_wrapper(
            siprec.siprec_sid_json,
        )
