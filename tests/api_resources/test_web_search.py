# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    WebSearchCreateResponse,
    WebSearchContentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        web_search = client.web_search.create(
            query="latest AI agent frameworks",
        )
        assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        web_search = client.web_search.create(
            query="latest AI agent frameworks",
            count=10,
            country="US",
            exclude_domains=["pinterest.com"],
            freshness="week",
            include_domains=["arxiv.org", "github.com"],
            livecrawl=False,
            safesearch="moderate",
        )
        assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.web_search.with_raw_response.create(
            query="latest AI agent frameworks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_search = response.parse()
        assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.web_search.with_streaming_response.create(
            query="latest AI agent frameworks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_search = response.parse()
            assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_contents(self, client: Telnyx) -> None:
        web_search = client.web_search.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        )
        assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_contents_with_all_params(self, client: Telnyx) -> None:
        web_search = client.web_search.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
            crawl_timeout=10,
            formats=["markdown", "metadata"],
            max_age=None,
        )
        assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_contents(self, client: Telnyx) -> None:
        response = client.web_search.with_raw_response.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_search = response.parse()
        assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_contents(self, client: Telnyx) -> None:
        with client.web_search.with_streaming_response.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_search = response.parse()
            assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        web_search = await async_client.web_search.create(
            query="latest AI agent frameworks",
        )
        assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        web_search = await async_client.web_search.create(
            query="latest AI agent frameworks",
            count=10,
            country="US",
            exclude_domains=["pinterest.com"],
            freshness="week",
            include_domains=["arxiv.org", "github.com"],
            livecrawl=False,
            safesearch="moderate",
        )
        assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.web_search.with_raw_response.create(
            query="latest AI agent frameworks",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_search = await response.parse()
        assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.web_search.with_streaming_response.create(
            query="latest AI agent frameworks",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_search = await response.parse()
            assert_matches_type(WebSearchCreateResponse, web_search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_contents(self, async_client: AsyncTelnyx) -> None:
        web_search = await async_client.web_search.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        )
        assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_contents_with_all_params(self, async_client: AsyncTelnyx) -> None:
        web_search = await async_client.web_search.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
            crawl_timeout=10,
            formats=["markdown", "metadata"],
            max_age=None,
        )
        assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_contents(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.web_search.with_raw_response.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web_search = await response.parse()
        assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_contents(self, async_client: AsyncTelnyx) -> None:
        async with async_client.web_search.with_streaming_response.contents(
            urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web_search = await response.parse()
            assert_matches_type(WebSearchContentsResponse, web_search, path=["response"])

        assert cast(Any, response.is_closed) is True
