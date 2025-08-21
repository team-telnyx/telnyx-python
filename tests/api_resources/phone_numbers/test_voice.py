# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.phone_numbers import (
    VoiceListResponse,
    VoiceUpdateResponse,
    VoiceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        voice = client.phone_numbers.voice.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.phone_numbers.voice.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.phone_numbers.voice.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.voice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        voice = client.phone_numbers.voice.update(
            id="1293384261075731499",
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        voice = client.phone_numbers.voice.update(
            id="1293384261075731499",
            call_forwarding={
                "call_forwarding_enabled": True,
                "forwarding_type": "always",
                "forwards_to": "+13035559123",
            },
            call_recording={
                "inbound_call_recording_channels": "single",
                "inbound_call_recording_enabled": True,
                "inbound_call_recording_format": "wav",
            },
            caller_id_name_enabled=True,
            cnam_listing={
                "cnam_listing_details": "example",
                "cnam_listing_enabled": True,
            },
            inbound_call_screening="disabled",
            media_features={
                "accept_any_rtp_packets_enabled": True,
                "rtp_auto_adjust_enabled": True,
                "t38_fax_gateway_enabled": True,
            },
            tech_prefix_enabled=True,
            translated_number="+13035559999",
            usage_payment_method="pay-per-minute",
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.phone_numbers.voice.with_raw_response.update(
            id="1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.phone_numbers.voice.with_streaming_response.update(
            id="1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.voice.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        voice = client.phone_numbers.voice.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        voice = client.phone_numbers.voice.list(
            filter={
                "connection_name": {"contains": "test"},
                "customer_reference": "customer_reference",
                "phone_number": "phone_number",
                "voice_usage_payment_method": "channel",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.phone_numbers.voice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.phone_numbers.voice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        voice = await async_client.phone_numbers.voice.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.voice.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.voice.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceRetrieveResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.voice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        voice = await async_client.phone_numbers.voice.update(
            id="1293384261075731499",
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice = await async_client.phone_numbers.voice.update(
            id="1293384261075731499",
            call_forwarding={
                "call_forwarding_enabled": True,
                "forwarding_type": "always",
                "forwards_to": "+13035559123",
            },
            call_recording={
                "inbound_call_recording_channels": "single",
                "inbound_call_recording_enabled": True,
                "inbound_call_recording_format": "wav",
            },
            caller_id_name_enabled=True,
            cnam_listing={
                "cnam_listing_details": "example",
                "cnam_listing_enabled": True,
            },
            inbound_call_screening="disabled",
            media_features={
                "accept_any_rtp_packets_enabled": True,
                "rtp_auto_adjust_enabled": True,
                "t38_fax_gateway_enabled": True,
            },
            tech_prefix_enabled=True,
            translated_number="+13035559999",
            usage_payment_method="pay-per-minute",
        )
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.voice.with_raw_response.update(
            id="1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.voice.with_streaming_response.update(
            id="1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceUpdateResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.voice.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        voice = await async_client.phone_numbers.voice.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice = await async_client.phone_numbers.voice.list(
            filter={
                "connection_name": {"contains": "test"},
                "customer_reference": "customer_reference",
                "phone_number": "phone_number",
                "voice_usage_payment_method": "channel",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="connection_name",
        )
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.voice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.voice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True
