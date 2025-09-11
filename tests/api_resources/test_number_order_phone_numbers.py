# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    NumberOrderPhoneNumberListResponse,
    NumberOrderPhoneNumberRetrieveResponse,
    NumberOrderPhoneNumberUpdateRequirementsResponse,
    NumberOrderPhoneNumberUpdateRequirementGroupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumberOrderPhoneNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        number_order_phone_number = client.number_order_phone_numbers.retrieve(
            "number_order_phone_number_id",
        )
        assert_matches_type(NumberOrderPhoneNumberRetrieveResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.number_order_phone_numbers.with_raw_response.retrieve(
            "number_order_phone_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = response.parse()
        assert_matches_type(NumberOrderPhoneNumberRetrieveResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.number_order_phone_numbers.with_streaming_response.retrieve(
            "number_order_phone_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = response.parse()
            assert_matches_type(NumberOrderPhoneNumberRetrieveResponse, number_order_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `number_order_phone_number_id` but received ''"
        ):
            client.number_order_phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        number_order_phone_number = client.number_order_phone_numbers.list()
        assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        number_order_phone_number = client.number_order_phone_numbers.list(
            filter={"country_code": "US"},
        )
        assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.number_order_phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = response.parse()
        assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.number_order_phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = response.parse()
            assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_requirement_group(self, client: Telnyx) -> None:
        number_order_phone_number = client.number_order_phone_numbers.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementGroupResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_requirement_group(self, client: Telnyx) -> None:
        response = client.number_order_phone_numbers.with_raw_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = response.parse()
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementGroupResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_requirement_group(self, client: Telnyx) -> None:
        with client.number_order_phone_numbers.with_streaming_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = response.parse()
            assert_matches_type(
                NumberOrderPhoneNumberUpdateRequirementGroupResponse, number_order_phone_number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_requirement_group(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.number_order_phone_numbers.with_raw_response.update_requirement_group(
                id="",
                requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_requirements(self, client: Telnyx) -> None:
        number_order_phone_number = client.number_order_phone_numbers.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
        )
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_requirements_with_all_params(self, client: Telnyx) -> None:
        number_order_phone_number = client.number_order_phone_numbers.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
            regulatory_requirements=[
                {
                    "field_value": "45f45a04-b4be-4592-95b1-9306b9db2b21",
                    "requirement_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
                }
            ],
        )
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_requirements(self, client: Telnyx) -> None:
        response = client.number_order_phone_numbers.with_raw_response.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = response.parse()
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_requirements(self, client: Telnyx) -> None:
        with client.number_order_phone_numbers.with_streaming_response.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = response.parse()
            assert_matches_type(
                NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_requirements(self, client: Telnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `number_order_phone_number_id` but received ''"
        ):
            client.number_order_phone_numbers.with_raw_response.update_requirements(
                number_order_phone_number_id="",
            )


class TestAsyncNumberOrderPhoneNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        number_order_phone_number = await async_client.number_order_phone_numbers.retrieve(
            "number_order_phone_number_id",
        )
        assert_matches_type(NumberOrderPhoneNumberRetrieveResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_order_phone_numbers.with_raw_response.retrieve(
            "number_order_phone_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = await response.parse()
        assert_matches_type(NumberOrderPhoneNumberRetrieveResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_order_phone_numbers.with_streaming_response.retrieve(
            "number_order_phone_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = await response.parse()
            assert_matches_type(NumberOrderPhoneNumberRetrieveResponse, number_order_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `number_order_phone_number_id` but received ''"
        ):
            await async_client.number_order_phone_numbers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        number_order_phone_number = await async_client.number_order_phone_numbers.list()
        assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_order_phone_number = await async_client.number_order_phone_numbers.list(
            filter={"country_code": "US"},
        )
        assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_order_phone_numbers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = await response.parse()
        assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_order_phone_numbers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = await response.parse()
            assert_matches_type(NumberOrderPhoneNumberListResponse, number_order_phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        number_order_phone_number = await async_client.number_order_phone_numbers.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementGroupResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_order_phone_numbers.with_raw_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = await response.parse()
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementGroupResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_order_phone_numbers.with_streaming_response.update_requirement_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = await response.parse()
            assert_matches_type(
                NumberOrderPhoneNumberUpdateRequirementGroupResponse, number_order_phone_number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_requirement_group(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.number_order_phone_numbers.with_raw_response.update_requirement_group(
                id="",
                requirement_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_requirements(self, async_client: AsyncTelnyx) -> None:
        number_order_phone_number = await async_client.number_order_phone_numbers.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
        )
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_requirements_with_all_params(self, async_client: AsyncTelnyx) -> None:
        number_order_phone_number = await async_client.number_order_phone_numbers.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
            regulatory_requirements=[
                {
                    "field_value": "45f45a04-b4be-4592-95b1-9306b9db2b21",
                    "requirement_id": "8ffb3622-7c6b-4ccc-b65f-7a3dc0099576",
                }
            ],
        )
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_requirements(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_order_phone_numbers.with_raw_response.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number_order_phone_number = await response.parse()
        assert_matches_type(
            NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_requirements(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_order_phone_numbers.with_streaming_response.update_requirements(
            number_order_phone_number_id="number_order_phone_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number_order_phone_number = await response.parse()
            assert_matches_type(
                NumberOrderPhoneNumberUpdateRequirementsResponse, number_order_phone_number, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_requirements(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `number_order_phone_number_id` but received ''"
        ):
            await async_client.number_order_phone_numbers.with_raw_response.update_requirements(
                number_order_phone_number_id="",
            )
