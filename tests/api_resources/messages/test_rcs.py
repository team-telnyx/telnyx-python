# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.messages import RcGenerateDeeplinkResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRcs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_deeplink(self, client: Telnyx) -> None:
        rc = client.messages.rcs.generate_deeplink(
            agent_id="agent_id",
        )
        assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_deeplink_with_all_params(self, client: Telnyx) -> None:
        rc = client.messages.rcs.generate_deeplink(
            agent_id="agent_id",
            body="body",
            phone_number="phone_number",
        )
        assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_deeplink(self, client: Telnyx) -> None:
        response = client.messages.rcs.with_raw_response.generate_deeplink(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = response.parse()
        assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_deeplink(self, client: Telnyx) -> None:
        with client.messages.rcs.with_streaming_response.generate_deeplink(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = response.parse()
            assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_deeplink(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.messages.rcs.with_raw_response.generate_deeplink(
                agent_id="",
            )


class TestAsyncRcs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_deeplink(self, async_client: AsyncTelnyx) -> None:
        rc = await async_client.messages.rcs.generate_deeplink(
            agent_id="agent_id",
        )
        assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_deeplink_with_all_params(self, async_client: AsyncTelnyx) -> None:
        rc = await async_client.messages.rcs.generate_deeplink(
            agent_id="agent_id",
            body="body",
            phone_number="phone_number",
        )
        assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_deeplink(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messages.rcs.with_raw_response.generate_deeplink(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = await response.parse()
        assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_deeplink(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messages.rcs.with_streaming_response.generate_deeplink(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = await response.parse()
            assert_matches_type(RcGenerateDeeplinkResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_deeplink(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.messages.rcs.with_raw_response.generate_deeplink(
                agent_id="",
            )
