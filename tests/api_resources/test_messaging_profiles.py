# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MessagingProfileListResponse,
    MessagingProfileCreateResponse,
    MessagingProfileDeleteResponse,
    MessagingProfileUpdateResponse,
    MessagingProfileRetrieveResponse,
    MessagingProfileListShortCodesResponse,
    MessagingProfileListPhoneNumbersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessagingProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.create(
            name="My name",
            whitelisted_destinations=["US"],
        )
        assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.create(
            name="My name",
            whitelisted_destinations=["US"],
            alpha_sender="sqF",
            daily_spend_limit="269125115713",
            daily_spend_limit_enabled=True,
            enabled=True,
            mms_fall_back_to_sms=True,
            mms_transcoding=True,
            number_pool_settings={
                "long_code_weight": 1,
                "skip_unhealthy": True,
                "toll_free_weight": 10,
                "geomatch": False,
                "sticky_sender": False,
            },
            url_shortener_settings={
                "domain": "example.ex",
                "prefix": "",
                "replace_blacklist_only": True,
                "send_webhooks": False,
            },
            webhook_api_version="2",
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="https://www.example.com/hooks",
        )
        assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.create(
            name="My name",
            whitelisted_destinations=["US"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.create(
            name="My name",
            whitelisted_destinations=["US"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileRetrieveResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileRetrieveResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileRetrieveResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            alpha_sender="sqF",
            daily_spend_limit="269125115713",
            daily_spend_limit_enabled=True,
            enabled=True,
            mms_fall_back_to_sms=True,
            mms_transcoding=True,
            name="Updated Profile for Messages",
            number_pool_settings={
                "long_code_weight": 2,
                "skip_unhealthy": False,
                "toll_free_weight": 10,
                "geomatch": False,
                "sticky_sender": True,
            },
            url_shortener_settings={
                "domain": "example.ex",
                "prefix": "cmpny",
                "replace_blacklist_only": True,
                "send_webhooks": False,
            },
            v1_secret="rP1VamejkU2v0qIUxntqLW2c",
            webhook_api_version="2",
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="https://www.example.com/hooks",
            whitelisted_destinations=["US"],
        )
        assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_profiles.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.list()
        assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.list(
            filter={"name": "name"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileDeleteResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileDeleteResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileDeleteResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_phone_numbers(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_phone_numbers_with_all_params(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_phone_numbers(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_phone_numbers(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_phone_numbers(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_profiles.with_raw_response.list_phone_numbers(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_short_codes(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_short_codes_with_all_params(self, client: Telnyx) -> None:
        messaging_profile = client.messaging_profiles.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_short_codes(self, client: Telnyx) -> None:
        response = client.messaging_profiles.with_raw_response.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = response.parse()
        assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_short_codes(self, client: Telnyx) -> None:
        with client.messaging_profiles.with_streaming_response.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = response.parse()
            assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_short_codes(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_profiles.with_raw_response.list_short_codes(
                id="",
            )


class TestAsyncMessagingProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.create(
            name="My name",
            whitelisted_destinations=["US"],
        )
        assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.create(
            name="My name",
            whitelisted_destinations=["US"],
            alpha_sender="sqF",
            daily_spend_limit="269125115713",
            daily_spend_limit_enabled=True,
            enabled=True,
            mms_fall_back_to_sms=True,
            mms_transcoding=True,
            number_pool_settings={
                "long_code_weight": 1,
                "skip_unhealthy": True,
                "toll_free_weight": 10,
                "geomatch": False,
                "sticky_sender": False,
            },
            url_shortener_settings={
                "domain": "example.ex",
                "prefix": "",
                "replace_blacklist_only": True,
                "send_webhooks": False,
            },
            webhook_api_version="2",
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="https://www.example.com/hooks",
        )
        assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.create(
            name="My name",
            whitelisted_destinations=["US"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.create(
            name="My name",
            whitelisted_destinations=["US"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileCreateResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileRetrieveResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileRetrieveResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileRetrieveResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            alpha_sender="sqF",
            daily_spend_limit="269125115713",
            daily_spend_limit_enabled=True,
            enabled=True,
            mms_fall_back_to_sms=True,
            mms_transcoding=True,
            name="Updated Profile for Messages",
            number_pool_settings={
                "long_code_weight": 2,
                "skip_unhealthy": False,
                "toll_free_weight": 10,
                "geomatch": False,
                "sticky_sender": True,
            },
            url_shortener_settings={
                "domain": "example.ex",
                "prefix": "cmpny",
                "replace_blacklist_only": True,
                "send_webhooks": False,
            },
            v1_secret="rP1VamejkU2v0qIUxntqLW2c",
            webhook_api_version="2",
            webhook_failover_url="https://backup.example.com/hooks",
            webhook_url="https://www.example.com/hooks",
            whitelisted_destinations=["US"],
        )
        assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileUpdateResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_profiles.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.list()
        assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.list(
            filter={"name": "name"},
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileListResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileDeleteResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileDeleteResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileDeleteResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_phone_numbers_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.list_phone_numbers(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileListPhoneNumbersResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_profiles.with_raw_response.list_phone_numbers(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_short_codes(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_short_codes_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_profile = await async_client.messaging_profiles.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_short_codes(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.with_raw_response.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_profile = await response.parse()
        assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_short_codes(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.with_streaming_response.list_short_codes(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_profile = await response.parse()
            assert_matches_type(MessagingProfileListShortCodesResponse, messaging_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_short_codes(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_profiles.with_raw_response.list_short_codes(
                id="",
            )
