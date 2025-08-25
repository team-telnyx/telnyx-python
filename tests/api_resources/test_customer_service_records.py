# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    CustomerServiceRecordListResponse,
    CustomerServiceRecordCreateResponse,
    CustomerServiceRecordRetrieveResponse,
    CustomerServiceRecordVerifyPhoneNumberCoverageResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomerServiceRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        customer_service_record = client.customer_service_records.create(
            phone_number="+1234567890",
        )
        assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        customer_service_record = client.customer_service_records.create(
            phone_number="+1234567890",
            additional_data={
                "account_number": "123456789",
                "address_line_1": "123 Main St",
                "authorized_person_name": "John Doe",
                "billing_phone_number": "+12065551212",
                "city": "New York",
                "customer_code": "123456789",
                "name": "Entity Inc.",
                "pin": "1234",
                "state": "NY",
                "zip_code": "10001",
            },
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.customer_service_records.with_raw_response.create(
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = response.parse()
        assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.customer_service_records.with_streaming_response.create(
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = response.parse()
            assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        customer_service_record = client.customer_service_records.retrieve(
            "customer_service_record_id",
        )
        assert_matches_type(CustomerServiceRecordRetrieveResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.customer_service_records.with_raw_response.retrieve(
            "customer_service_record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = response.parse()
        assert_matches_type(CustomerServiceRecordRetrieveResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.customer_service_records.with_streaming_response.retrieve(
            "customer_service_record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = response.parse()
            assert_matches_type(CustomerServiceRecordRetrieveResponse, customer_service_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `customer_service_record_id` but received ''"
        ):
            client.customer_service_records.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        customer_service_record = client.customer_service_records.list()
        assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        customer_service_record = client.customer_service_records.list(
            filter={
                "created_at": {
                    "gt": parse_datetime("2020-01-01T00:00:00Z"),
                    "lt": parse_datetime("2020-01-01T00:00:00Z"),
                },
                "phone_number": {
                    "eq": "+12441239999",
                    "in": ["+12441239999"],
                },
                "status": {
                    "eq": "pending",
                    "in": ["pending"],
                },
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.customer_service_records.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = response.parse()
        assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.customer_service_records.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = response.parse()
            assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_phone_number_coverage(self, client: Telnyx) -> None:
        customer_service_record = client.customer_service_records.verify_phone_number_coverage(
            phone_numbers=["+1234567890"],
        )
        assert_matches_type(
            CustomerServiceRecordVerifyPhoneNumberCoverageResponse, customer_service_record, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify_phone_number_coverage(self, client: Telnyx) -> None:
        response = client.customer_service_records.with_raw_response.verify_phone_number_coverage(
            phone_numbers=["+1234567890"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = response.parse()
        assert_matches_type(
            CustomerServiceRecordVerifyPhoneNumberCoverageResponse, customer_service_record, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify_phone_number_coverage(self, client: Telnyx) -> None:
        with client.customer_service_records.with_streaming_response.verify_phone_number_coverage(
            phone_numbers=["+1234567890"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = response.parse()
            assert_matches_type(
                CustomerServiceRecordVerifyPhoneNumberCoverageResponse, customer_service_record, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomerServiceRecords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        customer_service_record = await async_client.customer_service_records.create(
            phone_number="+1234567890",
        )
        assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        customer_service_record = await async_client.customer_service_records.create(
            phone_number="+1234567890",
            additional_data={
                "account_number": "123456789",
                "address_line_1": "123 Main St",
                "authorized_person_name": "John Doe",
                "billing_phone_number": "+12065551212",
                "city": "New York",
                "customer_code": "123456789",
                "name": "Entity Inc.",
                "pin": "1234",
                "state": "NY",
                "zip_code": "10001",
            },
            webhook_url="https://example.com/webhook",
        )
        assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.customer_service_records.with_raw_response.create(
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = await response.parse()
        assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.customer_service_records.with_streaming_response.create(
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = await response.parse()
            assert_matches_type(CustomerServiceRecordCreateResponse, customer_service_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        customer_service_record = await async_client.customer_service_records.retrieve(
            "customer_service_record_id",
        )
        assert_matches_type(CustomerServiceRecordRetrieveResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.customer_service_records.with_raw_response.retrieve(
            "customer_service_record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = await response.parse()
        assert_matches_type(CustomerServiceRecordRetrieveResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.customer_service_records.with_streaming_response.retrieve(
            "customer_service_record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = await response.parse()
            assert_matches_type(CustomerServiceRecordRetrieveResponse, customer_service_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `customer_service_record_id` but received ''"
        ):
            await async_client.customer_service_records.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        customer_service_record = await async_client.customer_service_records.list()
        assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        customer_service_record = await async_client.customer_service_records.list(
            filter={
                "created_at": {
                    "gt": parse_datetime("2020-01-01T00:00:00Z"),
                    "lt": parse_datetime("2020-01-01T00:00:00Z"),
                },
                "phone_number": {
                    "eq": "+12441239999",
                    "in": ["+12441239999"],
                },
                "status": {
                    "eq": "pending",
                    "in": ["pending"],
                },
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.customer_service_records.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = await response.parse()
        assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.customer_service_records.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = await response.parse()
            assert_matches_type(CustomerServiceRecordListResponse, customer_service_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_phone_number_coverage(self, async_client: AsyncTelnyx) -> None:
        customer_service_record = await async_client.customer_service_records.verify_phone_number_coverage(
            phone_numbers=["+1234567890"],
        )
        assert_matches_type(
            CustomerServiceRecordVerifyPhoneNumberCoverageResponse, customer_service_record, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify_phone_number_coverage(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.customer_service_records.with_raw_response.verify_phone_number_coverage(
            phone_numbers=["+1234567890"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer_service_record = await response.parse()
        assert_matches_type(
            CustomerServiceRecordVerifyPhoneNumberCoverageResponse, customer_service_record, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify_phone_number_coverage(self, async_client: AsyncTelnyx) -> None:
        async with async_client.customer_service_records.with_streaming_response.verify_phone_number_coverage(
            phone_numbers=["+1234567890"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer_service_record = await response.parse()
            assert_matches_type(
                CustomerServiceRecordVerifyPhoneNumberCoverageResponse, customer_service_record, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
