# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.verifications.by_phone_number_list_response import ByPhoneNumberListResponse

__all__ = ["ByPhoneNumberResource", "AsyncByPhoneNumberResource"]


class ByPhoneNumberResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ByPhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ByPhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByPhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ByPhoneNumberResourceWithStreamingResponse(self)

    def list(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByPhoneNumberListResponse:
        """
        List verifications by phone number

        Args:
          phone_number: +E164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/verifications/by_phone_number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByPhoneNumberListResponse,
        )


class AsyncByPhoneNumberResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncByPhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncByPhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByPhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncByPhoneNumberResourceWithStreamingResponse(self)

    async def list(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByPhoneNumberListResponse:
        """
        List verifications by phone number

        Args:
          phone_number: +E164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/verifications/by_phone_number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByPhoneNumberListResponse,
        )


class ByPhoneNumberResourceWithRawResponse:
    def __init__(self, by_phone_number: ByPhoneNumberResource) -> None:
        self._by_phone_number = by_phone_number

        self.list = to_raw_response_wrapper(
            by_phone_number.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._by_phone_number.actions)


class AsyncByPhoneNumberResourceWithRawResponse:
    def __init__(self, by_phone_number: AsyncByPhoneNumberResource) -> None:
        self._by_phone_number = by_phone_number

        self.list = async_to_raw_response_wrapper(
            by_phone_number.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._by_phone_number.actions)


class ByPhoneNumberResourceWithStreamingResponse:
    def __init__(self, by_phone_number: ByPhoneNumberResource) -> None:
        self._by_phone_number = by_phone_number

        self.list = to_streamed_response_wrapper(
            by_phone_number.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._by_phone_number.actions)


class AsyncByPhoneNumberResourceWithStreamingResponse:
    def __init__(self, by_phone_number: AsyncByPhoneNumberResource) -> None:
        self._by_phone_number = by_phone_number

        self.list = async_to_streamed_response_wrapper(
            by_phone_number.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._by_phone_number.actions)
