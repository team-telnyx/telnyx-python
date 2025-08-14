# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.phone_numbers import (
    ActionEnableEmergencyResponse,
    ActionVerifyOwnershipResponse,
    ActionChangeBundleStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_change_bundle_status(self, client: Telnyx) -> None:
        action = client.phone_numbers.actions.change_bundle_status(
            id="1293384261075731499",
            bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
        )
        assert_matches_type(ActionChangeBundleStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_change_bundle_status(self, client: Telnyx) -> None:
        response = client.phone_numbers.actions.with_raw_response.change_bundle_status(
            id="1293384261075731499",
            bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionChangeBundleStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_change_bundle_status(self, client: Telnyx) -> None:
        with client.phone_numbers.actions.with_streaming_response.change_bundle_status(
            id="1293384261075731499",
            bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionChangeBundleStatusResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_change_bundle_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.actions.with_raw_response.change_bundle_status(
                id="",
                bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enable_emergency(self, client: Telnyx) -> None:
        action = client.phone_numbers.actions.enable_emergency(
            id="1293384261075731499",
            emergency_address_id="53829456729313",
            emergency_enabled=True,
        )
        assert_matches_type(ActionEnableEmergencyResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enable_emergency(self, client: Telnyx) -> None:
        response = client.phone_numbers.actions.with_raw_response.enable_emergency(
            id="1293384261075731499",
            emergency_address_id="53829456729313",
            emergency_enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionEnableEmergencyResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enable_emergency(self, client: Telnyx) -> None:
        with client.phone_numbers.actions.with_streaming_response.enable_emergency(
            id="1293384261075731499",
            emergency_address_id="53829456729313",
            emergency_enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionEnableEmergencyResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_enable_emergency(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.actions.with_raw_response.enable_emergency(
                id="",
                emergency_address_id="53829456729313",
                emergency_enabled=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_ownership(self, client: Telnyx) -> None:
        action = client.phone_numbers.actions.verify_ownership(
            phone_numbers=["+15551234567"],
        )
        assert_matches_type(ActionVerifyOwnershipResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify_ownership(self, client: Telnyx) -> None:
        response = client.phone_numbers.actions.with_raw_response.verify_ownership(
            phone_numbers=["+15551234567"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionVerifyOwnershipResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify_ownership(self, client: Telnyx) -> None:
        with client.phone_numbers.actions.with_streaming_response.verify_ownership(
            phone_numbers=["+15551234567"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionVerifyOwnershipResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_change_bundle_status(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.phone_numbers.actions.change_bundle_status(
            id="1293384261075731499",
            bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
        )
        assert_matches_type(ActionChangeBundleStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_change_bundle_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.actions.with_raw_response.change_bundle_status(
            id="1293384261075731499",
            bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionChangeBundleStatusResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_change_bundle_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.actions.with_streaming_response.change_bundle_status(
            id="1293384261075731499",
            bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionChangeBundleStatusResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_change_bundle_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.actions.with_raw_response.change_bundle_status(
                id="",
                bundle_id="5194d8fc-87e6-4188-baa9-1c434bbe861b",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enable_emergency(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.phone_numbers.actions.enable_emergency(
            id="1293384261075731499",
            emergency_address_id="53829456729313",
            emergency_enabled=True,
        )
        assert_matches_type(ActionEnableEmergencyResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enable_emergency(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.actions.with_raw_response.enable_emergency(
            id="1293384261075731499",
            emergency_address_id="53829456729313",
            emergency_enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionEnableEmergencyResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enable_emergency(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.actions.with_streaming_response.enable_emergency(
            id="1293384261075731499",
            emergency_address_id="53829456729313",
            emergency_enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionEnableEmergencyResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_enable_emergency(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.actions.with_raw_response.enable_emergency(
                id="",
                emergency_address_id="53829456729313",
                emergency_enabled=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_ownership(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.phone_numbers.actions.verify_ownership(
            phone_numbers=["+15551234567"],
        )
        assert_matches_type(ActionVerifyOwnershipResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify_ownership(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.actions.with_raw_response.verify_ownership(
            phone_numbers=["+15551234567"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionVerifyOwnershipResponse, action, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify_ownership(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.actions.with_streaming_response.verify_ownership(
            phone_numbers=["+15551234567"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionVerifyOwnershipResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True
