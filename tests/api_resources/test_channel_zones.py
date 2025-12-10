# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ChannelZoneListResponse,
    ChannelZoneUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChannelZones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        channel_zone = client.channel_zones.update(
            channel_zone_id="channel_zone_id",
            channels=0,
        )
        assert_matches_type(ChannelZoneUpdateResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.channel_zones.with_raw_response.update(
            channel_zone_id="channel_zone_id",
            channels=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_zone = response.parse()
        assert_matches_type(ChannelZoneUpdateResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.channel_zones.with_streaming_response.update(
            channel_zone_id="channel_zone_id",
            channels=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_zone = response.parse()
            assert_matches_type(ChannelZoneUpdateResponse, channel_zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_zone_id` but received ''"):
            client.channel_zones.with_raw_response.update(
                channel_zone_id="",
                channels=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        channel_zone = client.channel_zones.list()
        assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        channel_zone = client.channel_zones.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.channel_zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_zone = response.parse()
        assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.channel_zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_zone = response.parse()
            assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChannelZones:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        channel_zone = await async_client.channel_zones.update(
            channel_zone_id="channel_zone_id",
            channels=0,
        )
        assert_matches_type(ChannelZoneUpdateResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.channel_zones.with_raw_response.update(
            channel_zone_id="channel_zone_id",
            channels=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_zone = await response.parse()
        assert_matches_type(ChannelZoneUpdateResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.channel_zones.with_streaming_response.update(
            channel_zone_id="channel_zone_id",
            channels=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_zone = await response.parse()
            assert_matches_type(ChannelZoneUpdateResponse, channel_zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_zone_id` but received ''"):
            await async_client.channel_zones.with_raw_response.update(
                channel_zone_id="",
                channels=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        channel_zone = await async_client.channel_zones.list()
        assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        channel_zone = await async_client.channel_zones.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.channel_zones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        channel_zone = await response.parse()
        assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.channel_zones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            channel_zone = await response.parse()
            assert_matches_type(ChannelZoneListResponse, channel_zone, path=["response"])

        assert cast(Any, response.is_closed) is True
