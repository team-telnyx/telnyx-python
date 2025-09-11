# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PhoneNumberAssignmentByProfileAssignResponse,
    PhoneNumberAssignmentByProfileRetrieveStatusResponse,
    PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberAssignmentByProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_assign(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = client.phone_number_assignment_by_profile.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_assign_with_all_params(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = client.phone_number_assignment_by_profile.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            tcr_campaign_id="CWZTFH1",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_assign(self, client: Telnyx) -> None:
        response = client.phone_number_assignment_by_profile.with_raw_response.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_assign(self, client: Telnyx) -> None:
        with client.phone_number_assignment_by_profile.with_streaming_response.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_phone_number_status(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = client.phone_number_assignment_by_profile.retrieve_phone_number_status(
            task_id="taskId",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_phone_number_status_with_all_params(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = client.phone_number_assignment_by_profile.retrieve_phone_number_status(
            task_id="taskId",
            page=0,
            records_per_page=0,
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_phone_number_status(self, client: Telnyx) -> None:
        response = client.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_number_status(
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_phone_number_status(self, client: Telnyx) -> None:
        with client.phone_number_assignment_by_profile.with_streaming_response.retrieve_phone_number_status(
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_phone_number_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_number_status(
                task_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Telnyx) -> None:
        phone_number_assignment_by_profile = client.phone_number_assignment_by_profile.retrieve_status(
            "taskId",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveStatusResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Telnyx) -> None:
        response = client.phone_number_assignment_by_profile.with_raw_response.retrieve_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveStatusResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Telnyx) -> None:
        with client.phone_number_assignment_by_profile.with_streaming_response.retrieve_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrieveStatusResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.phone_number_assignment_by_profile.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncPhoneNumberAssignmentByProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_assign(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = await async_client.phone_number_assignment_by_profile.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_assign_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = await async_client.phone_number_assignment_by_profile.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            tcr_campaign_id="CWZTFH1",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_assignment_by_profile.with_raw_response.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = await response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_assignment_by_profile.with_streaming_response.assign(
            messaging_profile_id="4001767e-ce0f-4cae-9d5f-0d5e636e7809",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = await response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileAssignResponse, phone_number_assignment_by_profile, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_phone_number_status(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.phone_number_assignment_by_profile.retrieve_phone_number_status(
                task_id="taskId",
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_phone_number_status_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = (
            await async_client.phone_number_assignment_by_profile.retrieve_phone_number_status(
                task_id="taskId",
                page=0,
                records_per_page=0,
            )
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_phone_number_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_number_status(
            task_id="taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = await response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
            phone_number_assignment_by_profile,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_phone_number_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_assignment_by_profile.with_streaming_response.retrieve_phone_number_status(
            task_id="taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = await response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_phone_number_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.phone_number_assignment_by_profile.with_raw_response.retrieve_phone_number_status(
                task_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        phone_number_assignment_by_profile = await async_client.phone_number_assignment_by_profile.retrieve_status(
            "taskId",
        )
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveStatusResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_assignment_by_profile.with_raw_response.retrieve_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_assignment_by_profile = await response.parse()
        assert_matches_type(
            PhoneNumberAssignmentByProfileRetrieveStatusResponse, phone_number_assignment_by_profile, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_assignment_by_profile.with_streaming_response.retrieve_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_assignment_by_profile = await response.parse()
            assert_matches_type(
                PhoneNumberAssignmentByProfileRetrieveStatusResponse,
                phone_number_assignment_by_profile,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.phone_number_assignment_by_profile.with_raw_response.retrieve_status(
                "",
            )
