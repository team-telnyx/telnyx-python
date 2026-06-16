# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.enterprises.reputation import (
    RemediationListResponse,
    RemediationSubmitResponse,
    RemediationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRemediation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        remediation = client.enterprises.reputation.remediation.retrieve(
            remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.remediation.with_raw_response.retrieve(
            remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.enterprises.reputation.remediation.with_streaming_response.retrieve(
            remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.remediation.with_raw_response.retrieve(
                remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
                enterprise_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            client.enterprises.reputation.remediation.with_raw_response.retrieve(
                remediation_id="",
                enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        remediation = client.enterprises.reputation.remediation.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(SyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        remediation = client.enterprises.reputation.remediation.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            filter_created_at_gte=parse_datetime("2026-01-01T00:00:00Z"),
            filter_created_at_lte=parse_datetime("2026-12-31T23:59:59Z"),
            filter_status="in_progress",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(SyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.remediation.with_raw_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.enterprises.reputation.remediation.with_streaming_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.remediation.with_raw_response.list(
                enterprise_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Telnyx) -> None:
        remediation = client.enterprises.reputation.remediation.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
        )
        assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Telnyx) -> None:
        remediation = client.enterprises.reputation.remediation.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
            contact_email="ops@example.com",
            webhook_url="https://example.com/webhooks/remediation",
        )
        assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.remediation.with_raw_response.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = response.parse()
        assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Telnyx) -> None:
        with client.enterprises.reputation.remediation.with_streaming_response.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = response.parse()
            assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.remediation.with_raw_response.submit(
                enterprise_id="",
                call_purpose="Appointment reminders for our dental clinic.",
                phone_numbers=["+19493253498", "+12134445566"],
            )


class TestAsyncRemediation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        remediation = await async_client.enterprises.reputation.remediation.retrieve(
            remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.remediation.with_raw_response.retrieve(
            remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.remediation.with_streaming_response.retrieve(
            remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationRetrieveResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.remediation.with_raw_response.retrieve(
                remediation_id="b7c1f1c0-7a9d-4f0a-9d3e-2f6a1c4b8e21",
                enterprise_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `remediation_id` but received ''"):
            await async_client.enterprises.reputation.remediation.with_raw_response.retrieve(
                remediation_id="",
                enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        remediation = await async_client.enterprises.reputation.remediation.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )
        assert_matches_type(AsyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        remediation = await async_client.enterprises.reputation.remediation.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            filter_created_at_gte=parse_datetime("2026-01-01T00:00:00Z"),
            filter_created_at_lte=parse_datetime("2026-12-31T23:59:59Z"),
            filter_status="in_progress",
            page_number=1,
            page_size=20,
        )
        assert_matches_type(AsyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.remediation.with_raw_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.remediation.with_streaming_response.list(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[RemediationListResponse], remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.remediation.with_raw_response.list(
                enterprise_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncTelnyx) -> None:
        remediation = await async_client.enterprises.reputation.remediation.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
        )
        assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncTelnyx) -> None:
        remediation = await async_client.enterprises.reputation.remediation.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
            contact_email="ops@example.com",
            webhook_url="https://example.com/webhooks/remediation",
        )
        assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.remediation.with_raw_response.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation = await response.parse()
        assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.remediation.with_streaming_response.submit(
            enterprise_id="4a6192a4-573d-446d-b3ce-aff9117272a6",
            call_purpose="Appointment reminders for our dental clinic.",
            phone_numbers=["+19493253498", "+12134445566"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation = await response.parse()
            assert_matches_type(RemediationSubmitResponse, remediation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.remediation.with_raw_response.submit(
                enterprise_id="",
                call_purpose="Appointment reminders for our dental clinic.",
                phone_numbers=["+19493253498", "+12134445566"],
            )
