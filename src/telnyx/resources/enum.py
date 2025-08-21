# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.enum_retrieve_response import EnumRetrieveResponse

__all__ = ["EnumResource", "AsyncEnumResource"]


class EnumResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EnumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EnumResourceWithStreamingResponse(self)

    def retrieve(
        self,
        endpoint: Literal[
            "mno",
            "optionalAttributes",
            "usecase",
            "vertical",
            "altBusinessIdType",
            "brandIdentityStatus",
            "brandRelationship",
            "campaignStatus",
            "entityType",
            "extVettingProvider",
            "vettingStatus",
            "brandStatus",
            "operationStatus",
            "approvedPublicCompany",
            "stockExchange",
            "vettingClass",
        ],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnumRetrieveResponse:
        """
        Get Enum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        return cast(
            EnumRetrieveResponse,
            self._get(
                f"/enum/{endpoint}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EnumRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEnumResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEnumResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        endpoint: Literal[
            "mno",
            "optionalAttributes",
            "usecase",
            "vertical",
            "altBusinessIdType",
            "brandIdentityStatus",
            "brandRelationship",
            "campaignStatus",
            "entityType",
            "extVettingProvider",
            "vettingStatus",
            "brandStatus",
            "operationStatus",
            "approvedPublicCompany",
            "stockExchange",
            "vettingClass",
        ],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnumRetrieveResponse:
        """
        Get Enum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        return cast(
            EnumRetrieveResponse,
            await self._get(
                f"/enum/{endpoint}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EnumRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EnumResourceWithRawResponse:
    def __init__(self, enum: EnumResource) -> None:
        self._enum = enum

        self.retrieve = to_raw_response_wrapper(
            enum.retrieve,
        )


class AsyncEnumResourceWithRawResponse:
    def __init__(self, enum: AsyncEnumResource) -> None:
        self._enum = enum

        self.retrieve = async_to_raw_response_wrapper(
            enum.retrieve,
        )


class EnumResourceWithStreamingResponse:
    def __init__(self, enum: EnumResource) -> None:
        self._enum = enum

        self.retrieve = to_streamed_response_wrapper(
            enum.retrieve,
        )


class AsyncEnumResourceWithStreamingResponse:
    def __init__(self, enum: AsyncEnumResource) -> None:
        self._enum = enum

        self.retrieve = async_to_streamed_response_wrapper(
            enum.retrieve,
        )
