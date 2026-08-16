# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.web_search import research_create_params
from ...types.web_search.research_create_response import ResearchCreateResponse
from ...types.web_search.research_retrieve_response import ResearchRetrieveResponse

__all__ = ["ResearchResource", "AsyncResearchResource"]


class ResearchResource(SyncAPIResource):
    """Deep research with citations and async task polling."""

    @cached_property
    def with_raw_response(self) -> ResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ResearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: str,
        background: bool | Omit = omit,
        max_sources: int | Omit = omit,
        research_effort: Literal["lite", "standard", "deep"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchCreateResponse:
        """
        Starts a deep research task that runs multiple searches, reads sources, and
        synthesizes an answer with citations.

        ## Synchronous mode (default)

        When `background` is `false` or omitted, the request blocks until the research
        completes and returns the answer with citations. This can take up to 120 seconds
        depending on `research_effort`.

        ## Asynchronous mode

        When `background` is `true`, the request returns immediately with a `task_id`
        and `status: pending`. Poll `GET /web_search/research/{task_id}` to check when
        the research completes and retrieve the answer.

        Args:
          query: The research question or topic.

          background: When `true`, the research runs asynchronously. The response returns a `task_id`
              immediately instead of waiting for the result. Poll
              `GET /web_search/research/{task_id}` to check status.

          max_sources: Maximum number of sources to use.

          research_effort: Research depth level. `lite` is fastest, `deep` is most thorough.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web_search/research",
            body=maybe_transform(
                {
                    "query": query,
                    "background": background,
                    "max_sources": max_sources,
                    "research_effort": research_effort,
                },
                research_create_params.ResearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchCreateResponse,
        )

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchRetrieveResponse:
        """Polls the status of a previously started asynchronous research task.

        When the
        status is `completed`, the response includes the answer and citations. When the
        status is `failed`, the response includes an error message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/web_search/research/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchRetrieveResponse,
        )


class AsyncResearchResource(AsyncAPIResource):
    """Deep research with citations and async task polling."""

    @cached_property
    def with_raw_response(self) -> AsyncResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncResearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: str,
        background: bool | Omit = omit,
        max_sources: int | Omit = omit,
        research_effort: Literal["lite", "standard", "deep"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchCreateResponse:
        """
        Starts a deep research task that runs multiple searches, reads sources, and
        synthesizes an answer with citations.

        ## Synchronous mode (default)

        When `background` is `false` or omitted, the request blocks until the research
        completes and returns the answer with citations. This can take up to 120 seconds
        depending on `research_effort`.

        ## Asynchronous mode

        When `background` is `true`, the request returns immediately with a `task_id`
        and `status: pending`. Poll `GET /web_search/research/{task_id}` to check when
        the research completes and retrieve the answer.

        Args:
          query: The research question or topic.

          background: When `true`, the research runs asynchronously. The response returns a `task_id`
              immediately instead of waiting for the result. Poll
              `GET /web_search/research/{task_id}` to check status.

          max_sources: Maximum number of sources to use.

          research_effort: Research depth level. `lite` is fastest, `deep` is most thorough.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web_search/research",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "background": background,
                    "max_sources": max_sources,
                    "research_effort": research_effort,
                },
                research_create_params.ResearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchCreateResponse,
        )

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchRetrieveResponse:
        """Polls the status of a previously started asynchronous research task.

        When the
        status is `completed`, the response includes the answer and citations. When the
        status is `failed`, the response includes an error message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/web_search/research/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchRetrieveResponse,
        )


class ResearchResourceWithRawResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create = to_raw_response_wrapper(
            research.create,
        )
        self.retrieve = to_raw_response_wrapper(
            research.retrieve,
        )


class AsyncResearchResourceWithRawResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create = async_to_raw_response_wrapper(
            research.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            research.retrieve,
        )


class ResearchResourceWithStreamingResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create = to_streamed_response_wrapper(
            research.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            research.retrieve,
        )


class AsyncResearchResourceWithStreamingResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create = async_to_streamed_response_wrapper(
            research.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            research.retrieve,
        )
