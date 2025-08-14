# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MessagingHostedNumberOrderListResponse,
    MessagingHostedNumberOrderCreateResponse,
    MessagingHostedNumberOrderDeleteResponse,
    MessagingHostedNumberOrderRetrieveResponse,
    MessagingHostedNumberOrderValidateCodesResponse,
    MessagingHostedNumberOrderCheckEligibilityResponse,
    MessagingHostedNumberOrderCreateVerificationCodesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessagingHostedNumberOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.create()
        assert_matches_type(MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.create(
            messaging_profile_id="dc8f39ac-953d-4520-b93b-786ae87db0da",
            phone_numbers=["+18665550001", "+18665550002"],
        )
        assert_matches_type(MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.retrieve(
            "id",
        )
        assert_matches_type(
            MessagingHostedNumberOrderRetrieveResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderRetrieveResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderRetrieveResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_number_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.list()
        assert_matches_type(MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.delete(
            "id",
        )
        assert_matches_type(MessagingHostedNumberOrderDeleteResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(MessagingHostedNumberOrderDeleteResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderDeleteResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_number_orders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_eligibility(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.check_eligibility(
            phone_numbers=["string"],
        )
        assert_matches_type(
            MessagingHostedNumberOrderCheckEligibilityResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_eligibility(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.check_eligibility(
            phone_numbers=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderCheckEligibilityResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_eligibility(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.check_eligibility(
            phone_numbers=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderCheckEligibilityResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_verification_codes(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.create_verification_codes(
            id="id",
            phone_numbers=["string"],
            verification_method="sms",
        )
        assert_matches_type(
            MessagingHostedNumberOrderCreateVerificationCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_verification_codes(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.create_verification_codes(
            id="id",
            phone_numbers=["string"],
            verification_method="sms",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderCreateVerificationCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_verification_codes(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.create_verification_codes(
            id="id",
            phone_numbers=["string"],
            verification_method="sms",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderCreateVerificationCodesResponse,
                messaging_hosted_number_order,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_verification_codes(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_number_orders.with_raw_response.create_verification_codes(
                id="",
                phone_numbers=["string"],
                verification_method="sms",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_codes(self, client: Telnyx) -> None:
        messaging_hosted_number_order = client.messaging_hosted_number_orders.validate_codes(
            id="id",
            verification_codes=[
                {
                    "code": "code",
                    "phone_number": "phone_number",
                }
            ],
        )
        assert_matches_type(
            MessagingHostedNumberOrderValidateCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_codes(self, client: Telnyx) -> None:
        response = client.messaging_hosted_number_orders.with_raw_response.validate_codes(
            id="id",
            verification_codes=[
                {
                    "code": "code",
                    "phone_number": "phone_number",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderValidateCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_codes(self, client: Telnyx) -> None:
        with client.messaging_hosted_number_orders.with_streaming_response.validate_codes(
            id="id",
            verification_codes=[
                {
                    "code": "code",
                    "phone_number": "phone_number",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderValidateCodesResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_validate_codes(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_hosted_number_orders.with_raw_response.validate_codes(
                id="",
                verification_codes=[
                    {
                        "code": "code",
                        "phone_number": "phone_number",
                    }
                ],
            )


class TestAsyncMessagingHostedNumberOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.create()
        assert_matches_type(MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.create(
            messaging_profile_id="dc8f39ac-953d-4520-b93b-786ae87db0da",
            phone_numbers=["+18665550001", "+18665550002"],
        )
        assert_matches_type(MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderCreateResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.retrieve(
            "id",
        )
        assert_matches_type(
            MessagingHostedNumberOrderRetrieveResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderRetrieveResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderRetrieveResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_number_orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.list()
        assert_matches_type(MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderListResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.delete(
            "id",
        )
        assert_matches_type(MessagingHostedNumberOrderDeleteResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(MessagingHostedNumberOrderDeleteResponse, messaging_hosted_number_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderDeleteResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_number_orders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_eligibility(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.check_eligibility(
            phone_numbers=["string"],
        )
        assert_matches_type(
            MessagingHostedNumberOrderCheckEligibilityResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_eligibility(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.check_eligibility(
            phone_numbers=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderCheckEligibilityResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_eligibility(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.check_eligibility(
            phone_numbers=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderCheckEligibilityResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_verification_codes(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.create_verification_codes(
            id="id",
            phone_numbers=["string"],
            verification_method="sms",
        )
        assert_matches_type(
            MessagingHostedNumberOrderCreateVerificationCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_verification_codes(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.create_verification_codes(
            id="id",
            phone_numbers=["string"],
            verification_method="sms",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderCreateVerificationCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_verification_codes(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.create_verification_codes(
            id="id",
            phone_numbers=["string"],
            verification_method="sms",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderCreateVerificationCodesResponse,
                messaging_hosted_number_order,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_verification_codes(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_number_orders.with_raw_response.create_verification_codes(
                id="",
                phone_numbers=["string"],
                verification_method="sms",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_codes(self, async_client: AsyncTelnyx) -> None:
        messaging_hosted_number_order = await async_client.messaging_hosted_number_orders.validate_codes(
            id="id",
            verification_codes=[
                {
                    "code": "code",
                    "phone_number": "phone_number",
                }
            ],
        )
        assert_matches_type(
            MessagingHostedNumberOrderValidateCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_codes(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_hosted_number_orders.with_raw_response.validate_codes(
            id="id",
            verification_codes=[
                {
                    "code": "code",
                    "phone_number": "phone_number",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messaging_hosted_number_order = await response.parse()
        assert_matches_type(
            MessagingHostedNumberOrderValidateCodesResponse, messaging_hosted_number_order, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_codes(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_hosted_number_orders.with_streaming_response.validate_codes(
            id="id",
            verification_codes=[
                {
                    "code": "code",
                    "phone_number": "phone_number",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messaging_hosted_number_order = await response.parse()
            assert_matches_type(
                MessagingHostedNumberOrderValidateCodesResponse, messaging_hosted_number_order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_validate_codes(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_hosted_number_orders.with_raw_response.validate_codes(
                id="",
                verification_codes=[
                    {
                        "code": "code",
                        "phone_number": "phone_number",
                    }
                ],
            )
