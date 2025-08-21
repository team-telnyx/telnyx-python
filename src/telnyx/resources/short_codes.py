# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import short_code_list_params, short_code_update_params
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
from ..types.short_code_list_response import ShortCodeListResponse
from ..types.short_code_update_response import ShortCodeUpdateResponse
from ..types.short_code_retrieve_response import ShortCodeRetrieveResponse

__all__ = ["ShortCodesResource", "AsyncShortCodesResource"]


class ShortCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShortCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ShortCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShortCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ShortCodesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShortCodeRetrieveResponse:
        """
        Retrieve a short code

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/short_codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShortCodeRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        messaging_profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShortCodeUpdateResponse:
        """Update the settings for a specific short code.

        To unbind a short code from a
        profile, set the `messaging_profile_id` to `null` or an empty string.

        Args:
          messaging_profile_id: Unique identifier for a messaging profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/short_codes/{id}",
            body=maybe_transform(
                {"messaging_profile_id": messaging_profile_id}, short_code_update_params.ShortCodeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShortCodeUpdateResponse,
        )

    def list(
        self,
        *,
        filter: short_code_list_params.Filter | NotGiven = NOT_GIVEN,
        page: short_code_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShortCodeListResponse:
        """
        List short codes

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[messaging_profile_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/short_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    short_code_list_params.ShortCodeListParams,
                ),
            ),
            cast_to=ShortCodeListResponse,
        )


class AsyncShortCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShortCodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShortCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShortCodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncShortCodesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShortCodeRetrieveResponse:
        """
        Retrieve a short code

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/short_codes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShortCodeRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        messaging_profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShortCodeUpdateResponse:
        """Update the settings for a specific short code.

        To unbind a short code from a
        profile, set the `messaging_profile_id` to `null` or an empty string.

        Args:
          messaging_profile_id: Unique identifier for a messaging profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/short_codes/{id}",
            body=await async_maybe_transform(
                {"messaging_profile_id": messaging_profile_id}, short_code_update_params.ShortCodeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShortCodeUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: short_code_list_params.Filter | NotGiven = NOT_GIVEN,
        page: short_code_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShortCodeListResponse:
        """
        List short codes

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[messaging_profile_id]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/short_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    short_code_list_params.ShortCodeListParams,
                ),
            ),
            cast_to=ShortCodeListResponse,
        )


class ShortCodesResourceWithRawResponse:
    def __init__(self, short_codes: ShortCodesResource) -> None:
        self._short_codes = short_codes

        self.retrieve = to_raw_response_wrapper(
            short_codes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            short_codes.update,
        )
        self.list = to_raw_response_wrapper(
            short_codes.list,
        )


class AsyncShortCodesResourceWithRawResponse:
    def __init__(self, short_codes: AsyncShortCodesResource) -> None:
        self._short_codes = short_codes

        self.retrieve = async_to_raw_response_wrapper(
            short_codes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            short_codes.update,
        )
        self.list = async_to_raw_response_wrapper(
            short_codes.list,
        )


class ShortCodesResourceWithStreamingResponse:
    def __init__(self, short_codes: ShortCodesResource) -> None:
        self._short_codes = short_codes

        self.retrieve = to_streamed_response_wrapper(
            short_codes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            short_codes.update,
        )
        self.list = to_streamed_response_wrapper(
            short_codes.list,
        )


class AsyncShortCodesResourceWithStreamingResponse:
    def __init__(self, short_codes: AsyncShortCodesResource) -> None:
        self._short_codes = short_codes

        self.retrieve = async_to_streamed_response_wrapper(
            short_codes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            short_codes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            short_codes.list,
        )
