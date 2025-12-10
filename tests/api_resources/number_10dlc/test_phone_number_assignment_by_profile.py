# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.number_10dlc import (
    PhoneNumberAssignmentByProfileRetrieveResponse,
    PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
    PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberAssignmentByProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = client.number_10dlc.phone_number_assignment_by_profile.retrieve(
            "taskId",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_10dlc.phone_number_assignment_by_profile.with_streaming_response.retrieve(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrieveResponse, phone_number_assignment_by_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_phone_number_assignment_by_profile(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = (
            client.number_10dlc.phone_number_assignment_by_profile.phone_number_assignment_by_profile(
                messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_phone_number_assignment_by_profile_with_all_params(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = (
            client.number_10dlc.phone_number_assignment_by_profile.phone_number_assignment_by_profile(
                messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
                campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
                tcr_campaign_id="CWZTFH1",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_phone_number_assignment_by_profile(self, client: Telnyx) -> None:
        response = (
            client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.phone_number_assignment_by_profile(
                messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_phone_number_assignment_by_profile(self, client: Telnyx) -> None:
        with client.number_10dlc.phone_number_assignment_by_profile.with_streaming_response.phone_number_assignment_by_profile(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_phone_numbers(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = (
            client.number_10dlc.phone_number_assignment_by_profile.retrieve_phone_numbers(
                task_id="taskId",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_phone_numbers_with_all_params(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = (
            client.number_10dlc.phone_number_assignment_by_profile.retrieve_phone_numbers(
                task_id="taskId",
                page=0,
                records_per_page=0,
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_phone_numbers(self, client: Telnyx) -> None:
        response = client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_numbers(
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_phone_numbers(self, client: Telnyx) -> None:
        with client.number_10dlc.phone_number_assignment_by_profile.with_streaming_response.retrieve_phone_numbers(
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_phone_numbers(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_numbers(
                task_id="",
            )


class TestAsyncPhoneNumberAssignmentByProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.number_10dlc.phone_number_assignment_by_profile.retrieve(
                "taskId",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = await response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.phone_number_assignment_by_profile.with_streaming_response.retrieve(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = await response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrieveResponse, phone_number_assignment_by_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_phone_number_assignment_by_profile(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.number_10dlc.phone_number_assignment_by_profile.phone_number_assignment_by_profile(
                messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_phone_number_assignment_by_profile_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.number_10dlc.phone_number_assignment_by_profile.phone_number_assignment_by_profile(
                messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
                campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
                tcr_campaign_id="CWZTFH1",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_phone_number_assignment_by_profile(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.phone_number_assignment_by_profile(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = await response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_phone_number_assignment_by_profile(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.phone_number_assignment_by_profile.with_streaming_response.phone_number_assignment_by_profile(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = await response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfilePhoneNumberAssignmentByProfileResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.number_10dlc.phone_number_assignment_by_profile.retrieve_phone_numbers(
                task_id="taskId",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_phone_numbers_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.number_10dlc.phone_number_assignment_by_profile.retrieve_phone_numbers(
                task_id="taskId",
                page=0,
                records_per_page=0,
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        response = (
            await async_client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_numbers(
                task_id="taskId",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = await response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.number_10dlc.phone_number_assignment_by_profile.with_streaming_response.retrieve_phone_numbers(
                task_id="taskId",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = await response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrievePhoneNumbersResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_phone_numbers(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.number_10dlc.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_numbers(
                task_id="",
            )
