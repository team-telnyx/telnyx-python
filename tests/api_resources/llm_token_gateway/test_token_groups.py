# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.llm_token_gateway import (
    TokenGroup,
    TokenGroupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
            blocked=True,
            budget_duration="1d",
            cache_ttl=1,
            fallbacks={"Kimi-K3": ["GLM-5.3-Flash"]},
            guardrails={
                "dlp": {
                    "profiles": ["financial"],
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "secrets": {
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "streaming": "buffered",
            },
            max_budget=0,
            max_parallel_requests=20,
            provider_key_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            retries={
                "max_attempts": 2,
                "backoff": "exponential",
                "request_timeout_ms": 10000,
                "retry_delay_ms": 250,
            },
            rpm_limit=0,
            tpm_limit=0,
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_groups.with_raw_response.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = response.parse()
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_groups.with_streaming_response.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = response.parse()
            assert_matches_type(TokenGroupResponse, token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_groups.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = response.parse()
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_groups.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = response.parse()
            assert_matches_type(TokenGroupResponse, token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.llm_token_gateway.token_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            blocked=True,
            budget_duration="1d",
            cache_ttl=1,
            fallbacks={"Kimi-K3": ["GLM-5.3-Flash"]},
            guardrails={
                "dlp": {
                    "profiles": ["financial"],
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "secrets": {
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "streaming": "buffered",
            },
            max_budget=0,
            max_parallel_requests=20,
            name="support-backend",
            provider_key_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            retries={
                "max_attempts": 2,
                "backoff": "exponential",
                "request_timeout_ms": 10000,
                "retry_delay_ms": 250,
            },
            rpm_limit=0,
            tpm_limit=0,
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_groups.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = response.parse()
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_groups.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = response.parse()
            assert_matches_type(TokenGroupResponse, token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.llm_token_gateway.token_groups.with_raw_response.update(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.list()
        assert_matches_type(SyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.list(
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
        )
        assert_matches_type(SyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        token_group = client.llm_token_gateway.token_groups.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert token_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_groups.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = response.parse()
        assert token_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_groups.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = response.parse()
            assert token_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.llm_token_gateway.token_groups.with_raw_response.delete(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )


class TestAsyncTokenGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
            blocked=True,
            budget_duration="1d",
            cache_ttl=1,
            fallbacks={"Kimi-K3": ["GLM-5.3-Flash"]},
            guardrails={
                "dlp": {
                    "profiles": ["financial"],
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "secrets": {
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "streaming": "buffered",
            },
            max_budget=0,
            max_parallel_requests=20,
            provider_key_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            retries={
                "max_attempts": 2,
                "backoff": "exponential",
                "request_timeout_ms": 10000,
                "retry_delay_ms": 250,
            },
            rpm_limit=0,
            tpm_limit=0,
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_groups.with_raw_response.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = await response.parse()
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_groups.with_streaming_response.create(
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            name="support-backend",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = await response.parse()
            assert_matches_type(TokenGroupResponse, token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_groups.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = await response.parse()
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_groups.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = await response.parse()
            assert_matches_type(TokenGroupResponse, token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.llm_token_gateway.token_groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
            allowed_models=["Kimi-K3", "GLM-5.3-Flash"],
            blocked=True,
            budget_duration="1d",
            cache_ttl=1,
            fallbacks={"Kimi-K3": ["GLM-5.3-Flash"]},
            guardrails={
                "dlp": {
                    "profiles": ["financial"],
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "secrets": {
                    "prompt": "ignore",
                    "response": "ignore",
                },
                "streaming": "buffered",
            },
            max_budget=0,
            max_parallel_requests=20,
            name="support-backend",
            provider_key_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            retries={
                "max_attempts": 2,
                "backoff": "exponential",
                "request_timeout_ms": 10000,
                "retry_delay_ms": 250,
            },
            rpm_limit=0,
            tpm_limit=0,
        )
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_groups.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = await response.parse()
        assert_matches_type(TokenGroupResponse, token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_groups.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = await response.parse()
            assert_matches_type(TokenGroupResponse, token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.llm_token_gateway.token_groups.with_raw_response.update(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.list()
        assert_matches_type(AsyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.list(
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
        )
        assert_matches_type(AsyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[TokenGroup], token_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        token_group = await async_client.llm_token_gateway.token_groups.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert token_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_groups.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_group = await response.parse()
        assert token_group is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_groups.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_group = await response.parse()
            assert token_group is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.llm_token_gateway.token_groups.with_raw_response.delete(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )
