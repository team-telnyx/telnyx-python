# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    OutboundVoiceProfileListResponse,
    OutboundVoiceProfileCreateResponse,
    OutboundVoiceProfileDeleteResponse,
    OutboundVoiceProfileUpdateResponse,
    OutboundVoiceProfileRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutboundVoiceProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.create(
            name="office",
        )
        assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.create(
            name="office",
            billing_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            call_recording={
                "call_recording_caller_phone_numbers": ["+19705555098"],
                "call_recording_channels": "dual",
                "call_recording_format": "mp3",
                "call_recording_type": "by_caller_phone_number",
            },
            concurrent_call_limit=10,
            daily_spend_limit="100.00",
            daily_spend_limit_enabled=True,
            enabled=True,
            max_destination_rate=10,
            service_plan="global",
            tags=["office-profile"],
            traffic_type="conversational",
            usage_payment_method="rate-deck",
            whitelisted_destinations=["US", "BR", "AU"],
        )
        assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.outbound_voice_profiles.with_raw_response.create(
            name="office",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = response.parse()
        assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.outbound_voice_profiles.with_streaming_response.create(
            name="office",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = response.parse()
            assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(OutboundVoiceProfileRetrieveResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.outbound_voice_profiles.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = response.parse()
        assert_matches_type(OutboundVoiceProfileRetrieveResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.outbound_voice_profiles.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = response.parse()
            assert_matches_type(OutboundVoiceProfileRetrieveResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.outbound_voice_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.update(
            id="1293384261075731499",
            name="office",
        )
        assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.update(
            id="1293384261075731499",
            name="office",
            billing_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            call_recording={
                "call_recording_caller_phone_numbers": ["+19705555098"],
                "call_recording_channels": "dual",
                "call_recording_format": "mp3",
                "call_recording_type": "by_caller_phone_number",
            },
            concurrent_call_limit=10,
            daily_spend_limit="100.00",
            daily_spend_limit_enabled=True,
            enabled=True,
            max_destination_rate=10,
            service_plan="global",
            tags=["office-profile"],
            traffic_type="conversational",
            usage_payment_method="rate-deck",
            whitelisted_destinations=["US", "BR", "AU"],
        )
        assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.outbound_voice_profiles.with_raw_response.update(
            id="1293384261075731499",
            name="office",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = response.parse()
        assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.outbound_voice_profiles.with_streaming_response.update(
            id="1293384261075731499",
            name="office",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = response.parse()
            assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.outbound_voice_profiles.with_raw_response.update(
                id="",
                name="office",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.list()
        assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.list(
            filter={"name": {"contains": "office-profile"}},
            page={
                "number": 1,
                "size": 1,
            },
            sort="name",
        )
        assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.outbound_voice_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = response.parse()
        assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.outbound_voice_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = response.parse()
            assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        outbound_voice_profile = client.outbound_voice_profiles.delete(
            "1293384261075731499",
        )
        assert_matches_type(OutboundVoiceProfileDeleteResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.outbound_voice_profiles.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = response.parse()
        assert_matches_type(OutboundVoiceProfileDeleteResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.outbound_voice_profiles.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = response.parse()
            assert_matches_type(OutboundVoiceProfileDeleteResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.outbound_voice_profiles.with_raw_response.delete(
                "",
            )


class TestAsyncOutboundVoiceProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.create(
            name="office",
        )
        assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.create(
            name="office",
            billing_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            call_recording={
                "call_recording_caller_phone_numbers": ["+19705555098"],
                "call_recording_channels": "dual",
                "call_recording_format": "mp3",
                "call_recording_type": "by_caller_phone_number",
            },
            concurrent_call_limit=10,
            daily_spend_limit="100.00",
            daily_spend_limit_enabled=True,
            enabled=True,
            max_destination_rate=10,
            service_plan="global",
            tags=["office-profile"],
            traffic_type="conversational",
            usage_payment_method="rate-deck",
            whitelisted_destinations=["US", "BR", "AU"],
        )
        assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.outbound_voice_profiles.with_raw_response.create(
            name="office",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = await response.parse()
        assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.outbound_voice_profiles.with_streaming_response.create(
            name="office",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = await response.parse()
            assert_matches_type(OutboundVoiceProfileCreateResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(OutboundVoiceProfileRetrieveResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.outbound_voice_profiles.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = await response.parse()
        assert_matches_type(OutboundVoiceProfileRetrieveResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.outbound_voice_profiles.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = await response.parse()
            assert_matches_type(OutboundVoiceProfileRetrieveResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.outbound_voice_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.update(
            id="1293384261075731499",
            name="office",
        )
        assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.update(
            id="1293384261075731499",
            name="office",
            billing_group_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            call_recording={
                "call_recording_caller_phone_numbers": ["+19705555098"],
                "call_recording_channels": "dual",
                "call_recording_format": "mp3",
                "call_recording_type": "by_caller_phone_number",
            },
            concurrent_call_limit=10,
            daily_spend_limit="100.00",
            daily_spend_limit_enabled=True,
            enabled=True,
            max_destination_rate=10,
            service_plan="global",
            tags=["office-profile"],
            traffic_type="conversational",
            usage_payment_method="rate-deck",
            whitelisted_destinations=["US", "BR", "AU"],
        )
        assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.outbound_voice_profiles.with_raw_response.update(
            id="1293384261075731499",
            name="office",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = await response.parse()
        assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.outbound_voice_profiles.with_streaming_response.update(
            id="1293384261075731499",
            name="office",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = await response.parse()
            assert_matches_type(OutboundVoiceProfileUpdateResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.outbound_voice_profiles.with_raw_response.update(
                id="",
                name="office",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.list()
        assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.list(
            filter={"name": {"contains": "office-profile"}},
            page={
                "number": 1,
                "size": 1,
            },
            sort="name",
        )
        assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.outbound_voice_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = await response.parse()
        assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.outbound_voice_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = await response.parse()
            assert_matches_type(OutboundVoiceProfileListResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        outbound_voice_profile = await async_client.outbound_voice_profiles.delete(
            "1293384261075731499",
        )
        assert_matches_type(OutboundVoiceProfileDeleteResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.outbound_voice_profiles.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outbound_voice_profile = await response.parse()
        assert_matches_type(OutboundVoiceProfileDeleteResponse, outbound_voice_profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.outbound_voice_profiles.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outbound_voice_profile = await response.parse()
            assert_matches_type(OutboundVoiceProfileDeleteResponse, outbound_voice_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.outbound_voice_profiles.with_raw_response.delete(
                "",
            )
