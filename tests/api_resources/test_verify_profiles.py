# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    VerifyProfileData,
    VerifyProfileListResponse,
    VerifyProfileRetrieveTemplatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifyProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.create(
            name="Test Profile",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.create(
            name="Test Profile",
            call={
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                "whitelisted_destinations": ["US", "CA"],
            },
            flashcall={
                "default_verification_timeout_secs": 300,
                "whitelisted_destinations": ["US", "CA"],
            },
            language="en-US",
            sms={
                "whitelisted_destinations": ["US", "CA"],
                "alpha_sender": "sqF",
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
            },
            webhook_failover_url="http://example.com/webhook/failover",
            webhook_url="http://example.com/webhook",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.verify_profiles.with_raw_response.create(
            name="Test Profile",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.verify_profiles.with_streaming_response.create(
            name="Test Profile",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.verify_profiles.with_raw_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.verify_profiles.with_streaming_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verify_profile_id` but received ''"):
            client.verify_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            call={
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                "whitelisted_destinations": ["US", "CA"],
            },
            flashcall={
                "default_verification_timeout_secs": 300,
                "whitelisted_destinations": ["US", "CA"],
            },
            language="en-US",
            name="Test Profile",
            sms={
                "alpha_sender": "sqF",
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                "whitelisted_destinations": ["US", "CA"],
            },
            webhook_failover_url="http://example.com/webhook/failover",
            webhook_url="http://example.com/webhook",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.verify_profiles.with_raw_response.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.verify_profiles.with_streaming_response.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verify_profile_id` but received ''"):
            client.verify_profiles.with_raw_response.update(
                verify_profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.list()
        assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.list(
            filter={"name": "name"},
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.verify_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = response.parse()
        assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.verify_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = response.parse()
            assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.delete(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.verify_profiles.with_raw_response.delete(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.verify_profiles.with_streaming_response.delete(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verify_profile_id` but received ''"):
            client.verify_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_templates(self, client: Telnyx) -> None:
        verify_profile = client.verify_profiles.retrieve_templates()
        assert_matches_type(VerifyProfileRetrieveTemplatesResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_templates(self, client: Telnyx) -> None:
        response = client.verify_profiles.with_raw_response.retrieve_templates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = response.parse()
        assert_matches_type(VerifyProfileRetrieveTemplatesResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_templates(self, client: Telnyx) -> None:
        with client.verify_profiles.with_streaming_response.retrieve_templates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = response.parse()
            assert_matches_type(VerifyProfileRetrieveTemplatesResponse, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerifyProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.create(
            name="Test Profile",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.create(
            name="Test Profile",
            call={
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                "whitelisted_destinations": ["US", "CA"],
            },
            flashcall={
                "default_verification_timeout_secs": 300,
                "whitelisted_destinations": ["US", "CA"],
            },
            language="en-US",
            sms={
                "whitelisted_destinations": ["US", "CA"],
                "alpha_sender": "sqF",
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
            },
            webhook_failover_url="http://example.com/webhook/failover",
            webhook_url="http://example.com/webhook",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verify_profiles.with_raw_response.create(
            name="Test Profile",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = await response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verify_profiles.with_streaming_response.create(
            name="Test Profile",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = await response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verify_profiles.with_raw_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = await response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verify_profiles.with_streaming_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = await response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verify_profile_id` but received ''"):
            await async_client.verify_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            call={
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                "whitelisted_destinations": ["US", "CA"],
            },
            flashcall={
                "default_verification_timeout_secs": 300,
                "whitelisted_destinations": ["US", "CA"],
            },
            language="en-US",
            name="Test Profile",
            sms={
                "alpha_sender": "sqF",
                "app_name": "Example Secure App",
                "code_length": 6,
                "default_verification_timeout_secs": 300,
                "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                "whitelisted_destinations": ["US", "CA"],
            },
            webhook_failover_url="http://example.com/webhook/failover",
            webhook_url="http://example.com/webhook",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verify_profiles.with_raw_response.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = await response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verify_profiles.with_streaming_response.update(
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = await response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verify_profile_id` but received ''"):
            await async_client.verify_profiles.with_raw_response.update(
                verify_profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.list()
        assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.list(
            filter={"name": "name"},
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verify_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = await response.parse()
        assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verify_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = await response.parse()
            assert_matches_type(VerifyProfileListResponse, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.delete(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verify_profiles.with_raw_response.delete(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = await response.parse()
        assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verify_profiles.with_streaming_response.delete(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = await response.parse()
            assert_matches_type(VerifyProfileData, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verify_profile_id` but received ''"):
            await async_client.verify_profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_templates(self, async_client: AsyncTelnyx) -> None:
        verify_profile = await async_client.verify_profiles.retrieve_templates()
        assert_matches_type(VerifyProfileRetrieveTemplatesResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_templates(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verify_profiles.with_raw_response.retrieve_templates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_profile = await response.parse()
        assert_matches_type(VerifyProfileRetrieveTemplatesResponse, verify_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_templates(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verify_profiles.with_streaming_response.retrieve_templates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_profile = await response.parse()
            assert_matches_type(VerifyProfileRetrieveTemplatesResponse, verify_profile, path=["response"])

        assert cast(Any, response.is_closed) is True
