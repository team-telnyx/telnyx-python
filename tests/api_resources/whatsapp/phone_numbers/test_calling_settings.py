# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.whatsapp.phone_numbers import (
    CallingSettingUpdateResponse,
    CallingSettingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallingSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        calling_setting = client.whatsapp.phone_numbers.calling_settings.retrieve(
            "phone_number",
        )
        assert_matches_type(CallingSettingRetrieveResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.calling_settings.with_raw_response.retrieve(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_setting = response.parse()
        assert_matches_type(CallingSettingRetrieveResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.calling_settings.with_streaming_response.retrieve(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_setting = response.parse()
            assert_matches_type(CallingSettingRetrieveResponse, calling_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.calling_settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        calling_setting = client.whatsapp.phone_numbers.calling_settings.update(
            phone_number="phone_number",
            enabled=True,
        )
        assert_matches_type(CallingSettingUpdateResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.calling_settings.with_raw_response.update(
            phone_number="phone_number",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_setting = response.parse()
        assert_matches_type(CallingSettingUpdateResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.calling_settings.with_streaming_response.update(
            phone_number="phone_number",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_setting = response.parse()
            assert_matches_type(CallingSettingUpdateResponse, calling_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.calling_settings.with_raw_response.update(
                phone_number="",
                enabled=True,
            )


class TestAsyncCallingSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        calling_setting = await async_client.whatsapp.phone_numbers.calling_settings.retrieve(
            "phone_number",
        )
        assert_matches_type(CallingSettingRetrieveResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.calling_settings.with_raw_response.retrieve(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_setting = await response.parse()
        assert_matches_type(CallingSettingRetrieveResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.calling_settings.with_streaming_response.retrieve(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_setting = await response.parse()
            assert_matches_type(CallingSettingRetrieveResponse, calling_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.calling_settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        calling_setting = await async_client.whatsapp.phone_numbers.calling_settings.update(
            phone_number="phone_number",
            enabled=True,
        )
        assert_matches_type(CallingSettingUpdateResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.calling_settings.with_raw_response.update(
            phone_number="phone_number",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling_setting = await response.parse()
        assert_matches_type(CallingSettingUpdateResponse, calling_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.calling_settings.with_streaming_response.update(
            phone_number="phone_number",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling_setting = await response.parse()
            assert_matches_type(CallingSettingUpdateResponse, calling_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.calling_settings.with_raw_response.update(
                phone_number="",
                enabled=True,
            )
