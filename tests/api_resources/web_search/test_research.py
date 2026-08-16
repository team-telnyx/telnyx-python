# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.web_search import ResearchCreateResponse, ResearchRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        research = client.web_search.research.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        research = client.web_search.research.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
            background=False,
            max_sources=20,
            research_effort="standard",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.web_search.research.with_raw_response.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = response.parse()
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.web_search.research.with_streaming_response.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = response.parse()
            assert_matches_type(ResearchCreateResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        research = client.web_search.research.retrieve(
            "bf3026a5-dd57-44dd-b922-200041be3a4b",
        )
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.web_search.research.with_raw_response.retrieve(
            "bf3026a5-dd57-44dd-b922-200041be3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = response.parse()
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.web_search.research.with_streaming_response.retrieve(
            "bf3026a5-dd57-44dd-b922-200041be3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = response.parse()
            assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.web_search.research.with_raw_response.retrieve(
                "",
            )


class TestAsyncResearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        research = await async_client.web_search.research.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        research = await async_client.web_search.research.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
            background=False,
            max_sources=20,
            research_effort="standard",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.web_search.research.with_raw_response.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = await response.parse()
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.web_search.research.with_streaming_response.create(
            query="Compare the performance of RAG vs fine-tuning for domain-specific QA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = await response.parse()
            assert_matches_type(ResearchCreateResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        research = await async_client.web_search.research.retrieve(
            "bf3026a5-dd57-44dd-b922-200041be3a4b",
        )
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.web_search.research.with_raw_response.retrieve(
            "bf3026a5-dd57-44dd-b922-200041be3a4b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = await response.parse()
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.web_search.research.with_streaming_response.retrieve(
            "bf3026a5-dd57-44dd-b922-200041be3a4b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = await response.parse()
            assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.web_search.research.with_raw_response.retrieve(
                "",
            )
