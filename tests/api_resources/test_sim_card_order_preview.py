# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import SimCardOrderPreviewPreviewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimCardOrderPreview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_preview(self, client: Telnyx) -> None:
        sim_card_order_preview = client.sim_card_order_preview.preview(
            address_id="1293384261075731499",
            quantity=21,
        )
        assert_matches_type(SimCardOrderPreviewPreviewResponse, sim_card_order_preview, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_preview(self, client: Telnyx) -> None:
        response = client.sim_card_order_preview.with_raw_response.preview(
            address_id="1293384261075731499",
            quantity=21,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order_preview = response.parse()
        assert_matches_type(SimCardOrderPreviewPreviewResponse, sim_card_order_preview, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_preview(self, client: Telnyx) -> None:
        with client.sim_card_order_preview.with_streaming_response.preview(
            address_id="1293384261075731499",
            quantity=21,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order_preview = response.parse()
            assert_matches_type(SimCardOrderPreviewPreviewResponse, sim_card_order_preview, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimCardOrderPreview:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncTelnyx) -> None:
        sim_card_order_preview = await async_client.sim_card_order_preview.preview(
            address_id="1293384261075731499",
            quantity=21,
        )
        assert_matches_type(SimCardOrderPreviewPreviewResponse, sim_card_order_preview, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_order_preview.with_raw_response.preview(
            address_id="1293384261075731499",
            quantity=21,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card_order_preview = await response.parse()
        assert_matches_type(SimCardOrderPreviewPreviewResponse, sim_card_order_preview, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_order_preview.with_streaming_response.preview(
            address_id="1293384261075731499",
            quantity=21,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card_order_preview = await response.parse()
            assert_matches_type(SimCardOrderPreviewPreviewResponse, sim_card_order_preview, path=["response"])

        assert cast(Any, response.is_closed) is True
