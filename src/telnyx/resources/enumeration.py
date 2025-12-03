# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.enumeration_retrieve_response import EnumerationRetrieveResponse

__all__ = ["EnumerationResource", "AsyncEnumerationResource"]


class EnumerationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnumerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EnumerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnumerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EnumerationResourceWithStreamingResponse(self)

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnumerationRetrieveResponse:
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
            EnumerationRetrieveResponse,
            self._get(
                f"/enum/{endpoint}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EnumerationRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEnumerationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnumerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnumerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnumerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEnumerationResourceWithStreamingResponse(self)

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnumerationRetrieveResponse:
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
            EnumerationRetrieveResponse,
            await self._get(
                f"/enum/{endpoint}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EnumerationRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EnumerationResourceWithRawResponse:
    def __init__(self, enumeration: EnumerationResource) -> None:
        self._enumeration = enumeration

        self.retrieve = to_raw_response_wrapper(
            enumeration.retrieve,
        )


class AsyncEnumerationResourceWithRawResponse:
    def __init__(self, enumeration: AsyncEnumerationResource) -> None:
        self._enumeration = enumeration

        self.retrieve = async_to_raw_response_wrapper(
            enumeration.retrieve,
        )


class EnumerationResourceWithStreamingResponse:
    def __init__(self, enumeration: EnumerationResource) -> None:
        self._enumeration = enumeration

        self.retrieve = to_streamed_response_wrapper(
            enumeration.retrieve,
        )


class AsyncEnumerationResourceWithStreamingResponse:
    def __init__(self, enumeration: AsyncEnumerationResource) -> None:
        self._enumeration = enumeration

        self.retrieve = async_to_streamed_response_wrapper(
            enumeration.retrieve,
        )
