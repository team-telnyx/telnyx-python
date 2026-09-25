# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import overload

import httpx

from .sources import (
    SourcesResource,
    AsyncSourcesResource,
    SourcesResourceWithRawResponse,
    AsyncSourcesResourceWithRawResponse,
    SourcesResourceWithStreamingResponse,
    AsyncSourcesResourceWithStreamingResponse,
)
from .memories import (
    MemoriesResource,
    AsyncMemoriesResource,
    MemoriesResourceWithRawResponse,
    AsyncMemoriesResourceWithRawResponse,
    MemoriesResourceWithStreamingResponse,
    AsyncMemoriesResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ......types.ai.memory.namespaces import (
    profile_list_params,
    profile_ingest_params,
    profile_recall_params,
    profile_remember_params,
)
from ......types.ai.memory.namespaces.profile_list_response import ProfileListResponse
from ......types.ai.memory.namespaces.profile_delete_response import ProfileDeleteResponse
from ......types.ai.memory.namespaces.profile_ingest_response import ProfileIngestResponse
from ......types.ai.memory.namespaces.profile_recall_response import ProfileRecallResponse
from ......types.ai.memory.namespaces.profile_remember_response import ProfileRememberResponse
from ......types.ai.memory.namespaces.profile_retrieve_summary_response import ProfileRetrieveSummaryResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    @cached_property
    def memories(self) -> MemoriesResource:
        """What a namespace and a profile hold."""
        return MemoriesResource(self._client)

    @cached_property
    def sources(self) -> SourcesResource:
        """What a profile stored, and what its memories came from."""
        return SourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def list(
        self,
        namespace: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ProfileListResponse]:
        """
        Profiles are never created, only written to, so this lists the ones that hold a
        memory. A profile whose first ingest is still running is not here yet. Ordered
        by memory count, largest first, so a profile written to while the listing is
        paged can move between pages and be repeated or missed.

        Args:
          page_number: The page to return, counting from 1. Bounded in depth: (page[number] - 1) \\**
              page[size] may be at most 10000.

          page_size: How many results a page holds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get_api_list(
            path_template("/ai/memory/namespaces/{namespace}/profiles", namespace=namespace),
            page=SyncDefaultFlatPagination[ProfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    profile_list_params.ProfileListParams,
                ),
            ),
            model=ProfileListResponse,
        )

    def delete(
        self,
        profile_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileDeleteResponse:
        """Delete everything held about one profile.

        A 2xx means none of its memories are
        left, and its summary goes with them. There is no undo.

        Args:
          namespace: The namespace. `default` exists for every organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}", namespace=namespace, profile_id=profile_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileDeleteResponse,
        )

    @overload
    def ingest(
        self,
        profile_id: str,
        *,
        namespace: str,
        body: Dict[str, object],
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileIngestResponse:
        """Store a session.

        Facts are extracted from whatever you send — the body is taken
        as any JSON value and stored whole, so a framework's own transcript shape works
        unchanged. `messages` of `role`/`content` is the conventional shape, not a
        requirement. An empty object or a null body is refused. Carry a `session_id` to
        name the session: re-ingesting the same one replaces what it held. Omit it and a
        session is opened and returned. Extraction runs asynchronously — poll the
        returned operation.

        Args:
          session_id: Names the session. Re-ingesting the same session replaces what it held and keeps
              its `source_id`. Omit it to have one derived from the content and returned. No
              whitespace, control characters, or any of / \\  # ? %.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def ingest(
        self,
        profile_id: str,
        *,
        namespace: str,
        body: Union[Iterable[object], str, float, bool],
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileIngestResponse:
        """Store a session.

        Facts are extracted from whatever you send — the body is taken
        as any JSON value and stored whole, so a framework's own transcript shape works
        unchanged. `messages` of `role`/`content` is the conventional shape, not a
        requirement. An empty object or a null body is refused. Carry a `session_id` to
        name the session: re-ingesting the same one replaces what it held. Omit it and a
        session is opened and returned. Extraction runs asynchronously — poll the
        returned operation.

        Args:
          session_id: Names the session. Re-ingesting the same session replaces what it held and keeps
              its `source_id`. Omit it to have one derived from the content and returned. No
              whitespace, control characters, or any of / \\  # ? %.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["namespace", "body"])
    def ingest(
        self,
        profile_id: str,
        *,
        namespace: str,
        body: Dict[str, object] | Union[Iterable[object], str, float, bool],
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileIngestResponse:
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._post(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/ingest",
                namespace=namespace,
                profile_id=profile_id,
            ),
            body=maybe_transform(body, profile_ingest_params.ProfileIngestParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, profile_ingest_params.ProfileIngestParams),
            ),
            cast_to=ProfileIngestResponse,
        )

    def recall(
        self,
        profile_id: str,
        *,
        namespace: str,
        query: str,
        top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRecallResponse:
        """Ranked memories for a question.

        Matching runs over the profile's memories and
        returns them in rank order with a relevance `score`; the score is null where the
        deployment's reranker is a passthrough, in which case order is the only signal.
        No model runs in this path — recall returns facts, it does not compose an
        answer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._post(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/recall",
                namespace=namespace,
                profile_id=profile_id,
            ),
            body=maybe_transform(
                {
                    "query": query,
                    "top_k": top_k,
                },
                profile_recall_params.ProfileRecallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRecallResponse,
        )

    def remember(
        self,
        profile_id: str,
        *,
        namespace: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRememberResponse:
        """
        For a fact the agent has already distilled: `text` is stored as given, with
        nothing extracted from it. Send a transcript to `ingest` instead. Remembering
        the same text again writes the same memory rather than a second copy of it, so a
        retry is safe. The write runs asynchronously -- poll the returned operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._post(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/remember",
                namespace=namespace,
                profile_id=profile_id,
            ),
            body=maybe_transform({"text": text}, profile_remember_params.ProfileRememberParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRememberResponse,
        )

    def retrieve_summary(
        self,
        profile_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveSummaryResponse:
        """The whole profile as one card, precomputed, with no query.

        Built for the start
        of a session, where there is no question to ask yet.

        A summary is generated in the background. `is_stale` tells you newer memories
        have arrived since it was written; that is ordinary and the card is still
        usable.

        Args:
          namespace: The namespace. `default` exists for every organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/summary",
                namespace=namespace,
                profile_id=profile_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveSummaryResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        """What a namespace and a profile hold."""
        return AsyncMemoriesResource(self._client)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        """What a profile stored, and what its memories came from."""
        return AsyncSourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    def list(
        self,
        namespace: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProfileListResponse, AsyncDefaultFlatPagination[ProfileListResponse]]:
        """
        Profiles are never created, only written to, so this lists the ones that hold a
        memory. A profile whose first ingest is still running is not here yet. Ordered
        by memory count, largest first, so a profile written to while the listing is
        paged can move between pages and be repeated or missed.

        Args:
          page_number: The page to return, counting from 1. Bounded in depth: (page[number] - 1) \\**
              page[size] may be at most 10000.

          page_size: How many results a page holds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        return self._get_api_list(
            path_template("/ai/memory/namespaces/{namespace}/profiles", namespace=namespace),
            page=AsyncDefaultFlatPagination[ProfileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    profile_list_params.ProfileListParams,
                ),
            ),
            model=ProfileListResponse,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileDeleteResponse:
        """Delete everything held about one profile.

        A 2xx means none of its memories are
        left, and its summary goes with them. There is no undo.

        Args:
          namespace: The namespace. `default` exists for every organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}", namespace=namespace, profile_id=profile_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileDeleteResponse,
        )

    @overload
    async def ingest(
        self,
        profile_id: str,
        *,
        namespace: str,
        body: Dict[str, object],
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileIngestResponse:
        """Store a session.

        Facts are extracted from whatever you send — the body is taken
        as any JSON value and stored whole, so a framework's own transcript shape works
        unchanged. `messages` of `role`/`content` is the conventional shape, not a
        requirement. An empty object or a null body is refused. Carry a `session_id` to
        name the session: re-ingesting the same one replaces what it held. Omit it and a
        session is opened and returned. Extraction runs asynchronously — poll the
        returned operation.

        Args:
          session_id: Names the session. Re-ingesting the same session replaces what it held and keeps
              its `source_id`. Omit it to have one derived from the content and returned. No
              whitespace, control characters, or any of / \\  # ? %.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def ingest(
        self,
        profile_id: str,
        *,
        namespace: str,
        body: Union[Iterable[object], str, float, bool],
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileIngestResponse:
        """Store a session.

        Facts are extracted from whatever you send — the body is taken
        as any JSON value and stored whole, so a framework's own transcript shape works
        unchanged. `messages` of `role`/`content` is the conventional shape, not a
        requirement. An empty object or a null body is refused. Carry a `session_id` to
        name the session: re-ingesting the same one replaces what it held. Omit it and a
        session is opened and returned. Extraction runs asynchronously — poll the
        returned operation.

        Args:
          session_id: Names the session. Re-ingesting the same session replaces what it held and keeps
              its `source_id`. Omit it to have one derived from the content and returned. No
              whitespace, control characters, or any of / \\  # ? %.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["namespace", "body"])
    async def ingest(
        self,
        profile_id: str,
        *,
        namespace: str,
        body: Dict[str, object] | Union[Iterable[object], str, float, bool],
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileIngestResponse:
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._post(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/ingest",
                namespace=namespace,
                profile_id=profile_id,
            ),
            body=await async_maybe_transform(body, profile_ingest_params.ProfileIngestParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, profile_ingest_params.ProfileIngestParams
                ),
            ),
            cast_to=ProfileIngestResponse,
        )

    async def recall(
        self,
        profile_id: str,
        *,
        namespace: str,
        query: str,
        top_k: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRecallResponse:
        """Ranked memories for a question.

        Matching runs over the profile's memories and
        returns them in rank order with a relevance `score`; the score is null where the
        deployment's reranker is a passthrough, in which case order is the only signal.
        No model runs in this path — recall returns facts, it does not compose an
        answer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._post(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/recall",
                namespace=namespace,
                profile_id=profile_id,
            ),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "top_k": top_k,
                },
                profile_recall_params.ProfileRecallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRecallResponse,
        )

    async def remember(
        self,
        profile_id: str,
        *,
        namespace: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRememberResponse:
        """
        For a fact the agent has already distilled: `text` is stored as given, with
        nothing extracted from it. Send a transcript to `ingest` instead. Remembering
        the same text again writes the same memory rather than a second copy of it, so a
        retry is safe. The write runs asynchronously -- poll the returned operation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._post(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/remember",
                namespace=namespace,
                profile_id=profile_id,
            ),
            body=await async_maybe_transform({"text": text}, profile_remember_params.ProfileRememberParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRememberResponse,
        )

    async def retrieve_summary(
        self,
        profile_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveSummaryResponse:
        """The whole profile as one card, precomputed, with no query.

        Built for the start
        of a session, where there is no question to ask yet.

        A summary is generated in the background. `is_stale` tells you newer memories
        have arrived since it was written; that is ordinary and the card is still
        usable.

        Args:
          namespace: The namespace. `default` exists for every organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/profiles/{profile_id}/summary",
                namespace=namespace,
                profile_id=profile_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveSummaryResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            profiles.delete,
        )
        self.ingest = to_raw_response_wrapper(
            profiles.ingest,
        )
        self.recall = to_raw_response_wrapper(
            profiles.recall,
        )
        self.remember = to_raw_response_wrapper(
            profiles.remember,
        )
        self.retrieve_summary = to_raw_response_wrapper(
            profiles.retrieve_summary,
        )

    @cached_property
    def memories(self) -> MemoriesResourceWithRawResponse:
        """What a namespace and a profile hold."""
        return MemoriesResourceWithRawResponse(self._profiles.memories)

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        """What a profile stored, and what its memories came from."""
        return SourcesResourceWithRawResponse(self._profiles.sources)


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            profiles.delete,
        )
        self.ingest = async_to_raw_response_wrapper(
            profiles.ingest,
        )
        self.recall = async_to_raw_response_wrapper(
            profiles.recall,
        )
        self.remember = async_to_raw_response_wrapper(
            profiles.remember,
        )
        self.retrieve_summary = async_to_raw_response_wrapper(
            profiles.retrieve_summary,
        )

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithRawResponse:
        """What a namespace and a profile hold."""
        return AsyncMemoriesResourceWithRawResponse(self._profiles.memories)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        """What a profile stored, and what its memories came from."""
        return AsyncSourcesResourceWithRawResponse(self._profiles.sources)


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            profiles.delete,
        )
        self.ingest = to_streamed_response_wrapper(
            profiles.ingest,
        )
        self.recall = to_streamed_response_wrapper(
            profiles.recall,
        )
        self.remember = to_streamed_response_wrapper(
            profiles.remember,
        )
        self.retrieve_summary = to_streamed_response_wrapper(
            profiles.retrieve_summary,
        )

    @cached_property
    def memories(self) -> MemoriesResourceWithStreamingResponse:
        """What a namespace and a profile hold."""
        return MemoriesResourceWithStreamingResponse(self._profiles.memories)

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        """What a profile stored, and what its memories came from."""
        return SourcesResourceWithStreamingResponse(self._profiles.sources)


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            profiles.delete,
        )
        self.ingest = async_to_streamed_response_wrapper(
            profiles.ingest,
        )
        self.recall = async_to_streamed_response_wrapper(
            profiles.recall,
        )
        self.remember = async_to_streamed_response_wrapper(
            profiles.remember,
        )
        self.retrieve_summary = async_to_streamed_response_wrapper(
            profiles.retrieve_summary,
        )

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """What a namespace and a profile hold."""
        return AsyncMemoriesResourceWithStreamingResponse(self._profiles.memories)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        """What a profile stored, and what its memories came from."""
        return AsyncSourcesResourceWithStreamingResponse(self._profiles.sources)
