# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import web_search_create_params, web_search_contents_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .research import (
    ResearchResource,
    AsyncResearchResource,
    ResearchResourceWithRawResponse,
    AsyncResearchResourceWithRawResponse,
    ResearchResourceWithStreamingResponse,
    AsyncResearchResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.web_search_create_response import WebSearchCreateResponse
from ...types.web_search_contents_response import WebSearchContentsResponse

__all__ = ["WebSearchResource", "AsyncWebSearchResource"]


class WebSearchResource(SyncAPIResource):
    @cached_property
    def research(self) -> ResearchResource:
        """Deep research with citations and async task polling."""
        return ResearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WebSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WebSearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: str,
        count: int | Omit = omit,
        country: str | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        freshness: str | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        livecrawl: bool | Omit = omit,
        safesearch: Literal["off", "moderate", "strict"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchCreateResponse:
        """
        Performs a real-time web search and returns structured, LLM-ready JSON results
        with titles, URLs, descriptions, and snippets. Supports filtering by domain,
        country, safe search, freshness, and live crawl.

        **Note:** `include_domains` and `exclude_domains` cannot be used in the same
        request. Use one or the other.

        Args:
          query: The search query text.

          count: Number of results to return (1-100).

          country: Two-letter country code (ISO 3166-1 alpha-2) to bias results.

          exclude_domains: Exclude results from these domains (bare hostnames, e.g. `pinterest.com`).

          freshness: Time-based filter for results. Common values: `day`, `week`, `month`, `year`.

          include_domains: Restrict results to these domains (bare hostnames, e.g. `arxiv.org`).

          livecrawl: When true, the provider crawls pages in real-time for fresh content. The boolean
              is translated to the provider's internal enum internally; callers always pass
              `true` or `false`.

          safesearch: Safe search filter level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web_search",
            body=maybe_transform(
                {
                    "query": query,
                    "count": count,
                    "country": country,
                    "exclude_domains": exclude_domains,
                    "freshness": freshness,
                    "include_domains": include_domains,
                    "livecrawl": livecrawl,
                    "safesearch": safesearch,
                },
                web_search_create_params.WebSearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchCreateResponse,
        )

    def contents(
        self,
        *,
        urls: SequenceNotStr[str],
        crawl_timeout: int | Omit = omit,
        formats: List[Literal["html", "markdown", "metadata"]] | Omit = omit,
        max_age: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchContentsResponse:
        """Retrieves clean HTML or Markdown content from a list of URLs.

        Supports up to 20
        URLs per request (public API limit). Specify which formats to return: `html`,
        `markdown`, `metadata`.

        Args:
          urls: List of URLs to retrieve content from (max 20 for public API).

          crawl_timeout: Timeout for crawling each URL, in seconds (1-60).

          formats: Content formats to return. If omitted, `html` and `metadata` are returned by
              default. Retrieval is best-effort per URL: a format field appears only when that
              content could be produced, and a freshly crawled page may also include `html`
              even when not requested.

          max_age: Maximum age of cached content in seconds. `null` means no limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web_search/contents",
            body=maybe_transform(
                {
                    "urls": urls,
                    "crawl_timeout": crawl_timeout,
                    "formats": formats,
                    "max_age": max_age,
                },
                web_search_contents_params.WebSearchContentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchContentsResponse,
        )


class AsyncWebSearchResource(AsyncAPIResource):
    @cached_property
    def research(self) -> AsyncResearchResource:
        """Deep research with citations and async task polling."""
        return AsyncResearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWebSearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: str,
        count: int | Omit = omit,
        country: str | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        freshness: str | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        livecrawl: bool | Omit = omit,
        safesearch: Literal["off", "moderate", "strict"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchCreateResponse:
        """
        Performs a real-time web search and returns structured, LLM-ready JSON results
        with titles, URLs, descriptions, and snippets. Supports filtering by domain,
        country, safe search, freshness, and live crawl.

        **Note:** `include_domains` and `exclude_domains` cannot be used in the same
        request. Use one or the other.

        Args:
          query: The search query text.

          count: Number of results to return (1-100).

          country: Two-letter country code (ISO 3166-1 alpha-2) to bias results.

          exclude_domains: Exclude results from these domains (bare hostnames, e.g. `pinterest.com`).

          freshness: Time-based filter for results. Common values: `day`, `week`, `month`, `year`.

          include_domains: Restrict results to these domains (bare hostnames, e.g. `arxiv.org`).

          livecrawl: When true, the provider crawls pages in real-time for fresh content. The boolean
              is translated to the provider's internal enum internally; callers always pass
              `true` or `false`.

          safesearch: Safe search filter level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web_search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "count": count,
                    "country": country,
                    "exclude_domains": exclude_domains,
                    "freshness": freshness,
                    "include_domains": include_domains,
                    "livecrawl": livecrawl,
                    "safesearch": safesearch,
                },
                web_search_create_params.WebSearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchCreateResponse,
        )

    async def contents(
        self,
        *,
        urls: SequenceNotStr[str],
        crawl_timeout: int | Omit = omit,
        formats: List[Literal["html", "markdown", "metadata"]] | Omit = omit,
        max_age: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchContentsResponse:
        """Retrieves clean HTML or Markdown content from a list of URLs.

        Supports up to 20
        URLs per request (public API limit). Specify which formats to return: `html`,
        `markdown`, `metadata`.

        Args:
          urls: List of URLs to retrieve content from (max 20 for public API).

          crawl_timeout: Timeout for crawling each URL, in seconds (1-60).

          formats: Content formats to return. If omitted, `html` and `metadata` are returned by
              default. Retrieval is best-effort per URL: a format field appears only when that
              content could be produced, and a freshly crawled page may also include `html`
              even when not requested.

          max_age: Maximum age of cached content in seconds. `null` means no limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web_search/contents",
            body=await async_maybe_transform(
                {
                    "urls": urls,
                    "crawl_timeout": crawl_timeout,
                    "formats": formats,
                    "max_age": max_age,
                },
                web_search_contents_params.WebSearchContentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchContentsResponse,
        )


class WebSearchResourceWithRawResponse:
    def __init__(self, web_search: WebSearchResource) -> None:
        self._web_search = web_search

        self.create = to_raw_response_wrapper(
            web_search.create,
        )
        self.contents = to_raw_response_wrapper(
            web_search.contents,
        )

    @cached_property
    def research(self) -> ResearchResourceWithRawResponse:
        """Deep research with citations and async task polling."""
        return ResearchResourceWithRawResponse(self._web_search.research)


class AsyncWebSearchResourceWithRawResponse:
    def __init__(self, web_search: AsyncWebSearchResource) -> None:
        self._web_search = web_search

        self.create = async_to_raw_response_wrapper(
            web_search.create,
        )
        self.contents = async_to_raw_response_wrapper(
            web_search.contents,
        )

    @cached_property
    def research(self) -> AsyncResearchResourceWithRawResponse:
        """Deep research with citations and async task polling."""
        return AsyncResearchResourceWithRawResponse(self._web_search.research)


class WebSearchResourceWithStreamingResponse:
    def __init__(self, web_search: WebSearchResource) -> None:
        self._web_search = web_search

        self.create = to_streamed_response_wrapper(
            web_search.create,
        )
        self.contents = to_streamed_response_wrapper(
            web_search.contents,
        )

    @cached_property
    def research(self) -> ResearchResourceWithStreamingResponse:
        """Deep research with citations and async task polling."""
        return ResearchResourceWithStreamingResponse(self._web_search.research)


class AsyncWebSearchResourceWithStreamingResponse:
    def __init__(self, web_search: AsyncWebSearchResource) -> None:
        self._web_search = web_search

        self.create = async_to_streamed_response_wrapper(
            web_search.create,
        )
        self.contents = async_to_streamed_response_wrapper(
            web_search.contents,
        )

    @cached_property
    def research(self) -> AsyncResearchResourceWithStreamingResponse:
        """Deep research with citations and async task polling."""
        return AsyncResearchResourceWithStreamingResponse(self._web_search.research)
