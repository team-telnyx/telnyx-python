# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import UserProfileListResponse, UserProfilePatchAllResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        user_profile = client.user_profile.list()
        assert_matches_type(UserProfileListResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.user_profile.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_profile = response.parse()
        assert_matches_type(UserProfileListResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.user_profile.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_profile = response.parse()
            assert_matches_type(UserProfileListResponse, user_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: Telnyx) -> None:
        user_profile = client.user_profile.patch_all()
        assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all_with_all_params(self, client: Telnyx) -> None:
        user_profile = client.user_profile.patch_all(
            address_1="123 Example Street",
            address_2="Suite 100",
            business_name="Example Company",
            city="Chicago",
            company_size="11-50",
            country="US",
            data_locality="DEU",
            default_managed_account_allow_custom_pricing=False,
            default_managed_account_inherit_emergency_terms_of_service=False,
            default_managed_account_rollup_billing=False,
            default_notify_manager_account=True,
            default_numbers_external_pin="1234",
            first_name="Alex",
            got_free_number_at_signup=False,
            last_name="Taylor",
            low_balance_notification_frequency=12,
            low_balance_threshold_amount=10,
            notify_on_invoice_available=True,
            notify_on_invoice_payment=False,
            npac_user=False,
            onboarding_build_method=["API"],
            onboarding_industries=["software"],
            onboarding_monthly_budget=["1000-5000"],
            onboarding_product_interest=["voice"],
            onboarding_project_types=["contact center"],
            onboarding_reasons_for_consideration=["API integration"],
            onboarding_referrer=["search engine"],
            onboarding_use_cases_other=["customer support"],
            phone_number="+13125550100",
            port_out_pin_validation=False,
            primary_use_case="configure sip trunks",
            role="account manager",
            state="IL",
            ui_theme=1,
            use_cases=["voice"],
            user_subscription_opt_in=False,
            zip="60601",
        )
        assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: Telnyx) -> None:
        response = client.user_profile.with_raw_response.patch_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_profile = response.parse()
        assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: Telnyx) -> None:
        with client.user_profile.with_streaming_response.patch_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_profile = response.parse()
            assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        user_profile = await async_client.user_profile.list()
        assert_matches_type(UserProfileListResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.user_profile.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_profile = await response.parse()
        assert_matches_type(UserProfileListResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.user_profile.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_profile = await response.parse()
            assert_matches_type(UserProfileListResponse, user_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncTelnyx) -> None:
        user_profile = await async_client.user_profile.patch_all()
        assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all_with_all_params(self, async_client: AsyncTelnyx) -> None:
        user_profile = await async_client.user_profile.patch_all(
            address_1="123 Example Street",
            address_2="Suite 100",
            business_name="Example Company",
            city="Chicago",
            company_size="11-50",
            country="US",
            data_locality="DEU",
            default_managed_account_allow_custom_pricing=False,
            default_managed_account_inherit_emergency_terms_of_service=False,
            default_managed_account_rollup_billing=False,
            default_notify_manager_account=True,
            default_numbers_external_pin="1234",
            first_name="Alex",
            got_free_number_at_signup=False,
            last_name="Taylor",
            low_balance_notification_frequency=12,
            low_balance_threshold_amount=10,
            notify_on_invoice_available=True,
            notify_on_invoice_payment=False,
            npac_user=False,
            onboarding_build_method=["API"],
            onboarding_industries=["software"],
            onboarding_monthly_budget=["1000-5000"],
            onboarding_product_interest=["voice"],
            onboarding_project_types=["contact center"],
            onboarding_reasons_for_consideration=["API integration"],
            onboarding_referrer=["search engine"],
            onboarding_use_cases_other=["customer support"],
            phone_number="+13125550100",
            port_out_pin_validation=False,
            primary_use_case="configure sip trunks",
            role="account manager",
            state="IL",
            ui_theme=1,
            use_cases=["voice"],
            user_subscription_opt_in=False,
            zip="60601",
        )
        assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.user_profile.with_raw_response.patch_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_profile = await response.parse()
        assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncTelnyx) -> None:
        async with async_client.user_profile.with_streaming_response.patch_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_profile = await response.parse()
            assert_matches_type(UserProfilePatchAllResponse, user_profile, path=["response"])

        assert cast(Any, response.is_closed) is True
