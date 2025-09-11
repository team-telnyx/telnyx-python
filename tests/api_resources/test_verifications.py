# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CreateVerificationResponse,
    VerificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        verification = client.verifications.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.verifications.with_raw_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.verifications.with_streaming_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.verifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_call(self, client: Telnyx) -> None:
        verification = client.verifications.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_call_with_all_params(self, client: Telnyx) -> None:
        verification = client.verifications.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            custom_code="43612",
            timeout_secs=300,
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger_call(self, client: Telnyx) -> None:
        response = client.verifications.with_raw_response.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger_call(self, client: Telnyx) -> None:
        with client.verifications.with_streaming_response.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(CreateVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_flashcall(self, client: Telnyx) -> None:
        verification = client.verifications.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_flashcall_with_all_params(self, client: Telnyx) -> None:
        verification = client.verifications.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            timeout_secs=300,
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger_flashcall(self, client: Telnyx) -> None:
        response = client.verifications.with_raw_response.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger_flashcall(self, client: Telnyx) -> None:
        with client.verifications.with_streaming_response.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(CreateVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_sms(self, client: Telnyx) -> None:
        verification = client.verifications.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_sms_with_all_params(self, client: Telnyx) -> None:
        verification = client.verifications.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            custom_code="43612",
            timeout_secs=300,
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger_sms(self, client: Telnyx) -> None:
        response = client.verifications.with_raw_response.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger_sms(self, client: Telnyx) -> None:
        with client.verifications.with_streaming_response.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(CreateVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verifications.with_raw_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verifications.with_streaming_response.retrieve(
            "12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationRetrieveResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.verifications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_call(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_call_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            custom_code="43612",
            timeout_secs=300,
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger_call(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verifications.with_raw_response.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_call(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verifications.with_streaming_response.trigger_call(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(CreateVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_flashcall(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_flashcall_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            timeout_secs=300,
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger_flashcall(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verifications.with_raw_response.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_flashcall(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verifications.with_streaming_response.trigger_flashcall(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(CreateVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_sms(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_sms_with_all_params(self, async_client: AsyncTelnyx) -> None:
        verification = await async_client.verifications.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
            custom_code="43612",
            timeout_secs=300,
        )
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger_sms(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.verifications.with_raw_response.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(CreateVerificationResponse, verification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger_sms(self, async_client: AsyncTelnyx) -> None:
        async with async_client.verifications.with_streaming_response.trigger_sms(
            phone_number="+13035551234",
            verify_profile_id="12ade33a-21c0-473b-b055-b3c836e1c292",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(CreateVerificationResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True
