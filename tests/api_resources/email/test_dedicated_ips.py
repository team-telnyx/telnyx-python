# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.email import (
    DedicatedIPListResponse,
    DedicatedIPShowResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDedicatedIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
            ip_version="ipv4",
            region="ewr-nj1",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email.dedicated_ips.with_raw_response.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email.dedicated_ips.with_streaming_response.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.email.dedicated_ips.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.email.dedicated_ips.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email.dedicated_ips.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            drain=True,
            force=True,
            pool_id="9b1c4d70-abcd-4e5f-8a9b-0c1d2e3f4a5b",
            warmup={"paused": True},
            warmup_paused=True,
            weight=100,
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.email.dedicated_ips.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.email.dedicated_ips.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email.dedicated_ips.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.list()
        assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.list(
            filter_pool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_region="filter[region]",
            filter_status="provisioning",
        )
        assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.email.dedicated_ips.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = response.parse()
        assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.email.dedicated_ips.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = response.parse()
            assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Telnyx) -> None:
        dedicated_ip = client.email.dedicated_ips.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_drain=True,
            query_force=True,
            query_reason="reason",
            body_drain=True,
            body_force=True,
            body_reason="No longer needed",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email.dedicated_ips.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email.dedicated_ips.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email.dedicated_ips.with_raw_response.delete(
                id="",
            )


class TestAsyncDedicatedIPs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
            ip_version="ipv4",
            region="ewr-nj1",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.dedicated_ips.with_raw_response.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = await response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.dedicated_ips.with_streaming_response.create(
            idempotency_key="8e03978e-40d5-43e8-bc93-6894a57f9326",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = await response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.dedicated_ips.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = await response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.dedicated_ips.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = await response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email.dedicated_ips.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            drain=True,
            force=True,
            pool_id="9b1c4d70-abcd-4e5f-8a9b-0c1d2e3f4a5b",
            warmup={"paused": True},
            warmup_paused=True,
            weight=100,
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.dedicated_ips.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = await response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.dedicated_ips.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = await response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email.dedicated_ips.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.list()
        assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.list(
            filter_pool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter_region="filter[region]",
            filter_status="provisioning",
        )
        assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.dedicated_ips.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = await response.parse()
        assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.dedicated_ips.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = await response.parse()
            assert_matches_type(DedicatedIPListResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dedicated_ip = await async_client.email.dedicated_ips.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query_drain=True,
            query_force=True,
            query_reason="reason",
            body_drain=True,
            body_force=True,
            body_reason="No longer needed",
        )
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.dedicated_ips.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dedicated_ip = await response.parse()
        assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.dedicated_ips.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dedicated_ip = await response.parse()
            assert_matches_type(DedicatedIPShowResponse, dedicated_ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email.dedicated_ips.with_raw_response.delete(
                id="",
            )
