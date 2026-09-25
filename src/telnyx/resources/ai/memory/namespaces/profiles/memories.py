# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ......_base_client import AsyncPaginator, make_request_options
from ......types.ai.memory.namespaces.profiles import memory_list_params
from ......types.ai.memory.namespaces.profiles.memory_list_response import MemoryListResponse
from ......types.ai.memory.namespaces.profiles.memory_retrieve_response import MemoryRetrieveResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    """What a namespace and a profile hold."""

    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        memory_id: str,
        *,
        namespace: str,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryRetrieveResponse:
        """
        One memory by its id, as `recall` and the listing return it, together with what
        it came from. A fact names its `source_id`: read it with
        `GET .../sources/{source_id}` to see what was stored. A memory derived from
        other memories names them in `derived_from` instead; read each of those to reach
        its source.

        Args:
          namespace: The namespace. `default` exists for every organization.

          profile_id: The profile: your identifier for the user, caller or agent this memory is about.

          memory_id: A memory's id, as `recall` and the listing return it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/memories/{memory_id}",
                namespace=namespace,
                profile_id=profile_id,
                memory_id=memory_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryRetrieveResponse,
        )

    def list(
        self,
        profile_id: str,
        *,
        namespace: str,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[MemoryListResponse]:
        """
        Everything stored under one profile, unranked -- ask `recall` for the memories
        that answer a question. A profile that holds nothing is an empty page rather
        than a 404: profiles exist by being written to. Each memory names the
        `source_id` it was extracted from, or null for a memory derived from other
        memories -- which can read almost the same as the fact it restates. A
        `source_id` narrows the listing to the memories extracted from that source, and
        a `session_id` to those extracted from the session, which is the same thing
        named another way; pass one or the other. Neither is everything the source led
        to: a memory derived from several sources belongs to no single one and appears
        only in the unfiltered listing. A memory written while the listing is paged
        shifts the pages after it, so an entry can be repeated or missed at a page
        boundary.

        Args:
          page_number: The page to return, counting from 1. Bounded in depth: (page[number] - 1) \\**
              page[size] may be at most 10000.

          page_size: How many results a page holds.

          session_id: An ingested session, by the `session_id` it was ingested with. Narrows the
              request to the source that session was stored as.

          source_id: Narrows the listing to the memories extracted from one source, a remembered fact
              as well as a session. Pass this or `session_id`, not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get_api_list(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/memories",
                namespace=namespace,
                profile_id=profile_id,
            ),
            page=SyncDefaultFlatPagination[MemoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "session_id": session_id,
                        "source_id": source_id,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            model=MemoryListResponse,
        )


class AsyncMemoriesResource(AsyncAPIResource):
    """What a namespace and a profile hold."""

    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        memory_id: str,
        *,
        namespace: str,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryRetrieveResponse:
        """
        One memory by its id, as `recall` and the listing return it, together with what
        it came from. A fact names its `source_id`: read it with
        `GET .../sources/{source_id}` to see what was stored. A memory derived from
        other memories names them in `derived_from` instead; read each of those to reach
        its source.

        Args:
          namespace: The namespace. `default` exists for every organization.

          profile_id: The profile: your identifier for the user, caller or agent this memory is about.

          memory_id: A memory's id, as `recall` and the listing return it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not memory_id:
            raise ValueError(f"Expected a non-empty value for `memory_id` but received {memory_id!r}")
        return await self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/memories/{memory_id}",
                namespace=namespace,
                profile_id=profile_id,
                memory_id=memory_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryRetrieveResponse,
        )

    def list(
        self,
        profile_id: str,
        *,
        namespace: str,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        source_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MemoryListResponse, AsyncDefaultFlatPagination[MemoryListResponse]]:
        """
        Everything stored under one profile, unranked -- ask `recall` for the memories
        that answer a question. A profile that holds nothing is an empty page rather
        than a 404: profiles exist by being written to. Each memory names the
        `source_id` it was extracted from, or null for a memory derived from other
        memories -- which can read almost the same as the fact it restates. A
        `source_id` narrows the listing to the memories extracted from that source, and
        a `session_id` to those extracted from the session, which is the same thing
        named another way; pass one or the other. Neither is everything the source led
        to: a memory derived from several sources belongs to no single one and appears
        only in the unfiltered listing. A memory written while the listing is paged
        shifts the pages after it, so an entry can be repeated or missed at a page
        boundary.

        Args:
          page_number: The page to return, counting from 1. Bounded in depth: (page[number] - 1) \\**
              page[size] may be at most 10000.

          page_size: How many results a page holds.

          session_id: An ingested session, by the `session_id` it was ingested with. Narrows the
              request to the source that session was stored as.

          source_id: Narrows the listing to the memories extracted from one source, a remembered fact
              as well as a session. Pass this or `session_id`, not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get_api_list(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/memories",
                namespace=namespace,
                profile_id=profile_id,
            ),
            page=AsyncDefaultFlatPagination[MemoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "session_id": session_id,
                        "source_id": source_id,
                    },
                    memory_list_params.MemoryListParams,
                ),
            ),
            model=MemoryListResponse,
        )


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.retrieve = to_raw_response_wrapper(
            memories.retrieve,
        )
        self.list = to_raw_response_wrapper(
            memories.list,
        )


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.retrieve = async_to_raw_response_wrapper(
            memories.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            memories.list,
        )


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.retrieve = to_streamed_response_wrapper(
            memories.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            memories.list,
        )


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.retrieve = async_to_streamed_response_wrapper(
            memories.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            memories.list,
        )
