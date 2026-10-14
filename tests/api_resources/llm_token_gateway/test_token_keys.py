# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.llm_token_gateway import (
    TokenKey,
    TokenKeyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
            allowed_models=["J!Q0Ok0bzJb7"],
            blocked=True,
            budget_duration="1d",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_budget=0.000001,
            max_parallel_requests=5,
            required_end_user_id=True,
            rpm_limit=1,
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tpm_limit=1,
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_keys.with_raw_response.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = response.parse()
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_keys.with_streaming_response.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = response.parse()
            assert_matches_type(TokenKeyResponse, token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_keys.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = response.parse()
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_keys.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = response.parse()
            assert_matches_type(TokenKeyResponse, token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.llm_token_gateway.token_keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
            allowed_models=["J!Q0Ok0bzJb7"],
            blocked=True,
            budget_duration="1d",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_budget=0.000001,
            max_parallel_requests=5,
            name="name",
            required_end_user_id=True,
            rpm_limit=1,
            tpm_limit=1,
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_keys.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = response.parse()
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_keys.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = response.parse()
            assert_matches_type(TokenKeyResponse, token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.llm_token_gateway.token_keys.with_raw_response.update(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.list()
        assert_matches_type(SyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.list(
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        token_key = client.llm_token_gateway.token_keys.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert token_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.llm_token_gateway.token_keys.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = response.parse()
        assert token_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.llm_token_gateway.token_keys.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = response.parse()
            assert token_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.llm_token_gateway.token_keys.with_raw_response.delete(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )


class TestAsyncTokenKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
            allowed_models=["J!Q0Ok0bzJb7"],
            blocked=True,
            budget_duration="1d",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_budget=0.000001,
            max_parallel_requests=5,
            required_end_user_id=True,
            rpm_limit=1,
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tpm_limit=1,
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_keys.with_raw_response.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = await response.parse()
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_keys.with_streaming_response.create(
            name="support-service",
            token_group_id="11111111-1111-4111-8111-111111111111",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = await response.parse()
            assert_matches_type(TokenKeyResponse, token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_keys.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = await response.parse()
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_keys.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = await response.parse()
            assert_matches_type(TokenKeyResponse, token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.llm_token_gateway.token_keys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
            allowed_models=["J!Q0Ok0bzJb7"],
            blocked=True,
            budget_duration="1d",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            max_budget=0.000001,
            max_parallel_requests=5,
            name="name",
            required_end_user_id=True,
            rpm_limit=1,
            tpm_limit=1,
        )
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_keys.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = await response.parse()
        assert_matches_type(TokenKeyResponse, token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_keys.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = await response.parse()
            assert_matches_type(TokenKeyResponse, token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.llm_token_gateway.token_keys.with_raw_response.update(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.list()
        assert_matches_type(AsyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.list(
            page_number=1,
            page_size=1,
            page_snapshot="page[snapshot]",
            token_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_keys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_keys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[TokenKey], token_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        token_key = await async_client.llm_token_gateway.token_keys.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )
        assert token_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.llm_token_gateway.token_keys.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token_key = await response.parse()
        assert token_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.llm_token_gateway.token_keys.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="Idempotency-Key",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token_key = await response.parse()
            assert token_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.llm_token_gateway.token_keys.with_raw_response.delete(
                id="",
                idempotency_key="Idempotency-Key",
                if_match="If-Match",
            )
