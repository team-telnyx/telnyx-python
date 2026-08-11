# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.collections import (
    SourceListResponse,
    SourceCreateResponse,
    SourceReplaceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        source = client.ai.collections.sources.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
        )
        assert_matches_type(SourceCreateResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        source = client.ai.collections.sources.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
            bucket_id="policy-docs",
        )
        assert_matches_type(SourceCreateResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.collections.sources.with_raw_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceCreateResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.collections.sources.with_streaming_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceCreateResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.sources.with_raw_response.create(
                uuid="",
                source_type="voice",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        source = client.ai.collections.sources.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.collections.sources.with_raw_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.collections.sources.with_streaming_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.sources.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        source = client.ai.collections.sources.delete(
            source_id="42",
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.collections.sources.with_raw_response.delete(
            source_id="42",
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.collections.sources.with_streaming_response.delete(
            source_id="42",
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.sources.with_raw_response.delete(
                source_id="42",
                uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.ai.collections.sources.with_raw_response.delete(
                source_id="",
                uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Telnyx) -> None:
        source = client.ai.collections.sources.replace(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            sources=[{"source_type": "voice"}],
        )
        assert_matches_type(SourceReplaceResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Telnyx) -> None:
        response = client.ai.collections.sources.with_raw_response.replace(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            sources=[{"source_type": "voice"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceReplaceResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Telnyx) -> None:
        with client.ai.collections.sources.with_streaming_response.replace(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            sources=[{"source_type": "voice"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceReplaceResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.ai.collections.sources.with_raw_response.replace(
                uuid="",
                sources=[{"source_type": "voice"}],
            )


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        source = await async_client.ai.collections.sources.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
        )
        assert_matches_type(SourceCreateResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        source = await async_client.ai.collections.sources.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
            bucket_id="policy-docs",
        )
        assert_matches_type(SourceCreateResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.sources.with_raw_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceCreateResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.sources.with_streaming_response.create(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            source_type="voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceCreateResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.sources.with_raw_response.create(
                uuid="",
                source_type="voice",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        source = await async_client.ai.collections.sources.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.sources.with_raw_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceListResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.sources.with_streaming_response.list(
            "6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceListResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.sources.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        source = await async_client.ai.collections.sources.delete(
            source_id="42",
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.sources.with_raw_response.delete(
            source_id="42",
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert source is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.sources.with_streaming_response.delete(
            source_id="42",
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert source is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.sources.with_raw_response.delete(
                source_id="42",
                uuid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.ai.collections.sources.with_raw_response.delete(
                source_id="",
                uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncTelnyx) -> None:
        source = await async_client.ai.collections.sources.replace(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            sources=[{"source_type": "voice"}],
        )
        assert_matches_type(SourceReplaceResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.collections.sources.with_raw_response.replace(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            sources=[{"source_type": "voice"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceReplaceResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.collections.sources.with_streaming_response.replace(
            uuid="6a09ccbd-8f9b-4c3a-9b0e-2f1d3c4b5a6e",
            sources=[{"source_type": "voice"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceReplaceResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.ai.collections.sources.with_raw_response.replace(
                uuid="",
                sources=[{"source_type": "voice"}],
            )
