# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOsr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_attributes(self, client: Telnyx) -> None:
        osr = client.campaign.osr.get_attributes(
            "campaignId",
        )
        assert_matches_type(object, osr, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_attributes(self, client: Telnyx) -> None:
        response = client.campaign.osr.with_raw_response.get_attributes(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osr = response.parse()
        assert_matches_type(object, osr, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_attributes(self, client: Telnyx) -> None:
        with client.campaign.osr.with_streaming_response.get_attributes(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osr = response.parse()
            assert_matches_type(object, osr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_attributes(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.campaign.osr.with_raw_response.get_attributes(
                "",
            )


class TestAsyncOsr:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_attributes(self, async_client: AsyncTelnyx) -> None:
        osr = await async_client.campaign.osr.get_attributes(
            "campaignId",
        )
        assert_matches_type(object, osr, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_attributes(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.campaign.osr.with_raw_response.get_attributes(
            "campaignId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osr = await response.parse()
        assert_matches_type(object, osr, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_attributes(self, async_client: AsyncTelnyx) -> None:
        async with async_client.campaign.osr.with_streaming_response.get_attributes(
            "campaignId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osr = await response.parse()
            assert_matches_type(object, osr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_attributes(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.campaign.osr.with_raw_response.get_attributes(
                "",
            )
