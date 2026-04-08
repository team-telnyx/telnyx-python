# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.shared import ReputationPhoneNumberWithReputationData
from telnyx.types.enterprises.reputation import (
    NumberRetrieveResponse,
    NumberAssociateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number = client.enterprises.reputation.numbers.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        number = client.enterprises.reputation.numbers.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            fresh=True,
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.numbers.with_raw_response.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.enterprises.reputation.numbers.with_streaming_response.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(NumberRetrieveResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.numbers.with_raw_response.retrieve(
                phone_number="+16035551234",
                enterprise_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.enterprises.reputation.numbers.with_raw_response.retrieve(
                phone_number="",
                enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        number = client.enterprises.reputation.numbers.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            SyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        number = client.enterprises.reputation.numbers.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            page_number=1,
            page_size=1,
            phone_number="+16035551234",
        )
        assert_matches_type(
            SyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.numbers.with_raw_response.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(
            SyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.enterprises.reputation.numbers.with_streaming_response.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(
                SyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.numbers.with_raw_response.list(
                enterprise_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_associate(self, client: Telnyx) -> None:
        number = client.enterprises.reputation.numbers.associate(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            phone_numbers=["+16035551234"],
        )
        assert_matches_type(NumberAssociateResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_associate(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.numbers.with_raw_response.associate(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            phone_numbers=["+16035551234"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(NumberAssociateResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_associate(self, client: Telnyx) -> None:
        with client.enterprises.reputation.numbers.with_streaming_response.associate(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            phone_numbers=["+16035551234"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(NumberAssociateResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_associate(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.numbers.with_raw_response.associate(
                enterprise_id="",
                phone_numbers=["+16035551234"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disassociate(self, client: Telnyx) -> None:
        number = client.enterprises.reputation.numbers.disassociate(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disassociate(self, client: Telnyx) -> None:
        response = client.enterprises.reputation.numbers.with_raw_response.disassociate(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disassociate(self, client: Telnyx) -> None:
        with client.enterprises.reputation.numbers.with_streaming_response.disassociate(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disassociate(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            client.enterprises.reputation.numbers.with_raw_response.disassociate(
                phone_number="+16035551234",
                enterprise_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.enterprises.reputation.numbers.with_raw_response.disassociate(
                phone_number="",
                enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )


class TestAsyncNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number = await async_client.enterprises.reputation.numbers.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number = await async_client.enterprises.reputation.numbers.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            fresh=True,
        )
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.numbers.with_raw_response.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(NumberRetrieveResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.numbers.with_streaming_response.retrieve(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(NumberRetrieveResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.numbers.with_raw_response.retrieve(
                phone_number="+16035551234",
                enterprise_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.enterprises.reputation.numbers.with_raw_response.retrieve(
                phone_number="",
                enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        number = await async_client.enterprises.reputation.numbers.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number = await async_client.enterprises.reputation.numbers.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            page_number=1,
            page_size=1,
            phone_number="+16035551234",
        )
        assert_matches_type(
            AsyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.numbers.with_raw_response.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(
            AsyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.numbers.with_streaming_response.list(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(
                AsyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData], number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.numbers.with_raw_response.list(
                enterprise_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_associate(self, async_client: AsyncTelnyx) -> None:
        number = await async_client.enterprises.reputation.numbers.associate(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            phone_numbers=["+16035551234"],
        )
        assert_matches_type(NumberAssociateResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_associate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.numbers.with_raw_response.associate(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            phone_numbers=["+16035551234"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(NumberAssociateResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_associate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.numbers.with_streaming_response.associate(
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            phone_numbers=["+16035551234"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(NumberAssociateResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_associate(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.numbers.with_raw_response.associate(
                enterprise_id="",
                phone_numbers=["+16035551234"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disassociate(self, async_client: AsyncTelnyx) -> None:
        number = await async_client.enterprises.reputation.numbers.disassociate(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disassociate(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.enterprises.reputation.numbers.with_raw_response.disassociate(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert number is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disassociate(self, async_client: AsyncTelnyx) -> None:
        async with async_client.enterprises.reputation.numbers.with_streaming_response.disassociate(
            phone_number="+16035551234",
            enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert number is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disassociate(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `enterprise_id` but received ''"):
            await async_client.enterprises.reputation.numbers.with_raw_response.disassociate(
                phone_number="+16035551234",
                enterprise_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.enterprises.reputation.numbers.with_raw_response.disassociate(
                phone_number="",
                enterprise_id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            )
