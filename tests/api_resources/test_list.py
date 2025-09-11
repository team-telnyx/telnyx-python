# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import ListRetrieveAllResponse, ListRetrieveByZoneResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestList:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_all(self, client: Telnyx) -> None:
        list_ = client.list.retrieve_all()
        assert_matches_type(ListRetrieveAllResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_all(self, client: Telnyx) -> None:
        response = client.list.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveAllResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_all(self, client: Telnyx) -> None:
        with client.list.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveAllResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_by_zone(self, client: Telnyx) -> None:
        list_ = client.list.retrieve_by_zone(
            "channel_zone_id",
        )
        assert_matches_type(ListRetrieveByZoneResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_zone(self, client: Telnyx) -> None:
        response = client.list.with_raw_response.retrieve_by_zone(
            "channel_zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveByZoneResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_zone(self, client: Telnyx) -> None:
        with client.list.with_streaming_response.retrieve_by_zone(
            "channel_zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveByZoneResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_by_zone(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_zone_id` but received ''"):
            client.list.with_raw_response.retrieve_by_zone(
                "",
            )


class TestAsyncList:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_all(self, async_client: AsyncTelnyx) -> None:
        list_ = await async_client.list.retrieve_all()
        assert_matches_type(ListRetrieveAllResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.list.with_raw_response.retrieve_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveAllResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.list.with_streaming_response.retrieve_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveAllResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_by_zone(self, async_client: AsyncTelnyx) -> None:
        list_ = await async_client.list.retrieve_by_zone(
            "channel_zone_id",
        )
        assert_matches_type(ListRetrieveByZoneResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_zone(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.list.with_raw_response.retrieve_by_zone(
            "channel_zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveByZoneResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_zone(self, async_client: AsyncTelnyx) -> None:
        async with async_client.list.with_streaming_response.retrieve_by_zone(
            "channel_zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveByZoneResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_by_zone(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_zone_id` but received ''"):
            await async_client.list.with_raw_response.retrieve_by_zone(
                "",
            )
