# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SimCardListResponse,
    SimCardDeleteResponse,
    SimCardUpdateResponse,
    SimCardRetrieveResponse,
    SimCardGetPublicIPResponse,
    SimCardGetDeviceDetailsResponse,
    SimCardGetActivationCodeResponse,
    SimCardListWirelessConnectivityLogsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            include_pin_puk_codes=True,
            include_sim_card_group=True,
        )
        assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            authorized_imeis=["106516771852751", "534051870479563", "508821468377961"],
            data_limit={
                "amount": "2048.1",
                "unit": "MB",
            },
            sim_card_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            status={},
            tags=["personal", "customers", "active-customers"],
        )
        assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.list()
        assert_matches_type(SimCardListResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.list(
            filter={
                "iccid": "89310410106543789301",
                "status": ["enabled"],
                "tags": ["personal", "customers", "active-customers"],
            },
            filter_sim_card_group_id="47a1c2b0-cc7b-4ab1-bb98-b33fb0fc61b9",
            include_sim_card_group=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort="current_billing_period_consumed_data.amount",
        )
        assert_matches_type(SimCardListResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardListResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardListResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            report_lost=True,
        )
        assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_activation_code(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.get_activation_code(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGetActivationCodeResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_activation_code(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.get_activation_code(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardGetActivationCodeResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_activation_code(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.get_activation_code(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardGetActivationCodeResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_activation_code(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.get_activation_code(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_device_details(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.get_device_details(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGetDeviceDetailsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_device_details(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.get_device_details(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardGetDeviceDetailsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_device_details(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.get_device_details(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardGetDeviceDetailsResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_device_details(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.get_device_details(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_public_ip(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.get_public_ip(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGetPublicIPResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_public_ip(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.get_public_ip(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardGetPublicIPResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_public_ip(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.get_public_ip(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardGetPublicIPResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_public_ip(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.get_public_ip(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_wireless_connectivity_logs(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_wireless_connectivity_logs_with_all_params(self, client: Telnyx) -> None:
        sim_card = client.sim_cards.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_wireless_connectivity_logs(self, client: Telnyx) -> None:
        response = client.sim_cards.with_raw_response.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = response.parse()
        assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_wireless_connectivity_logs(self, client: Telnyx) -> None:
        with client.sim_cards.with_streaming_response.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = response.parse()
            assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_wireless_connectivity_logs(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sim_cards.with_raw_response.list_wireless_connectivity_logs(
                id="",
            )


class TestAsyncSimCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            include_pin_puk_codes=True,
            include_sim_card_group=True,
        )
        assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.retrieve(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardRetrieveResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            authorized_imeis=["106516771852751", "534051870479563", "508821468377961"],
            data_limit={
                "amount": "2048.1",
                "unit": "MB",
            },
            sim_card_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            status={},
            tags=["personal", "customers", "active-customers"],
        )
        assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardUpdateResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.list()
        assert_matches_type(SimCardListResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.list(
            filter={
                "iccid": "89310410106543789301",
                "status": ["enabled"],
                "tags": ["personal", "customers", "active-customers"],
            },
            filter_sim_card_group_id="47a1c2b0-cc7b-4ab1-bb98-b33fb0fc61b9",
            include_sim_card_group=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort="current_billing_period_consumed_data.amount",
        )
        assert_matches_type(SimCardListResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardListResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardListResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            report_lost=True,
        )
        assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.delete(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardDeleteResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_activation_code(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.get_activation_code(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGetActivationCodeResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_activation_code(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.get_activation_code(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardGetActivationCodeResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_activation_code(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.get_activation_code(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardGetActivationCodeResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_activation_code(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.get_activation_code(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_device_details(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.get_device_details(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGetDeviceDetailsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_device_details(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.get_device_details(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardGetDeviceDetailsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_device_details(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.get_device_details(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardGetDeviceDetailsResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_device_details(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.get_device_details(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_public_ip(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.get_public_ip(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardGetPublicIPResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_public_ip(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.get_public_ip(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardGetPublicIPResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_public_ip(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.get_public_ip(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardGetPublicIPResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_public_ip(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.get_public_ip(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_wireless_connectivity_logs(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_wireless_connectivity_logs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sim_card = await async_client.sim_cards.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_wireless_connectivity_logs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sim_cards.with_raw_response.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sim_card = await response.parse()
        assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_wireless_connectivity_logs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sim_cards.with_streaming_response.list_wireless_connectivity_logs(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sim_card = await response.parse()
            assert_matches_type(SimCardListWirelessConnectivityLogsResponse, sim_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_wireless_connectivity_logs(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sim_cards.with_raw_response.list_wireless_connectivity_logs(
                id="",
            )
