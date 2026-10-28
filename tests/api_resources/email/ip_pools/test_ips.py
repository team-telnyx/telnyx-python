# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.email.ip_pools import IPCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        ip = client.email.ip_pools.ips.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
        )
        assert_matches_type(IPCreateResponse, ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        ip = client.email.ip_pools.ips.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
            weight=100,
        )
        assert_matches_type(IPCreateResponse, ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.email.ip_pools.ips.with_raw_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(IPCreateResponse, ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.email.ip_pools.ips.with_streaming_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(IPCreateResponse, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email.ip_pools.ips.with_raw_response.create(
                id="",
                dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        ip = client.email.ip_pools.ips.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert ip is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Telnyx) -> None:
        ip = client.email.ip_pools.ips.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            drain=True,
            force=True,
        )
        assert ip is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.email.ip_pools.ips.with_raw_response.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert ip is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.email.ip_pools.ips.with_streaming_response.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert ip is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email.ip_pools.ips.with_raw_response.delete(
                ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_id` but received ''"):
            client.email.ip_pools.ips.with_raw_response.delete(
                ip_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncIPs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        ip = await async_client.email.ip_pools.ips.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
        )
        assert_matches_type(IPCreateResponse, ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ip = await async_client.email.ip_pools.ips.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
            weight=100,
        )
        assert_matches_type(IPCreateResponse, ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.ip_pools.ips.with_raw_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(IPCreateResponse, ip, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.ip_pools.ips.with_streaming_response.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(IPCreateResponse, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email.ip_pools.ips.with_raw_response.create(
                id="",
                dedicated_ip_id="6a7f9a30-1234-4b5c-8d9e-0f1a2b3c4d5e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        ip = await async_client.email.ip_pools.ips.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert ip is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncTelnyx) -> None:
        ip = await async_client.email.ip_pools.ips.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            drain=True,
            force=True,
        )
        assert ip is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.email.ip_pools.ips.with_raw_response.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert ip is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.email.ip_pools.ips.with_streaming_response.delete(
            ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert ip is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email.ip_pools.ips.with_raw_response.delete(
                ip_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_id` but received ''"):
            await async_client.email.ip_pools.ips.with_raw_response.delete(
                ip_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
