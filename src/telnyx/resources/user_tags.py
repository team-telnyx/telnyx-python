# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import user_tag_list_params
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
from ..types.user_tag_list_response import UserTagListResponse

__all__ = ["UserTagsResource", "AsyncUserTagsResource"]


class UserTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UserTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UserTagsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: user_tag_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserTagListResponse:
        """
        List all user tags.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[starts_with]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user_tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, user_tag_list_params.UserTagListParams),
            ),
            cast_to=UserTagListResponse,
        )


class AsyncUserTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUserTagsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: user_tag_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserTagListResponse:
        """
        List all user tags.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[starts_with]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user_tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"filter": filter}, user_tag_list_params.UserTagListParams),
            ),
            cast_to=UserTagListResponse,
        )


class UserTagsResourceWithRawResponse:
    def __init__(self, user_tags: UserTagsResource) -> None:
        self._user_tags = user_tags

        self.list = to_raw_response_wrapper(
            user_tags.list,
        )


class AsyncUserTagsResourceWithRawResponse:
    def __init__(self, user_tags: AsyncUserTagsResource) -> None:
        self._user_tags = user_tags

        self.list = async_to_raw_response_wrapper(
            user_tags.list,
        )


class UserTagsResourceWithStreamingResponse:
    def __init__(self, user_tags: UserTagsResource) -> None:
        self._user_tags = user_tags

        self.list = to_streamed_response_wrapper(
            user_tags.list,
        )


class AsyncUserTagsResourceWithStreamingResponse:
    def __init__(self, user_tags: AsyncUserTagsResource) -> None:
        self._user_tags = user_tags

        self.list = async_to_streamed_response_wrapper(
            user_tags.list,
        )
