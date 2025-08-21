# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.porting_orders import (
    PhoneNumberConfigurationListResponse,
    PhoneNumberConfigurationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        phone_number_configuration = client.porting_orders.phone_number_configurations.create()
        assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        phone_number_configuration = client.porting_orders.phone_number_configurations.create(
            phone_number_configurations=[
                {
                    "porting_phone_number_id": "927f4687-318c-44bc-9f2f-22a5898143a4",
                    "user_bundle_id": "ff901545-3e27-462a-ba9d-2b34654cab82",
                }
            ],
        )
        assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_configuration = response.parse()
        assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_configuration = response.parse()
            assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number_configuration = client.porting_orders.phone_number_configurations.list()
        assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number_configuration = client.porting_orders.phone_number_configurations.list(
            filter={
                "porting_order_status": ["activation-in-progress"],
                "porting_phone_number": ["5d6f7ede-1961-4717-bfb5-db392c5efc2d"],
                "user_bundle_id": ["5d6f7ede-1961-4717-bfb5-db392c5efc2d"],
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.phone_number_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_configuration = response.parse()
        assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.phone_number_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_configuration = response.parse()
            assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneNumberConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        phone_number_configuration = await async_client.porting_orders.phone_number_configurations.create()
        assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_configuration = await async_client.porting_orders.phone_number_configurations.create(
            phone_number_configurations=[
                {
                    "porting_phone_number_id": "927f4687-318c-44bc-9f2f-22a5898143a4",
                    "user_bundle_id": "ff901545-3e27-462a-ba9d-2b34654cab82",
                }
            ],
        )
        assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_configuration = await response.parse()
        assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_configuration = await response.parse()
            assert_matches_type(PhoneNumberConfigurationCreateResponse, phone_number_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number_configuration = await async_client.porting_orders.phone_number_configurations.list()
        assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_configuration = await async_client.porting_orders.phone_number_configurations.list(
            filter={
                "porting_order_status": ["activation-in-progress"],
                "porting_phone_number": ["5d6f7ede-1961-4717-bfb5-db392c5efc2d"],
                "user_bundle_id": ["5d6f7ede-1961-4717-bfb5-db392c5efc2d"],
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.phone_number_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_configuration = await response.parse()
        assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.phone_number_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_configuration = await response.parse()
            assert_matches_type(PhoneNumberConfigurationListResponse, phone_number_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
