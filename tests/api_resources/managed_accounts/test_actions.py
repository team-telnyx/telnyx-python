# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.managed_accounts import ActionEnableResponse, ActionDisableResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_disable(self, client: Telnyx) -> None:
        action = client.managed_accounts.actions.disable(
            "id",
        )
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Telnyx) -> None:
        response = client.managed_accounts.actions.with_raw_response.disable(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Telnyx) -> None:
        with client.managed_accounts.actions.with_streaming_response.disable(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionDisableResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.managed_accounts.actions.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enable(self, client: Telnyx) -> None:
        action = client.managed_accounts.actions.enable(
            id="id",
        )
        assert_matches_type(ActionEnableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enable_with_all_params(self, client: Telnyx) -> None:
        action = client.managed_accounts.actions.enable(
            id="id",
            reenable_all_connections=True,
        )
        assert_matches_type(ActionEnableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Telnyx) -> None:
        response = client.managed_accounts.actions.with_raw_response.enable(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionEnableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Telnyx) -> None:
        with client.managed_accounts.actions.with_streaming_response.enable(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionEnableResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.managed_accounts.actions.with_raw_response.enable(
                id="",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.managed_accounts.actions.disable(
            "id",
        )
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.actions.with_raw_response.disable(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.actions.with_streaming_response.disable(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionDisableResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.managed_accounts.actions.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.managed_accounts.actions.enable(
            id="id",
        )
        assert_matches_type(ActionEnableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enable_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.managed_accounts.actions.enable(
            id="id",
            reenable_all_connections=True,
        )
        assert_matches_type(ActionEnableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.managed_accounts.actions.with_raw_response.enable(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionEnableResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncTelnyx) -> None:
        async with async_client.managed_accounts.actions.with_streaming_response.enable(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionEnableResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.managed_accounts.actions.with_raw_response.enable(
                id="",
            )
