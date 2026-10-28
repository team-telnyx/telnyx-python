# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    BrowserSessionListResponse,
    BrowserSessionCreateResponse,
    BrowserSessionDeleteResponse,
    BrowserSessionRetrieveResponse,
    BrowserSessionRetrieveArtifactResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowserSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.create(
            policy={"allowed_domains": ["example.com"]},
        )
        assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.create(
            policy={"allowed_domains": ["example.com"]},
            idempotency_key="x",
            limits={
                "idle_timeout_s": 30,
                "lifetime_s": 60,
            },
            metadata={},
        )
        assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.browser_sessions.with_raw_response.create(
            policy={"allowed_domains": ["example.com"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = response.parse()
        assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.browser_sessions.with_streaming_response.create(
            policy={"allowed_domains": ["example.com"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = response.parse()
            assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.retrieve(
            "id",
        )
        assert_matches_type(BrowserSessionRetrieveResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.browser_sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = response.parse()
        assert_matches_type(BrowserSessionRetrieveResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.browser_sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = response.parse()
            assert_matches_type(BrowserSessionRetrieveResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.list()
        assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.list(
            status="provisioning",
        )
        assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.browser_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = response.parse()
        assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.browser_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = response.parse()
            assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.delete(
            "id",
        )
        assert_matches_type(BrowserSessionDeleteResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.browser_sessions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = response.parse()
        assert_matches_type(BrowserSessionDeleteResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.browser_sessions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = response.parse()
            assert_matches_type(BrowserSessionDeleteResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_artifact(self, client: Telnyx) -> None:
        browser_session = client.browser_sessions.retrieve_artifact(
            artifact_id="artifactId",
            id="id",
        )
        assert_matches_type(BrowserSessionRetrieveArtifactResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_artifact(self, client: Telnyx) -> None:
        response = client.browser_sessions.with_raw_response.retrieve_artifact(
            artifact_id="artifactId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = response.parse()
        assert_matches_type(BrowserSessionRetrieveArtifactResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_artifact(self, client: Telnyx) -> None:
        with client.browser_sessions.with_streaming_response.retrieve_artifact(
            artifact_id="artifactId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = response.parse()
            assert_matches_type(BrowserSessionRetrieveArtifactResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_artifact(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.with_raw_response.retrieve_artifact(
                artifact_id="artifactId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.browser_sessions.with_raw_response.retrieve_artifact(
                artifact_id="",
                id="id",
            )


class TestAsyncBrowserSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.create(
            policy={"allowed_domains": ["example.com"]},
        )
        assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.create(
            policy={"allowed_domains": ["example.com"]},
            idempotency_key="x",
            limits={
                "idle_timeout_s": 30,
                "lifetime_s": 60,
            },
            metadata={},
        )
        assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.with_raw_response.create(
            policy={"allowed_domains": ["example.com"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = await response.parse()
        assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.with_streaming_response.create(
            policy={"allowed_domains": ["example.com"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = await response.parse()
            assert_matches_type(BrowserSessionCreateResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.retrieve(
            "id",
        )
        assert_matches_type(BrowserSessionRetrieveResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = await response.parse()
        assert_matches_type(BrowserSessionRetrieveResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = await response.parse()
            assert_matches_type(BrowserSessionRetrieveResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.list()
        assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.list(
            status="provisioning",
        )
        assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = await response.parse()
        assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = await response.parse()
            assert_matches_type(BrowserSessionListResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.delete(
            "id",
        )
        assert_matches_type(BrowserSessionDeleteResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = await response.parse()
        assert_matches_type(BrowserSessionDeleteResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = await response.parse()
            assert_matches_type(BrowserSessionDeleteResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_artifact(self, async_client: AsyncTelnyx) -> None:
        browser_session = await async_client.browser_sessions.retrieve_artifact(
            artifact_id="artifactId",
            id="id",
        )
        assert_matches_type(BrowserSessionRetrieveArtifactResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_artifact(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.with_raw_response.retrieve_artifact(
            artifact_id="artifactId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_session = await response.parse()
        assert_matches_type(BrowserSessionRetrieveArtifactResponse, browser_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_artifact(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.with_streaming_response.retrieve_artifact(
            artifact_id="artifactId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_session = await response.parse()
            assert_matches_type(BrowserSessionRetrieveArtifactResponse, browser_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_artifact(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.with_raw_response.retrieve_artifact(
                artifact_id="artifactId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.browser_sessions.with_raw_response.retrieve_artifact(
                artifact_id="",
                id="id",
            )
