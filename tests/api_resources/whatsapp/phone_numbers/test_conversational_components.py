# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.whatsapp.phone_numbers import (
    ConversationalComponentListResponse,
    ConversationalComponentPatchAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversationalComponents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        conversational_component = client.whatsapp.phone_numbers.conversational_components.list(
            "phone_number",
        )
        assert_matches_type(ConversationalComponentListResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.conversational_components.with_raw_response.list(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversational_component = response.parse()
        assert_matches_type(ConversationalComponentListResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.conversational_components.with_streaming_response.list(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversational_component = response.parse()
            assert_matches_type(ConversationalComponentListResponse, conversational_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.conversational_components.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: Telnyx) -> None:
        conversational_component = client.whatsapp.phone_numbers.conversational_components.patch_all(
            phone_number="phone_number",
        )
        assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all_with_all_params(self, client: Telnyx) -> None:
        conversational_component = client.whatsapp.phone_numbers.conversational_components.patch_all(
            phone_number="phone_number",
            commands=[
                {
                    "command": "command",
                    "description": "description",
                }
            ],
            ice_breakers=["string"],
        )
        assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.conversational_components.with_raw_response.patch_all(
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversational_component = response.parse()
        assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.conversational_components.with_streaming_response.patch_all(
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversational_component = response.parse()
            assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch_all(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.conversational_components.with_raw_response.patch_all(
                phone_number="",
            )


class TestAsyncConversationalComponents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        conversational_component = await async_client.whatsapp.phone_numbers.conversational_components.list(
            "phone_number",
        )
        assert_matches_type(ConversationalComponentListResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.conversational_components.with_raw_response.list(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversational_component = await response.parse()
        assert_matches_type(ConversationalComponentListResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.conversational_components.with_streaming_response.list(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversational_component = await response.parse()
            assert_matches_type(ConversationalComponentListResponse, conversational_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.conversational_components.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncTelnyx) -> None:
        conversational_component = await async_client.whatsapp.phone_numbers.conversational_components.patch_all(
            phone_number="phone_number",
        )
        assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all_with_all_params(self, async_client: AsyncTelnyx) -> None:
        conversational_component = await async_client.whatsapp.phone_numbers.conversational_components.patch_all(
            phone_number="phone_number",
            commands=[
                {
                    "command": "command",
                    "description": "description",
                }
            ],
            ice_breakers=["string"],
        )
        assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.conversational_components.with_raw_response.patch_all(
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversational_component = await response.parse()
        assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.conversational_components.with_streaming_response.patch_all(
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversational_component = await response.parse()
            assert_matches_type(ConversationalComponentPatchAllResponse, conversational_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch_all(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.conversational_components.with_raw_response.patch_all(
                phone_number="",
            )
