# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.sim_card_groups import (
    ActionListResponse,
    ActionRetrieveResponse,
    ActionSetWirelessBlocklistResponse,
    ActionRemoveWirelessBlocklistResponse,
    ActionSetPrivateWirelessGatewayResponse,
    ActionRemovePrivateWirelessGatewayResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sim_card_groups.actions.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sim_card_groups.actions.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.actions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.list()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.list(
            filter_sim_card_group_id="47a1c2b0-cc7b-4ab1-bb98-b33fb0fc61b9",
            filter_status="in-progress",
            filter_type="set_private_wireless_gateway",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.sim_card_groups.actions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.sim_card_groups.actions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_private_wireless_gateway(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.remove_private_wireless_gateway(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionRemovePrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_private_wireless_gateway(self, client: Telnyx) -> None:
        response = client.sim_card_groups.actions.with_raw_response.remove_private_wireless_gateway(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRemovePrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_private_wireless_gateway(self, client: Telnyx) -> None:
        with client.sim_card_groups.actions.with_streaming_response.remove_private_wireless_gateway(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRemovePrivateWirelessGatewayResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_private_wireless_gateway(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.actions.with_raw_response.remove_private_wireless_gateway(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_wireless_blocklist(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.remove_wireless_blocklist(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionRemoveWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_wireless_blocklist(self, client: Telnyx) -> None:
        response = client.sim_card_groups.actions.with_raw_response.remove_wireless_blocklist(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRemoveWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_wireless_blocklist(self, client: Telnyx) -> None:
        with client.sim_card_groups.actions.with_streaming_response.remove_wireless_blocklist(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRemoveWirelessBlocklistResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_wireless_blocklist(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.actions.with_raw_response.remove_wireless_blocklist(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_private_wireless_gateway(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.set_private_wireless_gateway(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionSetPrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_private_wireless_gateway(self, client: Telnyx) -> None:
        response = client.sim_card_groups.actions.with_raw_response.set_private_wireless_gateway(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSetPrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_private_wireless_gateway(self, client: Telnyx) -> None:
        with client.sim_card_groups.actions.with_streaming_response.set_private_wireless_gateway(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSetPrivateWirelessGatewayResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set_private_wireless_gateway(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.actions.with_raw_response.set_private_wireless_gateway(
                id="",
                private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_wireless_blocklist(self, client: Telnyx) -> None:
        action = client.sim_card_groups.actions.set_wireless_blocklist(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionSetWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_wireless_blocklist(self, client: Telnyx) -> None:
        response = client.sim_card_groups.actions.with_raw_response.set_wireless_blocklist(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSetWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_wireless_blocklist(self, client: Telnyx) -> None:
        with client.sim_card_groups.actions.with_streaming_response.set_wireless_blocklist(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSetWirelessBlocklistResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set_wireless_blocklist(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_card_groups.actions.with_raw_response.set_wireless_blocklist(
                id="",
                wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.actions.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.actions.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.actions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.list()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.list(
            filter_sim_card_group_id="47a1c2b0-cc7b-4ab1-bb98-b33fb0fc61b9",
            filter_status="in-progress",
            filter_type="set_private_wireless_gateway",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.actions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.actions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.remove_private_wireless_gateway(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionRemovePrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.actions.with_raw_response.remove_private_wireless_gateway(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRemovePrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.actions.with_streaming_response.remove_private_wireless_gateway(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRemovePrivateWirelessGatewayResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.actions.with_raw_response.remove_private_wireless_gateway(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.remove_wireless_blocklist(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionRemoveWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.actions.with_raw_response.remove_wireless_blocklist(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRemoveWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.actions.with_streaming_response.remove_wireless_blocklist(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRemoveWirelessBlocklistResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.actions.with_raw_response.remove_wireless_blocklist(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.set_private_wireless_gateway(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionSetPrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.actions.with_raw_response.set_private_wireless_gateway(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSetPrivateWirelessGatewayResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.actions.with_streaming_response.set_private_wireless_gateway(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSetPrivateWirelessGatewayResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set_private_wireless_gateway(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.actions.with_raw_response.set_private_wireless_gateway(
                id="",
                private_wireless_gateway_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.sim_card_groups.actions.set_wireless_blocklist(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(ActionSetWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_card_groups.actions.with_raw_response.set_wireless_blocklist(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSetWirelessBlocklistResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_card_groups.actions.with_streaming_response.set_wireless_blocklist(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSetWirelessBlocklistResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set_wireless_blocklist(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_card_groups.actions.with_raw_response.set_wireless_blocklist(
                id="",
                wireless_blocklist_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )
