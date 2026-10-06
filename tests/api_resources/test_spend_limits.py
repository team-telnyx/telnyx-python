# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SpendLimitResponse,
    SpendLimitListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpendLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.create(
            amount=100,
            product="inference",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.create(
            amount=100,
            product="inference",
            period="daily",
            reason="Team budget",
            unlimited=False,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Telnyx) -> None:
        response = client.spend_limits.with_raw_response.create(
            amount=100,
            product="inference",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Telnyx) -> None:
        with client.spend_limits.with_streaming_response.create(
            amount=100,
            product="inference",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.create(
            product="inference",
            unlimited=True,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.create(
            product="inference",
            unlimited=True,
            period="daily",
            reason="Team budget",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Telnyx) -> None:
        response = client.spend_limits.with_raw_response.create(
            product="inference",
            unlimited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Telnyx) -> None:
        with client.spend_limits.with_streaming_response.create(
            product="inference",
            unlimited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.update(
            product="inference",
            amount=100,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.update(
            product="inference",
            amount=100,
            period="daily",
            reason="Raised for the product launch",
            unlimited=False,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Telnyx) -> None:
        response = client.spend_limits.with_raw_response.update(
            product="inference",
            amount=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Telnyx) -> None:
        with client.spend_limits.with_streaming_response.update(
            product="inference",
            amount=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product` but received ''"):
            client.spend_limits.with_raw_response.update(
                product="",
                amount=100,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.update(
            product="inference",
            unlimited=True,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.update(
            product="inference",
            unlimited=True,
            period="daily",
            reason="Raised for the product launch",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Telnyx) -> None:
        response = client.spend_limits.with_raw_response.update(
            product="inference",
            unlimited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Telnyx) -> None:
        with client.spend_limits.with_streaming_response.update(
            product="inference",
            unlimited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product` but received ''"):
            client.spend_limits.with_raw_response.update(
                product="",
                unlimited=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.list()
        assert_matches_type(SpendLimitListResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.spend_limits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = response.parse()
        assert_matches_type(SpendLimitListResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.spend_limits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = response.parse()
            assert_matches_type(SpendLimitListResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.delete(
            product="inference",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Telnyx) -> None:
        spend_limit = client.spend_limits.delete(
            product="inference",
            period="daily",
            reason="reason",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.spend_limits.with_raw_response.delete(
            product="inference",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.spend_limits.with_streaming_response.delete(
            product="inference",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product` but received ''"):
            client.spend_limits.with_raw_response.delete(
                product="",
            )


class TestAsyncSpendLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.create(
            amount=100,
            product="inference",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.create(
            amount=100,
            product="inference",
            period="daily",
            reason="Team budget",
            unlimited=False,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.spend_limits.with_raw_response.create(
            amount=100,
            product="inference",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = await response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.spend_limits.with_streaming_response.create(
            amount=100,
            product="inference",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = await response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.create(
            product="inference",
            unlimited=True,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.create(
            product="inference",
            unlimited=True,
            period="daily",
            reason="Team budget",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.spend_limits.with_raw_response.create(
            product="inference",
            unlimited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = await response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.spend_limits.with_streaming_response.create(
            product="inference",
            unlimited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = await response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.update(
            product="inference",
            amount=100,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.update(
            product="inference",
            amount=100,
            period="daily",
            reason="Raised for the product launch",
            unlimited=False,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.spend_limits.with_raw_response.update(
            product="inference",
            amount=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = await response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.spend_limits.with_streaming_response.update(
            product="inference",
            amount=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = await response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product` but received ''"):
            await async_client.spend_limits.with_raw_response.update(
                product="",
                amount=100,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.update(
            product="inference",
            unlimited=True,
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.update(
            product="inference",
            unlimited=True,
            period="daily",
            reason="Raised for the product launch",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.spend_limits.with_raw_response.update(
            product="inference",
            unlimited=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = await response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.spend_limits.with_streaming_response.update(
            product="inference",
            unlimited=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = await response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product` but received ''"):
            await async_client.spend_limits.with_raw_response.update(
                product="",
                unlimited=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.list()
        assert_matches_type(SpendLimitListResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.spend_limits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = await response.parse()
        assert_matches_type(SpendLimitListResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.spend_limits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = await response.parse()
            assert_matches_type(SpendLimitListResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.delete(
            product="inference",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncTelnyx) -> None:
        spend_limit = await async_client.spend_limits.delete(
            product="inference",
            period="daily",
            reason="reason",
        )
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.spend_limits.with_raw_response.delete(
            product="inference",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_limit = await response.parse()
        assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.spend_limits.with_streaming_response.delete(
            product="inference",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_limit = await response.parse()
            assert_matches_type(SpendLimitResponse, spend_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product` but received ''"):
            await async_client.spend_limits.with_raw_response.delete(
                product="",
            )
