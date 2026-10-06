# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.whatsapp.phone_numbers import (
    CallingRoutingListResponse,
    CallingRoutingPatchAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallingRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        calling_routing = client.whatsapp.phone_numbers.calling_routing.list(
            "+13125550100",
        )
        assert_matches_type(CallingRoutingListResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.calling_routing.with_raw_response.list(
            "+13125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_routing = response.parse()
        assert_matches_type(CallingRoutingListResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.calling_routing.with_streaming_response.list(
            "+13125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_routing = response.parse()
            assert_matches_type(CallingRoutingListResponse, calling_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.phone_numbers.calling_routing.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: Telnyx) -> None:
        calling_routing = client.whatsapp.phone_numbers.calling_routing.patch_all(
            id="+13125550100",
            connection_id="1234567890",
        )
        assert_matches_type(CallingRoutingPatchAllResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.calling_routing.with_raw_response.patch_all(
            id="+13125550100",
            connection_id="1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_routing = response.parse()
        assert_matches_type(CallingRoutingPatchAllResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.calling_routing.with_streaming_response.patch_all(
            id="+13125550100",
            connection_id="1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_routing = response.parse()
            assert_matches_type(CallingRoutingPatchAllResponse, calling_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.phone_numbers.calling_routing.with_raw_response.patch_all(
                id="",
                connection_id="1234567890",
            )


class TestAsyncCallingRouting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        calling_routing = await async_client.whatsapp.phone_numbers.calling_routing.list(
            "+13125550100",
        )
        assert_matches_type(CallingRoutingListResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.calling_routing.with_raw_response.list(
            "+13125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_routing = await response.parse()
        assert_matches_type(CallingRoutingListResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.calling_routing.with_streaming_response.list(
            "+13125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_routing = await response.parse()
            assert_matches_type(CallingRoutingListResponse, calling_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.phone_numbers.calling_routing.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncTelnyx) -> None:
        calling_routing = await async_client.whatsapp.phone_numbers.calling_routing.patch_all(
            id="+13125550100",
            connection_id="1234567890",
        )
        assert_matches_type(CallingRoutingPatchAllResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.calling_routing.with_raw_response.patch_all(
            id="+13125550100",
            connection_id="1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_routing = await response.parse()
        assert_matches_type(CallingRoutingPatchAllResponse, calling_routing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.calling_routing.with_streaming_response.patch_all(
            id="+13125550100",
            connection_id="1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_routing = await response.parse()
            assert_matches_type(CallingRoutingPatchAllResponse, calling_routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.phone_numbers.calling_routing.with_raw_response.patch_all(
                id="",
                connection_id="1234567890",
            )
