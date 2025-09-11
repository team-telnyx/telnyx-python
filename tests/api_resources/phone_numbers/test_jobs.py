# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.phone_numbers import (
    JobListResponse,
    JobRetrieveResponse,
    JobDeleteBatchResponse,
    JobUpdateBatchResponse,
    JobUpdateEmergencySettingsBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.retrieve(
            "id",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.phone_numbers.jobs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.phone_numbers.jobs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.phone_numbers.jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.list(
            filter={"type": "update_emergency_settings"},
            page={
                "number": 1,
                "size": 1,
            },
            sort="created_at",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.phone_numbers.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.phone_numbers.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_batch(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.delete_batch(
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )
        assert_matches_type(JobDeleteBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_batch(self, client: Telnyx) -> None:
        response = client.phone_numbers.jobs.with_raw_response.delete_batch(
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobDeleteBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_batch(self, client: Telnyx) -> None:
        with client.phone_numbers.jobs.with_streaming_response.delete_batch(
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobDeleteBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
        )
        assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch_with_all_params(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "has_bundle": "has_bundle",
                "phone_number": "phone_number",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
            billing_group_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            connection_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            customer_reference="customer-reference",
            external_pin="123456",
            hd_voice_enabled=True,
            tags=["tag"],
            voice={
                "call_forwarding": {
                    "call_forwarding_enabled": True,
                    "forwarding_type": "always",
                    "forwards_to": "+13035559123",
                },
                "call_recording": {
                    "inbound_call_recording_channels": "single",
                    "inbound_call_recording_enabled": True,
                    "inbound_call_recording_format": "wav",
                },
                "caller_id_name_enabled": True,
                "cnam_listing": {
                    "cnam_listing_details": "example",
                    "cnam_listing_enabled": True,
                },
                "inbound_call_screening": "disabled",
                "media_features": {
                    "accept_any_rtp_packets_enabled": True,
                    "rtp_auto_adjust_enabled": True,
                    "t38_fax_gateway_enabled": True,
                },
                "tech_prefix_enabled": True,
                "translated_number": "translated_number",
                "usage_payment_method": "pay-per-minute",
            },
        )
        assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: Telnyx) -> None:
        response = client.phone_numbers.jobs.with_raw_response.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: Telnyx) -> None:
        with client.phone_numbers.jobs.with_streaming_response.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_emergency_settings_batch(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )
        assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_emergency_settings_batch_with_all_params(self, client: Telnyx) -> None:
        job = client.phone_numbers.jobs.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
            emergency_address_id="53829456729313",
        )
        assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_emergency_settings_batch(self, client: Telnyx) -> None:
        response = client.phone_numbers.jobs.with_raw_response.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_emergency_settings_batch(self, client: Telnyx) -> None:
        with client.phone_numbers.jobs.with_streaming_response.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.retrieve(
            "id",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.jobs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.jobs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.phone_numbers.jobs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.list()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.list(
            filter={"type": "update_emergency_settings"},
            page={
                "number": 1,
                "size": 1,
            },
            sort="created_at",
        )
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobListResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobListResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_batch(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.delete_batch(
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )
        assert_matches_type(JobDeleteBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_batch(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.jobs.with_raw_response.delete_batch(
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobDeleteBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_batch(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.jobs.with_streaming_response.delete_batch(
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobDeleteBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
        )
        assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch_with_all_params(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
            filter={
                "billing_group_id": "62e4bf2e-c278-4282-b524-488d9c9c43b2",
                "connection_id": "1521916448077776306",
                "customer_reference": "customer_reference",
                "emergency_address_id": "9102160989215728032",
                "has_bundle": "has_bundle",
                "phone_number": "phone_number",
                "status": "active",
                "tag": "tag",
                "voice_connection_name": {
                    "contains": "test",
                    "ends_with": "test",
                    "eq": "test",
                    "starts_with": "test",
                },
                "voice_usage_payment_method": "channel",
            },
            billing_group_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            connection_id="dc8e4d67-33a0-4cbb-af74-7b58f05bd494",
            customer_reference="customer-reference",
            external_pin="123456",
            hd_voice_enabled=True,
            tags=["tag"],
            voice={
                "call_forwarding": {
                    "call_forwarding_enabled": True,
                    "forwarding_type": "always",
                    "forwards_to": "+13035559123",
                },
                "call_recording": {
                    "inbound_call_recording_channels": "single",
                    "inbound_call_recording_enabled": True,
                    "inbound_call_recording_format": "wav",
                },
                "caller_id_name_enabled": True,
                "cnam_listing": {
                    "cnam_listing_details": "example",
                    "cnam_listing_enabled": True,
                },
                "inbound_call_screening": "disabled",
                "media_features": {
                    "accept_any_rtp_packets_enabled": True,
                    "rtp_auto_adjust_enabled": True,
                    "t38_fax_gateway_enabled": True,
                },
                "tech_prefix_enabled": True,
                "translated_number": "translated_number",
                "usage_payment_method": "pay-per-minute",
            },
        )
        assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.jobs.with_raw_response.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.jobs.with_streaming_response.update_batch(
            phone_numbers=["1583466971586889004", "+13127367254"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobUpdateBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_emergency_settings_batch(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )
        assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_emergency_settings_batch_with_all_params(self, async_client: AsyncTelnyx) -> None:
        job = await async_client.phone_numbers.jobs.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
            emergency_address_id="53829456729313",
        )
        assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_emergency_settings_batch(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.jobs.with_raw_response.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_emergency_settings_batch(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.jobs.with_streaming_response.update_emergency_settings_batch(
            emergency_enabled=True,
            phone_numbers=["+19705555098", "+19715555098", "32873127836"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobUpdateEmergencySettingsBatchResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True
