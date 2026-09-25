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
from ......types.ai.collections.source import Source
from ......types.ai.memory.namespaces.profiles import source_list_params
from ......types.ai.memory.namespaces.profiles.source_delete_response import SourceDeleteResponse
from ......types.ai.memory.namespaces.profiles.source_retrieve_response import SourceRetrieveResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    """What a profile stored, and what its memories came from."""

    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        source_id: str,
        *,
        namespace: str,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRetrieveResponse:
        """
        One source and its content, as it was stored: an ingested session's payload or a
        remembered fact. A source whose ingest is still queued answers 404 until it has
        been stored.

        Args:
          namespace: The namespace. `default` exists for every organization.

          profile_id: The profile: your identifier for the user, caller or agent this memory is about.

          source_id: Identifies one source within its profile: an ingested session, or one remembered
              fact. Returned by `ingest` and `remember` when the write is accepted.
              Re-ingesting a session keeps its source id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/sources/{source_id}",
                namespace=namespace,
                profile_id=profile_id,
                source_id=source_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceRetrieveResponse,
        )

    def list(
        self,
        profile_id: str,
        *,
        namespace: str,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[Source]:
        """
        Everything a profile has stored and extracts memories from: each ingested
        session, and each remembered fact, which has no session. Content is not listed;
        read one source for it. A source whose ingest is still queued is not here yet.
        Re-ingesting a session moves it to the front, so a listing paged while sessions
        are written can repeat or miss one at a page boundary. A `session_id` narrows
        the listing to the source that session was stored as: one source or none, and
        none -- an empty page, not a 404 -- for a session never ingested, still queued,
        or another profile's.

        Args:
          page_number: The page to return, counting from 1. Bounded in depth: (page[number] - 1) \\**
              page[size] may be at most 10000.

          page_size: How many results a page holds.

          session_id: An ingested session, by the `session_id` it was ingested with. Narrows the
              request to the source that session was stored as.

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
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/sources",
                namespace=namespace,
                profile_id=profile_id,
            ),
            page=SyncDefaultFlatPagination[Source],
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
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            model=Source,
        )

    def delete(
        self,
        source_id: str,
        *,
        namespace: str,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteResponse:
        """
        Deletes one source -- an ingested session or a remembered fact -- together with
        the memories derived from it. A memory derived from this source and others is
        deleted too, and derived again from what remains in the background. It answers
        only once the source is gone. A source that is not there -- never stored,
        another profile's, or already deleted -- answers 404, so on a `502` or a `504`
        repeat the identical request and read a 404 as done. An ingest of the same
        session that is still queued is not cancelled, and stores the session again when
        it runs. Nothing here can be undone.

        Args:
          namespace: The namespace. `default` exists for every organization.

          profile_id: The profile: your identifier for the user, caller or agent this memory is about.

          source_id: Identifies one source within its profile: an ingested session, or one remembered
              fact. Returned by `ingest` and `remember` when the write is accepted.
              Re-ingesting a session keeps its source id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._delete(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/sources/{source_id}",
                namespace=namespace,
                profile_id=profile_id,
                source_id=source_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceDeleteResponse,
        )


class AsyncSourcesResource(AsyncAPIResource):
    """What a profile stored, and what its memories came from."""

    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        source_id: str,
        *,
        namespace: str,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceRetrieveResponse:
        """
        One source and its content, as it was stored: an ingested session's payload or a
        remembered fact. A source whose ingest is still queued answers 404 until it has
        been stored.

        Args:
          namespace: The namespace. `default` exists for every organization.

          profile_id: The profile: your identifier for the user, caller or agent this memory is about.

          source_id: Identifies one source within its profile: an ingested session, or one remembered
              fact. Returned by `ingest` and `remember` when the write is accepted.
              Re-ingesting a session keeps its source id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/sources/{source_id}",
                namespace=namespace,
                profile_id=profile_id,
                source_id=source_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceRetrieveResponse,
        )

    def list(
        self,
        profile_id: str,
        *,
        namespace: str,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Source, AsyncDefaultFlatPagination[Source]]:
        """
        Everything a profile has stored and extracts memories from: each ingested
        session, and each remembered fact, which has no session. Content is not listed;
        read one source for it. A source whose ingest is still queued is not here yet.
        Re-ingesting a session moves it to the front, so a listing paged while sessions
        are written can repeat or miss one at a page boundary. A `session_id` narrows
        the listing to the source that session was stored as: one source or none, and
        none -- an empty page, not a 404 -- for a session never ingested, still queued,
        or another profile's.

        Args:
          page_number: The page to return, counting from 1. Bounded in depth: (page[number] - 1) \\**
              page[size] may be at most 10000.

          page_size: How many results a page holds.

          session_id: An ingested session, by the `session_id` it was ingested with. Narrows the
              request to the source that session was stored as.

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
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/sources",
                namespace=namespace,
                profile_id=profile_id,
            ),
            page=AsyncDefaultFlatPagination[Source],
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
                    },
                    source_list_params.SourceListParams,
                ),
            ),
            model=Source,
        )

    async def delete(
        self,
        source_id: str,
        *,
        namespace: str,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceDeleteResponse:
        """
        Deletes one source -- an ingested session or a remembered fact -- together with
        the memories derived from it. A memory derived from this source and others is
        deleted too, and derived again from what remains in the background. It answers
        only once the source is gone. A source that is not there -- never stored,
        another profile's, or already deleted -- answers 404, so on a `502` or a `504`
        repeat the identical request and read a 404 as done. An ingest of the same
        session that is still queued is not cancelled, and stores the session again when
        it runs. Nothing here can be undone.

        Args:
          namespace: The namespace. `default` exists for every organization.

          profile_id: The profile: your identifier for the user, caller or agent this memory is about.

          source_id: Identifies one source within its profile: an ingested session, or one remembered
              fact. Returned by `ingest` and `remember` when the write is accepted.
              Re-ingesting a session keeps its source id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._delete(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/sources/{source_id}",
                namespace=namespace,
                profile_id=profile_id,
                source_id=source_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceDeleteResponse,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.retrieve = to_raw_response_wrapper(
            sources.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sources.list,
        )
        self.delete = to_raw_response_wrapper(
            sources.delete,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.retrieve = async_to_raw_response_wrapper(
            sources.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sources.delete,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.retrieve = to_streamed_response_wrapper(
            sources.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            sources.delete,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.retrieve = async_to_streamed_response_wrapper(
            sources.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sources.delete,
        )
